from emailslicer import email_process,printMsg

def main():
    emails = ["nhmv@gmail.com", "hn78@tucan.com", "v_n@ptw.com"]
    for email in emails:
        email_username, email_domain = email_process(email)
        printMsg(email_username,email_domain)

if __name__ == "__main__":
    main()