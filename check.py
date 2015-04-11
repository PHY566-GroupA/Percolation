
def check(xcluster,ycluster,n):
	'''
	check the existence of spanning cluster 
	'''
	ans = 1
	num = 0
	for i in range(len(xcluster)):
		if (len(xcluster[i])!=0):
			if(min(xcluster[i])==0 and max(xcluster[i])==n-1):
				if(min(ycluster[i])==0 and max(ycluster[i])==n-1):
					num = i
					ans = 0
					break
	return ans, num, len(xcluster[num])

