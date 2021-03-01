from flask import Response
from flask_restful import Resource
import json
from .schedule import Schedule
from .game import Game, GameEncoder

class PenaltyApi(Resource):
  def get(self):
    schedule = Schedule()
    responsejson = {"games" : []}

    for pk in schedule.gamepks:
      game = Game(pk)
      game.predict_next_penalty()
      gamejson = json.loads(json.dumps(game, cls=GameEncoder, indent=2))
      responsejson["games"].append(gamejson)

    return responsejson