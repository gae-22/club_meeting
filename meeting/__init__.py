from flask import Flask

app = Flask(__name__)
app.config.from_object("meeting.config")

import meeting.views
