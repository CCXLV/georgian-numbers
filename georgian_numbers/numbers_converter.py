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