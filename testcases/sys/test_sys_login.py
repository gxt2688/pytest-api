from common.commonDate import CommonData
from conftest import http
import allure

allure.feature("登录模块")
class Test_login():
    @allure.story("登录成功")
    def test_login_success(self):
        path="/api/auth/login"
        data={'username':CommonData.mobile,
              'password':CommonData.password}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'

    @allure.story("登录失败")
    def test_login_fail(self):
        path = "/api/auth/login"
        data = {'username': 123,
                'password': CommonData.password}
        resp = http.post(path, data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'