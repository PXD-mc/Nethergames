# Nethergames.py
<h2> How to Install: </h2> 
`pip install git+https://github.com/PXD-mc/Nethergames`


<h2> Player Attributes </h2>
- name  <br />
- id  <br />
- bio  <br />
- guild  <br />
- skin  <br />
- avatar  <br />
- level  <br />
- xp  <br />
- credits  <br />
- kdr  <br />
- kdrTotal  <br />
- allKills  <br />
- allDeaths  <br />
- kills  <br />
- deaths  <br />
- wins  <br />
- losses  <br />
- wlr  <br />
- keys  <br />
- tier  <br />
- server  <br />
- seen  <br />
- discordID  <br />
- tier_color  <br />
- ranks <br />
- zones <br />
- levelColors <br />
- rankColors <br />
- winsData <br />
- extra <br />
- extraNested <br />
- firstJoined <br />
- firstJoinedDate <br />
- lastJoined <br />
- lastJoinedDate <br />
- quit <br />
- lastRankTime <br />
- banned_until <br />
- staff <br />
- titan <br />
- muted <br />
- banned <br />
- skin_is_public <br />
- hasRank <br />
- hasTier <br />
- online <br />
- status <br />
- voteStatus <br />
- voted <br />


```python

import nethergames

player = nethergames.Player('PXDmc')
print(f'Name : {player.name}')
print(f'Level : {player.level}')

```
result
```

Name : PXDmc
Level : 351

```
