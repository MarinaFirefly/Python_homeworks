def check_emails(*email):
    if len(set(email)) < len(list(email)):
        "Some email isn't unique!"
    else:
        "Emails are unique"
check_emails ('sdsd','sdsd')

def check_emails2(*emails):
    print("Some email isn't unique!") if len(set(emails)) < len(list(emails)) else print("Emails are unique")

