''' randomized contraction algorithim to find the mincut of a 
undiricted graph'''
'''effeciency boost to be implemented later'''


#main part
inf=99999#arbitary infinity value
ar=[][]#adjency matrix
ls=[]#list of available pair of vertices
for i in range(len(ar)):
	for j in range(i,len(ar[0])):
		if(ar[i][j]!=inf):
			t=tuple([i,j])
			ls.append(t)



