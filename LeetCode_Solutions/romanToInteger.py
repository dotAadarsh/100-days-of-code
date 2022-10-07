# 13. Roman to Integer

def romanToInteger(s):
  value = 0
  roman_number = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  specific_roman_number={ "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900} 

  for i in specific_roman_number:
    if i in s:
      value += specific_roman_number[i]
      s = s.replace(i, '')

  for letter in s:
    for i in roman_number:
      if letter == i:
        value += roman_number[i]
        
  return value


s = "MCMXCIV"
print(romanToInteger(s))