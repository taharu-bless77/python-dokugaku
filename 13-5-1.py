sports = ['cricket', 'lacrosse', 'hockey', 'water_polo', 'kabaddi', 'tug_of_war']
n_players = [11,10,11,7,7,8]
sp_players = {sport:n_players[i] for i,sport in enumerate(sports)}
print(sp_players)

