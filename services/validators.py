import re

from services.constants import PATTERN
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap


class DataValidator:

    @staticmethod
    def validate_data(data):
        if data is None:
            raise InvalidAPIUsage('Отсутствует тело запроса')
        return data

    @staticmethod
    def validate_long(long):
        if long is None:
            raise InvalidAPIUsage('"url" является обязательным полем!')

    @staticmethod
    def validate_unique_short(short):
        if URLMap.query.filter_by(short=short).first() is not None:
            return True
        return False

    @staticmethod
    def validate_short(short):
        if URLMap.query.filter_by(short=short).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.')
        if re.search(PATTERN, short) is None:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
