import math
listofnumbers = []
maxlength = 1
while len(listofnumbers) < maxlength:
    digits = str(input("Enter the GTIN digits(with a space between them): "))
    digits2 = digits.split(" ")
    listofnumbers.append(digits)
    if len(digits) >14 :
        print("That is more than 7 digits")
        listofnumbers = []
    try:
        digits = int(digits)
    except ValueError:
        pass
    
x = 0 
while x == 0:
    number1 = int(digits2[0] * 3)
    number2 = int(digits2[1] * 1)
    number3 = int(digits2[2] * 3)
    number4 = int(digits2[3] * 1)
    number5 = int(digits2[4] * 3)
    number6 = int(digits2[5] * 1)
    number7 = int(digits2[6] * 3)
    number8 = number1+number2+number3+number4+number5+number6+number7
    number8rounded = math.ceil(number8 / 10.0) * 10
    realnumber8 = number8rounded - number8
    print("The eighth digit is",realnumber8)
    print("The whole GTIN is ",digits,realnumber8)
    x = 1 
z = 0
if z == 0 :
    listofnumbers2 = []
    digits = str(input("Enter the GTIN digits(with a space between them): "))
    digits2 = digits.split(" ")
    listofnumbers2.append(digits)
    if len(digits) >16 :
        print("That is more than 7 digits")
        listofnumbers2 = []
    try:
        digits = int(digits)
    except ValueError:
        pass
    listofnumbers = listofnumbers - listofnumbers[7]
    x = 0 
    while x == 0:
        number1 = int(digits2[0] * 3)
        number2 = int(digits2[1] * 1)
        number3 = int(digits2[2] * 3)
        number4 = int(digits2[3] * 1)
        number5 = int(digits2[4] * 3)
        number6 = int(digits2[5] * 1)
        number7 = int(digits2[6] * 3)
        number8 = number1+number2+number3+number4+number5+number6+number7
        number8rounded = math.ceil(number8 / 10.0) * 10
        realnumber8 = number8rounded - number8
        print("The eighth digit is",realnumber8)
        print("The whole GTIN is ",digits,realnumber8)
        x = 1
        z=1
digitcheck()
