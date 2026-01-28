players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

player_list = []
for k, v in players.items():
    item_list = []
    item_list.extend(k)
    item_list.extend(v)
    player_list.append(tuple(item_list))
print(player_list)
