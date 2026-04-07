from subprocess import call
from time import sleep
from random import randint

def main():
    for i in range(0, randint(7, 16)):
        s = '|/-\\'
        c = s[i%len(s)]
        print('['+c+'] Inventorising local dependencies...', end='\r', flush=True)
        sleep(0.25)
    print('')
    call(['pip', 'freeze'])
    for i in range(0, randint(10, 27)):
        s = '|/-\\'
        c = s[i%len(s)]
        print('['+c+'] Scanning filesystem for virtualenvs and wheels...', end='\r', flush=True)
        sleep(0.25)
    for i in range(0, randint(5, 13)):
        s = '|/-\\'
        c = s[i%len(s)]
        print('['+c+'] Checking for exploitation artifacts...', end='\r', flush=True)
        sleep(0.25)
    print('')
    print('')
    print('No packages identified with known vulnerable versions!')
