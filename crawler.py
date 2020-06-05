import requests
import shutil
import time
import urllib.parse
from urllib.request import urlopen, Request


def getTotalWorks(keyword):
    """
    keyword : (type == string) The keyword string from user input. \n
    return JSON["body"]["illustManga"]["data"]["total"] : (type == int) Return the total amounts of work which
    located at JSON. \n
    """

    keyword = urllib.parse.quote_plus(keyword)
    URL = (
        "https://www.pixiv.net/ajax/search/artworks/"
        + keyword
        + "?word="
        + keyword
        + "&order=date_d&mode=all&p=1&s_mode=s_tag&type=all"
    )
    headers = {
        "cookie": "__cfduid=d01c6240ac6ccd4b0989c38bb1baec9cb1589713950; first_visit_datetime_pc=2020-05-17+20%3A12%3A30; p_ab_id=2; p_ab_id_2=6; p_ab_d_id=706902938; yuid_b=JwgjliM; privacy_policy_agreement=2; device_token=b8791e3a6a03bd1459846e6400680c14; c_type=23; a_type=1; b_type=0; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; login_ever=yes; tag_view_ranking=4BGj8BYGiZ~Jsc_4Eudwc~qpeZSmEVVP~tgP8r-gOe_~nIDDwVKtJQ~YxYKMgmcme~HQrKJY4TRh~VsImVybebN~k3AcsamkCa~RTJMXD26Ak~PwDMGzD6xn~zj9gD1HFwG~PvCsalAgmW~BRqZEd57W7; PHPSESSID=v162ns0og3i6s463mnjquje2fdds6n1o; login_bc=1; is_sensei_service_user=1; p_b_type=1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "referer": URL,
    }

    # Try to get the website's session or throw an exception
    while True:
        try:
            session = requests.get(URL, headers=headers)
            print("Getting JSON data imformation from " + URL)
            break
        except requests.exceptions.ProxyError:
            print(
                "Time limit exceeded! Please check out your internet connection and try again."
            )
            time.sleep(5)

    JSON = session.json()
    session.close()
    return JSON["body"]["illustManga"]["data"]["total"]


def crawlerMain(keyword, target_directory):
    id_count = sub_id = total_work_count = 0
    page_index = 1
    max_page = 1
    begin_time = int(time.time())

    keyword = urllib.parse.quote_plus(keyword)

    while page_index <= max_page:
        URL = (
            "https://www.pixiv.net/ajax/search/artworks/"
            + keyword
            + "?word="
            + keyword
            + "&order=date_d&mode=all&p=1&s_mode=s_tag&type=all"
        )
        headers = {
            "cookie": "__cfduid=d01c6240ac6ccd4b0989c38bb1baec9cb1589713950; first_visit_datetime_pc=2020-05-17+20%3A12%3A30; p_ab_id=2; p_ab_id_2=6; p_ab_d_id=706902938; yuid_b=JwgjliM; privacy_policy_agreement=2; device_token=b8791e3a6a03bd1459846e6400680c14; c_type=23; a_type=1; b_type=0; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; login_ever=yes; tag_view_ranking=4BGj8BYGiZ~Jsc_4Eudwc~qpeZSmEVVP~tgP8r-gOe_~nIDDwVKtJQ~YxYKMgmcme~HQrKJY4TRh~VsImVybebN~k3AcsamkCa~RTJMXD26Ak~PwDMGzD6xn~zj9gD1HFwG~PvCsalAgmW~BRqZEd57W7; PHPSESSID=v162ns0og3i6s463mnjquje2fdds6n1o; login_bc=1; is_sensei_service_user=1; p_b_type=1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "referer": URL,
        }

        # Try to get the website's session or throw an exception
        while True:
            try:
                session = requests.get(URL, headers=headers)
                print("Getting JSON data imformation from " + URL)
                break
            except requests.exceptions.ProxyError:
                print(
                    "Time limit exceeded! Please check out your internet connection and try again."
                )
                time.sleep(5)
        JSON = session.json()
        session.close()
        while id_count < len(JSON["body"]["illustManga"]["data"]):
            ID = JSON["body"]["illustManga"]["data"][id_count]["id"]
            URL = "https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh_tw"
            while True:
                try:
                    session = requests.get(URL, headers=headers)
                    break
                except requests.exceptions.ProxyError:
                    print(
                        "Time limit exceeded! Please check out your internet connection and try again."
                    )
                    time.sleep(10)
            JSON1 = session.json()
            session.close()
            while sub_id < len(JSON1["body"]):
                target_url = JSON1["body"][sub_id]["urls"]["original"]
                request = Request(target_url, headers=headers)
                filename = target_directory + "/" + str(ID) + "_" + str(sub_id) + ".jpg"
                with urlopen(request) as response, open(filename, "wb") as out_file:
                    shutil.copyfileobj(response, out_file)
                sub_id += 1
                total_work_count += 1
            sub_id = 0
            id_count += 1
            time.sleep(0.5)
        id_count = 0
        page_index += 1
    print(
        "Downloaded total: "
        + str(total_work_count)
        + ", time cost: "
        + str(int(time.time()) - begin_time)
    )
