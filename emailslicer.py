def email_process(email):
    #minhvuong43199@gmail.com
    email_username = email[0:email.index("@")]
    email_domain= email[email.index("@")+1]

    return[email_username,email_domain]

def printMsg(email_username,email_domain):
    print(f"Username is {email_username}")
    print(f"Domain is {email_domain}")



def main():
    email = input('Please enter your email adress: ').strip()
    email_username, email_domain = email_process(email)
    printMsg(email_username, email_domain)


if __name__ == "__main__":
    main()
