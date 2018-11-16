relation1 = input("What is the first family relation: ")
relation2 = input("What is the second family relation:")
crelation = ""

#relation1.lower() creates a lower case version. This means
#you don't have to check Dad, dad, DaD etc
if relation1.lower() == "dad":
	print("relation 1 is baba")
	crelation = "baba"
#Program asks what relation 1 is and a possibility
#of Dad
#the relation of dad is baba
if relation2.lower() == "mom":
	print("relation 2 is mama")
	crelation = "nainai"


crelation == "nainai"
#Program asks what relation 2 is and a possibility
#of mom
#the relation of mom is mama


if relation1.lower() == "dad" and relation2.lower() == "mom":
	print (crelation)