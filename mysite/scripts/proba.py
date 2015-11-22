"""print ("hello django girls")
if 1==2:
	print ("ez mindig igaz")
else: 
	print ("ez nem mindig igaz")

a = 7
if a % 2 ==0:
	print ("ez a szam paros %s" % a)
else:
	print ("ez a szam paratlan %s" %a) 

def nev (text, text2=""):
	print ("nemeth livia %s %s" %(text, text2))
nev("szoveg")

girls = ["Laila", "Anna", "Livia", "Viki"]
for girl in [girls[1]]:
	if girl == "Anna":
		return ("ez a nev helyes")
	else: 
		print ("ez a nev helytelen")"""


def nev (text=''):
	return ("nemeth livia")
a = nev ("szoveg")
print (a)
print (nev())