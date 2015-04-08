from  pylab import *
from matplotlib import pyplot
import random


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

# plotting the spanning cluster for different values off N. Also, simulating each value off N, 50 times.
N=[5,10,15,20,30,50,80]
for i in N:
    if (i==5):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 5 X 5 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,10)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,10)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=50)
        pyplot.show()
    if (i==10):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 10 X 10 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,15)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,15)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=35)
        pyplot.show()
    if (i==15):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 15 X 15 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,15)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,15)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=35)
        pyplot.show()
    if (i==20):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 20 X 20 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,20)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,20)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=25)
        pyplot.show()
    if (i==30):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 30 X 30 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,30)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,30)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=20)
        pyplot.show()
    if (i==50):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 50 X 50 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,50)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,50)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=10)
        pyplot.show()
    if (i==80):
        for j in range(49):
            num,nc,xcluster,ycluster,grid = main(i)
        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 80 X 80 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,80)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,80)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=7)
        pyplot.show()



