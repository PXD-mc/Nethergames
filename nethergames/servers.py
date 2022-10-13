import json,urllib.request
class Servers():
  def __init__(self):
    request = urllib.request.Request(f"https://apiv2.nethergames.org/v1/servers", headers={'User-Agent': 'Mozilla/91.0'})  
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode('UTF-8'))

    self.raw = data
    
    self.lobby = data['lobby']
    self.lobbyMax = data['lobby']['max']
    self.lobbyCount = data['lobby']['count']
    
    self.bedwars = data['bw']
    self.bedwarsMax = data['bw']['max']
    self.bedwarsCount = data['bw']['count']
    
    self.conquest = data['cq']
    self.conquestMax = data['cq']['max']
    self.conquestCount = data['cq']['count']
    
    self.creative = data['creative']
    self.creativeMax = data['creative']['max']
    self.creativeCount = data['creative']['count']
    
    self.factions = data['factions']
    self.factionsMax = data['factions']['max']
    self.factionsCount = data['factions']['count']
    
    self.murdermystery = data['mm']
    self.murdermysteryMax = data['mm']['max']
    self.murdermysteryCount = data['mm']['count']
    
    self.mommasays = data['ms']
    self.mommasaysMax = data['cq']['ms']
    self.mommasaysCount = data['cq']['ms']
    
    self.replay = data['replay']
    self.replayMax = data['replay']['max']
    self.replayCount = data['replay']['count']
    
    self.survivalgames = data['sg']
    self.survivalgamesMax = data['sg']['max']
    self.survivalgamesCount = data['sg']['count']
    
    self.setup = data['setup']
    self.setupMax = data['setup']['max']
    self.setupCount = data['setup']['count']
    
    self.soccer = data['sc']
    self.soccerMax = data['sc']['max']
    self.soccerCount = data['sc']['count']
    
    self.uhc = data['uhc']
    self.uhcMax = data['uhc']['max']
    self.uhcCount = data['uhc']['count']
    
    self.skyblock = data['sb']
    self.skyblockMax = data['sb']['max']
    self.skyblockCount = data['sb']['count']
    
    self.bridge = data['tb']
    self.bridgeMax = data['tb']['max']
    self.bridgeCount = data['tb']['count']

    self.duels = data['duels']
    self.duelsMax = data['duels']['max']
    self.duelsCount = data['duels']['count']
    
    self.skywars = data['sw']
    self.skywarsMax = data['sw']['max']
    self.skywarsCount = data['sw']['count']

    self.total = 0
    self.max = 0
    for i in data:
      self.total += data[i]['count']
      self.max += data[i]['max']
