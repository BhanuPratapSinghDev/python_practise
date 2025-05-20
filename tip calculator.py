print(" Welcome to the tip calculator ! ")
bill = float ( input (" What was the total bill ? ") )
tip = int ( input (" How much would tip you like to give ? 0 ,10 ,20,40 percent  ? "))
split = int ( input (" How many persons to split the bill ? "))
each_pay = ( bill + (tip/100)*bill ) / split
print(" Each person should pay rupees : ",round(each_pay,2))
