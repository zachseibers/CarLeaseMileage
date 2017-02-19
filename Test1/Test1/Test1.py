# Tool for calculating remaining mileage on a lease car

print("Hello World")

MilesPerDay = 82
DaysPerYear = 365
MilesPerYear = MilesPerDay*DaysPerYear
print("For", MilesPerDay,"miles per day, there is a total of" ,MilesPerYear,"miles in a calendar year.")

from datetime  import date, datetime,timedelta
PickupDate = date(2016, 4, 8)
DueDate=date(2017, 4, 8)
#default date input form is yyyy, mo, dd; can change using date_format = "%m/%d/%Y"
CurrentDate = date(2017, 2, 19)
DaysRemaining = DueDate - CurrentDate

#DaysRemainingFloat =  DaysRemaining / datetime.timedelta (days = 1)
#Line does not work

CurrentMiles = 24790
RemainingMiles = MilesPerYear - CurrentMiles

DailyLimit = RemainingMiles /  48 #48 is hardcoded until I can figure out datetime object issue
print(DailyLimit, type(DailyLimit))
print("There are", RemainingMiles, "miles and", DaysRemaining, "days reamining on the lease, which means that the daly mileage limit is", "%.2f" %DailyLimit, "miles!")

