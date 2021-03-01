import requests
import json

class Schedule():
  def __init__(self):
    r = requests.get("https://statsapi.web.nhl.com/api/v1/schedule").json()
    self.totalGames = r["totalGames"]
    self.games = r["dates"][0]["games"]
    self.date = r["dates"][0]["date"]
    self.gamepks = self.set_gamepks()

  def set_gamepks(self):
    gamepks = []
    for g in self.games:
      gamepks.append(g["gamePk"])
    return gamepks