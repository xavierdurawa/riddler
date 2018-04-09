from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv

class Game(object):

    def __init__(self, game_lst):
        self.daynum = game_lst[0]
        self.date = game_lst[1]
        self.winner = game_lst[2]
        self.win_score = game_lst[4]
        self.loser = game_lst[5]
        self.lose_score = game_lst[7]

def create_csv_from_web(url, csv_name):
    page = urlopen(url)
    print("Connected to " + url)
    text = BeautifulSoup(page, 'html.parser').text
    file = open(csv_name, 'w')
    file.write(text)
    file.close()

# Collect data from masseyratings.com

games_url = "https://www.masseyratings.com/scores.php?s=298892&sub=12801&all=1&mode=3&format=1"
games_csv_name = "games.csv"
create_csv_from_web(games_url, games_csv_name)

# Read game data
games_csv = csv.reader(open('games.csv', 'r'))

# Convert data into Game objects
games = []
for game in games_csv:
    games.append(Game([s.strip() for s in game]))
print('Games have been read.')

# Construct record for each team; a list of teams each team lost to

records = {}
for g in games:
    if g.loser in records.keys():
        records[g.loser].append(g.winner)
        if g.winner not in records.keys():
            records[g.winner] = []
    else:
        records[g.loser] = []
print('Team records have been created')

# Construct a dictionary of transitive champions
# and keep track of whether the teams they lost to
# have been included in the transitive champion dictionary.

champions = {'989': False}    # Villanova's ID

while not all(champions.values()):
    for champ, checked in champions.items():
        if not checked:
            for new_champ in records[champ]:
                if new_champ not in champions.keys():
                    champions[new_champ] = False
            champions[champ] = True
print('Transitive champtions have been identified')

# Match the champion's IDs with their names

# Get team name/id pairs from masseyratings.com
teams_url = "https://www.masseyratings.com/scores.php?s=298892&sub=12801&all=1&mode=3&format=2"
teams_csv_name = "teams.csv"
create_csv_from_web(teams_url, teams_csv_name)

# Read team data
teams_csv = csv.reader(open(teams_csv_name, 'r'))

# Contruct list of transitive champion names and print list to a file
num_teams = 0
champions_names = []
non_champions_names = []
champions_file = open("champions.txt", 'w')
non_champions_file = open("non-champions.txt", 'w')

for t in teams_csv:
    num_teams += 1
    team_id, team_name = t
    if team_id.strip() in champions:
        champions_names.append(team_name)
        champions_file.write(team_name + "\n")
    else:
        non_champions_names.append(team_name)
        non_champions_file.write(team_name + "\n")

champions_file.write("** There are {0} transitive champions for the 2017-2018 season."
                     .format(len(champions)))
non_champions_file.write("** There are {0} non-champions for the 2017-2018 season."
                     .format(num_teams-len(champions)))

champions_file.close()
non_champions_file.close()