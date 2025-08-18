import webbrowser
from imap_tools import MailBox, AND
from ai_response import summarize_email

def main():
    #set up IMAP server
    mailbox = MailBox('imap.gmail.com')#if hotmail, use 'imap-mail.outlook.com'
    mailbox.login('Writeyourowngmail', 'TypeThePasswordGivenİnAppVerification', 'INBOX')

    summarized_mail = []
    email_objs = []

    #gather unread emails
    if mailbox.folder.exists('INBOX'):
        for msg in mailbox.fetch(AND(seen=False)):
            summarized_mail.append(msg.text)
            email_objs.append(msg)

    print(f"Total emails fetched: {len(summarized_mail)}")

    links = []
    for idx, mail in enumerate(summarized_mail):
        summary = summarize_email(mail)
        msg_id = email_objs[idx].uid
        gmail_link = f"https://mail.google.com/mail/u/0/#inbox/{msg_id}"
        links.append(gmail_link)
        print(f"{idx+1}. Summary: {summary}")
        print(f"Reply link: {gmail_link}")

    if not summarized_mail:
        print("No unread emails found.")
        return

    # Prompt user for email number to reply
    email_num = input("Enter the number of the email you want to reply to (or press Enter to exit): ")
    if email_num.isdigit():
        email_num = int(email_num)
        if 1 <= email_num <= len(links):
            print(f"Opening reply link for email {email_num} in Google Chrome...")
            chrome = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')#make sure to adjust the path to your Chrome executable,if necessary use another browser
            chrome.open(links[email_num-1])
            exit()
        else:
            print("Invalid email number.")
            exit()
    else:
        print("Exiting.")
        exit()

if __name__ == "__main__":
    main()