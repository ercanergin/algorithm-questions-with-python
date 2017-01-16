from datetime import date

sonuc = 0
for yil in range(1901,2001):
    for ay in range(1,13):
        if(date(yil,ay,1).weekday()==6):
            sonuc += 1
print(sonuc)
