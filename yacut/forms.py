from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional


class LinkForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Поле обязательно для ввода!'),
            URL(require_tld=False, message='Введите правильный адрес!')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(6, 16, message='ID ссылки не в диапазоне от 6-16 символов!'),
            Optional(),
        ]
    )
    submit = SubmitField('Создать')
