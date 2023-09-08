def checkleapyear(year):
  import calendar
  return (calendar.isleap(year))
year=int(input("enter the year:"))
if(checkleapyear(year)):
   print("leap year")
else:
   print("not a leap year")