file = open("newdata2.csv", "w")
data = open("newdata.csv", "r")

cnt = 0
for line in data:
	if not cnt:
		file.write(line)
		cnt = 1
		continue
	id1 = 0
	for x in line:
		if x >= '0' and x <= '9':
			id1 *= 10
			id1 += int(x)
		else:
			break
	
	if id1 <= 105410:
		continue
	else:
		file.write(line)
	
file.close()
data.close()

 