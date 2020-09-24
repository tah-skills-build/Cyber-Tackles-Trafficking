# FBI Incidents Analysis

## Welcome!
Welcome, SkillsBuild learner, and congratulations on making it to the project-based learning component of the Cyber Tackles Trafficking learning plan!

Completing this project will give you some hands-on experience working with a real human trafficking-related dataset; specifically, human trafficking incidents that were reported by the United States Federal Bureau of Investigations (FBI).

What you've learned in SkillsBuild so far should provide a solid foundation for completing this project. In the Jupyter Notebook* environment where you'll be doing the FBI data analysis (and in what follows on this page), you'll get all the additional guidance you'll need to succeed.

To start with, we suggest you click the green button ("Read the Guide") at the top of this page, which will help orient you to GitHub and GitHub lingo such as "repository." It'll take about 10 minutes.

After that, go through each section below to understand more about the project you'll be working on, and the steps you'll need to take to begin your analysis and complete the project within Jupyter Notebook.

_*Jupyter Notebook: a free web application where you can work with data (cleaning, visualization, etc.), while receiving guidance directly within the coding interface. More information below!_

## Repository
A GitHub repository is essentially a place where projects - such as the one you're about to work on - are organized, and where project resources can be found.

<b> Right now, you are in a GitHub repository called "Cyber Tackles Trafficking,"</b> which contains resources to help you complete the "FBI Incidents Analysis" project for SkillsBuild learners. <br>

If you scroll up, you'll see all the resources that have been provided for this project - for example, there's a folder called "Data Source" (which contains the code to crawl and preprocess the FBI incidents data); a file called "README.md" (which is what you're reading right now); and another file called "HumanTrafficking_Incidents_Analysis.ipynb". You don't need to understand what each of these are for right now; they'll be explained as you go along.  

## Data Source
The data for this project comes from the FBI Crime Data Explorer (CDE): https://crime-data-explorer.fr.cloud.gov/downloads-and-docs. Take a few minutes to visit this site and read about the Crime Data Explorer. 

## Analysis
As mentioned above, Jupyter Notebook is where you'll actually complete this project and do your analysis.

<b>Important Note:</b> For first time users of Jupyter Notebook, please refer to https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html for installation procedures. You'll need to install Jupyter Notebook before moving on to "Project Instructions" below.

## Project Instructions

Ok, let's get started on the actual project! 

<b>STEP 1:</b><br>
Clone the Cyber Tackles Trafficking GitHub repository (the one you're in right now) to your local computer, by following these steps:<br>
   1. Create a folder on your computer for your project e.g. HumanTrafficking<br>
   2. Open command line (Not sure how? Read [this](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955)!)<br>
   3. In the command line interface, type the letters cd, and then paste your project folder link (e.g., if you saved your folder in "Documents" on your C drive, then you'd type <code> cd C:/Documents/HumanTrafficking</code>), then and click Enter
   4. You are now in your project directory. The next step is to copy and paste the following into the command line interface: <code>git clone https://github.com/tah-skills-build/Cyber-Tackles-Trafficking.git</code> (Here is a guide to help you understand this step: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
   5. You will be prompted to provide user name and password<br>
   6. Click Enter<br>
   7. All files are now cloned to your project directory (i.e., the folder on your local machine that you created in step 1 above)!<br>
   
<b>STEP 2:</b>    
In settings.py in the Data_Source folder (which is now located within the project directory on your local computer, e.g., C:/Documents/HumanTrafficking), update the state abbreviations, start_year and end_year to define what data to download

<b>STEP 3:</b> <br>
<b>For Mac users</b><br>
On command line, cd to your project directory (as you did above: e.g., type cd C:/Documents/HumanTrafficking on command line). 
Run <code>
		sh setup.sh
	</code>
		on the terminal to install python requirements, download the data from the FBI website for the state and the years specified in step 2. 
		The data is then cleaned up and stored locally in the crawl_data_output folder (Update the directory in the settings.py to change the location)<br>	
<br><b>For windows users</b><br>
On command line, cd to your project directory. 
   Run <code>
		setup.bat
	</code> on the command line to install python requirements, download the data from the FBI website for the state and the years specified in step 2. 
		The data is then cleaned up and stored locally in the crawl_data_output folder (Update the directory in the settings.py to change the location)<br>
		
<b>STEP 4:</b><br>
After step 3, run <code>
	  jupyter notebook
	</code> on the command line to launch the notebook
	
<b>STEP 5:</b><br>
In the notebook, you can import the dataset and follow the specific instructions to run the analysis

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

Once you've launched Jupyter Notebook you will find the following analyses:
1. Offenses Analysis
2. Offenders Demographics Analysis
3. Victims Demographics Analysis
4. Offenses & Population Relationship Analysis
5. Victims-Offenders Connections
6. Victim-Offender Relationships
