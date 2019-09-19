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

totalYards = 0
for p in playersWeek2.receiving().sort('receiving_rec'):
    if (p.receiving_rec > 0) & (p.team == "DET"):
        totalYards += p.receiving_yds
        msg = '%s %d Targets, %d YAC on %d receptions, %d yards, %d TDs'
        print(msg % (p, p.receiving_tar, p.receiving_yac_yds, p.receiving_rec, p.receiving_yds, p.receiving_tds))
        
print("Total Yards: %d"  % totalYards)

# for p in playersAllWeeks.sort('rushing_att'):
#     if (p.rushing_att > 0):
#         if (p.rushing_yds / p.rushing_att > 6) & (p.rushing_att > 3):
#             msg = '%s %d carries for %d yards and %d TDs, YPC: %f'
#             print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds, float(p.rushing_yds) / float(p.rushing_att)))

# for p in playersAllWeeks.receiving().sort('receiving_yac_yds'):
#     if p.receiving_rec > 0:
#         if p.receiving_yac_yds / p.receiving_rec > 10:
#             msg = '%s %d YAC on %d receptions'
#             print(msg % (p, p.receiving_yac_yds, p.receiving_rec))

# for p in playersAllWeeks.receiving().sort('receiving_tar'):
#     if p.receiving_tar > 10:
#         if p.receiving_rec / p.receiving_tar > .7:
#             msg = '%s %d targets for %d receptions, %d yards, and %d TDs'
#             print(msg % (p, p.receiving_tar, p.receiving_rec, p.receiving_yds, p.receiving_tds))

# for p in playersAllWeeks.sort('rushing_att').limit(20):
#     msg = '%s %d carries for %d yards and %d TDs'
#     print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))