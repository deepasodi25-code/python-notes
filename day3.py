age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
traveling_alone = input("Are you traveling alone? (yes/no): ")
tatkal = input("Is it a Tatkal ticket? (yes/no): ")
blackout_date = input("Is it a blackout festival date? (yes/no): ")

if (age >= 60 or (gender == "female" and traveling_alone == "yes")) and tatkal == "no" and blackout_date == "no":
    print("Passenger is eligible for senior citizen preference and discount.")
else:
    print("Passenger is not eligible.")