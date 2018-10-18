#group1
#number1
def sleep_in(weekday, vacation):
    return not weekday or vacation

#number2
def monkey_trouble(a_smile, b_smile):
    return a_smile and b_smile or not a_smile and not b_smile

#number3
def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)


#number4
def sum_double(a, b):
  if a == b:
    return a * 4
  return a + b

#numebr5
def makes10(a, b):
  return a + b == 10 or a == 10 or b == 10

#numebr6
def not_string(str):
  if str[:3] == "not":
    return str
  return "not " + str






