# FASTag Highway Toll Tax Calculator

vehicle_type = input("Enter vehicle type: ")
fastag_active = True
is_national_holiday = False

if fastag_active == False:
    print("Double toll penalty applied: cash mode")

else:
    if is_national_holiday == True:
        print("Festive waiver applied: half toll")

    else:
        if vehicle_type == "car":
            print("Toll amount: 100 rupees")

        elif vehicle_type == "SUV":
            print("Toll amount: 150 rupees")

        elif vehicle_type == "truck":
            print("Toll amount: 300 rupees")

        else:
            print("Invalid vehicle category")