# xcel2yaml

This is a simple python script to convert an excel spreadsheet to yaml format.
Initially it was built for use with Cisco pyATS but most likely can be used in other tools that use yaml files.
I build it in a python3 virtual environment to isolate it from any host OS python packages you may have.

Usage:
python get_routers.py {testbed_name} {excel_file_name} {router_uname} {router_password}

Sample:
python get_routers.py MyTestBed routers.xlsx cisco cisco


    
    
