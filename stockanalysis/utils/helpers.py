from typing import Dict, List


def set_value(original_value, value):
    og_type = type(original_value)
    if og_type == type([]):  # noqa: E721
        original_value.append(value)
        return original_value
    elif og_type == type({}):  # noqa: E721
        for k, v in original_value.items():
            checker(original_value, k, v)
        return original_value
    elif og_type == type(1):  # noqa: E721
        return original_value + value
    elif og_type == type(""):  # noqa: E721
        if original_value == value:
            return original_value
        return original_value + value
    elif og_type == type(set()):  # noqa: E721
        if type(value) == type(set()):  # noqa: E721
            original_value.update(value)
        else:
            original_value.update(set(value))
        return original_value
    else:
        raise Exception(f"Does not support {og_type}")


def checker(src: Dict, key, value):
    if key in src:
        original_value = src.get(key)
        new_value = set_value(original_value, value)
        src[key] = new_value
    else:
        src[key] = value
    return src


class Snake:
    @classmethod
    def set(cls, src, *values: List[Dict]):
        local_copy = src
        for value in values:
            print(value)
            for k, v in value.items():
                print(k, v)
                local_copy = checker(local_copy, k, v)
        return local_copy
