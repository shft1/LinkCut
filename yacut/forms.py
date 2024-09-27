from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Optional, Regexp

pattern = r'^[\dA-Za-z]{1,16}$'


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
                pattern,
                message='Указано недопустимое имя для короткой ссылки'
            ),
            Optional(),
        ]
    )
    submit = SubmitField('Создать')
