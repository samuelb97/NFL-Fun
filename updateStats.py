import nflgame
import pickle

games = nflgame.games(2019)
players = nflgame.combine(games, plays = True)

with open('2019Full.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(players, f)

games = nflgame.games(2019, week=1)
players = nflgame.combine(games, plays = True)

with open('2019Week1.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(players, f)

games = nflgame.games(2019, week=2)
players = nflgame.combine(games, plays = True)

with open('2019Week2.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(players, f)


