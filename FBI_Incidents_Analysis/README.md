# FBI Incidents Analysis
This is a research project on incidents reported by the FBI. 

This repository contains two folders - Data_Source and Notebooks<br>
<b>Data_Source</b> folder contains the code to crawl, preprocess data (data merge, and clean up) <br>
<b>Notebooks</b> folder contains the code to run the analysis

## Analysis
In the notebook, users will find the following analyses
1. Offenses Analysis
2. Offenders Demographics Analysis
3. Victims Demographics Analysis
4. Offenses & Population Relationship Analysis
5. Victims-Offenders Connections
6. Victim-Offender Relationships

## Data Source
The data is obtained from the FBI Crime Data Explorer (CDE) on https://crime-data-explorer.fr.cloud.gov/downloads-and-docs.

## Instructions
1. Clone this repository to your local computer <br>
   a. Create a folder for your project e.g. HumanTrafficking<br>
   b. Open command line<br>
   c. On command line, type cd, paste your project link (e.g. <code> cd C:/Documents/HumanTrafficking</code>), then click Enter<br>
   d. You are now in your project directory, copy and paste <code> git clone https://github.com/TraffikAnalysisHub/FBI_Incidents_Analysis.git </code> on the command line<br>
   e. You will be prompted to provide user name and password<br>
   f. Click Enter<br>
   g. All files are now cloned to your project directory<br>
2. In settings.py in the Data_Source folder, update the state abbreviations, start_year and end_year to define what data to download
3. <b>For Mac users</b><br>
On command line, cd to your project directory. Run <code>
		sh setup.sh
	</code>
		on the terminal to install python requirements, download the data from the FBI website for the state and the years specified in step 2. 
		The data is then cleaned up and stored locally in the crawl_data_output folder (Update the directory in the settings.py to change the location)<br>
   <b>For windows users</b><br>
   On command line, cd to your project directory. 
   Run <code>
		setup.bat
	</code> on the command line to install python requirements, download the data from the FBI website for the state and the years specified in step 2. 
		The data is then cleaned up and stored locally in the crawl_data_output folder (Update the directory in the settings.py to change the location)<br>
4. After step 3, run <code>
	  jupyter notebook
	</code> on the command line to launch the notebook
5. In the notebook, you can import the dataset and follow the specific instructions to run the analysis

## State Abbreviations
In step 2, settings.py contains configurations for the years and the state of data download. Use below abbreviations to set the states variable. <br>
Alabama: AL; 
Arizona: AZ; 
Arkansa: AR; 
Colorado: CO; 
Connecticut: CT; 
Delaware: DE; 
District of Columbia: DC;
Georgia: GA; 
Hawaii: HI; 
Idaho: ID; 
Illinois: IL; 
Indiana: IN; 
Iowa: IA; 
Kansas: KS; 
Kentucky: KY; 
Louisiana: LA; 
Maine: ME; 
Maryland: MD; 
Massachusetts: MA; 
Michigan: MI; 
Minnesota: MN; 
Mississippi: MS; 
Missouri: MO; 
Montana: MT; 
Nebraska: NE; 
New Hampshire: NH; 
New Mexico: NM; 
North Dakota: ND; 
Ohio: OH; 
Oklahoma: OK; 
Oregon: OR;
Pennsylvania: PA; 
Rhode Island: RI; 
South Carolina: SC; 
South Dakota: SD; 
Tennessee: TN; 
Texas: TX; 
Utah: UT; 
Vermont: VT; 
Virginia: VA; 
Washington: WA; 
West Virginia: WV; 
Wisconsin: WI

### Jupyter Notebook
For first time user, please refer to https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html for installation procedures
