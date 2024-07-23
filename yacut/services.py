from http import HTTPStatus

from sqlalchemy.exc import IntegrityError

from .error_handlers import InvalidUsage, DuplicateValue
from .generate_short import create_urlmap


def create_short_link(original, short):
    """Создаём короткую ссылку, выбрасываем свои исключения"""
    try:
        return create_urlmap(original, short)

    except ValueError:
        raise InvalidUsage(
            'Указано недопустимое имя для короткой ссылки',
            HTTPStatus.BAD_REQUEST
        )
    except IntegrityError:
        raise DuplicateValue(
            'Предложенный вариант короткой ссылки уже существует.',
            HTTPStatus.BAD_REQUEST
        )
