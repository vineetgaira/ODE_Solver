def get_user_input():
    valid_choices = {1, 2, 3, 4}
    try:
        user = int(input("Enter your choice:"))
        if user in valid_choices:
            return user
        else:
            print("Please enter a valid choice.")
    except ValueError:
        print("Please enter a valid choice.")
