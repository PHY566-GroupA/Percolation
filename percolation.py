from  pylab import *
from matplotlib import pyplot
import random
from scipy.optimize import curve_fit


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

def fit_func(x, a, b):
    return a*x + b

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
pc=[]
s=50
N_inverse=[]
for e in N:
	g=1.0/float(e)
	N_inverse.append(g)
for i in N:
    if (i==5):
        pc_5_dummy1=0
        pc_5_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_5=0.0
            b_5=len(xcluster)
            for t in range(b_5):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_5=a_5+1
            pc_5=a_5/25.0
            print pc_5
            pc_5_dummy.append(pc_5)
        for p in pc_5_dummy:
            pc_5_dummy1=pc_5_dummy1+p
        pc_5_dummy2=pc_5_dummy1/50
        print pc_5_dummy2
        pc.append(pc_5_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 5 X 5 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,5)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,5)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=95)
        pyplot.savefig('5x5grid.png')
        pyplot.show()
        
    if (i==10):
        pc_10_dummy1=0
        pc_10_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_10=0.0
            b_10=len(xcluster)
            for t in range(b_10):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_10=a_10+1
            pc_10=a_10/100.0
            print pc_10
            pc_10_dummy.append(pc_10)
        for p in pc_10_dummy:
            pc_10_dummy1=pc_10_dummy1+p
        pc_10_dummy2=pc_10_dummy1/50
        print pc_10_dummy2
        pc.append(pc_10_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 10 X 10 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,10)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,10)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=50)
        pyplot.savefig('10x10grid.png')
        pyplot.show()

    if (i==15):
        pc_15_dummy1=0
        pc_15_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_15=0.0
            b_15=len(xcluster)
            for t in range(b_15):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_15=a_15+1
            pc_15=a_15/225.0
            print pc_15
            pc_15_dummy.append(pc_15)
        for p in pc_15_dummy:
            pc_15_dummy1=pc_15_dummy1+p
        pc_15_dummy2=pc_15_dummy1/50
        print pc_15_dummy2
        pc.append(pc_15_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 15 X 15 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,15)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,15)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=35)
        pyplot.savefig('15x15grid.png')
        pyplot.show()

    if (i==20):
        pc_20_dummy1=0
        pc_20_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_20=0.0
            b_20=len(xcluster)
            for t in range(b_20):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_20=a_20+1
            pc_20=a_20/400.0
            print pc_20
            pc_20_dummy.append(pc_20)
        for p in pc_20_dummy:
            pc_20_dummy1=pc_20_dummy1+p
        pc_20_dummy2=pc_20_dummy1/50
        print pc_20_dummy2
        pc.append(pc_20_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 20 X 20 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,20)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,20)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=25)
        pyplot.savefig('20x20grid.png')
        pyplot.show()

    if (i==30):
        pc_30_dummy1=0
        pc_30_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_30=0.0
            b_30=len(xcluster)
            for t in range(b_30):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_30=a_30+1
            pc_30=a_30/900.0
            print pc_30
            pc_30_dummy.append(pc_30)
        for p in pc_30_dummy:
            pc_30_dummy1=pc_30_dummy1+p
        pc_30_dummy2=pc_30_dummy1/50
        print pc_30_dummy2
        pc.append(pc_30_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 30 X 30 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,30)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,30)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=20)
        pyplot.savefig('30x30grid.png')
        pyplot.show()

    if (i==50):
        pc_50_dummy1=0
        pc_50_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_50=0.0
            b_50=len(xcluster)
            for t in range(b_50):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_50=a_50+1
            pc_50=a_50/2500.0
            print pc_50
            pc_50_dummy.append(pc_50)
        for p in pc_50_dummy:
            pc_50_dummy1=pc_50_dummy1+p
        pc_50_dummy2=pc_50_dummy1/50
        print pc_50_dummy2
        pc.append(pc_50_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 50 X 50 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,50)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,50)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=10)
        pyplot.savefig('50x50grid.png')
        pyplot.show()

    if (i==80):
        pc_80_dummy1=0
        pc_80_dummy=[]
        for j in range(s):
            num,nc,xcluster,ycluster,grid = main(i)
            a_80=0.0
            b_80=len(xcluster)
            for t in range(b_80):
                if xcluster[t]!=[]:
                    l=len(xcluster[t])
                    for k in range(l):
                        a_80=a_80+1
            pc_80=a_80/6400.0
            print pc_80
            pc_80_dummy.append(pc_80)
        for p in pc_80_dummy:
            pc_80_dummy1=pc_80_dummy1+p
        pc_80_dummy2=pc_80_dummy1/50
        print pc_80_dummy2
        pc.append(pc_80_dummy2)

        pyplot.figure(figsize=(10,10))
        pyplot.title('Percolation transition for a 80 X 80 grid')
        pyplot.xlabel('x coordinate -->')
        pyplot.xlim(-1,80)
        pyplot.ylabel('y coordinate -->')
        pyplot.ylim(-1,80)
        pyplot.plot(xcluster[num],ycluster[num],'bo',markersize=7)
        pyplot.savefig('80x80grid.png')
        pyplot.show()

print pc
print N_inverse

x=np.array(N_inverse)
y=np.array(pc)
params = curve_fit(fit_func,x,y)
[a, b] = params[0]
print a,b

pyplot.ylim(0,1)
pyplot.plot(N_inverse,pc)
pyplot.savefig('pcvsN.png')
pyplot.show()


