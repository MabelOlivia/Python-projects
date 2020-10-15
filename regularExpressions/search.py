import re

str_ = "Take up one idea. one idea at a time"
str1 = "Take up 1 one  45 idea. one idea 89 at a time"

result = re.search(r'o\w\w', str_)
print(result.group())

result = re.findall(r'o\w\w', str_)
print(result)

result = re.match(r'T\w\w\w', str_)
print(result.group())

result = re.split(r'\d+', str1)
print(result)

result = re.sub(r'one', 'two', str_)
print(result)

