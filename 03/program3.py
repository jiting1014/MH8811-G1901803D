print('Welcome!')
print('Input the corresponding number of the program you would like to choose. Or input "exit" to quit this program')
print("01-Say hello to the world!\n02-Say hello to Someone!\n03-Know the temparature (from Celsius to Fahrenheit)")
def a_01():
    print('Hello, world!')
def a_02():
    nam=input('Who are you?')
    print('Hello',nam,'!')
def a_03():
    c=input('Temparature in Celsius=')
    f=float(c)*1.8+32
    print('Fahrenheit=',f)
while True:
    a=input('Which one do you want to choose? (01 or 02 or 03 or exit)')
    if a=='01':
        a_01()
        continue
    if a=='02':
        a_02()
        continue
    if a=='03':
        a_03()
        continue
    if a=='exit':
        print('Thanks for your try! Byebye!')
        break
    else:
        print('No such choice. Please choose again!')
        continue
