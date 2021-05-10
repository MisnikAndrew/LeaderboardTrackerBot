import misc
import requests
import json

url1 = 'https://api.telegram.org/bot{}/'.format(misc.tgtoken)



global_lm = ''


def get_data(server, mode):
    if server == 'EU' and mode == 'STD':
        f = open('STD_EU.json', 'r')
        ans = json.loads(f.read())
        f.close()
        return ans

    elif server == 'US' and mode == 'STD':
        f = open('STD_US.json', 'r')
        ans = json.loads(f.read())
        f.close()
        return ans

    elif server == 'AP' and mode == 'STD':
        f = open('STD_AP.json', 'r')
        ans = json.loads(f.read())
        f.close()
        return ans

    elif server == 'EU' and mode == 'WILD':
        f = open('WILD_EU.json', 'r')
        ans = json.loads(f.read())
        f.close()
        return ans

    elif server == 'US' and mode == 'WILD':
        f = open('WILD_US.json', 'r')
        ans = json.loads(f.read())
        f.close()
        return ans

    elif server == 'AP' and mode == 'WILD':
        f = open('WILD_AP.json', 'r')
        ans = json.loads(f.read())
        f.close()
        return ans

def get_BT_by_rank(rank, server='EU', mode='STD'):
    rank -= 1
    if server == 'EU' and mode == 'STD':
        r = get_data(server, mode)
        ans = r['top'][rank]
        if len(ans) > 20:
            ans = bytes(ans, 'utf-8').decode()
        return ans

    elif server == 'US' and mode == 'STD':
        r = get_data(server, mode)
        ans = r['top'][rank]
        if len(ans) > 20:
            ans = bytes(ans, 'utf-8').decode()
        return ans

    elif server == 'AP' and mode == 'STD':
        r = get_data(server, mode)
        ans = r['top'][rank]
        if len(ans) > 20:
            ans = bytes(ans, 'utf-8').decode()
        return ans

    elif server == 'EU' and mode == 'WILD':
        r = get_data(server, mode)
        ans = r['top'][rank]
        if len(ans) > 20:
            ans = bytes(ans, 'utf-8').decode()
        return ans

    elif server == 'US' and mode == 'WILD':
        r = get_data(server, mode)
        ans =  r['top'][rank]
        if len(ans) > 20:
            ans = bytes(ans, 'utf-8').decode()
        return ans

    elif server == 'AP' and mode == 'WILD':
        r = get_data(server, mode)
        ans = r['top'][rank]
        if len(ans) > 20:
            ans = bytes(ans, 'utf-8').decode()
        return ans


def get_ranks():
    r = requests.get(misc.urlSTD_EU).json()
    for i in r['leaderboard']['table']['rows']:
        print(i['player'][0]['battleTag'])
    #return r['leaderboard']['table']['rows'][199]['player'][0]['battleTag']


def get_updates():
    URL = url1 + 'getupdates'
    r = requests.get(URL).json()
    return r


def add_to_tracklist(nickname, server, mode, ID):
    f = open('data.json', 'r')
    data = json.loads(f.read())
    print(data)
    f.close()
    try:
        if ID not in data[mode][server][nickname]:
            data[mode][server][nickname].append(ID)
        else:
            return 'Error: This person is already in your tracklist'
    except:
        data[mode][server][nickname] = [ID]
    f = open('data.json', 'w')
    json.dump(data, f)
    f.close()
    return 'Done'

def remove_from_tracklist(nickname, server, mode, ID):
    f = open('data.json', 'r')
    data = json.loads(f.read())
    print(data)
    f.close()
    try:
        if ID in data[mode][server][nickname]:
            data[mode][server][nickname].remove(ID)
        else:
            print('1231234')
            return 'Error: This person is not in your tracklist'
    except:
        return 'Error: This person is not in your tracklist'
        print('123123')
    f = open('data.json', 'w')
    json.dump(data, f)
    f.close()
    return 'Done'


def clear_tracklist(ID):
    f = open('data.json', 'r')
    data = json.loads(f.read())
    f.close()
    for pair in list(data.items()):
        mode = pair[0]
        for a_pair in list(pair[1].items()):
            server = a_pair[0]
            for b_pair in list(a_pair[1].items()):
                if ID in b_pair[1]:
                    print(b_pair)
                    data[mode][server][b_pair[0]].remove(ID)
    f = open('data.json', 'w')
    json.dump(data, f)
    f.close()


def show_tracklist(ID):
    f = open('data.json', 'r')
    data = json.loads(f.read())
    tracklist = []
    for pair in list(data.items()):
        mode = pair[0]
        for a_pair in list(pair[1].items()):
            server = a_pair[0]
            for b_pair in list(a_pair[1].items()):
                if ID in b_pair[1]:
                    tracklist.append(b_pair[0] + ' ' + server + ' ' + mode)

    return tracklist


def get_message():
    d = get_updates()
    try:
        chat_id = d['result'][-1]['message']['chat']['id']
        message_text = d['result'][-1]['message']['text']

        message = {'chat_id': chat_id, 'text': message_text}

        return message
    except:
        message = {'chat_id': 0, 'text': '0'}
        return message


def send_message(chat_id, text):
    URL = url1 + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(URL)


def main():
    clear_tracklist(0)
    global global_lm
    while True:
        lm = get_message()
        if lm != global_lm:
            global_lm = lm
            if lm['text'].startswith('!add'):
                data = lm['text'].split()
                print(data)
                if len(data) >= 4 and (data[-2] == 'EU' or data[-2] == 'US' or data[-2] == 'AP') and (data[-1] == 'STD' or data[-1] == 'WILD'):
                    for i in range(len(data) - 3):
                        add_to_tracklist(data[i+1], data[-2], data[-1], lm['chat_id'])
                    p = show_tracklist(lm['chat_id'])
                    ans = ''
                    for i in range(len(p)):
                        ans += p[i] + '\n'
                    send_message(lm['chat_id'], 'Done, now your tracklist is \n' + ans)


            elif lm['text'] == ('!showtracklist'):
                if show_tracklist(lm['chat_id']):
                    p = show_tracklist(lm['chat_id'])
                    ans = ''
                    for i in range(len(p)):
                        ans += p[i] + '\n'
                    send_message(lm['chat_id'], ans)
                else:
                    send_message(lm['chat_id'], 'Your tracklist is empty')

            elif lm['text'] == ('!cleartracklist'):
                clear_tracklist(lm['chat_id'])
                send_message(lm['chat_id'], 'Done')

            elif lm['text'].startswith('!remove'):
                data = lm['text'].split()
                if len(data) >= 4 and (data[-2] == 'EU' or data[-2] == 'US' or data[-2] == 'AP') and (data[-1] == 'STD' or data[-1] == 'WILD'):
                    for i in range(len(data) - 3):
                        remove_from_tracklist(data[i+1], data[-2], data[-1], lm['chat_id'])
                p = show_tracklist(lm['chat_id'])
                ans = ''
                for i in range(len(p)):
                    ans += p[i] + '\n'
                send_message(lm['chat_id'], 'Done, now your tracklist is \n' + ans)

            elif lm['text'].startswith('!track'):
                h = lm['text'].split()
                if len(h) == 4 and (h[-2] == 'EU' or h[-2] == 'US' or h[-2] == 'AP') and (h[-1] == 'STD' or h[-1] == 'WILD'):
                    k = get_data(h[-2], h[-1])
                    if h[1] in k['top']:
                        send_message(lm['chat_id'], h[1] + ' is rank ' + str(k['top'].index(h[1]) + 1))
                    else:
                        send_message(lm['chat_id'], h[1] + ' is not in top-200 now')

            elif lm['text'].startswith('!rank'):
                j = lm['text'].split()
                if len(j) == 4 and (j[-2] == 'EU' or j[-2] == 'US' or j[-2] == 'AP') and (j[-1] == 'STD' or j[-1] == 'WILD'):
                    a = get_BT_by_rank(int(j[1]), j[2], j[3])
                    send_message(lm['chat_id'], a)

            elif lm['text'] == '/start':
                send_message(lm['chat_id'], "Hello, I'm HSTrackBot, here is my commands list: \n server can be [EU, US, AP], mode can be [WILD, STD] \n 1. !add <nick> <server> <mode> - adds person to your tracklist \n 2. !remove <nick> <server> <mode> - removes person to your tracklist \n 3. !showtracklist - show your current tracklist \n 4. !cleartracklist - remove everybody from your tracklist \n 5. !track <nick> <server> <mode> - returns rank of a person (if in top 200) \n 6. !rank <rank(1-200)> <server> <mode> - returns nickname of a person that is input rank \n Each ~10 minutes I will send you information about persons from your tracklist, their changes on leaderboard.")


    # with open('updates.json', 'w') as f:
    #     json.dump(d, f, indent=2, ensure_ascii=False)







main()