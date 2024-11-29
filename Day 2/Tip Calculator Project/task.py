print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

totalTip = (100+tip)/100
result = (bill/people) * totalTip
pay = format(result, '.2f')  # format the amount to be paid to 2 decimal places

print(f"Each person should pay ${pay}")


'''
Note: round(result,2) will give 33.6 and not 33.60 as Python keeps the number of digits manageable by displaying a rounded value.
For eg.
if Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display:
>>> 0.1
0.1000000000000000055511151231257827021181583404541015625
That is more digits than most people find useful, so Python keeps the number of digits manageable by displaying a rounded value instead:
>>> 1 / 10
0.1
Just remember, even though the printed result looks like the exact value of 1/10, the actual stored value is the nearest representable binary fraction.

Thus, string formatting can be used to format the result and display it to produce a limited number of significant digits.
String formatting used: '.2f' (quotes included) for 2 significant digits after decimal, '.12g' for 12 significant digits and so on...
'''






# tipPercent = tip/100
# totalTipAmount = bill * tipPercent
# totalBillAmount = bill + totalTipAmount
# billPerPerson = totalBillAmount / people
# pay = round(billPerPerson, 2)  # format the amount to be paid to 2 decimal places