#example
#time = "09:00 PM  "
#it is assumed that there are no wrong entries in this program
time = input("enter time :")
time = time.strip()
if((time[-2]+time[-1]).upper()== "PM"):
    result = str(12 + int(time[0]+time[1]))
    lresult = result + time[2]+time[3]+time[4]
    print(lresult)
else:
    result = time[0:5]
    print(result)
