#number1
def cigar_party(cigars, is_weekend):
  return cigars >= 40 if is_weekend else 40 <= cigars <= 60
#number2
def love6(a, b):
   return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6

#number3
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0

    if you >= 8 or date >= 8:
        return 2

return 1

#numebr4
def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  return 60 <= temp <= 90
    
  

#numebr5 
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  return 1
