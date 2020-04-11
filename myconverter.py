#euros to dollars

def display_menu():
    print("Enter 1 to convert euros to dollars")
    print("Enter 2 to convert centimeters to inches")
    print("Enter 3 to convert litres to gallons")
    r = raw_input()
    return r

def euro_dollar(euro):
    message = " euros is equal to "
    return str(euro) + message + str(1.08 * euro) + "dollars."

def cm_inch(cms):
    message = " cemtimeters is equal to "
    return str(cms) + message + str(0.393 * cms) + "inches."

def li_gallon(lis):
    message = " liters is equal to "
    return str(lis) + message + str(0.264 * lis) + "gallons."
a = display_menu()
if a == "1":
    ip_euro = raw_input("Enter the number of euros to be converted to dollars: ")
    print(euro_dollar(float(ip_euro)))
elif a == "2":
    ip_cms = raw_input("Enter the number of centimeters to be converted to inches: ")
    print(cm_inch(float(ip_cms)))
else:
    ip_lis = raw_input("Enter the number of liters to be converted to gallons: ")
    print(li_gallon(float(litres)))