from meeting.models.thread import update


def get_agendas():
    BBS_ARRAY = update()
    length = len(BBS_ARRAY)
    agendas = []
    for i in range(0, length):
        element = BBS_ARRAY[length - i - 1][0]
        if element.startswith("--"):
            agendas = BBS_ARRAY[length - i - 2 : length]
            break

    return agendas
