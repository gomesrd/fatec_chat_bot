import re


def remove_special_characters(input_text):
    pattern = re.compile(r'[^\w\s]', re.UNICODE)

    input_text_remove = pattern.sub('', input_text)

    return input_text_remove
