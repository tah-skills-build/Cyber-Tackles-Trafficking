import os
import shutil
import requests
from zipfile import ZipFile
from settings import *


def create_folder_directories(crawl_outputDir):
    '''
    :param outDir: the directory for storing output
    :return:
    '''
    if not os.path.exists(crawl_outputDir):
        os.mkdir(crawl_outputDir)

    for state in states:
        try:
            if os.path.exists(crawl_outputDir + state + '/'):
                shutil.rmtree(crawl_outputDir + state + '/')
            os.mkdir(crawl_outputDir + state + '/')
        except OSError as err:
            print("Creation of the directory %s failed" % crawl_outputDir, err)
        else:
            print("Successfully created the directory %s " % crawl_outputDir)


def build_URL(state, year):
    '''
    :param state: the state abbreviation of the data extracted
    :param year: the year required
    :return: url for data download
    '''
    url = None
    if year >= 2016:
        url = awsUrl2017
    else:
        url = awsUrl

    year = str(year)
    return url + "/" + year + "/" + state + "-" + year + '.zip'


def download_to_temp_dir():
    outDir = tempOutputDir
    create_folder_directories(outDir)
    for state in states:
        for year in range(start_year, end_year):
            download_data(state, year, outDir)


def get_data():
    # Create a temp folder
    download_to_temp_dir()

    # Check if the directory exists
    if os.path.exists(crawl_outputDir):
        print('The path exists')
        # Delete the directory
        shutil.rmtree(crawl_outputDir)

    shutil.copytree(tempOutputDir, crawl_outputDir)

    # Call cleanup method
    for state in states:
        for year in range(start_year, end_year):
            cleanup(state, year)


def cleanup(state, year):
    '''
    :param state: the state abbreviation of the data extracted
    :param year: year
    :return: data folders with consistent files
    '''
    filename = crawl_outputDir + state + '/' + state + '_' + str(year) + ".zip"

    ## Unzip the file
    folder = crawl_outputDir + state + '/' + state + '_' + str(year)
    with ZipFile(filename, 'r') as zip_file:
        # extracting all the files
        print('Extracting all the files now...')
        zip_file.extractall(folder)  # extract file to dir

        # move the files into the folder
        src = crawl_outputDir + state + '/' + state + '_' + str(year) + '/' + state
        if os.path.exists(src):
            # print("this path has directory")
            tempDir = crawl_outputDir + "temp"
            shutil.move(src, tempDir)
            shutil.rmtree(folder)
            shutil.move(tempDir, folder)

        else:
            print("this path has no directory")

        # uppercase
        uppercase_filenames(folder)

        # rename file names
        rename_filesnames(folder)

        zip_file.close()  # close file
        os.remove(filename)  # delete zipped file
        # print('Done!')


def download_data(state, year, crawl_outputDir):
    '''
    :param state: the state abbreviation of the data extracted
    :param year: the year
    :param outDir: the directory to store the extracted data
    :return:
    '''
    url = build_URL(state, year)
    r = requests.get(url, verify=False, stream=True)
    r.raw.decode_content = True

    if r.status_code == 200:
        filename = crawl_outputDir + state + '/' + state + '_' + str(year) + ".zip"
        with open(filename, 'wb') as out_file:
            out_file.write(r.content)


def uppercase_filenames(folder):
    '''
    :param folder: the folders containing files for converting to uppercase
    :return: All filenames in the folder are in uppercase
    '''
    for fname in os.listdir(folder):
        name, ext = os.path.splitext(fname)
        os.rename(os.path.join(folder, fname), os.path.join(folder, name.upper() + ext))


def rename_filesnames(folder):
    '''
    :param folder: data folder containing the files
    :return: renamed files in the folder
    '''
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        if 'CDE_AGENCIES' in name:
            os.rename(os.path.join(folder, filename), os.path.join(folder, 'AGENCIES' + ext))



