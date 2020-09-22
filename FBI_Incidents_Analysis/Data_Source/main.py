import crawl_data_from_s3
import data_processing
import os
import shutil
import pandas as pd
from settings import *


def process_data_folders():
    df = pd.DataFrame()
    for state in states:
        for year in range(start_year, end_year):
            input_folder = inputDir + state + '/' + state + '_' + str(year)

            # Create path link for required doc
            VICTIM_OFFENSE_PATH = input_folder + '/NIBRS_VICTIM_OFFENSE.csv'
            OFFENSE_PATH = input_folder + '/NIBRS_OFFENSE.csv'
            OFFENSE_TYPE_PATH = input_folder + '/NIBRS_OFFENSE_TYPE.csv'
            VICTIMS_PATH = input_folder + '/NIBRS_VICTIM.csv'
            OFFENDERS_PATH = input_folder + '/NIBRS_OFFENDER.csv'
            INCIDENTS_PATH = input_folder + '/NIBRS_incident.csv'
            LOCATION_TYPE_PATH = input_folder + '/NIBRS_LOCATION_TYPE.csv'
            VICTIMS_TYPE_PATH = input_folder + '/NIBRS_VICTIM_TYPE.csv'
            AGE_PATH = input_folder + '/NIBRS_AGE.csv'
            RACE_PATH = input_folder + '/REF_RACE.csv'
            ETHNICITY_PATH = input_folder + '/NIBRS_ETHNICITY.csv'
            RELATIONSHIP_PATH = input_folder + '/NIBRS_RELATIONSHIP.csv'
            VICTIMS_OFFENDER_REL_PATH = input_folder + '/NIBRS_VICTIM_OFFENDER_REL.csv'
            AGENCIES_PATH = input_folder + '/AGENCIES.csv'

            ## convert csv to df & uppercase the join column
            victims_offense_df = data_processing.get_df_from_csv(VICTIM_OFFENSE_PATH)
            victims_offense_df.columns = [c.upper() for c in victims_offense_df.columns]

            offense_df = data_processing.get_df_from_csv(OFFENSE_PATH)
            offense_df.columns = [c.upper() for c in offense_df.columns]

            offense_type_df = data_processing.get_df_from_csv(OFFENSE_TYPE_PATH)
            offense_type_df.columns = [c.upper() for c in offense_type_df.columns]

            victims_df = data_processing.get_df_from_csv(VICTIMS_PATH)
            victims_df.columns = [c.upper() for c in victims_df.columns]

            offenders_df = data_processing.get_df_from_csv(OFFENDERS_PATH)
            offenders_df.columns = [c.upper() for c in offenders_df.columns]

            incidents_df = data_processing.get_df_from_csv(INCIDENTS_PATH)
            incidents_df.columns = [c.upper() for c in incidents_df.columns]

            relations_df = data_processing.get_df_from_csv(VICTIMS_OFFENDER_REL_PATH)
            relations_df.columns = [c.upper() for c in relations_df.columns]

            agencies_df = data_processing.get_df_from_csv(AGENCIES_PATH)
            agencies_df.columns = [c.upper() for c in agencies_df.columns]

            ## convert lookup table to df & uppercase the columns
            locations_df = data_processing.get_df_from_csv(LOCATION_TYPE_PATH)
            locations_df.columns = [c.upper() for c in locations_df.columns]

            victims_type_df = data_processing.get_df_from_csv(VICTIMS_TYPE_PATH)
            victims_type_df.columns = [c.upper() for c in victims_type_df.columns]

            age_df = data_processing.get_df_from_csv(AGE_PATH)
            age_df.columns = [c.upper() for c in age_df.columns]

            race_df = data_processing.get_df_from_csv(RACE_PATH)
            race_df.columns = [c.upper() for c in race_df.columns]

            ethnicity_df = data_processing.get_df_from_csv(ETHNICITY_PATH)
            ethnicity_df.columns = [c.upper() for c in ethnicity_df.columns]

            relationship_df = data_processing.get_df_from_csv(RELATIONSHIP_PATH)
            relationship_df.columns = [c.upper() for c in relationship_df.columns]

            ## Merge victim_offense table with offense table
            combined_df = data_processing.merge_data(victims_offense_df, offense_df, 'OFFENSE_ID', 'left')

            if 'DATA_YEAR_y' in combined_df.columns:
                combined_df = combined_df.drop('DATA_YEAR_y', axis=1)

            if 'OFFENSE_TYPE_ID_y' in combined_df.columns:
                combined_df = data_processing.rename_columns(combined_df, 'OFFENSE_TYPE_ID_y', 'OFFENSE_TYPE_ID')

            if 'INCIDENT_ID_y' in combined_df.columns:
                combined_df = data_processing.rename_columns(combined_df, 'INCIDENT_ID_y', 'INCIDENT_ID')

            # Merge with offense_type table
            combined_df = data_processing.merge_data(combined_df, offense_type_df, 'OFFENSE_TYPE_ID', 'left')

            # # query HT data
            # ht_df = combined_df.query("OFFENSE_TYPE_ID == 59 or OFFENSE_TYPE_ID == 60")
            # # extract the list of IncidentID from OFFENSE_TYPE_ID == 59 or OFFENSE_TYPE_ID == 60
            # ht_incident_list = ht_df['INCIDENT_ID'].values.tolist()
            # combined_df = combined_df[combined_df['INCIDENT_ID'].isin(ht_incident_list)]

            ## Merge with victims table
            combined_df = data_processing.merge_data(combined_df, victims_df, 'VICTIM_ID', 'left')

            rename_dict = {
                'INCIDENT_ID_x': 'INCIDENT_ID',
                'FF_LINE_NUMBER_x': 'FF_LINE_NUMBER',
                'AGE_ID': 'VICTIM_AGE_ID',
                'AGE_NUM': 'VICTIM_AGE_NUM',
                'SEX_CODE': 'VICTIM_SEX_CODE',
                'RACE_ID': 'VICTIM_RACE_ID',
                'ETHNICITY_ID': 'VICTIM_ETHNICITY_ID',
                'RESIDENT_STATUS_CODE': 'VICTIM_RESIDENT_STATUS_CODE',
                'AGE_RANGE_LOW_NUM': 'VICTIM_AGE_RANGE_LOW_NUM',
                'AGE_RANGE_HIGH_NUM': 'VICTIM_AGE_RANGE_HIGH_NUM',
            }

            for k, v in rename_dict.items():
                combined_df = data_processing.rename_columns(combined_df, k, v)

            if 'INCIDENT_ID_y' in combined_df.columns:
                combined_df = combined_df.drop('INCIDENT_ID_y', axis=1)

            if 'FF_LINE_NUMBER_y' in combined_df.columns:
                combined_df = combined_df.drop('FF_LINE_NUMBER_y', axis=1)

            if 'DATA_YEAR_x' in combined_df.columns:
                combined_df = combined_df.drop('DATA_YEAR_x', axis=1)

            # Merge with offender table
            combined_df = data_processing.merge_data(combined_df, offenders_df, 'INCIDENT_ID', 'left')

            rename_dict = {
                'AGE_ID': 'OFFENDERS_AGE_ID',
                'AGE_NUM': 'OFFENDERS_AGE_NUM',
                'SEX_CODE': 'OFFENDERS_SEX_CODE',
                'RACE_ID': 'OFFENDERS_RACE_ID',
                'ETHNICITY_ID': 'OFFENDERS_ETHNICITY_ID',
                'RESIDENT_STATUS_CODE': 'OFFENDERS_RESIDENT_STATUS_CODE',
                'AGE_RANGE_LOW_NUM': 'OFFENDERS_AGE_RANGE_LOW_NUM',
                'AGE_RANGE_HIGH_NUM': 'OFFENDERS_AGE_RANGE_HIGH_NUM',
                'FF_LINE_NUMBER_x': 'FF_LINE_NUMBER'
            }

            # Rename Offenders' demographic data
            for k, v in rename_dict.items():
                combined_df = data_processing.rename_columns(combined_df, k, v)

            if 'FF_LINE_NUMBER_y' in combined_df.columns:
                combined_df = combined_df.drop('FF_LINE_NUMBER_y', axis=1)

            # Merge with Incident table
            combined_df = data_processing.merge_data(combined_df, incidents_df, 'INCIDENT_ID', 'left')

            if 'FF_LINE_NUMBER_y' in combined_df.columns:
                combined_df = combined_df.drop('FF_LINE_NUMBER_y', axis=1)
            if 'DATA_YEAR_x' in combined_df.columns:
                combined_df = combined_df.drop('DATA_YEAR_x', axis=1)
            if 'DATA_YEAR_y' in combined_df.columns:
                combined_df = combined_df.drop('DATA_YEAR_y', axis=1)

            # Merge with agencies csv
            combined_df = data_processing.merge_data(combined_df, agencies_df, 'AGENCY_ID', 'left')

            if 'DATA_YEAR_x' in combined_df.columns:
                combined_df = data_processing.rename_columns(combined_df, 'DATA_YEAR_x', 'DATA_YEAR')
            if 'DATA_YEAR_y' in combined_df.columns:
                combined_df = combined_df.drop('DATA_YEAR_y', axis=1)

            # Merge with Victim_Offender Relation table
            combined_df = data_processing.merge_data(combined_df, relations_df, ['VICTIM_ID', 'OFFENDER_ID'], 'left')

            if 'DATA_YEAR_y' in combined_df.columns:
                combined_df = combined_df.drop('DATA_YEAR_y', axis=1)
            if 'DATA_YEAR_x' in combined_df.columns:
                combined_df = data_processing.rename_columns(combined_df, 'DATA_YEAR_x', 'DATA_YEAR')

            ## Lookup values
            combined_df.insert(6, 'LOCATION_NAME', combined_df['LOCATION_ID'].map(locations_df.set_index('LOCATION_ID')
                                                                                  ['LOCATION_NAME']))
            combined_df.insert(19, 'VICTIM_TYPE_NAME',
                               combined_df['VICTIM_TYPE_ID'].map(victims_type_df.set_index('VICTIM_TYPE_ID')
                                                                 ['VICTIM_TYPE_NAME']))
            combined_df.insert(24, 'VICTIM_AGE_NAME', combined_df['VICTIM_AGE_ID'].map(age_df.set_index('AGE_ID')
                                                                                       ['AGE_NAME']))
            combined_df.insert(28, 'VICTIM_RACE_DESC', combined_df['VICTIM_RACE_ID'].map(race_df.set_index('RACE_ID')
                                                                                         ['RACE_DESC']))
            combined_df.insert(30, 'VICTIM_ETHNICITY_NAME', combined_df['VICTIM_ETHNICITY_ID'].map(ethnicity_df.
                                                                                                   set_index(
                'ETHNICITY_ID')
                                                                                                   ['ETHNICITY_NAME']))
            combined_df.insert(37, 'OFFENDERS_AGE_NAME', combined_df['OFFENDERS_AGE_ID'].map(age_df.set_index('AGE_ID')
                                                                                             ['AGE_NAME']))
            combined_df.insert(40, 'OFFENDERS_RACE_DESC',
                               combined_df['OFFENDERS_RACE_ID'].map(race_df.set_index('RACE_ID')
                                                                    ['RACE_DESC']))
            combined_df.insert(41, 'OFFENDERS_ETHNICITY_NAME', combined_df['OFFENDERS_ETHNICITY_ID'].map(ethnicity_df.
                                                                                                         set_index(
                'ETHNICITY_ID')['ETHNICITY_NAME']))
            combined_df.insert(64, 'RELATIONSHIP_CODE', combined_df['RELATIONSHIP_ID'].map(
                relationship_df.set_index('RELATIONSHIP_ID')['RELATIONSHIP_CODE']))
            combined_df.insert(65, 'RELATIONSHIP_NAME', combined_df['RELATIONSHIP_ID'].map(
                relationship_df.set_index('RELATIONSHIP_ID')['RELATIONSHIP_NAME']))

            # extract relation family from the dict
            combined_df = data_processing.extract_relations_family(combined_df)

            # Add a DATA_YEAR column
            combined_df['YEAR'] = year

            # Factorize ID columns

            # Append to the dataframe
            df = df.append(combined_df)

    # Remove weird columns
    if '0' in df.columns:
        df = df.drop('0', axis=1)
    elif 0.1 in df.columns:
        df = df.drop('0.1', axis=1)
    elif '0' in df.columns and 0.1 in df.columns:
        df = df.drop(['0', '0.1'], axis=1)
    else:
        pass

    # rename column names
    df.columns = df.columns.str.replace(".", "_")

    data_processing.export_to_csv(df, outputDir + '/' + state + '.csv')
    print('Data is exported as csv')

    return df

# Run this code to start the process
crawl_data_from_s3.get_data()
process_data_folders()
