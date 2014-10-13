import re

def analysis(text_file, csv_file):
	matches = []
	fi = open(text_file,'r')	
	a = fi.read()
	m = re.findall(r"[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+",a)
	cs = open(csv_file, 'r')
	v = cs.read()
	c = v.split('\n')
	for y in c:
		#print y
		for x in m:
			if y in x:
				if x not in matches:
					matches.append(x)
					#matches.append('test')
	print matches
    
	
if __name__ == "__main__":
	tex_file = 'something.txt'
	#raw_input("What is the file you want to read?:")
	cs_file = 'top1001names.csv'
	#raw_input("Which list of words?:")
	analysis(tex_file,cs_file)
