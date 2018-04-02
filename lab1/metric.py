# calculates average precision

while True:

	print('********')
	labels = input()
	
	count = 0
	tp = 0.0
	
	for i,l in enumerate(labels):
		if l == '1':
			count += 1
			tp += count/(i+1)
		if i == 4:
			print("P@5: ", count/5)
		if i == 9:
			print("P@10: ", count/10)
	
	print("AP: ", tp/count)

