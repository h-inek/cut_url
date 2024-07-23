from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

from .constants import MAX_LENGTH_SHORT


class UrlForm(FlaskForm):
    original_link = StringField(
        'Вставьте сюда полную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Здесь можно предложить свой вариант ссылки',
        validators=[
            Length(max=MAX_LENGTH_SHORT,
                   message='Слишком длинное имя ссылки')
        ]
    )
    submit = SubmitField('Укоротить')
