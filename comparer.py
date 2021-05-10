import json
from time import sleep
import requests
from misc import tgtoken

f = open('STD_EU.json', 'r')
lbeustd = json.loads(f.read())['top']
f.close()

f = open('STD_US.json', 'r')
lbusstd = json.loads(f.read())['top']
f.close()

f = open('STD_AP.json', 'r')
lbapstd = json.loads(f.read())['top']
f.close()

f = open('WILD_EU.json', 'r')
lbeuwild = json.loads(f.read())['top']
f.close()

f = open('WILD_US.json', 'r')
lbuswild = json.loads(f.read())['top']
f.close()

f = open('WILD_AP.json', 'r')
lbapwild = json.loads(f.read())['top']
f.close()

def send_message(chat_id, text):
    URL = 'https://api.telegram.org/bot{}/sendmessage?chat_id={}&text={}'.format(tgtoken, chat_id, text)
    requests.get(URL)





while True:
    f = open('STD_EU.json', 'r')
    new_lbeustd = json.loads(f.read())['top']
    f.close()

    f = open('STD_US.json', 'r')
    new_lbusstd = json.loads(f.read())['top']
    f.close()

    f = open('STD_AP.json', 'r')
    new_lbapstd = json.loads(f.read())['top']
    f.close()

    f = open('WILD_EU.json', 'r')
    new_lbeuwild = json.loads(f.read())['top']
    f.close()

    f = open('WILD_US.json', 'r')
    new_lbuswild = json.loads(f.read())['top']
    f.close()

    f = open('WILD_AP.json', 'r')
    new_lbapwild = json.loads(f.read())['top']
    f.close()

    if new_lbeustd != lbeustd or new_lbeuwild != lbeuwild or new_lbusstd != lbusstd or new_lbuswild != lbuswild or new_lbapstd != lbapstd or new_lbapwild != lbapwild:

        f = open('data.json', 'r')
        data = json.loads(f.read())
        f.close()

        for pair in list(data.items()):
            mode = pair[0]
            for a_pair in list(pair[1].items()):
                server = a_pair[0]
                for b_pair in list(a_pair[1].items()):
                    if mode == 'STD' and server == 'EU':
                        if b_pair[0] in new_lbeustd and not b_pair[0] in lbeustd:
                            ans = b_pair[0] + ' is now in top-200 at ' + server + ' server specifically his place is ' + str(new_lbeustd.index(b_pair[0]) + 1)

                        elif b_pair[0] not in new_lbeustd and b_pair[0] in lbeustd:
                            ans = b_pair[0] + ' is now kicked out from top-200 at ' + server + ' server'

                        elif b_pair[0] in new_lbeustd and b_pair[0] in lbeustd:
                            if abs(new_lbeustd.index(b_pair[0]) - lbeustd.index(b_pair[0])) >= 15:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeustd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbeustd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeustd.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbeustd.index(b_pair[0]) - lbeustd.index(b_pair[0])) > 4 and 20 <= lbeustd.index(b_pair[0]) < 50:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeustd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbeustd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeustd.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbeustd.index(b_pair[0]) - lbeustd.index(b_pair[0])) > 1 and 10 <= lbeustd.index(b_pair[0]) < 20:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeustd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbeustd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeustd.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbeustd.index(b_pair[0]) - lbeustd.index(b_pair[0])) != 0 and 0 <= lbeustd.index(b_pair[0]) < 10:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeustd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbeustd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeustd.index(b_pair[0]) + 1) + ')'

                    elif mode == 'STD' and server == 'US':
                        if b_pair[0] in new_lbusstd and not b_pair[0] in lbusstd:
                            ans = b_pair[0] + ' is now in top-200 at ' + server + ' server , specifically his place is ' + str(new_lbusstd.index(b_pair[0]) + 1)

                        elif b_pair[0] not in new_lbusstd and b_pair[0] in lbusstd:
                            ans = b_pair[0] + ' is now kicked out from top-200 at ' + server + ' server'

                        elif b_pair[0] in new_lbusstd and b_pair[0] in lbusstd:
                            if abs(new_lbusstd.index(b_pair[0]) - lbusstd.index(b_pair[0])) >= 15:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbusstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbusstd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbusstd.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbusstd.index(b_pair[0]) - lbusstd.index(b_pair[0])) > 4 and 20 <= lbusstd.index(b_pair[0]) < 50:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbusstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbusstd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbusstd.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbusstd.index(b_pair[0]) - lbusstd.index(b_pair[0])) > 1 and 10 <= lbusstd.index(b_pair[0]) < 20:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbusstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbusstd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbusstd.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbusstd.index(b_pair[0]) - lbusstd.index(b_pair[0])) != 0 and 0 <= lbusstd.index(b_pair[0]) < 10:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbusstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbusstd.index(b_pair[0]) + 1) + ' -> ' + str(new_lbusstd.index(b_pair[0]) + 1) + ')'

                    elif mode == 'STD' and server == 'AP':
                        if b_pair[0] in new_lbapstd and not b_pair[0] in lbapstd:
                            ans = b_pair[0] + ' is now in top-200 at ' + server + ' server , specifically his place is ' + str(new_lbapstd.index(b_pair[0]) + 1)

                        elif b_pair[0] not in new_lbapstd and b_pair[0] in lbapstd:
                            ans = b_pair[0] + ' is now kicked out from top-200 at ' + server + ' server'

                        elif b_pair[0] in new_lbapstd and b_pair[0] in lbapstd:
                            if abs(new_lbapstd.index(b_pair[0]) - lbapstd.index(b_pair[0])) >= 15:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbapstd.index(b_pair[0])) + ' -> ' + str(new_lbapstd.index(b_pair[0])) + ')'
                            elif abs(new_lbapstd.index(b_pair[0]) - lbapstd.index(b_pair[0])) > 4 and 20 <= lbapstd.index(b_pair[0]) < 50:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbapstd.index(b_pair[0])) + ' -> ' + str(new_lbapstd.index(b_pair[0])) + ')'
                            elif abs(new_lbapstd.index(b_pair[0]) - lbapstd.index(b_pair[0])) > 1 and 10 <= lbapstd.index(b_pair[0]) < 20:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbapstd.index(b_pair[0])) + ' -> ' + str(new_lbapstd.index(b_pair[0])) + ')'
                            elif abs(new_lbapstd.index(b_pair[0]) - lbapstd.index(b_pair[0])) != 0 and 0 <= lbapstd.index(b_pair[0]) < 10:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapstd.index(b_pair[0]) + 1) + ' at ' + server + ' server STD (' + str(lbapstd.index(b_pair[0])) + ' -> ' + str(new_lbapstd.index(b_pair[0])) + ')'

                    elif mode == 'WILD' and server == 'EU':
                        if b_pair[0] in new_lbeuwild and not b_pair[0] in lbeuwild:
                            ans = b_pair[0] + ' is now in top-200 at ' + server + ' server specifically his place is ' + str(new_lbeuwild.index(b_pair[0]) + 1)

                        elif b_pair[0] not in new_lbeuwild and b_pair[0] in lbeuwild:
                            ans = b_pair[0] + ' is now kicked out from top-200 at ' + server + ' server'

                        elif b_pair[0] in new_lbeuwild and b_pair[0] in lbeuwild:
                            if abs(new_lbeuwild.index(b_pair[0]) - lbeuwild.index(b_pair[0])) >= 15:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbeuwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbeuwild.index(b_pair[0]) - lbeuwild.index(b_pair[0])) > 4 and 20 <= lbeuwild.index(b_pair[0]) < 50:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbeuwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbeuwild.index(b_pair[0]) - lbeuwild.index(b_pair[0])) > 1 and 10 <= lbeuwild.index(b_pair[0]) < 20:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbeuwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbeuwild.index(b_pair[0]) - lbeuwild.index(b_pair[0])) != 0 and 0 <= lbeuwild.index(b_pair[0]) < 10:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbeuwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbeuwild.index(b_pair[0]) + 1) + ')'

                    elif mode == 'WILD' and server == 'US':
                        if b_pair[0] in new_lbuswild and not b_pair[0] in lbuswild:
                            ans = b_pair[0] + ' is now in top-200 at ' + server + ' server , specifically his place is ' + str(new_lbuswild.index(b_pair[0]) + 1)

                        elif b_pair[0] not in new_lbuswild and b_pair[0] in lbuswild:
                            ans = b_pair[0] + ' is now kicked out from top-200 at ' + server + ' server'

                        elif b_pair[0] in new_lbuswild and b_pair[0] in lbuswild:
                            if abs(new_lbuswild.index(b_pair[0]) - lbuswild.index(b_pair[0])) >= 15:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbuswild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbuswild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbuswild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbuswild.index(b_pair[0]) - lbuswild.index(b_pair[0])) > 4 and 20 <= lbuswild.index(b_pair[0]) < 50:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbusstd.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbuswild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbuswild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbuswild.index(b_pair[0]) - lbuswild.index(b_pair[0])) > 1 and 10 <= lbuswild.index(b_pair[0]) < 20:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbuswild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbuswild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbuswild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbuswild.index(b_pair[0]) - lbuswild.index(b_pair[0])) != 0 and 0 <= lbuswild.index(b_pair[0]) < 10:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbuswild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbuswild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbuswild.index(b_pair[0]) + 1) + ')'

                    elif mode == 'WILD' and server == 'AP':
                        if b_pair[0] in new_lbapwild and not b_pair[0] in lbapwild:
                            ans = b_pair[0] + ' is now in top-200 at ' + server + ' server , specifically his place is ' + str(new_lbapwild.index(b_pair[0]) + 1)

                        elif b_pair[0] not in new_lbapwild and b_pair[0] in lbapwild:
                            ans = b_pair[0] + ' is now kicked out from top-200 at ' + server + ' server'

                        elif b_pair[0] in new_lbapwild and b_pair[0] in lbapwild:
                            if abs(new_lbapwild.index(b_pair[0]) - lbapwild.index(b_pair[0])) >= 15:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbapwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbapwild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbapwild.index(b_pair[0]) - lbapwild.index(b_pair[0])) > 4 and 20 <= lbapwild.index(b_pair[0]) < 50:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbapwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbapwild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbapwild.index(b_pair[0]) - lbapwild.index(b_pair[0])) > 1 and 10 <= lbapwild.index(b_pair[0]) < 20:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbapwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbapwild.index(b_pair[0]) + 1) + ')'
                            elif abs(new_lbapwild.index(b_pair[0]) - lbapwild.index(b_pair[0])) != 0 and 0 <= lbapwild.index(b_pair[0]) < 10:
                                ans = b_pair[0] + ' is now rank ' + str(new_lbapwild.index(b_pair[0]) + 1) + ' at ' + server + ' server WILD (' + str(lbapwild.index(b_pair[0]) + 1) + ' -> ' + str(new_lbapwild.index(b_pair[0]) + 1) + ')'
                    try:
                        for i in range(len(b_pair[1])):
                            send_message(b_pair[1][i], ans)
                        del ans
                    except:
                        pass
        lbapwild = new_lbapwild
        lbapstd = new_lbapstd

        lbuswild = new_lbuswild
        lbusstd = new_lbusstd
        lbeuwild = new_lbeuwild
        lbeustd = new_lbeustd
    sleep(275)