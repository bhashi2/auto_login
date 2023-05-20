#Program by Bilal Hashim
#Made to sign into league of legends and insert log in information for any account

#League Client
# C:\Riot Games\League of Legends\LeagueClient.exe
#Riot Client
# C:\Riot Games\Riot Client\RiotClientServices.exe
import sys
import argparse
from functions import *


parser = argparse.ArgumentParser(description="login to riot client",
                                 epilog='program by Bilal Hashim with the help of stackoverflow and library documentation')
parser.add_argument('user', metavar='username', nargs='?', default='Viollet46', help="login to client with username")
parser.add_argument('-r', '--resignin',dest='r', action='store_true',help='sign out and sign into a different account')
parser.add_argument('-l', '--login', dest='l', action='store_true', help='login if the client is already open')

try:
    args = parser.parse_args()
    print(args.user)
except argparse.ArgumentError:
    print('issue with command line arguements')
    exit()

if args.l:
    login(args.user)
    print("in l")
elif args.r:
    switch_account(args.user)
    print("in r")
else:
    start_and_login(args.user)
    print("in default")

