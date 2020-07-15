
########################################################################################################################
"""
#Soru 1'in Cevabı
def puts(text,**kwargs):
    if kwargs["reverse"] == False:
        if kwargs["center"] < len(text):
            print(f"{text}" * int(kwargs["repait"]))
        else:
            text = text.center(kwargs["center"], kwargs["fillchar"])
            print(f"{text}" * int(kwargs["repait"])) # Burada kullanıcı repait argumanını str girese bile ben onu inte cast ettim.

    else:
        text = " ".join(reversed(text.split())) #texti ters cevirdim.
        if kwargs["center"] < len(text):
            print(f"{text}" * int(kwargs["repait"]))
        else:
            text = text.center(kwargs["center"],kwargs["fillchar"])
            print(f"{text}" * int(kwargs["repait"]))  # Burada kullanıcı repait argumanını str girese bile ben onu inte cast ett


reverse = {"reverse":False}
repait = {"repait" : 1}
center = {"center": 0}
fillchar = {"fillchar" : " "}
puts("Merhaba Ben Ozgur",center = 65, **reverse, **repait, fillchar = "-")

"""
########################################################################################################################

########################################################################################################################

"""
#2.Soru Cevabı(Tam)
def exclude_repeated_items(a):
    l = []
    for i in a:
        if i not in l:
            l.append(i)
    return l
a = [1, 2, 2, 5, 3, 6, 6, 7, 3, 8, 9, 2, 1, 4, 4]
result  = exclude_repeated_items(a)
print(result)
"""
########################################################################################################################
"""
#Soru3'un Cevabı(Tam)
def fact(n):
    total = 1
    for i in range(n, 1, -1):
        total *= i
    return total

result  = fact(6)
print(result)

def combination(n,k):
    return fact(n) // ((fact(n - k)) * fact(k))
result2 = combination(0,0)
print(result2)

def disp_pascal_triangle(val):

    sol_bosluk = val - 1
    for i in range(val):
        print(" " * sol_bosluk, end="")
        for j in range(i + 1):
            # print(" " * sol_bosluk,end="")

            print(combination(i, j), end=" ")
        sol_bosluk -= 1

        print()
disp_pascal_triangle(4)
"""
########################################################################################################################


"""
#Soru4'ün Cevabı(Yarım)
val = int(input("Bir sayi giriniz="))
sayac1 = val #Bunu yapma sebebim bir sabit aldım
for i in range(ord("a") + val - 1 ,ord("a") - 1 , - 1): #c,b,a seklinde alabilmek icin yaptım
    # print(chr(i),end=" ")
    print("-" * (2 *sayac1 - 2),end="")
    for j in range(ord("a") + val - 1, i - 1, -1): #c,cb,cba seklinde alabilmek icin yazıldı bu for.
        print(chr(j),end="-")
    print()
    sayac1 -= 1

sayac1 = val #Bunu yapma sebebim bir sabit aldım
sayac2 = 3
for i in range(ord("a") + val - 1 ,ord("a") , - 1): #c,b,a seklinde alabilmek icin yaptım
    print("-" * (2 *sayac1 - 4),end="")
    for j in range(ord("a") + val - 1 ,ord("a") + val -sayac2 , - 1): #c,cb,cba seklinde alabilmek icin yazıldı bu for.
        print(chr(j),end="-")
    sayac2 -= 1
    print()
    sayac1 += 1
"""



########################################################################################################################
"""
#Soru5'in Cevabı(Tam)
def is_domino(l):
    count = 0
    liste1 = []
    liste2 = []
    for i in range(len(l)):
        if i == len(l) - 1:
            break
        else:
            if l[i][1] == l[i + 1][0]:
                count += 1
    if count == len(l) -1:
        return True
    else:
        return False

l = [(1, 3), (3, 6), (6, 9), (9, 1),(1,8),(8,4),(4,5)]
result = is_domino(l)
print(result)
"""

########################################################################################################################



########################################################################################################################




########################################################################################################################

"""
val = int(input("Bir sayi giriniz="))
for i in range(val , 0, -1):
    #print(i,end=" ")
    for j in range(val, i - 1, -1):
        print(j,end=" ")

    print()
for i in range(val , 1, -1):
    for j in range(val, val - i + 1, -1):
        print(j,end=" ")
    print()
"""
