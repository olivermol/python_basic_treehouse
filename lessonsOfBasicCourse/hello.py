first_name = input("What is your first name?")
last_name = input("What is your last name?")
print(first_name, "is learning Python and Data Analyst")
if first_name == "Oliver":
    print(first_name, "You have a greate first name! :)")
elif first_name == "Rasta":
    print(first_name, "You have AWESOME first name!")
else:
    age = int(input("How old are you?"))
    if age <= 18:
      print("Wow, you are {}! If you're confident with your reading already... ".format(age))
print("You should totaly learn Python {} {} , bacause you are only {}".format(first_name, last_name, int(age)))
print("Have a great day {}!".format(first_name))