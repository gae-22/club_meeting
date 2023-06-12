import requests, re
from bs4 import BeautifulSoup
from datetime import datetime


def update():
    WIKI_USER = "gae"
    WIKI_PASS = "Golfpolo9658"

    current_year = datetime.now().year
    current_month = datetime.now().month
    if current_month <= 3:
        current_year -= 1

    BBS_URL = (
        "https://wiki.mma.club.uec.ac.jp/bbs/%E9%83%A8%E4%BC%9A%E3%82%B9%E3%83%AC"
        + str(current_year)
        + "/?action=login"
    )

    login_info = {
        "name": WIKI_USER,
        "password": WIKI_PASS,
        "login": "ログイン",
        "login": "ログイン",
    }

    session = requests.session()
    res = session.post(BBS_URL, data=login_info)
    soup = BeautifulSoup(res.content, "html.parser")

    tbody = soup.find("tbody")
    mat = []
    trs = tbody.find_all("tr")
    for tr in trs:
        r = []
        for td in tr.find_all("td"):
            instead = [
                "<td>",
                "</td>",
                "<strong>",
                "</strong>",
                '<td colspan="3" style="text-align: center;">',
                '<td colspan="3" style="text-align: left;">',
                "</a>",
            ]
            td = str(td).replace("<br/>", "\n")
            td = re.sub(r"<a href=(.*?)\">", "", td)
            for item in instead:
                td = str(td).replace(item, "")
            r.append(td)
        mat.append(r)

    return mat[0:-1]
