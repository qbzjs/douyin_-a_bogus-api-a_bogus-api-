import urllib.parse

import requests

params = {"device_platform": "webapp", "aid": "6383", "channel": "channel_pc_web", "publish_video_strategy_type": "2",
          "source": "channel_pc_web",
          "sec_user_id": "MS4wLjABAAAAymEThRftAJXz_lZyeqNpVlVGmc94mYZWrbCxIXGbToai4k5kuDGr_Z9ovF52P4GC",
          "personal_center_strategy": "1", "update_version_code": "170400", "pc_client_type": "1",
          "version_code": "170400", "version_name": "17.4.0", "cookie_enabled": "true", "screen_width": "1920",
          "screen_height": "1080", "browser_language": "zh-CN", "browser_platform": "Linux+x86_64",
          "browser_name": "Chrome", "browser_version": "124.0.0.0", "browser_online": "true", "engine_name": "Blink",
          "engine_version": "124.0.0.0", "os_name": "Linux", "os_version": "x86_64", "cpu_core_num": "4",
          "device_memory": "8", "platform": "PC", "downlink": "1.5", "effective_type": "3g", "round_trip_time": "600",
          "webid": "7346392148281640502"}

ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# 1
try:
    response = requests.post("https://abogus.jackluson.workers.dev/", json={
        "url": urllib.parse.urlencode(params),
        "data": "",
        "ua": ua,
    }, timeout=3, proxies={"https": "http://192.168.20.66:10809"})
    a_bogus = response.json()["res"]["abogus"]
except:
    a_bogus = ""

print("1:  {}  {}".format(a_bogus, len(a_bogus)))

# 2 (部分接口无效)
try:
    def json_to_url_params(json_data):
        url_params = ""
        for key, value in json_data.items():
            url_params += key + "=" + str(value) + "&"
        return url_params[:-1]


    resp = requests.post("http://47.98.247.93:6655/api/v1/ab/info", json={
        "params": json_to_url_params(params),
        "user_agent": ua,
    })
    a_bogus = resp.json()["data"]["a_bogus"]
except:
    a_bogus = ""

print("2:  {}  {}".format(a_bogus, len(a_bogus)))

# 3
try:
    resp = requests.post("http://39.107.101.62:8111/dy/abogus/", json={
        "params": urllib.parse.urlencode(params),
        "data": "",
        "ua": ua,
        "index_0": 0,
        "index_1": 1,
        "index_2": 14
    })
    a_bogus = resp.json()["a_bogus"]
except:
    a_bogus = ""
print("3:  {}  {}".format(a_bogus, len(a_bogus)))

# 4 # 接口速度慢
try:
    url = "https://live.douyin.com/aweme/v1/web/user/following/list/"
    resp = requests.post("https://beta.tikhub.io/api/v1/douyin/web/generate_a_bogus", json={
        "url": url + "?" + urllib.parse.urlencode(params),
        "data": "",
        "user_agent": ua,
    }, timeout=3)
    new_url = resp.json()["data"]["url"]
    a_bogus = resp.json()["data"]["a_bogus"]
    a_bogus = urllib.parse.unquote(a_bogus)
except:
    a_bogus = ""
print("4:  {}  {}".format(a_bogus, len(a_bogus)))
