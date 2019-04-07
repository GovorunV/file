'''str=input("vedite text:") #записть в файл
str += "\n"
file = open('date/text.txt','a')
file.write(str)
file.close()
try:
    file = open('date/text.txt', 'rt')  # чтение з файла
    for line in file:
        print(line)
    file.close()
except FileNotFoundError:
    print("Fail ne daiden")
'''

# Исключения!!!
userinp2=False
while userinp2==False:
    try:
        a=int(input("Vedite chislo"))
        userinp2=True
    except ValueError:
        print("vedite chislo 1")
userinp=False
while userinp==False:
    try:
        b=int(input("Vedite chislo"))
        userinp=True
    except ValueError:
        print("vedite chislo 2")

print("rezult sumu=",a+b)