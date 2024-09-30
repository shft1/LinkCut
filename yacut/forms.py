from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Optional, Regexp

from services.constants import PATTERN


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
            Regexp(
                PATTERN,
                message='Указано недопустимое имя для короткой ссылки'
            ),
            Optional(),
        ]
    )
    submit = SubmitField('Создать')
