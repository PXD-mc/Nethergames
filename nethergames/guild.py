import urllib.request, json

class Guild():
  def __init__(self,guild:str):
    self.guild = str(guild)
    request = urllib.request.Request(f"https://apiv2.nethergames.org/v1/guilds/{str(guild).replace(' ','%20')}", headers={'User-Agent': 'Mozilla/91.0'})  
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode('UTF-8'))

    self.raw = data

    ##
    self.name = data['name']
    self.max = data['maxSize']
    self.id = data['id']
    self.member_count = data['memberCount']
    self.motd = data['motd']
    self.position = data['position']
    self.tag = data['tag']
    self.xp = data['xp']
    self.level = data['level']
    self.leader = data['leader']
    self.tagColour = self.tagColor = data['tagColor']
    self.xp_till_next_level = data['xpToNextLevel']

    self.slots = self.max-self.member_count
    
    self.is_full = self.full = False
    if self.max <= self.member_count:
      self.is_full = self.full = True

    self.members = data['members']
    self.officers = data['officers']
