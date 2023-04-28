# import django template library
from django import template

# json to make json serializations
import json

# import ast for abstract syntax
import ast

# import marksafe to generate html code visible sintax
from django.utils.safestring import mark_safe

# intialize register template library
register = template.Library()


# turn json to serialization
@register.filter
def json_loads(value):
    return json.loads(value)


# type casting to dict
@register.filter
def to_dict(value):
    return ast.literal_eval(value)


# acess dictionary keys values
@register.filter
def lookup(d, key):
    return d[key]


# identify and dont display None value from db
@register.filter
def noneop(value):
    if value == "None" or value == "0":
        return ("")
    else:
        return (value)


# drop strings from template
@register.filter
def drophttps(drop):
    drop = str(drop)
    if ("https://") in drop:
        return drop.replace("https://", "")
    else:
        if ("http://") in drop:
            return drop.replace("http://", "")


# make lower string data from template
@register.filter
def makelower(makelower):
    makelower = makelower.lower()
    return makelower


# make replace string corrections http to https
@register.filter
def rephttps(rep):
    rep = str(rep)
    if ("http://") in rep:
        return rep.replace("http://", "https://")
    else:
        return rep


# make html safe mode to output on template
@register.filter(is_safe=True)
def format_description(audio):
    audio = audio.lower()
    text = (f"""<audio controls >
    <source src="https://hidedomain.info/sd/{audio}.mp3" type="audio/mpeg">
    <source src="https://hidedomain.info/sd/{audio}.ogg" type="audio/ogg">
    Your browser does not support the audio element.
            </audio>""")
    return mark_safe(text)
