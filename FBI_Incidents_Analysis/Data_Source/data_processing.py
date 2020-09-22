import pandas as pd

relations_family = {"SE": "Within Family",
                    "CS": "Within Family",
                    "PA": "Within Family",
                    "SB": "Within Family",
                    "CH": "Within Family",
                    "GP": "Within Family",
                    "GC": "Within Family",
                    "IL": "Within Family",
                    "SP": "Within Family",
                    "SC": "Within Family",
                    "SS": "Within Family",
                    "OF": "Within Family",
                    "AQ": "Outside Family But Known to Victim",
                    "FR": "Outside Family But Known to Victim",
                    "NE": "Outside Family But Known to Victim",
                    "BE": "Outside Family But Known to Victim",
                    "BG": "Outside Family But Known to Victim",
                    "CF": "Outside Family But Known to Victim",
                    "XS": "Outside Family But Known to Victim",
                    "EE": "Outside Family But Known to Victim",
                    "ER": "Outside Family But Known to Victim",
                    "OK": "Outside Family But Known to Victim",
                    "RU": "Not Known By Victim",
                    "ST": "Not Known By Victim",
                    "VO": "Other",
                    "HR": "Homosexual Relationship"}


def get_df_from_csv(path):
    '''
    Import csv data as a DataFrame
    :param path: Path of the csv file
    :return: pd.Dataframe
    '''
    return pd.read_csv(path)


def merge_data(dataframe1, dataframe2, merge_criteria, merge_method):
    '''
    Merge datasets by id
    :param dataframe1: main dataframe
    :param dataframe2: dataframe to be merged to the main dataframe
    :param merge_criteria: Column or index level names to join dfs
    :param merge_method: Type of merge to be performed, e.g. left, right, inner, outer
    :return: a combined dataframe
    '''
    combined_df = dataframe1.merge(dataframe2, on=merge_criteria, how=merge_method)
    return combined_df


def rename_columns(document, ori_column, new_column):
    '''
    :param document: a pandas dataframe
    :param ori_column: original column name
    :param new_column: New column name
    :return:
    '''
    document = document.rename(columns={ori_column: new_column})
    return document


def extract_relations_family(document):
    document['Relationship_Family'] = document['RELATIONSHIP_CODE'].replace(relations_family, inplace=False)
    return document


def export_to_csv(document, filename):
    return document.to_csv(filename)


