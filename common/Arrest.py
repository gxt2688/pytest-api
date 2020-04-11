import json
from common.logger import Logger

class Assertions:
    def __init__(self):
        self.log=Logger(logger='Assertions').getlog()
    def assert_code(self,code,expected_code):
        try:
            assert code==expected_code
            return True
        except:
            self.log.error("statusCode error,expected_code is %s, statusCode is %s"%(expected_code,code))
            raise
    def assert_body(self,body,body_msg,expected_msg):
        try:
            msg=body[body_msg]
            assert msg==expected_msg
            return True
        except:
            self.log.error("Response body msg!=expected_msg,expected_msg is %s,body_msg is %s"%expected_msg)
            raise
    def assert_in_text(self,body,expect_msg):
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert expect_msg in text
            return True
        except:
            self.log.error("Response body Does not contain expected_msg,expected_msg is %s" % expect_msg)
            raise
    def assert_text(self,body,expect_msg):
        try:
            assert body==expect_msg
            return True
        except:
            self.log.error("Response body !=expected_msg is %s,body is %s"%(expect_msg,body))
            raise
    def assert_time(self,time,expect_time):
        try:
            assert time<expect_time
            return True
        except:
            self.log.error("Response time>expect_time,expect_time is %s ，time is %s "%(expect_time,time))
            raise 



