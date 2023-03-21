def encoder(password):
    new_password = ''
    for i in range(0, len(password)):
        if 0 <= int(password[i]) <= 6 :
            new_password = new_password + str(int(password[i]) + 3)
        elif int(password[i]) == 7:
            new_password = new_password + "0"
        elif int(password[i]) == 8:
            new_password = new_password + "1"
        elif int(password[i]) == 9:
            new_password = new_password + "2"
    print(new_password)


def decode(pw):
    # Turns every single digit in the password into an integer so that arithmetic operators can be applied to them
    lst_pw = [int(i) for i in pw]

    # For every number greater than 2 in the first list, subtract 3 and then turn back into a string
    # If the number is less than or equal to 2, concatenate a "1" to the string version of the number
    lst_pw2 = [(str(number - 3)) if number > 2 else ("1" + str(number)) for number in lst_pw]

    # For every number greater than or equal to 10 in the second list, subtract 3 and then revert to string
    lst_pw3 = [(str(int(number) - 3)) if int(number) >= 10 else number for number in lst_pw2]

    # Join the strings in the third list together
    string_pw = "".join(lst_pw3)

    return string_pw


def main():
    encoded_pw = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            pw = input("Please enter your password to encode: ")
            encoded_pw = encoder(pw)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            if encoded_pw is None:
                print("No password stored.")
                continue
            decoded_pw = decode(encoded_pw)
            print(f"The encoded password is {encoded_pw}, and the original password is {decoded_pw}.")

        elif option == 3:
            break


if __name__ == '__main__':
    main()