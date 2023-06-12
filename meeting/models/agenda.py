from meeting.models.wikiScraping import update

BBS_ARRAY = update()
length = len(BBS_ARRAY)


def get_agendas():
    agendas = []
    for i in range(0, length):
        element = BBS_ARRAY[length - i - 1][0]
        if element.startswith("--"):
            agendas = BBS_ARRAY[length - i - 2 : length]
            break

    return agendas
