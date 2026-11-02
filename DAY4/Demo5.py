
try:
    a = int(input("Enter A value : "))    
    b = "20";
    print(a + b)

except TypeError as error:
    print("Cannot add number and string")
    print(error)
except ValueError as error :                                # this will handle it 
    print("Please Enter the NUmber only...!")