import requests

# post请求
# pay_load = {loginId: "GXT", password: "123456", orgId: 14}
# response = requests.post("http://acv3.learn.it101.live/api/auth/login",pay_load)
# data = response.json()
# print(data)
# assert  data['ok'] == True

#get请求
# header = {"ac-token":"SdrbddskxixX9ZM7gSUkzi2j8msIBWLW"}
# response = requests.get("http://acv3.learn.it101.live/api/courses/v3/trends",headers = header)
# data = response.json()
# print(data)
# assert  data['ok'] == True


# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n---------HTTP response *begin-------')
    print(response.status_code)  # 获取状态码

    # 获取所有响应头相关的所有信息 response.headers.items()
    for k, v in response.headers.items():  # 遍历输出键值对
        print(f'{k}:{v}')
    print(' ')

    print(response.content.decode('utf8'))   #获取响应实体，相当于上边的print(data)
    print('\n\n---------HTTP response *end-------')
#使用session
session = requests.session()
# 登录
pay_load = {"loginId": "gxt", "password": "123456", "orgId": 14}
response = session.post('http://acv3.learn.it101.live/api/auth/login', pay_load)
printResponse(response)
# 获取最近学习动态
response = session.get('http://acv3.learn.it101.live/api/courses/v3/trends')
printResponse(response)
# 获取课程列表
response = session.get('http://acv3.learn.it101.live/api/courses/v3/myCourses')
printResponse(response)
# 获取最近学习小节
response = session.get('http://acv3.learn.it101.live/api/learning/v3/184/recentLesson')
printResponse(response)
# 获取课程角色
response = session.get('http://acv3.learn.it101.live/api/courses/v3/184/courseRole/')
printResponse(response)
# 获取课程详情
response = session.get('http://acv3.learn.it101.live/api/courses/v3/184/detail')
printResponse(response)
# 获取菜单
response = session.get('http://acv3.learn.it101.live/api/courses/v3/184/modules/')
printResponse(response)
# 获取大纲
response = session.get('http://acv3.learn.it101.live/api/courses/v3/184/chapters')
printResponse(response)
# 获取章节
response = session.get('http://acv3.learn.it101.live/api/courses/v3/184/chapters')
printResponse(response)
# 获取小节详情
response = session.get('http://acv3.learn.it101.live/api/courses/v3/184/statistics/teacher/lesson')
printResponse(response)

# 退出登录
response = session.get('http://acv3.learn.it101.live/api/auth/logout')
printResponse(response)