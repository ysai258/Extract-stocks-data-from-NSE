import calendar
import datetime

def isLastThursday(input_date):
    # spliting the given string with '-' and converting it into integer using map
    # then storing it into day , month and year respectively
    day,month,year=map(int,input_date.split('-'))
    # converting ti into date
    d=datetime.date(year,month,day)
    # checking it with last thursday of that month
    return d==getLastThursday(month,year)

# added year to this function as with out year it is impossible to find last thursday with only month
def getLastThursday(input_month,year):
    # fining number of days in the month of that year
    month,noOfDaysInMonth=calendar.monthrange(year,input_month)
    # looping until days become to 1
    while(noOfDaysInMonth>0):
        # converting date with given year month and day
        b=datetime.date(year,input_month,noOfDaysInMonth)
        # finding week
        # 1 for monday 2 for tuesday and so on..
        # so as we want ot find thursday we compare it with 4
        if(b.isoweekday()==4):
            return b # returning that date
        noOfDaysInMonth-=1

print(getLastThursday(5,2021))
print(isLastThursday('19-5-2021'))
print(isLastThursday('27-5-2021'))    
