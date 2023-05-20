#Program by Bilal Hashim
#Made to sign into league of legends and insert log in information for any account

#League Client
# C:\Riot Games\League of Legends\LeagueClient.exe
#Riot Client
# C:\Riot Games\Riot Client\RiotClientServices.exe
import sys
from functions import *

#get the name inserted in command line, argv[0] is the program name
accName = sys.argv[1]

start_and_login(accName)