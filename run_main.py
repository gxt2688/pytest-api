import pytest
import os

if __name__=='__main__':
    pytest.main(['-s','--alluredir','./report/xml'])
    html_report_generate='allure generate report/xml/ -o report/html --clean'
    result=os.system(html_report_generate)