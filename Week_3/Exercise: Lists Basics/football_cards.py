team_a = ['A-'+str(number) for number in range(1,11+1)]
team_b = ['B-'+str(number) for number in range(1,11+1)]

list_of_players_with_red_cards = input().split()
list_of_kicked_players = []
for player in list_of_players_with_red_cards:
    if player in list_of_kicked_players:
        continue
    else:
        list_of_kicked_players.append(player)
        if player in team_a:
            team_a.remove(player)
        elif player in team_b:
            team_b.remove(player)
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print(f'Game was terminated')
