
while True:
    print("Your choice? \n" \
    "1. °F to °C \n" \
    "2. °C to °F " \
    )
    try:
        temp_choice = int(input("Enter your choice 1/2? : "))

        if temp_choice == 1:
            def celsius_calc(f_temp):
                c_temp = (f_temp - 32) * 5/9
                print(f_temp, "°F =", int(c_temp), "°C")

            f_temp = int(input("Enter the temp in °F: "))
            celsius_calc(f_temp)

            choice = input("Do you want to convert more? (Yes/No): ")
            if choice not in ["Yes", "yes", "Y", "y"]:
                print("Program end. Thank You! ")
                break

        elif temp_choice == 2:
            def faren_calc(c_temp):
                f_temp = (c_temp * 1.8) + 32
                print(c_temp, "°C =", int(f_temp), "°F")

            c_temp = int(input("Enter the temp in °C: "))
            faren_calc(c_temp)

            choice = input("Do you want to convert more? (Yes/No): ")
            if choice not in ["Yes", "yes", "Y", "y"]:
                print("Program end. Thank You! ")
                break
    except ValueError:
            print("Invalid value! ")
            
    