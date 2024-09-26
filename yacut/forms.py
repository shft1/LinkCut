from flask_wtf import FlaskForm
from wtforms import StringField, URLField
from wtforms.validators import DataRequired, Length


class LinkForm(FlaskForm):
    original_link = URLField(
        'Ваша ссылка',
        validators=[
            DataRequired(message='Поле обязательно для ввода'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(6, 16, message='ID ссылки не в диапазоне от 6-16 символов')
        ]
    )
