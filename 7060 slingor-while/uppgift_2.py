text1 = input("Hur många heltal vill du ha?")
antal = int(text1)
text2 = input("Vilket är det minsta talet i serien?")
minsta= int(text2)
stop = minsta + antal
while minsta < stop:
    print(minsta)
    minsta = minsta + 1
print ("klar")    