
GENERAL_NUMBERS = {
    "0": "ნული",
    "1": "ერთი",
    "2": "ორი",
    "3": "სამი",
    "4": "ოთხი",
    "5": "ხუთი",
    "6": "ექვსი",
    "7": "შვიდი",
    "8": "რვა",
    "9": "ცხრა"
}

HARD_TENS = {
    "1": "ათი",
    "2": "ოცი",
    "4": "ორმოცი",
    "6": "სამოცი",
    "8": "ოთხმოცი"
}

FIRST_PARTS = {
    "1": "",
    "2": "ოცდა",
    "3": "ოცდა",
    "4": "ორმოცდა",
    "5": "ორმოცდა",
    "6": "სამოცდა",
    "7": "სამოცდა",
    "8": "ოთხმოცდა",
    "9": "ოთხმოცდა"
}

SECOND_PARTS = {
    "0": "ათი",
    "1": "თერთმეტი",
    "2": "თორმეტი",
    "3": "ცამეტი",
    "4": "თოთხმეტი",
    "5": "თხუთმეტი",
    "6": "თექვსმეტი",
    "7": "ჩვიდმეტი",
    "8": "თვრამეტი",
    "9": "ცხრამეტი"
}

HARD_NUMBERS = [
    "1", "3", "5", "7", "9"
]

HUNDREDS = {
    '1': 'ას',
    '2': 'ორას',
    '3': 'სამას',
    '4': 'ოთხას',
    '5': 'ხუთას',
    '6': 'ექვსას',
    '7': 'შვიდას',
    '8': 'რვაას',
    '9': 'ცხრაას'
}


def two_digits(number: str) -> str:
    digits = [digit for digit in number]

    result = ""
    if digits[0] != "0":
        if digits[0] in FIRST_PARTS and digits[0] != "1" and digits[1] != "0":
            if digits[0] not in HARD_NUMBERS:
                result = FIRST_PARTS[digits[0]] + GENERAL_NUMBERS[digits[1]]
            else:
                result = FIRST_PARTS[digits[0]] + SECOND_PARTS[digits[1]]
        elif digits[0] in FIRST_PARTS and digits[1] == "0":
            if digits[0] not in HARD_NUMBERS:
                result = HARD_TENS[digits[0]]
            elif digits[0] == "1":
                result = "ათი"
            elif digits[0] in HARD_NUMBERS:
                result = FIRST_PARTS[digits[0]] + "ათი"
        elif digits[0] == "1":
            result = SECOND_PARTS[digits[1]]
        

    return result

def triple_digits(number: str) -> str:
    digits = [digit for digit in number]
    
    result = ""
    if digits[0] != "0":
        if digits[1] != "0":
            result = HUNDREDS[digits[0]] + " " + two_digits(digits[1] + digits[2])
        elif digits[1] == "0" and digits[2] != "0":
            result = HUNDREDS[digits[0]] + " " + GENERAL_NUMBERS[digits[2]]
        elif digits[1] == "0" and digits[2] == "0":
            result = HUNDREDS[digits[0]] + "ი"

    return result

def four_digits(number: str) -> str:
    digits = [digit for digit in number]

    result = ""
    if digits[0] != "0":
        if digits[0] == "1":
            if int("".join(number)) % 1000 == 0:
                result = "ათასი"
            elif digits[1] == "0" and digits[2] != "0":
                result = "ათას " + two_digits(digits[2] + digits[3])
            elif digits[1] == "0" and digits[2] == "0" and digits[3] != "0":
                result = "ათას " + GENERAL_NUMBERS[digits[3]]
            else:
                result = "ათას " + triple_digits(digits[1] + digits[2] + digits[3])
        else:
            if int("".join(number)) % 1000 == 0:
                result = GENERAL_NUMBERS[digits[0]] + " ათასი"
            elif digits[1] == "0" and digits[2] != "0":
                result = GENERAL_NUMBERS[digits[0]] + " ათას " + two_digits(digits[2] + digits[3])
            elif digits[1] == "0" and digits[2] == "0" and digits[3] != "0":
                result = GENERAL_NUMBERS[digits[0]] + " ათას " + GENERAL_NUMBERS[digits[3]]
            else:
                result = GENERAL_NUMBERS[digits[0]] + " ათას " + triple_digits(digits[1] + digits[2] + digits[3])
    
    return result