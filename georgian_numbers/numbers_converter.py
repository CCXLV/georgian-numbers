import re
from .utils.utils import two_digits, triple_digits, four_digits


def number_converter(number: str) -> str:

    digits = [digit for digit in number]

    result = ""
    if len(digits) == 1:
        return 
    else:   
        if len(digits) == 2:
            result = two_digits(digits)
        elif len(digits) == 3:
            result = triple_digits(digits)
        elif len(digits) == 4:
            result = four_digits(digits)
                    
        return result

def text_converter(text: str) -> str:
    pattern = r'\b\d{1,4}\b'
    years = re.findall(pattern, text)

    for year in years:
        if len(year) <= 4:
            text_year = number_converter(str(year))
            if text_year:
                text = text.replace(year, text_year)

    return text