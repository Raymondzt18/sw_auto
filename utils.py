from lackey import *
import time
import random

#returns match with the highest confidence
def find_best_match(list_of_matches):
    best_match = list_of_matches[0]
    for match in list_of_matches:
        if match.getScore() > best_match.getScore():
            best_match = match
    return best_match


#list_of_matches = list(findAll("images/5_energy_start.png"))
#click(find_best_match(list_of_matches))

def click_5_energy_start():
    best_match = None
    while True:
        list_of_matches = list(findAll("images/5_energy_start.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            break
        time.sleep(1)
    click(best_match)

def click_start_battle():
    best_match = None
    while True:
        list_of_matches = list(findAll("images/start_battle.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            break
        time.sleep(1)
    click(best_match)

def click_next_stage():
    best_match = None
    while True:
        list_of_matches = list(findAll("images/next_stage.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            break
        time.sleep(1)
    click(best_match)

def click_victory():
    best_match = None
    while True:
        list_of_matches = list(findAll("images/victory.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            break
        time.sleep(1)
    click(best_match)

def click_sell(limit = 10000):
    i = 0
    best_match = None
    while i < limit:
        list_of_matches = list(findAll("images/sell.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            click(best_match)
            return True
        i = i + 1
        time.sleep(1)
    return False

def click_5_energy_replay():
    best_match = None
    while True:
        list_of_matches = list(findAll("images/5_energy_replay.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            break
        time.sleep(1)
    click(best_match)

def click_replay():
    best_match = None
    while True:
        list_of_matches = list(findAll("images/replay.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            break
        time.sleep(1)
    click(best_match)


def click_ok(limit = 10000):
    i = 0
    best_match = None
    while i < limit:
        list_of_matches = list(findAll("images/ok.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            click(best_match)
            return True
        i = i + 1
        time.sleep(1)
    return False

def click_get(limit = 10000):
    i = 0
    best_match = None
    while i < limit:
        list_of_matches = list(findAll("images/get.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            click(best_match)
            return True
        i = i + 1
        time.sleep(1)
    return False

def click_yes(limit = 10000):
    i = 0
    best_match = None
    while i < limit:
        list_of_matches = list(findAll("images/yes.png"))
        if list_of_matches:
            best_match = find_best_match(list_of_matches)
            click(best_match)
            return True
        i = i + 1
        time.sleep(1)
    return False

