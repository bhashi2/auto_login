import os
import pyautogui as pyg
import time
from passwords import passMap

#opens league client
#waits for it to open (maybe better way?)
#first moveto is to username, 2nd is pass and finally clicks on submit
def start_and_login(name):
    os.startfile ("C:\Riot Games\League of Legends\LeagueClient.exe")
    time.sleep(5)
    pyg.moveTo(700, 775)
    pyg.leftClick()
    pyg.write(name)
    pyg.moveTo(700, 900)
    pyg.leftClick()
    pyg.write(passMap[name])
    pyg.moveTo(930, 1555)
    pyg.leftClick()

def login(name):
    pyg.moveTo(700, 775)
    pyg.leftClick()
    pyg.write(name)
    pyg.moveTo(700, 900)
    pyg.leftClick()
    pyg.write(passMap[name])
    pyg.moveTo(930, 1555)
    pyg.leftClick()

def switch_account(name):
    pyg.moveTo(3004, 432)
    pyg.click()
    pyg.moveTo(1988, 1100)
    pyg.click()
    time.sleep(2)
    login(name)

