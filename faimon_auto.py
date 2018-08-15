from utils import *

while True:

    click_5_energy_start()

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

    if click_ok(limit = 1):
        sleeptime = random.uniform(1,1.5)
        print("Sleeping for " + str(sleeptime) + "secs")
        time.sleep(sleeptime)

    elif click_sell(limit = 1):
        sleeptime = random.uniform(1,1.5)
        print("Sleeping for " + str(sleeptime) + "secs")
        time.sleep(sleeptime)

        if click_yes(limit = 1):
            sleeptime = random.uniform(1,1.5)
            print("Sleeping for " + str(sleeptime) + "secs")
            time.sleep(sleeptime)

    click_5_energy_replay()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)
