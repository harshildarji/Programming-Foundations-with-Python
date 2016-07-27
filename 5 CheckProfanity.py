import os
import urllib.request as url

def readText(path):
    quotes = open(path)
    contents = quotes.read()
    quotes.close()
    text = list(contents.split('\n'))
    line = 1
    for item in text:
        checkProfanity(item, line)
        line += 1
        
def checkProfanity(text, line):
    address = ("http://www.wdylike.appspot.com/?q=%s" % text).replace(' ', '%20')
    connection = url.urlopen(address)
    output = str(connection.read())[1:]
    if output == "'true'":
        print('Line #%s: %s | %s' % (line, output.title(), text))
    connection.close()

cwd = os.getcwd()
path = cwd + '\MovieQuotes.txt'
print('Checking profanity...')
readText(path)
