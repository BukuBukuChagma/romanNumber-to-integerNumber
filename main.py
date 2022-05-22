

romantoInt = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'M':1000}


def checkIfNumberisCorrect(romanValue, romandic):
  if all(rv in romandic for rv in romanValue):
    return True
  else:
    return False


def convertRomantoInt(val, dic):
  if checkIfNumberisCorrect(val, dic):
    integerResult = dic[val[-1]]
    for i in range(len(val)-1, 0, -1):
      if dic[val[i]] <= dic[val[i-1]]:
        integerResult+= dic[val[i-1]]
      else:
        integerResult-= dic[val[i-1]]
  else:
    return False

  return integerResult


print("I : 1, V : 5, X : 10, 'L : 50\ne.g: Enter a number : XIV\nAnswer : 14\n")
romanNumber = input('Enter the roman number : ')
integer = convertRomantoInt(romanNumber, romantoInt)
if integer:
  print(f"Integer Counterpart is : {integer}\n")
else:
  print('Invalid Input')
