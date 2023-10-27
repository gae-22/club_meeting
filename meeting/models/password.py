import datetime, random, string
from meeting.models.spread import write_password

password_past = ""


def reload_time():  # 時刻を確認して部会前かどうかを判定
    mtg_time = datetime.time(16, 40, 00)
    mtg_wkdy = 0

    now_time = datetime.datetime.now().time()
    now_wkdy = datetime.datetime.now().weekday()

    return True if now_time > mtg_time and now_wkdy == mtg_wkdy else False


def choose_random():  # ファイルからランダムにパスワードを選択
    pass_path = "./datas/password.txt"

    # ファイルから読み込み
    with open(pass_path, "r") as f:
        lines = f.read().splitlines()

    password = random.choice(lines)
    write_password(password)
    return password


def randomname(n):
    global password_past
    password = ""

    if reload_time():  # 月曜16:40以降にはパスワードは変更しない
        password = password_past
    elif password == "":  # 月曜16:40以前にはパスワードを変更する
        password = choose_random()

    if password == 1:
        # ランダム生成
        randlst = [
            random.choice(string.ascii_lowercase + string.digits) for i in range(n)
        ]
        password_past = password = "".join(randlst)
        write_password(password)

    return password
