from decimal import Decimal


def decimal_json_array(array):
    for index, item in enumerate(array):
        obj = item.items()
        for key, value in obj:
            if isinstance(value, Decimal):
                array[index][key] = str(value)

    return array


def decimal_json(obj):
    obj_items = obj.items()
    for key, value in obj_items:
        if isinstance(value, Decimal):
            obj[key] = str(value)

    return obj
