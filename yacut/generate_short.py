from random import choice
from string import ascii_letters, digits

from sqlalchemy.exc import IntegrityError

from . import db
from .models import URLMap
from .constants import LENGTH_GENERATE_URL, MAX_LENGTH_SHORT
from .utils import get_url


def validate_data(data):
    """Если в теле запроса ничего не передано"""
    if not data:
        raise TypeError


def validate_url(data):
    """Если нет поля 'url' в теле запроса"""
    if 'url' not in data:
        raise KeyError


def validate_short(short):
    """Проверяем предложенную пользователем короткую ссылку"""
    if not short or short == '':
        return True

    if len(short) >= MAX_LENGTH_SHORT:
        raise ValueError

    for symbol in short:
        if symbol not in ascii_letters and symbol not in digits:
            raise ValueError


def validate_unique_short(short):
    """Ищем совпадения в базе"""
    if get_url(short) is not None:

        raise IntegrityError(statement=None, params=None, orig=None)


def generate_unique_short_id(length=LENGTH_GENERATE_URL):
    """Функция создания короткой ссылки"""
    data_symbol = ascii_letters + digits
    short = ''.join(choice(data_symbol) for _ in range(length))
    while get_url(short):
        short = ''.join(
            ''.join(choice(data_symbol) for _ in range(length))
        )

    return short


def create_urlmap(original, short):
    """Добавление ссылки в базу данных"""
    if not short or short == '':
        short = generate_unique_short_id()
    else:
        validate_short(short)
        validate_unique_short(short)

    link = URLMap(
        original=original,
        short=short
    )
    db.session.add(link)
    db.session.commit()

    return link
