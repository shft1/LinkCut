from http import HTTPStatus

from flask import jsonify, request

from services.snippets import get_unique_short_id
from services.validators import DataValidator

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_url_map():
    data = DataValidator.validate_data(request.get_json(silent=True))
    DataValidator.validate_long(data.get('url'))
    short_id = get_unique_short_id(data.get('custom_id'))
    DataValidator.validate_short(short_id)
    data['custom_id'] = short_id
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url_map(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original})
