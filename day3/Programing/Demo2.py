def addtwonumber():
    a = int( input("Enter A  : "));              # type      ?String 
    b = int(input("Enter B  : "));
    result = a + b ;
    print("Sum of A + B  :  " ,  result );
    
def findevenOrOdd():
    num = int(input("Enter Number "))
    if num%2==0 :
        print("Even...!")
    else :
        print("Odd...!");

def display():
        print("Hi Student class Display MEthod")

display();
print("------------")
findevenOrOdd();
print("---------------")
addtwonumber();


