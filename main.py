import os
from exchangelib import Credentials, Account

def getVarFromEnv(EnvVarName):
    if os.getenv(EnvVarName) != None:
        return os.getenv(EnvVarName)
    else:
        print('failed to get', EnvVarName)
        exit

def getEmail():
    emailAddress = getVarFromEnv('workEmailAddress')
    emailPassword = getVarFromEnv('workEmailPassword')
    credentials = Credentials(emailAddress, emailPassword)
    account = Account(emailAddress, credentials=credentials, autodiscover=True)
    return account

def BackupLogs01():
    account = getEmail()
    subjectLine = getVarFromEnv('backupEmailSubjectCustomer01')
    for item in account.inbox.all().order_by('-datetime_received')[:10]:
        if item.subject == subjectLine:
            print(item.datetime_received)

BackupLogs01()
