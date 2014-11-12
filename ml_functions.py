def base_elo(ds):
  correct = 0
  total = float(len(ds))
  for x in ds:
    if ds[x].whelo > ds[x].blelo:
      if ds[x].white == 1:
        correct += 1
  return correct/total

def white_wins(ds):
  correct = 0
  total = float(len(ds))
  for x in ds:
    if ds[x].white == 1:
      correct += 1
  return correct/total     
  
def black_wins(ds):
  correct = 0
  total = float(len(ds))
  for x in ds:
    if ds[x].black == 1:
      correct += 1
  return correct/total     
  
def plus_ties_elo(ds,factor):
  correct = 0
  total = float(len(ds))
  for x in ds:
    if ds[x].whelo - ds[x].blelo <= factor:
      if ds[x].white == .5:
        correct += 1
    elif ds[x].whelo > ds[x].blelo+factor:
      if ds[x].white == 1:
        correct += 1
  return correct/total

