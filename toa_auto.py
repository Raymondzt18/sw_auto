from utils import *

while True:

    click_start_battle()

    click_victory()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    click_victory()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    click_victory()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    click_ok(limit = 1)
    
    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    click_next_stage()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)
