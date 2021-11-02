from decimal import Decimal


def decimal_json_array(array):
    for index, item in enumerate(array):
        obj = item.array()
        for key, value in obj:
            print(type(value))
            print(value)
            if isinstance(value, Decimal):
                array[index][key] = str(value)

    return array
