month=int(input("enter the month (1-12): "))
days=int(input("enter the days (1-31): "))

if (month==3 and days>=20) or (month==4) or (month==5) or (month==6 and days<=20):
    season = "spring"
elif (month==6 and days >=21) or (month==7) or (month==8) or (month==9 and days<=21):
    season="summer"
elif (month==9 and days >=22) or (month==10) or (month==11) or (month==12 and days<=20):
    season="fall"

else:
    season="winter"



print(season)


