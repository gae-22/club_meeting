import gspread
from meeting.models.agenda import get_agendas

key_name = "./datas/meeting.json"
sheet_name = "部会"
sheet_id = "1SLP8YSEvr7KY5J5g4SNAC4xaaRrCfoFStgmxBl1xkao"


def write_password(password):
    sheet_name = "概要"
    gc = gspread.service_account(filename=key_name)
    wks = gc.open_by_key(sheet_id).worksheet(sheet_name)
    wks.update_cell(8, 2, password)


def write_agenda():
    sheet_name = "質問"
    gc = gspread.service_account(filename=key_name)
    wks = gc.open_by_key(sheet_id).worksheet(sheet_name)
    agendas = get_agendas()
    k = 3
    cnt = 0
    for agenda in agendas:
        cnt += 1
        if cnt % 2 == 0:
            agenda = agenda[0]
            idx = agenda.find("+")
            agenda = agenda[idx + 1 :]
            idx = agenda.find("\n")
            agenda = agenda[:idx]
            if "告知" not in agenda:
                wks.update_cell(k, 1, agenda)
                k += 1
