from  pylab import *
import matplotlib as mpl
import random
import time 


def initialize(n):
	'''
	initialize n*n grids and the vacant position 
	'''
	grid = zeros((n,n))
	vacancy = []
	for i in range(n):
		for j in range(n):
			vacancy.append([i,j])
	return grid, vacancy 

def selection(vacancy,grid):	
	'''
	randomly choose a vacant site to put paticle.
	'''
	choice = random.choice(vacancy)
	p0=int(choice[0])
	p1=int(choice[1])
	vacancy.remove([p0,p1])
	return choice 

def gainxy(x,y,xcluster,ycluster):
	'''
	subtract x y from the random choice,and add it to the list
	'''
	xcluster=xcluster+([x],)
	ycluster=ycluster+([y],)

	return xcluster, ycluster


def listcomb(num1, num2, xcluster,ycluster):
	'''
	add the elements in cluster#num2 to cluster#num1 when num1<num2
	'''		
	l = len(xcluster[num2])
	for i in range(l):
		xcluster[num1].append(xcluster[num2][l-1-i])
		ycluster[num1].append(ycluster[num2][l-1-i])
		xcluster[num2].pop()
		ycluster[num2].pop()	
	return

def renumgrid(num1,num2,xcluster,ycluster,grid):
	'''
	renumber the number elements in grid when cluster2 join to
	'''
	l = len(xcluster[num2]) 
	for i in range(l):
		x=int(xcluster[num2][i])
		y=int(ycluster[num2][i])
		grid[x][y]=num1
	return

def percolation(num1,num2,xcluster,ycluster,grid):
	if (num1<num2):
		renumgrid(num1,num2,xcluster,ycluster,grid)
		listcomb(num1, num2, xcluster, ycluster)
	if (num1>num2):
		renumgrid(num2,num1,xcluster,ycluster,grid)
		listcomb(num2, num1, xcluster, ycluster)
	return

def check(xcluster,ycluster,n):
	'''
	check the existence of spanning cluster 
	'''
	ans = 1
	num = 0
	for i in range(len(xcluster)):
		if (len(xcluster[i])!=0):
			if(min(xcluster[i])==0 and max(xcluster[i])==n-1):	
				num  = i
				ans = 0		
				break			
			if(min(ycluster[i])==0 and max(ycluster[i])==n-1):
				num = i
				ans = 0
				break
	return ans, num, len(xcluster[num])



def main(n):
	grid,vacancy = initialize(n)
	ans = 1
	clnum = 1
	xcluster = ([],)
	ycluster = ([],)
	while(ans==1):	
		p = selection(vacancy, grid)
		x = int(p[0])
		y = int(p[1])
		grid[x][y] = clnum
		xcluster,ycluster=gainxy(x,y,xcluster,ycluster)
			
		if (x!=0):
			if (grid[x-1][y]):
				num1 = int(grid[x-1][y])
				num2 = int(grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		if (y!=0):
			if (grid[x][y-1]):
				num1 = int(grid[x][y-1])
				num2 = int(grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		if (x!=n-1):
			if (grid[x+1][y]):
				num1 = int(grid[x+1][y])
				num2 = int(grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		if (y!=n-1):
			if (grid[x][y+1]):
				num1 = int(grid[x][y+1])
				num2 = int(grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)

		if (x==0):
			if (grid[x+1][y]):
				num1 =int( grid[x+1][y])
				num2 =int( grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		if (y==0):
			if (grid[x][y+1]):
				num1 =int( grid[x][y+1])
				num2 =int( grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		if (x==n-1):
			if (grid[x-1][y]):
				num1 = int(grid[x-1][y])
				num2 = int(grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		if (y==n-1):
			if (grid[x][y-1]):
				num1 = int(grid[x][y-1])
				num2 = int(grid[x][y])
				percolation(num1,num2,xcluster,ycluster,grid)
		print xcluster
		ans,num,nc = check(xcluster, ycluster,n)
		clnum=clnum+1	  
	return num, nc, xcluster, ycluster, grid




num,nc,xcluster,ycluster,grid = main(5)
figure(figsize=(10,10))
xlim(-0.5,9.5)
ylim(-0.5,9.5)
plot(xcluster[num],ycluster[num],'bo',markersize=50)




