from settings import *
import requests
import traceback


def getUndoneSeps():
    url = f"https://weiban.mycourse.cn/pharos/usercourse/listCategory.do?timestamp={getTime()}"
    data = {
        "tenantCode": TENANT_CODE,
        "userId": USER_ID,
        "userProjectId": USER_PROJECT_ID,
        "chooseType": "3"
    }
    res = requests.post(url, data=data, headers=HEADERS, cookies=COOKIES)
    try:
        l = []
        js = res.json()
        for i in js["data"]:
            if i["finishedNum"] == i['totalNum']:
                continue
            l.append(i["categoryCode"])
        return l
    except:
        traceback.print_exc()
        return res


def getUndoneCourse(categoryCode):
    url = f"https://weiban.mycourse.cn/pharos/usercourse/listCourse.do?timestamp={getTime()}"
    data = {
        "tenantCode": TENANT_CODE,
        "userId": USER_ID,
        "userProjectId": USER_PROJECT_ID,
        "chooseType": "3",
        "categoryCode": categoryCode
    }
    res = requests.post(url, data=data, headers=HEADERS, cookies=COOKIES)
    try:
        l = []
        js = res.json()
        for i in js["data"]:
            if i["finished"] == 1:
                continue
            l.append(i["resourceId"])
        return l
    except:
        traceback.print_exc()
        return res
