"""Utilities to re-use in the project"""
from decimal import Decimal
from datetime import date


def decimal_json_array(array):
    """Take an array of objects that contains Decimal or Date fields and convert it fields to str"""
    for index, item in enumerate(array):
        obj = item.items()
        for key, value in obj:
            if isinstance(value, Decimal) or isinstance(value, date):
                array[index][key] = str(value)

    return array


def decimal_json(obj):
    """Take an object that contains Decimal or Date fields and convert it fields to str"""
    obj_items = obj.items()
    for key, value in obj_items:
        if isinstance(value, Decimal) or isinstance(value, date):
            obj[key] = str(value)

    return obj
