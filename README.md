# Nethergames.py
<h2> How to Install: </h2> <h4> pip install git+https://github.com/PXD-mc/Nethergames </h4>

<h2> Examples: </h2>


You can fetch Guilds, Players and Leaderboards.

<h2> Player Attributes </h2>
name  
id  
bio  
guild  
skin  
avatar  
level  
xp  
credits  
kdr  
kdrTotal  
allKills  
allDeaths  
kills  
deaths  
wins  
losses  
wlr  
keys  
tier  
server  
seen  
discordID  
tier_color  


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
