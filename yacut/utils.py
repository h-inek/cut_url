from .models import URLMap


def get_url(short):
    """Функция получения ссылки."""
    return URLMap.query.filter_by(short=short).first()
