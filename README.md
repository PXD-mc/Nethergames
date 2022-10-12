# Nethergames.py
<h2> How to Install: </h2> <h4> pip install git+https://github.com/PXD-mc/Nethergames </h4>

<h2> Examples: </h2>


You can fetch Guilds, Players and Leaderboards.

<h2> Player Attributes </h2>
name   \n
id\n
bio\n
guild\n
skin\n
avatar\n
level\n
xp  \n
credits\n
kdr   \n
kdrTotal\n
allKills\n
allDeaths\n
kills   \n
deaths\n
wins\n
losses\n
wlr\n
keys\n
tier\n
server\n
seen\n
discordID\n
tier_color\n


```python

import nethergames

player = nethergames.Player('PXDmc')
print(f'Name : {player.name}')
print(f'Level : {player.level}')

```
result
```

Name: PXDmc
Level: 351

```
