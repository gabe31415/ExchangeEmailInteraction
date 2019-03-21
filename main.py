import os
from exchangelib import Credentials, Account

# Get email address that is stored in environment variable
if os.getenv('workEmailAddress') != None:
    workEmailAddress = os.getenv('workEmailAddress')
else:
    print('failed to get Email Address')
    exit

# Get email password that is stored in environment variable
if os.getenv('workEmailPassword') != None:
    workEmailPassword = os.getenv('workEmailPassword')
else:
    print('failed to get Email Password')
    exit

credentials = Credentials(workEmailAddress, workEmailPassword)
account = Account(workEmailAddress, credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:2]:
    print(item.subject, item.sender, item.datetime_received)
