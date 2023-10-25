import random, string
import datetime

password_past = ""


def reload_time():
    mtg_time = datetime.time(16, 40, 0)
    mtg_wkdy = 0

    now_time = datetime.datetime.now().time()
    now_wkdy = datetime.datetime.now().weekday()

    return True if now_wkdy == mtg_wkdy and now_time < mtg_time else False


def randomname(n):
    global password_past
    if reload_time():
        randlst = [
            random.choice(string.ascii_lowercase + string.digits) for i in range(n)
        ]
        password_past = password = "".join(randlst)
    else:
        password = password_past

    return password
