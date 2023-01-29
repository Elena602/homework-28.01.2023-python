from isdigit import IsDigit

digits = IsDigit(allow_floats=True, allow_ints=True)

print(digits.is_digit('567')) # returns True
print(digits.is_digit('1988.08422')) # returns True
print(digits.is_digit('hacker')) # returns False
print(digits.is_digit('0.9.764')) # returns False