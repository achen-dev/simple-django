import re


def slugify(text):
    return re.sub(r'[^\w]+', '-', text.lower())


