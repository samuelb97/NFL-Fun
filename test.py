import nflgame
import pickle

playersWeek1 = None
playersWeek2 = None
playersAllWeeks = None

with open('2019Full.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    playersAllWeeks = pickle.load(f)

with open('2019Week1.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    playersWeek1 = pickle.load(f)

with open('2019Week2.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    playersWeek2 = pickle.load(f)



def RecievingByTeam(players, team):
    playerList = []
    totalYards = 0
    for p in players.receiving().sort('receiving_rec'):
        if (p.receiving_rec > 0) & (p.team == team):
            totalYards += p.receiving_yds
            msg = '%s %d Targets, %d YAC on %d receptions, %d yards, %d TDs'
            playerList.append(p)
            print(msg % (p, p.receiving_tar, p.receiving_yac_yds, p.receiving_rec, p.receiving_yds, p.receiving_tds))
            
    print("Total Yards: %d"  % totalYards)
    return playerList

def minYPC_minRushAttempts(ypc, rushAttempts):
    playerList =[]
    for p in playersAllWeeks.sort('rushing_att'):
        if (p.rushing_att > 0):
            if (p.rushing_yds / p.rushing_att >= ypc) & (p.rushing_att >= rushAttempts):
                msg = '%s %d carries for %d yards and %d TDs, YPC: %f'
                playerList.append(p)
                print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds, float(p.rushing_yds) / float(p.rushing_att)))

    return playerList

def YpcPerReceptionOver(x):
    playerList = []
    for p in playersAllWeeks.receiving().sort('receiving_yac_yds'):
        if p.receiving_rec > 0:
            if p.receiving_yac_yds / p.receiving_rec > x:
                msg = '%s %d YAC on %d receptions'
                playerList.append(p)
                print(msg % (p, p.receiving_yac_yds, p.receiving_rec))

    return playerList

def TargetCatchPercentOver(percent):
    playerList = []
    for p in playersAllWeeks.receiving().sort('receiving_tar'):
        if p.receiving_tar > 10:
            if p.receiving_rec / p.receiving_tar > percent:
                msg = '%s %d targets for %d receptions, %d yards, and %d TDs'
                playerList.append(p)
                print(msg % (p, p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_tds))
        
    return playerList

def RushingAttemptLeaders():
    playerList = []
    for p in playersAllWeeks.sort('rushing_att').limit(20):
        msg = '%s %d carries for %d yards and %d TDs'
        playerList.append(p)
        print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))

    return playerList