from settings import *
from duration import doStudy, doUpdate, getCourseUrl, parseURL, finishVideo
from course import getUndoneCourse, getUndoneSeps

def finishOne(tmp_course_id):
    tmp_do_study = doStudy(tmp_course_id)
    print(tmp_do_study)
    tmp_get_url = getCourseUrl(tmp_course_id)
    print(tmp_get_url)
    tmp_user_course_id, tmp_method_token = parseURL(tmp_get_url.json()["data"])
    print(tmp_user_course_id, "|", tmp_method_token)
#     tmp_html, tmp_m3u8_url = getVideoHTML(tmp_get_url.json()["data"])
#     print(tmp_m3u8_url)
#     tmp_m3u8, tmp_update_url, tmp_ts_list = getUpdateURL_TS(tmp_m3u8_url)
#     print(tmp_update_url, "|", tmp_ts_list)
#     res = doUpdate(tmp_m3u8_url, tmp_update_url, tmp_ts_list)
    tmp_finish_video = finishVideo(tmp_user_course_id, tmp_method_token)
    print(tmp_finish_video)

def _main():
    seps = getUndoneSeps()
    print(seps)

    courses = getUndoneCourse(seps[0])
    print(courses,"-",courses[0])
    finishOne(courses[0])
    time.sleep(5)
    # courses = getUndoneCourse(seps[1])
    # print(courses)

def main():
    # seps = getUndoneSeps()
    # while seps:
    _main()

if __name__ == "__main__":
    main()
