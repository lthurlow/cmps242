import csv
import pprint
import pdb
import collections

import ml_functions

class data:
  def __init__(self, eve, res, welo, belo, plays):
    self.event = int(eve)
    self.white = .5 if res.split('-')[0] == "1/2" else int(res.split('-')[0])
    self.black = .5 if res.split('-')[1] == "1/2" else int(res.split('-')[1])
    self.whelo = int(welo)
    self.blelo = int(belo)
    self.plays = [int(x) if x != "NA" else "NA" for x in plays]
  def __repr__(self):
    s = ','.join([str(self.event), str(self.white), str(self.black),\
                  str(self.whelo), str(self.blelo)]+\
                  [str(x) for x in self.plays])
    return s

csvfile = open('formatted_data.csv', 'rb')
data_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

data_set = collections.OrderedDict()

for row in data_reader:
  d = data(row[0], row[1], row[2], row[3], row[4:])
  data_set[int(row[0])] = d

sep = "-"*80
print sep
percent = ml_functions.white_wins(data_set)
print "White Always Wins: %s" % percent
percent = ml_functions.black_wins(data_set)
print "Black Always Wins: %s" % percent
percent = ml_functions.base_elo(data_set)
print sep
print "Using Elo: %s" % percent
percent = ml_functions.plus_ties_elo(data_set, 25)
print "Use Elo + Ties (25): %s" % percent
percent = ml_functions.plus_ties_elo(data_set, 50)
print "Use Elo + Ties (50): %s" % percent
percent = ml_functions.plus_ties_elo(data_set, 75)
print "Use Elo + Ties (75): %s" % percent
percent = ml_functions.plus_ties_elo(data_set, 100)
print "Use Elo + Ties (100): %s" % percent
percent = ml_functions.plus_ties_elo(data_set, 150)
print "Use Elo + Ties (150): %s" % percent
print sep
