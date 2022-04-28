# Start

# Lists Start



username_list = ["Buddy" "Alex" "Jordan" "Kizzy"]
phone_list = [316,555,712,888,913,681]
email_list = ["lol@gmail.com" "awesome@gmail.com" "orange@gmail.com"]
# Lists End



# Inputs Start
windows = input("Would you like to sign up for Windows 11?: ")
if windows == "yes":
    username_input = input("Please input your Microsoft username: ")
    
    if username_input in username_list:
        print("This username is already in use, please try again later")
        exit()
    username_list.append(username_input)


    password_input = input("Please input your Microsoft password: ")


    email_input = input("Please input your E-mail address: ")
    if email_input in email_list:
        print("This email is already in use")
        exit()
    email_list.append(email_input)


    phone_input = input("Please input your phone number: ")
    if phone_input in phone_list:
        print("This phone number is already in use, please retry. Closing program..")
        exit()
    phone_list.append(phone_input)

# Inputs End

# Character Checks Start

pass_count = 0
user_count = 0

for i in range(0, len(password_input)):  
    if(password_input[i] != ' '):  
        pass_count = pass_count + 1; 

for i in range(0, len(username_input)):  
    if(username_input[i] != ' '):  
        user_count = user_count + 1;

if pass_count < 3:
    print("Your password is less than 3 characters, please retry.")
    exit()
if user_count < 3:
    print("Your username is less than 3 character, please retry.")
    exit()

# Character Checks End

# Second login start

login = input("Account set up successful, would you like to login to your account?: ")

if login == "yes":
    username_input2 = input("Please input your Microsoft username: ")

if login == "no":
    print("Thanks for using this, closing program.")
    exit()

if username_input2 not in username_list:
    print("Username not found, closing program")
    exit()

password_input_2 = input("Please input your Microsoft password: ")

email_input_2 = input("Please input your E-mail address: ")
if email_input_2 not in email_list:
    print("E-mail not found, please retry. Closing program...")
    exit()

phone_input_2 = input("Please input your phone number: ")
if phone_input_2 not in phone_list:
    print("Phone number not found, please retry. Closing program...")
    exit()

# Second login end


print("Successfully logged into account...")





# End
