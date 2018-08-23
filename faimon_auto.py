from utils import *

click_5_energy_start()

loop_num = 0

while loop_num < 21:

    #click_5_energy_start()

    click_victory()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    click_victory()

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    click_victory()

    loop_num = loop_num + 1

    print("Succeeded " +  str(loop_num) + " times!")

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)

    if click_sell(limit = 1):
        sleeptime = random.uniform(1,1.5)
        print("Sleeping for " + str(sleeptime) + "secs")
        time.sleep(sleeptime)

        if click_yes(limit = 1):
            sleeptime = random.uniform(1,1.5)
            print("Sleeping for " + str(sleeptime) + "secs")
            time.sleep(sleeptime)

    else: 
        click_ok(limit = 1)
        sleeptime = random.uniform(1,1.5)
        print("Sleeping for " + str(sleeptime) + "secs")
        time.sleep(sleeptime)

    click_5_energy_replay()

    if find_open_shop(limit = 1):
        input("Press Enter to continue...")

    sleeptime = random.uniform(1,1.5)
    print("Sleeping for " + str(sleeptime) + "secs")
    time.sleep(sleeptime)
