# Nethergames.py
<h2> NOTES </h2> 

- You can use `nethergames.Leaderboard()` but it is not fully supported <br />
- <a href="https://docs.nethergames.org/#section/Rate-Limits" target="_blank" rel="noopener noreferrer"> Click here for information on rate-limits (Nethergames API Docs) </a>

<h2> How to Install: </h2>
 
```ruby
pip install git+https://github.com/PXD-mc/Nethergames
```


<h2> Player Attributes </h2>

```ruby
- raw 
- name  
- id  
- bio  
- guild  
- skin  
- avatar  
- level  
- xp  
- credits  
- kdr  
- kdrTotal  
- allKills  
- allDeaths  
- kills  
- deaths  
- wins  
- losses  
- wlr  
- keys  
- tier  
- server  
- seen  
- discordID  
- tier_color  
- ranks 
- zones 
- levelColors 
- rankColors 
- winsData 
- extra 
- extraNested 
- firstJoined 
- firstJoinedDate 
- lastJoined 
- lastJoinedDate 
- quit 
- lastRankTime 
- banned_until 
- staff 
- titan 
- muted 
- banned 
- skin_is_public 
- hasRank 
- hasTier 
- online 
- status 
- voteStatus 
- voted 
- bedwarsWins 
- skywarsWins 
- bridgeWins 
- duelsWins 
- survivalgamesWins 
- murdermysteryWins 
- mommasaysWins 
- tntrunWins 
- uhcWins 
- conquestWins 
- soccerWins 
- blockhuntWins

```


Example
```python

import nethergames

player = nethergames.Player('PXDmc')
print(f'Name : {player.name}')
print(f'Staff : {player.staff}')
print(f'Bedwars Wins : {player.bedwarsWins}')

```
Output
```

Name : PXDmc
Staff : False
Bedwars Wins : 5868

```

<h2> Guild Attributes </h2>

```ruby
- raw 
- name     
- max     
- id     
- member_count    
- motd     
- position    
- tag     
- xp     
- level     
- leader     
- tagColour 
- xp_till_next_level 
- slots 
- is_full 
- members   
- officers  
```


Example
```python

import nethergames

guild = nethergames.Guild('TotallyRealGuild')
print(f'Name : {guild.name}')
print(f'Open slots in guild : {guild.slots}')
print(f'Guild leader : {guild.leader}')

```
Output
```

Name : TotallyRealGuild
Open slots in guild : 12
Guild leader : PXDmc

```

<h2> Server Attributes </h2>

```ruby
replace [servername] with bedwars, skyways, duels and so on.

- raw 
- [servername]
- [servername]Max
- [servername]Count
- total
- max
```

Example
```python

import nethergames

servers = nethergames.Servers()
print(f'Total players online : {servers.total}')
print(f'Players in bedwars : {servers.bedwarsCount}')

```
Output
```

Total players online : 1002
Players in bedwars : 362 

```
