
def day_of_week(day,month,year):
    if month < 3:
        month = month + 10
        year = year - 1
    else:
        month = month - 2
    century = year // 100
    year2 = year % 100
    weekday = (((26*month-2)//10)+day+year2+(year2//4)+(century//4)-(2*century))%7
    if weekday < 0:
        weekday = weekday + 7
    return weekday

def is_leapyear(year):
    is_leapyear = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leapyear = True
        else:
            is_leapyear = True
    return is_leapyear

def cant_days(month, year):
    list_norm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    list_bis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cant_total = 0
    if is_leapyear(year) == True:
        cant_total = list_bis[month - 1]
    else:
        cant_total = list_norm[month - 1]
    return cant_total
        
def create_calendar(month, year):
    cont = day_of_week(1, month, year) # contador para saber inicio del día
    orig = cont # backup para alinear la primera fecha segun el día
    print("     D", "L", "M", "M", "J", "V", "S", sep="      ", end="\n\n") #Horrible, ya se. No quería usar otras cosas para el formato.
    for i in range(1, cant_days(month, year) + 1):
        if orig > 0:
            print("       " * orig, end="") #Horrible tmb
            orig = 0
        print("%6d" %i, end=" ")
        cont = cont + 1
        if cont % 7 == 0:
            print("\n")
            
month = int(input("Month:"))
year= int(input("Year:"))
while month>12 or month<=0:
    month = int(input("Month:"))
while year<0:
    year= int(input("Year:"))
#alternativa method
#month, year=input("Month?: year?:").split()
#month, year = [int(month), int(year)]
create_calendar(month,year)
