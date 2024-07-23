from urllib.parse import urljoin

from flask import flash, redirect, render_template

from . import app
from .forms import UrlForm
from .constants import LOCALHOST_URL
from .error_handlers import InvalidUsage, DuplicateValue
from .api_views import HTTPStatus
from .services import create_short_link
from .utils import get_url


@app.route('/', methods=['GET', 'POST'])
def add_link():
    """Создание ссылки. Исключения передаются в форме флеш-сообщений"""
    form = UrlForm()
    if form.validate_on_submit():
        short = form.custom_id.data

        try:
            link = create_short_link(form.original_link.data, short)
            flash(f'{urljoin(LOCALHOST_URL, link.short)}')

        except DuplicateValue:
            flash('Предложенный вариант короткой ссылки уже существует.')

            return render_template('main.html', form=form)

    return render_template('main.html', form=form), HTTPStatus.OK


@app.route('/<short_id>')
def redirect_on_link(short_id):
    """Редирект на оригинальный url по короткому url"""
    link = get_url(short=short_id)

    if link is not None:

        return redirect(link.original), HTTPStatus.FOUND

    raise InvalidUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
