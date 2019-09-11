# xcel2yaml

This is a simple python script to convert an excel spreadsheet to yaml format.
Initially it was built for use with Cisco pyATS but most likely can be used in other tools that use yaml files.
I build it in a python3 virtual environment to isolate it from any host OS python packages you may have.

Usage:
python get_routers.py {testbed_name} {excel_file_name} {router_uname} {router_password}

Sample:
python ger_routers.py MyTestBed routers.xlsx cisco cisco

To install:

1.  Clone the repository
2.  Build a virtual environment
    a. virtualenv -p python3 venv
3. Install python packages
    a. pip install -r requirements.txt
    
    
