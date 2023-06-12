# Formクラス及び使用するフィールドをインポート
from wtforms import (
    Form,
    BooleanField,
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
    RadioField,
)

# 使用するvalidatorをインポート
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange


class Ragistration(Form):
    password = PasswordField(
        "パスワード：",
        validators=[
            Length(1, 10, "長さは1文字以上10文字以内です"),
            EqualTo("re_password", "パスワードが一致しません"),
        ],
    )
    re_password = PasswordField("パスワード再入力：")

    vote = RadioField(label="議題", choices=[("賛成", "賛成"), ("反対", "反対")])
    comment = TextAreaField("コメント：")

    accept = BooleanField("内容確認：")
    submit = SubmitField("Submit")
