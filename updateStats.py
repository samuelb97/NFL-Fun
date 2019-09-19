import nflgame
import pickle

games = nflgame.games(2019)
players = nflgame.combine(games, plays = True)

with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(players, f)