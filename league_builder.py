import csv


LETTER_TEXT = """Dear {},

Your child, {} will be playing for the {}!

The first practice session is on {}.
We'll see you there!

Coach
"""

def add_team_field(team_name, team):
    for player in team:
        player["Team"] = team_name

def create_team_roster():
    """Write team names and assigned players to the teams.txt file."""
    inexperienced = []
    experienced = []
    dragons=[]
    sharks=[]
    raptors=[]
    teams=[sharks, dragons, raptors]
    date = 'Saturday, March 8'
    with open('soccer_players.csv', newline='') as csv_players_file:
        reader = csv.DictReader(csv_players_file, delimiter=',')
        for row in reader:
            if row['Soccer Experience'].upper() == 'YES':
                experienced.append(row)
            else:
                inexperienced.append(row)
        # print(f'The experienced players are: {experienced}')
        # print(f'The inexperienced players are: {inexperienced}')

    # count = 0
    # for exp in experienced:
    #     count+=1
    #     if count == 1:
    #         dragons.append(exp)
    #     elif count == 2:
    #         sharks.append(exp)
    #     elif count == 3:
    #         raptors.append(exp)
    #     elif count > 3:
    #         count = 0
    for players in experienced, inexperienced:
        for player in players:
            if len(dragons)<=len(sharks) & len(dragons)<=len(raptors):
                dragons.append(player)
            elif len(sharks)<=len(raptors):
                sharks.append(player)
            else:
                raptors.append(player)

    # print(f'The Dragon players are: {dragons}')
    # print(f'The Sharks players are: {sharks}')
    # print(f'The Raptors players are: {raptors}')
    with open("teams.txt", "w") as file:
        file.write("Sharks\n======\n")
        for player in sharks:
            file.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**player))
        file.write("\nDragons\n=======\n")
        for player in dragons:
            file.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**player))
        file.write("\nRaptors\n=======\n")
        for player in raptors:
            file.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**player))


        add_team_field("Sharks", sharks)
        add_team_field("Dragons", dragons)
        add_team_field("Raptors", raptors)

    all_players = sharks + dragons + raptors
    for player in all_players:
        player_name_file = "_".join(player["Name"].lower().split()) + ".txt"
        with open(player_name_file, "w") as file:
            file.write(LETTER_TEXT.format(player["Guardian Name(s)"], player["Name"], player["Team"], date))




if __name__ == '__main__':
    create_team_roster()
