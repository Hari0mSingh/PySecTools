from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description="\nUsage: python zipbrute.py -z <zipfile.zip> -p <passwordfile.txt>")
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="Password file")
parsed_args = parser.parse_args()

try:
    ziparchive = ZipFile(parsed_args.ziparchive)
    passfile = parsed_args.passfile
except FileNotFoundError:
    print("Error: Zip file or password file not found.")
    print(parser.description)
    exit(1)

password_found = False

with open(passfile, 'r') as f:
    for line in f:
        password = line.strip("\n").encode("utf-8")

        try:
            ziparchive.extractall(pwd=password)
            print("\nFound password:", password.decode())
            password_found = True
            break
        except RuntimeError:
            continue

if not password_found:
    print("\nPassword not found. Try a bigger password list.")