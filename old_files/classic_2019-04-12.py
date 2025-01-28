import requests
from bs4 import BeautifulSoup
import re
import queue

# Men's data
file_name = 'mens_ncaa_games.txt'
url = "https://www.masseyratings.com/scores.php?s=305972&sub=11590&all=1&mode=3&sch=on&format=0"

# # Women's data
# file_name = 'womens_ncaa_games.txt'
# url = "https://www.masseyratings.com/scores.php?s=305973&sub=305973&all=1"

try:
    f = open(file_name, 'r')

except FileNotFoundError:
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Clean the data a little
    data_txt = str(soup.find('pre')).lstrip('<pre>').rstrip('</pre>')
    data_txt = re.sub('&amp;', '&', data_txt)
    data_txt = re.sub('\n\nGames: [0-9]*\n\n','', data_txt)
    
    f = open(file_name, 'w', encoding='utf-8')
    f.write(data_txt)
else:
    f.close()

# determine all the teams each team lost to
team_losses = {}
all_teams = []
with open(file_name) as f:
    for l in f:
        losing_team = l[41:65].strip()
        winning_team = l[12:36].strip()
        if losing_team not in team_losses:
            team_losses[losing_team] = [winning_team, ]
        else:
            team_losses[losing_team].append(winning_team)
        
        # keep a list of all teams.  this will be converted to a set
        all_teams.append(losing_team)
        all_teams.append(winning_team)

all_teams = set(all_teams)
original_champ = 'Virginia'
transitive_champions = []
tracking_queue = queue.Queue()

tracking_queue.put(original_champ)

while not tracking_queue.empty():
    team = tracking_queue.get()
    if team not in transitive_champions:
        transitive_champions.append(team)
    else:
        continue
    
    if team in team_losses:
        for t in team_losses[team]: tracking_queue.put(t)
    else:
        continue

print("number of total teams: " + str(len(all_teams)))
print("number of transitive champions: " + str(len(transitive_champions)))