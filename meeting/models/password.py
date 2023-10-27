import datetime, random, string
from meeting.models.spread import write_password

password_past = ""


def reload_time():
    mtg_time = datetime.time(16, 40, 00)
    mtg_wkdy = 0

    now_time = datetime.datetime.now().time()
    now_wkdy = datetime.datetime.now().weekday()

    return True if now_time > mtg_time and now_wkdy == mtg_wkdy else False


def choose_random():
    pass_path = "./datas/password.txt"

    with open(pass_path, "r") as f:
        lines = f.read().splitlines()

    password = random.choice(lines)
    write_password(password)
    return password


def randomname(n):
    global password_past
    password = ""

    if reload_time():
        password = password_past
    elif password == "":
        password = choose_random()

    if password == 1:
        randlst = [
            random.choice(string.ascii_lowercase + string.digits) for i in range(n)
        ]
        password_past = password = "".join(randlst)
        write_password(password)

    return password
