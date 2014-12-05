import ml_functions


sep = "-"*80

def m_call_fun(fun,ds,val1=[],val2=[]):
  print sep
  if fun == "plus_ties_elo":
    for x in val1:
      percent = ml_functions.plus_ties_elo(ds,x)
      print "Use Elo + Ties (%s): %s" % (x,percent)
  elif fun == "pred_last":
    for x in val1:
      percent = ml_functions.pred_last(ds, x)
      print "Predition based on Score (%s): %s" % (x,percent)
  elif fun == "average_moves":
    for x in val1:
      percent = ml_functions.average_moves(ds,x)
      print "Prediction on Averages (%s): %s" % (x,percent)
  elif fun == "prune_moves":
    for x in val1:
      for y in val2:
        percent = ml_functions.prune_moves(ds,x,y)
        print "Predition based on Move number (%s,%s): %s" % (x,y,percent)
        
  print sep
