import pdb
import csv

fin = open('formatted_data.csv','r')
fout = open('weka2-chess.csv','w')
csvwrite = csv.writer(fout, delimiter=',', quotechar="'",quoting=csv.QUOTE_MINIMAL)

max_length = 0
for l in fin:
	length = 0
	for p in l.strip().split(',')[4:]:
		length += 1
	if length > max_length:
		max_length = length
	
csvwrite.writerow([a for a in xrange(1,max_length+1)]+['"y"'])
fin.close()
fin = open('formatted_data.csv','r')

for l in fin:
	#nl = [int(a) for a in l.strip().split(',')[4:]]
	# if we see an NA, lets just say it was the same score as previously happened
	# no game state changed over the course of these moves.
	last_seen = 0
	plays = []
	for x in l.strip().split(',')[4:]:
		try:
			plays.append(int(x))
			last_seen = int(x)
		except:
			plays.append(last_seen)
	
	t_len = len(plays)
	r_len = max_length - t_len
	
	plays += ['']*r_len

	t_label = l.split(',')[1].split('-')[0]
	label = ""
	if t_label == "1/2":
		label = '.5'
	elif t_label == "1":
		label = '1'
	else:
		label = '0'
	#print plays+[label]
	csvwrite.writerow(plays+['"'+str(label)+'"'])
