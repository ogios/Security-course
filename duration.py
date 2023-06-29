from settings import *
import requests
import traceback, re

def doStudy(course_id):
    url = f"https://weiban.mycourse.cn/pharos/usercourse/study.do?timestamp={getTime()}"
    data = {
        "tenantCode": TENANT_CODE,
        "userId": USER_ID,
        #         "courseId": "dd86078a-d32f-11eb-9a88-d4ae52bad611",
        "courseId": course_id,
        "userProjectId": USER_PROJECT_ID,
    }
    res = requests.post(url, data=data, headers=HEADERS, cookies=COOKIES)
#     print("doStudy:",res.text)
    return res


def getCourseUrl(course_id):
    url = f"https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do?timestamp={getTime()}"
    data = {
        "tenantCode": TENANT_CODE,
        "userId": USER_ID,
        "userProjectId": USER_PROJECT_ID,
        "courseId": course_id
    }
    res = requests.post(url, data=data, headers=HEADERS, cookies=COOKIES)
#     print("getCourseUrl:",res.text)
    return res


def parseURL(url):
    uci = re.findall("userCourseId=(.*?)&", url)
    mt = re.findall("methodToken=(.*?)&", url)
#     print("UserCourseID:", uci)
#     print("MethodToken:", mt)
    return uci[0], mt[0]


def getVideoHTML(url):
    """
    return: res, m3u8_url
    """
    res = requests.get(url, headers=HEADERS)
#     print("getVideoHTML:", res.text)
    c = re.findall(
        '<source src="(.*?)" type="application/x-mpegURL">', res.text)
#     print("M3U8: ",c)
    return res, c[0]


def getUpdateURL_TS(m3u8_url):
    """
    return: res, update_url, ts_list
    """
    res = requests.get(m3u8_url, headers=HEADERS)
#     print("getKey:", res.text)
    c = re.findall('#EXT-X-KEY:METHOD=AES-128,URI="(.*?)",', res.text)
#     print("updata_url:", c)
    d = re.findall(".*?\.ts", res.text)
#     print("ts:", d)
    return res, c[0], d


def doUpdate(jx_url, update_url, ts):
    base_url = "/".join(jx_url.split("/")[:-1])
    print("base_url:", base_url)
    for i in ts:
        print(f"{ts.index(i)+1}/{len(ts)}", end=" | ")
        res = requests.get(update_url)
        if res.status_code != 200:
            print("update fatal")
            return res
        res = requests.get(base_url + f"/{i}")
        if res.status_code != 200:
            print("get ts fatal")
            return res
    print("done.")


def finishVideo(user_course_id, method_token):
    url = f"https://weiban.mycourse.cn/pharos/usercourse/v1/{method_token}.do"
    params = {
        # "callback": f"jQuery34109530937163545008_{}",
        "userCourseId": user_course_id,
        "tenantCode": TENANT_CODE,
        "_": int(getTime()*100)
    }
    res = requests.get(url, params=params, headers=HEADERS, cookies=COOKIES)
    print("finishVideo:", res.text)
    return res
