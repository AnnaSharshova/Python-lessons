_dict = {"1": "monday", "2": "tuesday",
"3": "wednesday", "4": "thursday",
"5": "friday", "6": "saturday",
"7": "sunday"}
print (_dict["1"])

time = 13

print (_dict["3"])
if time < 12:
	print ("a.m.")
else:
	print ("p.m.")

# I didn't understand the task, but I tried

week_day = 2
if week_day < 2:
	print ("monday")
if week_day < 3:
	print ("tuesday")
if week_day < 4:
	print ("wednesday")
if week_day < 5:
	print ("thursday")
if week_day < 6:
	print ("friday")
if week_day < 7:
	print ("saturday")
else: 
	print ("sunday")