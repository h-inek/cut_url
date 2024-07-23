from http import HTTPStatus

from yacut.error_handlers import InvalidUsage
from yacut.generate_short import validate_url, validate_data


def custom_validate_data(data):
    """Валидируем поступающую информацию, выбрасываем свои исключение"""
    try:

        return validate_url(data), validate_data(data)

    except KeyError:
        raise InvalidUsage(
            '"url" является обязательным полем!', HTTPStatus.BAD_REQUEST
        )
    except TypeError:
        raise InvalidUsage('Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)