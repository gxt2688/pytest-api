import pytest
from common.commonDate import CommonData
from util.HttpUtil import HttpUtil

http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/api/auth/login"
    data={'username':CommonData.mobile,
          'password':CommonData.password}
    resp=http.post(path,data)
    CommonData.token=resp['object']['token']
    print("登录成功！！！！！")