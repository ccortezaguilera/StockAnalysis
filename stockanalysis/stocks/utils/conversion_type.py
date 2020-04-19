from ..common.constants import CONVERSION_TYPES


def get_conversion_type(conversion_type: str):
    return CONVERSION_TYPES.get(conversion_type)
