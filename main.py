def encode(password):
    encoded_password = ''
    password_list = list(password)
    for i in password_list[0:]:
        i = int(i)
        encoded_number = i + 3
        if encoded_number >= 10:
            encoded_number = str(encoded_number)[1]
        else:
            encoded_number = str(encoded_number)
        encoded_password += encoded_number
    return encoded_password

def decode(encoded_password):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = input("Please enter an option: ")
        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and store!")
            print()
            continue
        if option == 2:
            decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        if option == 3:
            break


main()