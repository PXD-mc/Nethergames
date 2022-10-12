# Nethergames.py
<h2> How to Install: </h2> <h4> pip install git+https://github.com/PXD-mc/Nethergames </h4>

<h2> Examples: </h2>


You can fetch Guilds, Players and Leaderboards.

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
