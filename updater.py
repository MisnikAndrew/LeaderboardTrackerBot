import requests
import json
from time import sleep
import misc
from random import randint

while True:
    lbeustd = []
    lbusstd = []
    lbapstd = []
    lbeuwild = []
    lbuswild = []
    lbapwild = []
    STD_EU = requests.get(misc.urlSTD_EU).json()
    STD_US = requests.get(misc.urlSTD_US).json()
    STD_AP = requests.get(misc.urlSTD_AP).json()
    WILD_EU = requests.get(misc.urlWILD_EU).json()
    WILD_US = requests.get(misc.urlWILD_US).json()
    WILD_AP = requests.get(misc.urlWILD_AP).json()
    print(STD_EU)
    f = open('STD_EU.json', 'w')
    for i in range(200):
        lbeustd.append(STD_EU['leaderboard']['table']['rows'][i]['player'][0]['battleTag'])
    json.dump({"top": lbeustd}, f)
    f.close()
    f = open('STD_US.json', 'w')
    for i in range(200):
        lbusstd.append(STD_US['leaderboard']['table']['rows'][i]['player'][0]['battleTag'])
    json.dump({"top":lbusstd}, f)
    f.close()
    f = open('STD_AP.json', 'w')
    for i in range(200):
        lbapstd.append(STD_AP['leaderboard']['table']['rows'][i]['player'][0]['battleTag'])
    json.dump({"top":lbapstd}, f)
    f.close()
    f = open('WILD_EU.json', 'w')
    for i in range(200):
        lbeuwild.append(WILD_EU['leaderboard']['table']['rows'][i]['player'][0]['battleTag'])
    json.dump({"top":lbeuwild}, f)
    f.close()
    f = open('WILD_US.json', 'w')
    for i in range(200):
        lbuswild.append(WILD_US['leaderboard']['table']['rows'][i]['player'][0]['battleTag'])
    json.dump({"top":lbuswild}, f)
    f.close()
    f = open('WILD_AP.json', 'w')
    for i in range(200):
        lbapwild.append(WILD_AP['leaderboard']['table']['rows'][i]['player'][0]['battleTag'])
    json.dump({"top":lbapwild}, f)
    f.close()
    sleep(300)

