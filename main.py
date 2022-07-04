#86
#97 zad
from collections import Counter
slownik={
    "piekarnia": ["chleb","paczek","bulki"],
    "warzywniak": ["marchew", "seler","rukola"]
}

upp={key.capitalize(): [v.capitalize() for v in slownik[key]] for key in slownik}

count=0
#slownik = {k.upper():v.capitalize() for k,v in slownik.items()}
for k,v in upp.items():#k to keys a v to values ale tutaj to nie ma znaczenia bo to tylko nadane nazwy przezemnie
    print("ide do", k ,"żeby kupić",v )#nadal nie umiem zrobić żeby wartości miały duża litere, jest jakis problem z tym
    count+= len(v)

    
print("Łącznie kupujemy",count,"produktów")

