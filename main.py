
import requests
from bs4 import BeautifulSoup
import csv


datas =[]

url = 'https://www.futbin.com/players?page='
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'


}

for page in range(1, 10):
    req =  requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    numbs = [1,2]
    for numb in numbs:
        players = soup.findAll('tr','player_tr_'+str(numb))
        for player in players:
            tgs = player.findAll('td')
            name = tgs[0].text.strip()
            ratings =tgs[1].text.strip()
            positions = tgs[2].text.strip()
            allstate = player.find('span', 'players_club_nation').findAll('a')
            club = allstate[0]['data-original-title'].replace('FUT 21 ICONS', 'unkwon').strip()
            nation = allstate[1]['data-original-title'].replace('Icons', 'unkwon').strip()
            league = allstate[2]['data-original-title'].replace('Icons', 'unkwon').strip()

            data_dict ={
                'Player Names': name,
                'Player Ratings': ratings,
                'The Best positions': positions,
                'Player Clubs': club,
                'Player Nations' : nation,
                'Player Leagues' : league,
            }
            #print(data_dict)
            datas.append(data_dict)
            head = ['Player Names', 'Player Ratings', 'The Best Positions', 'Player Clubs', 'Player Nations', 'Player League']
            write = csv.writer(open('futbin_item.csv', 'w', newline=''))
            write.writerow(head)
            for d in datas: write.writerow(d)









