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
    password = input("Give me a password: ")
    encoded_pw = encoder(password)
    print(encoded_pw)
    print(decode(encoded_pw))


if __name__ == '__main__':
    main()