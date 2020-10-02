REM First run to install requirement
pip3 install -r requirements.txt
python3 -m ipykernel install --user

REM Go to the project directory and run main.py
cd Data_Source
python main.py