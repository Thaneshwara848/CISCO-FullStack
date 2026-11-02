try :                                                           # try block : we will the risky code 
    n1 = int(input("Enter A value : "))                         # it will pass to Except but it will not come back 
    n2 = int(input("ENter B Value : "))
    result = n1 / n2 ;
    
except ValueError as error :                                # this will handle it 
    print("Please Enter the NUmber only...!")

except ZeroDivisionError as error :
    print("Boss we can not div anythng zero : please enter postive number ")

except TypeError as error:
    print("Cannot add number and string")
    print(error)

except IndexError:
    print("Index does not exist!")
    
except KeyError:
    print("Key does not exist!")
except NameError:
    print("Variable is not defined!")
    
except FileNotFoundError:
    print("File does not exist!")
except AttributeError:
    print("String does not support append()")
else :
    print("Sum of A / B : ", result);
    
finally :
    print("CACULATION COMPLETED ,Thank you ...!")
                                                # quickly copy and check 