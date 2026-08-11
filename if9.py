married = input("Is the driver married? (yes/no): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if married.lower() == "yes":
    print("Driver is insured")
elif married.lower() == "no" and gender.lower() == "male" and age > 30:
    print("Driver is insured")
elif married.lower() == "no" and gender.lower() == "female" and age > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")