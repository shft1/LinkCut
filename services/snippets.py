import random

from services.constants import LEN_ID
from services.validators import DataValidator


def get_short_id():
    choices = ([chr(i) for i in range(48, 58)] +
               [chr(i) for i in range(65, 91)] +
               [chr(i) for i in range(97, 123)])
    short_id = ''.join(random.choices(choices, k=LEN_ID))
    return short_id


def get_unique_short_id(short_id):
    if short_id in set(['', None]):
        short_id = get_short_id()
        while DataValidator.validate_unique_short(short_id):
            short_id = get_short_id()
    return short_id
