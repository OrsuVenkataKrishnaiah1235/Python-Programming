#Find Number of days in a month
month="January"
month_31_days=("January","March","May","July","August","October","December")
month_30_days=("April","June","September","November")
if month in month_31_days:
    print("{} 31 days ".format(month))
elif month in month_30_days:
    print("{} has 30 days".format(month))
else:
    print("February has 28 days") 
#January 31 days 
