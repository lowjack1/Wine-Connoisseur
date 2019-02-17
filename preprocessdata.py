file = open("newdata.csv", "w")
data = open("dataset.csv", "r")

for line in data:
	s = ""
	flag = 0
	for x in line:
		if(x == "\""):
			if(flag == 0):
				flag = 1
			else:
				flag = 0
		if(flag):
			if x == ",":
				s += " "
			else:
				s += x
		else:
			s += x
	file.write(s)
file.close()
data.close()

 