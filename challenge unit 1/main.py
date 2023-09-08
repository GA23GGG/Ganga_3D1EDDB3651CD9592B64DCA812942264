def isleapyear(year):
  if(year%4==0 and year%1000!=0)or year% 400==0:
    return True
  else:
    return False
year=2012
if isleapyear(year):
  print(format(year),"is a leap year")
else:
  print(format(year),"is not leapyear")