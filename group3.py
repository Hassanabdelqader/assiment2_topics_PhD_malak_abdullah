#number1
def string_times(str, n):
  return str * n

#number2
def front_times(str, n):
  if len(str) < 3:
    return str * n
  return str[:3] * n

#number3
def string_bits(str):
  result = ''
  for n in range(0, len(str)):
    if n%2 == 0:
      result += str[n]
  return result

#numebr4
def last2(str):
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1  
  return count

#number5
def string_splosion(str):
  result = ''
  for n in range(0,len(str)+1):
    result += str[:n]
  return result
