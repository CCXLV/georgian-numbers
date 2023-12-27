# Numbers in Georgian
Converts numbers (*2, 3 and 4 digits only*) into Georgian

## Installation
```cmd
pip install georgian-numbers
```

## Example #1
```python
from georgian_numbers import number_converter

number = "1121"
converted_number = number_converter(number)

print(converted_number) # Output: ათას ას ოცდაერთი
```

## Example #2
```python
from georgian_numbers import text_converter

text = "ბაგრატ მესამე (1027-1072) და გიორგი მეორე (1072-1089)"
converted_text = text_converter(text)

print(converted_text) # Output: ბაგრატ მესამე (ათას ოცდაშვიდი-ათას სამოცდათორმეტი) და გიორგი მეორე (ათას სამოცდათორმეტი-ათას ოთხმოცდაცხრა)
```

Author [CCXLV](https://github.com/CCXLV)

License MIT
