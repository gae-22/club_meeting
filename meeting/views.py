from flask import redirect, render_template, request, session, url_for
from meeting import app
from meeting.models.wikiScraping import update
from meeting.models.agenda import get_agendas
from meeting.models.form import Ragistration


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/thread")
def thread():
    BBS_ARRAY = update()
    return render_template(
        "public/thread.html", BBS_ARRAY=BBS_ARRAY, length=len(BBS_ARRAY)
    )


@app.route("/agenda")
def agenda():
    BBS_ARRAY = update()
    agendas = get_agendas()
    return render_template(
        "public/agenda.html", BBS_ARRAY=BBS_ARRAY, agendas=agendas, length=len(agendas)
    )


@app.route("/form", methods=["GET", "POST"])
def form():
    form = Ragistration(request.form)
    if request.method == "POST" and form.validate():
        session["vote"] = form.vote.data
        session["comment"] = form.comment.data
        return redirect(url_for("result"))
    return render_template("public/form.html", form=form)


@app.route("/result")
def result():
    return render_template("public/result.html")
