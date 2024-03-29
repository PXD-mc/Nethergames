import json,urllib.request
class Player():
  def __init__(self,player:str):
    self.player = str(player)
    request = urllib.request.Request(f"https://apiv2.nethergames.org/v1/players/{str(player).replace(' ','%20')}", headers={'User-Agent': 'Mozilla/91.0'})  
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode('UTF-8'))

    self.raw = data

    ##
    self.name = data['name']
    self.flags = data['flags']
    self.id = data['xuid']
    self.bio = data['bio']
    self.guild = data['guild']
    self.skin = data['skin']
    self.avatar = data['avatar']
    self.level = data['level']
    self.xp = data['xp']
    self.credits = data['credits']
    self.kdr = data['kdr']
    self.kdrTotal = data['kdrTotal']
    self.allKills = data['killsTotal']
    self.allDeaths = data['deathsTotal']
    self.kills = data['kills']
    self.deaths = data['deaths']
    self.wins = data['wins']
    self.losses = data['losses']
    self.wlr = data['wlr']
    self.keys = data['crateKeys']
    self.tier = data['tier']
    self.server = data['lastServer']
    self.seen = data['lastSeen']
    self.discord_id = self.discordId = self.discordID = data['discordId']
    self.tier_color = self.tier_colour = self.tierColor = self.tierColour = data['tierColor']
    
    self.bedwarsWins = data['winsData']['BW']
    self.skywarsWins = data['winsData']['SW']
    self.bridgeWins = data['winsData']['TB']
    self.duelsWins = data['winsData']['Duels']
    self.survivalgamesWins = data['winsData']['SG']
    self.murdermysteryWins = data['winsData']['MM']
    self.mommasaysWins = data['winsData']['MS']
    # self.tntrunWins = data['winsData']['TR']
    self.uhcWins = data['winsData']['UHC']
    self.conquestWins = data['winsData']['CQ']
    self.soccerWins = data['winsData']['SC']
    # self.blockhuntWins = data['winsData']['BH']

    #lists
    self.ranks = data['ranks']
    if self.ranks == []:
      self.ranks = None

    self.zones = data['discoveredZones']
    if self.zones == []:
      self.zones = None

    self.levelColors = self.levelColours = self.level_colours = self.level_colors = data['levelColors']
    if self.levelColors == []:
      self.levelColors = self.levelColours = self.level_colours = self.level_colors = None
    self.rankColours = self.rankColors = self.rank_colours = self.rank_colors = data['rankColors']
    if self.rankColors == []:
      self.rankColours = self.rankColors = self.rank_colours = self.rank_colors = None
    
    #dict
    self.winsData = {i: n for i, n in sorted(data['winsData'].items(), key=lambda game: game[1],reverse=True)}

    self.extra = data['extra']
    self.extraNested = data['extraNested']

    #times
    self.firstJoined = data['firstJoined']
    self.firstJoinedDate = data['firstJoin']
    self.lastJoined = data['lastJoined']
    self.lastJoinedDate = data['lastJoin']
    self.quit = data['lastQuit']
    self.lastRankTime = data['lastRankTimestamp']
    self.banned_until = data['bannedUntil']
    

    #boolens
    self.staff = data['staff']
    self.titan = data['titan']
    self.muted = data['muted']
    self.banned = data['banned']
    self.skin_is_public = data['skinVisibility']
    self.hasRank = False
    if self.ranks != None:
      self.hasRank = True
    self.hasTier = False
    if self.tier != None:
      self.hasTier = True
    
    self.online = data['online']
    if self.online == False:
      self.status = 'offline'
    else:
      self.status = 'online'

    self.voteStatus = data['voteStatus']
    if self.voteStatus == 0:
      self.voted = False
    else:
      self.voted = True
