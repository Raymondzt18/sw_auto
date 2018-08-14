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

    #if click_ok():
    #    sleeptime = random.uniform(1,1.5)
    #    print("Sleeping for " + str(sleeptime) + "secs")
    #    time.sleep(sleeptime)

    if click_sell():
        sleeptime = random.uniform(1,1.5)
        print("Sleeping for " + str(sleeptime) + "secs")
        time.sleep(sleeptime)

    if click_yes():
        sleeptime = random.uniform(1,1.5)
        print("Sleeping for " + str(sleeptime) + "secs")
        time.sleep(sleeptime)

    click_5_energy_replay()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)
