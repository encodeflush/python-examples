def printDocs(docs):
    print(docs)

def sendEmails(num, callback):
    print('This is the email count:', num)
    printDocs('Heres is a list of printed docs:...')

if __name__ == '__main__':
    sendEmails(7, printDocs)
