
Q-1)Check if two lists, a and b, are polydromes

#myAnswer
a=['selami','ali','veli',10]
b=[10,'veli','ali','selami']
#print(a.reverse()==b)
a.reverse()
print(a==b)

######################################################
Q-2)Create a list, change the first half and second half of the list and print the list on the screen.

#myAnswer
a=[10,20,30,40,50,60,70,80,90,100]
a=a[5:]+a[:5]
print(a)
######################################################
Q-3)Ask the keyboard for a list of names separated by the ',' character with the input function. Then put the names in a list and print the list.

#myAnswer
str=input('Enter name input with commas=')
str=str.split(',')
print(type(str))
######################################################

Q-4)
Read a single digit number on the keyboard. (This number is represented by n.) Print the sum below:
n + nn + nnn + nnnn + nnnnn

#myAnswer
n=input("Enter a number=")
n1=n+n
n2=n+n+n
n3=n+n+n+n
n4=n+n+n+n+n

print(int(n)+int(n1)+int(n2)+int(n3)+int(n4))
######################################################

Q-5)Ask for a 3-digit numeric text from the keyboard. Convert the text to numbers and print

#myAnswer
sayi=input("Enter a tree digit number=")

l=list(sayi)
yüzler=ord(l[0])
onlar=ord(l[1])
birler=ord(l[2])
print(yüzler*100+onlar*10+birler)
######################################################

Q-6)Read a text and a number on the keyboard. Center the text you entered with the spaces in the number of reads.

#myAnswer
word=input("Enter a word")
number=int(input("Enter a number"))

result=word.center(number,'x')
print(result)
######################################################
