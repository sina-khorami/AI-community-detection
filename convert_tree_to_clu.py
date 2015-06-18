
tree = open("facebook.tree", "r")
clu  = open("facebook.clu",  "w")

clu.write("*Vertices 4039\n")

line = tree.readline()

while line:
	x = line.split()
	clu.write(x[1] + "\n")
	line = tree.readline()

clu.close()
tree.close()