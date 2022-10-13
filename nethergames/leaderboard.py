class Leaderboard():
  def __init__(self,type):
    self.type = type
    request = urllib.request.Request(f"https://apiv2.nethergames.org/v1/leaderboard?type={type}", headers={'User-Agent': 'Mozilla/91.0'})  
    response = urllib.request.urlopen(request)
    self.data = json.loads(response.read().decode('UTF-8'))
    
    self.raw = self.data
    
    self.total = 0
    self.all = []
    for i in self.data:
      self.total+=1
      self.all.append({'name': list(i.values())[1], 'amount': list(i.values())[2],'id': list(i.values())[0]})
      self.players = [list(i.values())[0] for i in self.all]
  def leaderboard(self):
    return self.data
  def get_player_names(self):
    return [i['name'] for i in self.players]
  def get_player_amounts(self):
    return [i['amount'] for i in self.players]
  def get_player_ids(self):
    return [i['id'] for i in self.players]
