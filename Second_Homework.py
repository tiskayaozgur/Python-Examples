"""
#Yarım Yapıldı
#3. Sorunun 1. Kısmı
def is_armstrong(val):

    total = 0
    for i in val:
        total += int(i) ** 3
    if total == int(val):
        return True
    else:
        return False

while True:
    val = input("Bir sayi giriniz=")
    if val == "0":
        break
    else:
        result = is_armstrong(val)
        print(result)

#3.Sorunun 2.Kısmı
"""
#################################################################
"""
#Soru 4'ün Cevabı
yazi = input("Bir string giriniz=").strip()
l1 = yazi.split()
l2 = []
for i in reversed(l1):
    l2.append(i)
result = " ".join(l2)
print(result)"""
#################################################################
"""
#Yarım Yapıldı
#Soru 5 Cevabı
def digitate(l1):
    t = tuple()
    l2 = []
    for i in l1:
        t = tuple(str(i))
        l2.append(t)
    return l2

l1 = [23, 4, 765, 34589, 42]
result = digitate(l1)
print(result)
"""

#################################################################
"""
#Soru6'nın Cevabı
val = input("Bir yazi giriniz=")
l1 = val.split()
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        continue
print(l2)"""

#################################################################
"""
#Soru7'nin Cevabı
def print_shape(val):
    for i in range(val):
        print("*" * (val - i) + " " * (2 * i) + "*" * (val - i))

    for i in range(val):
        print("*" * (i + 1) + " " * (2 * val - (2 * i + 2)) + "*" * (i + 1))

val = int(input("Bir sayi giriniz="))
print_shape(val)"""

#################################################################
"""
#Soru 8'in Cevabı
def disp_char_pattern(val):
    sag_sol_bosluk = ord(val) - ord("A")
    harfler_arasi_bosluk = 1

    # 1.For
    for i in range(ord("A"), ord(val) + 1):
        if i == 65:  # İlk karakteri tek basmak icin yazdim
            print(" " * sag_sol_bosluk + str(chr(i)) + " " * sag_sol_bosluk)
            sag_sol_bosluk -= 1
            i += 1
        else:
            print(" " * sag_sol_bosluk + str(chr(i)) + " " * harfler_arasi_bosluk + str(chr(i)) + " " * sag_sol_bosluk)
            sag_sol_bosluk -= 1
            harfler_arasi_bosluk += 2

    # 2.For
    sag_sol_bosluk = ord(val) + 1 - ord(val)  # sag ve sol bosluga 1 egerini verdim ve onu arttıracagim
    harfler_arasi_bosluk = ord(val) - ord("A") + 2  # 7den basliyor F icin
    for i in range(ord(val) - 1, ord("A") - 1, -1):
        if i == 65:
            print(" " * sag_sol_bosluk + str(chr(i)) + " " * sag_sol_bosluk)
            sag_sol_bosluk += 1
            i += 1
        else:
            print(" " * sag_sol_bosluk + str(chr(i)) + " " * harfler_arasi_bosluk + str(chr(i)) + " " * sag_sol_bosluk)
            sag_sol_bosluk += 1
            harfler_arasi_bosluk -= 2

disp_char_pattern("F")
        
"""
#################################################################

