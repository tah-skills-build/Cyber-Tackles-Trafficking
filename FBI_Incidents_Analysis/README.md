# FBI Incidents Analysis

## Welcome!

Welcome, SkillsBuild learner, and congratulations on making it to the project-based learning section of the Cyber Tackles Trafficking learning plan. <br>

So, what is this project all about? 

While the main goal is to get you some hands-on experience working with a real human trafficking dataset (while not requiring any coding expertise), you’ll also get experience navigating GitHub; use Terminal or Command Line to lay the groundwork for data analysis; and become more comfortable using Python and Jupyter Notebook to explore and visualize a dataset. 

There are no right or wrong answers, no assessment, and this data analysis project doesn’t build directly off of what you learned in SkillsBuild (though it’ll certainly help that you went through those courses). It’s more about exploration and discovery. Also, don’t worry if this is your first time using Python or Jupyter Notebook. 

<i>*Jupyter Notebook is a free web application where you can work with data (cleaning, visualization, etc.), while receiving guidance directly within the coding interface. If you want to learn more about Jupyter Notebook, including basic operations, start here https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html</i>

## Repository
So, where are you right now? You’re in a GitHub repository! 

A GitHub repository – this one is called “Cyber Tackles Trafficking”, and it was created for you and other SkillsBuild learners – is a place where projects are organized, and where project resources can be found. 

If you scroll up, you'll see all the resources that have been provided for this data analysis project. It’s ok if you don’t know what these files and folders do.

## Data Source
The data for this project comes from the FBI Crime Data Explorer (CDE): https://crime-data-explorer.fr.cloud.gov/downloads-and-docs. Take a few minutes to visit this site and read about the Crime Data Explorer. You will not need to download any of the data yourself.

## Setup Instructions
Alright, on to the fun stuff. 

Below you’ll find step-by-step instructions to get you set up and ready to do your analysis in Jupyter Notebook. You might get stuck or face some error messages along the way. Don’t worry! Sites like Stack Overflow* can help, and you can also ask for help in the SkillsBuild Tribe Community.

<i>*Often, typing an error message in Google search will point you to a Stack Overflow thread that can help you troubleshoot. We’ve also provided some tips below for what to do if you get stuck at certain points.</i>

<b>STEP 1:</b><br>
You will use the Python programming language to do the data analysis for this project, by running and modifying some code we provide you with in Jupyter Notebook. So, you will need to install Python if you don’t already have it (it’s free). 
 
1.	Go to https://www.python.org/downloads/

2.	Scroll down to the section titled “Looking for a specific release?” and click on the one called Python 3.7.9*

3.	On the Python 3.7.9 page, scroll down to the “Files” table and click on the installer you need in the “Version” column (for Mac, click on macOS 64-bit installer; for Windows, click on Windows x86-64 executable installer)

4.	Follow and complete the Python installation process

<i>*You may also be able to use a different version of Python that you already have installed on your machine. However, given issues we have noticed when attempting to use Python 3.9 for this project, we suggest Python 3.7.9.</i>

<b>STEP 2:</b><br>

Clone the Cyber Tackles Trafficking GitHub repository to your local computer, by following these steps (this sounds more complicated than it is): 

1.	First, check your URL bar to make sure you are here (this is what you’ll need to clone): https://github.com/tah-skills-build/Cyber-Tackles-Trafficking 

2.	Find and click the “Code” button (the green button toward the top right of this page), and then click “Download ZIP”

3.	Save the zip file to your desired location, for example your Desktop

4.	You will now see a project folder called “Cyber-Tackles-Trafficking-master” in your chosen save location, and within that folder another folder called “FBI_Incidents_Analysis”

<b>STEP 3:</b><br>

Open Terminal (Mac) or Command Line (Windows). Not sure how? Read this!

<b>For Mac users</b><br>

1.	In Terminal, cd to the “FBI_Incidents_Analysis” folder by typing the letters cd followed by a space, then entering the address of the folder on your computer (simply right-click on the “FBI_Incidents_Analysis” folder to copy its address, then paste that information in Terminal), then hitting Enter

2.	Next, type sh setup.sh in Terminal and hit Enter, which will install the Python libraries that you’ll need, and will also automatically download the FBI data files for you (take a look at the files called setup.sh, requirements.txt, and main.py in your project folder, to better understand what’s happening here)* 

3.	The FBI data for Wisconsin, 2012-2018, is now cleaned up and stored locally on your computer in the crawl_data_output folder (which can be found within the “Data_Source” folder, located in your “FBI_Incidents_Analysis” folder). When you see “Data is exported as csv” in Terminal, it means the data is now ready for analysis**

<i>*You might see a pop-up asking if you’d like to install “command line developer tools.” If you are not able to complete this process due to receiving an error message, you can instead go here to search for and download Command Line Tools. Once you have Command Line Tools installed, you can go back into Terminal and type sh setup.sh again. </i>

<i>** You might get an error in Terminal that prevents the crawl_data_output folder from being created. If you see “ImportError: No module named requests” in Terminal instead of “Data is exported as csv,” try the following: Type cd Data_Source in Terminal, hit Enter, then type python3.7 main.py and hit Enter. This should solve the problem, and you should now see the crawl_data_output folder within your Data_Source folder.</i>

<b>For Windows users</b><br>

1.	In Command Line, cd to the “FBI_Incidents_Analysis” folder by typing the letters cd followed by a space, then entering the address of the folder on your computer (simply right-click on the “FBI_Incidents_Analysis” folder to copy its address, then paste that information in Command Line), then hitting Enter

2.	Next, type setup.bat in Command Line and hit Enter, which will install the Python libraries that you’ll need, and will also automatically download the FBI data files for you (take a look at the files called setup.bat, requirements.txt, and main.py in your project folder, to better understand what’s happening here)

3.	The FBI data for Wisconsin, 2012-2018, is now cleaned up and stored locally on your computer in the crawl_data_output folder (which can be found within the “Data Source” folder, located in your “FBI_Incidents_Analysis” folder)

4.	When you see “Data is exported as csv” in Command Line, it means the data is now ready for analysis

<b>STEP 4:</b><br>

Finally, cd to your “FBI_Incidents_Analysis” folder again (just like you did in Step 3 above); then type the words jupyter notebook in Terminal or Command Line and hit Enter to launch Jupyter Notebook in your web browser. 

Next, click on the file called “HumanTrafficking_Incidents_Analysis.ipynb” to import the dataset and launch the project notebook – then simply follow the instructions as you go through the notebook to do some basic analysis

Good luck!
