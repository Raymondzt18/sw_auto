from lackey import *
import time
import random

def click_5_energy_start():
    i = 0
    while i < 3:
        try:
            click("images/5_energy_start.png")
        except Exception:
            continue
        break
    if not i == 3:
        print("Clicked on 5_energy_start!")
    else:
        print("5_energy_start not found!")

def click_victory():
    while True:
        try:
            click("images/victory.png")
        except Exception:
            continue
        break
    print("Clicked on victory!")

def click_sell():
    i = 0
    while i < 1:
        try:
            click("images/sell.png")
        except Exception:
            i = i+1
            continue
        break
    if i == 0:
        print("Clicked on sell!")
        return True
    else:
        print("Sell not found!")
        return False

def click_5_energy_replay():
    while True:
        try:
            click("images/5_energy_replay.png")
        except Exception:
            continue
        break
    print("Clicked on 5_energy_replay!")

def click_ok():
    i = 0
    while i < 1:
        try:
            click("images/ok.png")
        except Exception:
            i = i+1
            continue
        break
    if i == 0:
        print("Clicked on ok!")
        return True
    else:
        print("Ok not found!")
        return False

def click_yes():
    i = 0
    while i < 1:
        try:
            click("images/yes.png")
        except Exception:
            i = i+1
            continue
        break
    if i == 0:
        print("Clicked on yes!")
        return True
    else:
        print("Yes not found!")
        return False
