# Nethergames.py
<h2> How to Install: </h2>
 
```ruby
pip install git+https://github.com/PXD-mc/Nethergames
```


<h2> Player Attributes </h2>

```json
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
```



```python

import nethergames

player = nethergames.Player('PXDmc')
print(f'Name : {player.name}')
print(f'Staff : {player.staff}')

```
result
```

Name : PXDmc
Staff : False

```

<h2> Guild Attributes </h2>
- raw <br/ >
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
