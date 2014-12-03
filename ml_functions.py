#!/usr/bin/python
import pdb
import math
import numpy as np

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

def pred_last(ds,factor):
  correct = 0
  total = float(len(ds))
  for x in ds:
    if ds[x].plays:
      rem_last = 0
      for y in ds[x].plays:
        if type(y) == int:
          rem_last = y
      ## predict tie
      if abs(rem_last) < factor:
        if ds[x].white == .5:
          correct += 1
      else:
        if rem_last > 0:
          if ds[x].white == 1:
            correct += 1
        else:
          if ds[x].white == 0:
            correct += 1
  return correct/total

def prune_moves(ds, num, factor=0):
  correct = 0
  total = float(len(ds))
  new_ds = {}
  for x in ds:
    new_ds[x] = []
    if ds[x].plays:
      rem_last = 0
      for y in ds[x].plays:
        if type(y) == int:
          rem_last = y
          new_ds[x].append(y)
        else:
          new_ds[x].append(rem_last)

  for x in ds:
    if abs(num) > (len(ds[x].plays)-1):
      total -= 1
    else:
      num_val = new_ds[x][num]
      try:
        if abs(num_val) < factor:
          if ds[x].white == .5:
            correct += 1
        else:
          if num_val >= 0 and ds[x].white == 1:
            correct += 1
          elif num_val < 0 and ds[x].white == 0:
            correct += 1
      except:
        print num_val
        pdb.set_trace()
    
      ## predict tie
      #if abs(rem_last) < factor:
      #  if ds[x].white == .5:
      #    correct += 1
      #else:
      #  if rem_last > 0:
      #    if ds[x].white == 1:
      #      correct += 1
      #  else:
      #    if ds[x].white == 0:
      #      correct += 1
  return correct/total

 


def dot_product(m1,m2):
  return np.dot(m1,m2)
def negate_vec(b,m1):
  return [b*i for i in m1]
def sum_vec(m1,m2):
  return np.add(m1,m2)

def perceptron(ds):

  vec_length = len(ds)

  largest_sub_array = 0
  for i in ds:
    len_x = len(ds[i].get_plays())
    if len_x > largest_sub_array:
      largest_sub_array = len_x
  
  weight_vector = np.array([0 for i in range(0,largest_sub_array)])
  temp_vector = np.array([])

  epoch = 0
  errors = 0
  temp_errors = 0

  while not np.array_equal(weight_vector,temp_vector):#\
    ##and epoch < 2: ## part (d
    temp_vector = weight_vector
    for line in ds:
      vector = []
      ## try just doing win/lose first - then add ties
      if ds[line].get_winner() != 0.5:
        label = -1 if ds[line].get_winner() == 0 else 1
        for a in ds[line].get_plays():
          if a == 'NA':
            vector.append(0)
          else:
            if int(a) >= 0:
              vector.append(1)
            else:
              vector.append(-1)

      if vector:
        #print "Train Vector:", vector
        #print "Weight Vector:", weight_vector
        ## here we will only use as much of the weight vector as needed.
        pred = dot_product(vector,weight_vector[:len(vector)])

        #print "Prediction:", pred
        #print "Label:",label
        if (label*pred) <= 0:
          neg_vector = negate_vec(label,vector)
          #temp = sum_vec(weight_vector[:len(vector)],neg_vector)
          other_temp = []
          for a in xrange(0,len(weight_vector)):
            if a >= len(neg_vector)-1:
              other_temp.append(weight_vector[a])
            else:
              other_temp.append(weight_vector[a]+neg_vector[a])
          weight_vector = other_temp
          print label, vector
              
          errors += 1
          #print "Updated weight: ", weight_vector
      
    epoch += 1
    print "Epoch: ", epoch
    print "\tErrors: ", errors-temp_errors
    temp_errors = errors

  print weight_vector
  print "Took %s Epochs" % str(epoch-1)
  print "Took %s Errors" % str(errors)
