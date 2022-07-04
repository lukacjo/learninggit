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


""" na tym ogarniałem jak działa sprawianie ze wartości moga miec duża litere
test_dict = {"Gfg" : ["ab", "cd", "ef"],
             "Best" : ["gh", "ij"], "is" : ["kl"]}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# using upper to convert to upper case 
res = {key: [ele.upper() for ele in test_dict[key] ] for key in test_dict }
  
# printing result 
print("The dictionary after conversion " + str(res)) """
#zad2

num=[]
triple=[]
for i in range(0,101):
    if i%5==0:
        #print(i)
        num.append(i)
    else:
        continue
for n in num:
    triple.append(n**3)

print(num)
print(triple)