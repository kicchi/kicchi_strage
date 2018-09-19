# coding: UTF-8

size_num = 3

for i in range(1,size_num+1):
	filename = "Inari"
	filename = filename + str(i).zfill(8) + ".txt"
	#print(filename)
	f = open(filename,'r')
	data1 = f.read()
	f.close()
	
	lines1 = data1.split('\n')
	lines2 = []
	for line in lines1:
		tmp = ""
		if line[:1] == '1':
			tmp = "0" + line[1:]
			lines2.append(tmp)
		else:
			lines2.append(line)

	f = open(filename,'w')
	idx = 0
	for line in lines2:
		f.write(line)
		idx += 1
		if idx != len(lines2):
			f.write("\n")


	f.close()
	
