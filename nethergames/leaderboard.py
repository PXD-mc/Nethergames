import urllib.request,json
class Leaderboard():
  def __init__(self,type:str,subtype:str=None,limit:int=100):
    self.type = type
    if (self.type).lower() == 'game':
      if subtype == None:
        raise Exception("\n\nsubtype cannot be empty when type is 'game'\nLeaderboard(type,subtype,limit)")
      request = urllib.request.Request(f"https://apiv2.nethergames.org/v1/leaderboard?type=game&column={subtype}&limit={limit}", headers={'User-Agent': 'Mozilla/91.0'})
    else:
      request = urllib.request.Request(f"https://apiv2.nethergames.org/v1/leaderboard?type={type}&limit={limit}", headers={'User-Agent': 'Mozilla/91.0'})
    response = urllib.request.urlopen(request)
    self.data = json.loads(response.read().decode('UTF-8'))
    
    self.leaderboard = self.data
    self.last = self.data[limit-1]
    self.top = self.data[0]
