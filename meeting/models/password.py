import random, string


def randomname(n):
    randlst = [random.choice(string.ascii_lowercase + string.digits) for i in range(n)]
    password = "".join(randlst)

    return password
