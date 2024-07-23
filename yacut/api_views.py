from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidUsage
from .services import create_short_link
from .utils import get_url
from .validators import custom_validate_data


@app.route('/api/id/', methods=['POST'])
def add_link_api():
    data = request.get_json()
    custom_validate_data(data)

    custom_id = data.get('custom_id', None)

    return (
        jsonify(create_short_link(data['url'], custom_id).to_dict()),
        HTTPStatus.CREATED
    )


@app.route('/api/id/<custom_id>/', methods=['get'])
def get_original_link(custom_id):
    link = get_url(custom_id)
    if link is not None:

        return jsonify({'url': link.original}), HTTPStatus.OK

    raise InvalidUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
