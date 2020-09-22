import os
import shutil

## These variables are used to build the download link. It's not likely to change. Please keep it as it is.
awsUrl = 'http://s3-us-gov-west-1.amazonaws.com/cg-d3f0433b-a53e-4934-8b94-c678aa2cbaf3'
awsUrl2017 = 'http://s3-us-gov-west-1.amazonaws.com/cg-d4b776d0-d898-4153-90c8-8336f86bdfec'

path = os.getcwd()

## These variables are used to download the data. Change the values to refine the criteria
# Setting output directory for crawl data
crawl_outputDir = path + "/crawl_data/"
tempOutputDir = path + "/temp_crawl_data/"

# setting input directory of extracted data for data processing
inputDir = path + "/crawl_data/"

# Setting output directory for clean data
outputDir = path + "/crawl_data_output/"
if os.path.exists(outputDir):
    shutil.rmtree(outputDir)
print(outputDir)
os.makedirs(outputDir)

# Select states
states = ["WI"]

# Select years
start_year = 2012
end_year = 2019
