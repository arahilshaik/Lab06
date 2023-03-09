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



def main():
    password = input("Give me a password: ")
    encoder(password)

if __name__ == '__main__':
    main()