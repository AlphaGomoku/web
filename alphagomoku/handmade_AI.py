def first_step(ar, num):
	arr = ar.copy()
	ans = (-1, -1)
	#it can complete 5 and win the game
	#horizontal
	for i in range(0, 15):
		for j in range(0, 11):
			if   arr[i][j]==num and arr[i][j+1]==num and arr[i][j+2]==num and arr[i][j+3]==num and arr[i][j+4]==0:
				ans = (i, j+4)
				return ans
			elif arr[i][j]==num and arr[i][j+1]==num and arr[i][j+2]==num and arr[i][j+3]==0 and arr[i][j+4]==num:
				ans = (i, j+3)
				return ans
			elif arr[i][j]==num and arr[i][j+1]==num and arr[i][j+2]==0 and arr[i][j+3]==num and arr[i][j+4]==num:
				ans = (i, j+2)
				return ans
			elif arr[i][j]==num and arr[i][j+1]==0 and arr[i][j+2]==num and arr[i][j+3]==num and arr[i][j+4]==num:
				ans = (i, j+1)
				return ans
			elif arr[i][j]==0 and arr[i][j+1]==num and arr[i][j+2]==num and arr[i][j+3]==num and arr[i][j+4]==num:
				ans = (i, j)
				return ans
	#vertical
	for i in range(0, 11):
		for j in range(0, 15):
			if   arr[i][j]==num and arr[i+1][j]==num and arr[i+2][j]==num and arr[i+3][j]==num and arr[i+4][j]==0:
				ans = (i+4, j)
				return ans
			elif arr[i][j]==num and arr[i+1][j]==num and arr[i+2][j]==num and arr[i+3][j]==0 and arr[i+4][j]==num:
				ans = (i+3, j)
				return ans
			elif arr[i][j]==num and arr[i+1][j]==num and arr[i+2][j]==0 and arr[i+3][j]==num and arr[i+4][j]==num:
				ans = (i+2, j)
				return ans
			elif arr[i][j]==num and arr[i+1][j]==0 and arr[i+2][j]==num and arr[i+3][j]==num and arr[i+4][j]==num:
				ans = (i+1, j)
				return ans
			elif arr[i][j]==0 and arr[i+1][j]==num and arr[i+2][j]==num and arr[i+3][j]==num and arr[i+4][j]==num:
				ans = (i, j)
				return ans
	#right_down
	for i in range(0, 11):
		for j in range(0, 11):
			if   arr[i][j]==num and arr[i+1][j+1]==num and arr[i+2][j+2]==num and arr[i+3][j+3]==num and arr[i+4][j+4]==0:
				ans = (i+4, j+4)
				return ans
			elif arr[i][j]==num and arr[i+1][j+1]==num and arr[i+2][j+2]==num and arr[i+3][j+3]==0 and arr[i+4][j+4]==num:
				ans = (i+3, j+3)
				return ans
			elif arr[i][j]==num and arr[i+1][j+1]==num and arr[i+2][j+2]==0 and arr[i+3][j+3]==num and arr[i+4][j+4]==num:
				ans = (i+2, j+2)
				return ans
			elif arr[i][j]==num and arr[i+1][j+1]==0 and arr[i+2][j+2]==num and arr[i+3][j+3]==num and arr[i+4][j+4]==num:
				ans = (i+1, j+1)
				return ans
			elif arr[i][j]==0 and arr[i+1][j+1]==num and arr[i+2][j+2]==num and arr[i+3][j+3]==num and arr[i+4][j+4]==num:
				ans = (i, j)
				return ans
	#left_down
	for i in range(4, 15):
		for j in range(0, 11):
			if   arr[i][j]==num and arr[i-1][j+1]==num and arr[i-2][j+2]==num and arr[i-3][j+3]==num and arr[i-4][j+4]==0:
				ans = (i-4, j+4)
				return ans
			elif arr[i][j]==num and arr[i-1][j+1]==num and arr[i-2][j+2]==num and arr[i-3][j+3]==0 and arr[i-4][j+4]==num:
				ans = (i-3, j+3)
				return ans
			elif arr[i][j]==num and arr[i-1][j+1]==num and arr[i-2][j+2]==0 and arr[i-3][j+3]==num and arr[i-4][j+4]==num:
				ans = (i-2, j+2)
				return ans
			elif arr[i][j]==num and arr[i-1][j+1]==0 and arr[i-2][j+2]==num and arr[i-3][j+3]==num and arr[i-4][j+4]==num:
				ans = (i-1, j+1)
				return ans
			elif arr[i][j]==0 and arr[i-1][j+1]==num and arr[i-2][j+2]==num and arr[i-3][j+3]==num and arr[i-4][j+4]==num:
				ans = (i, j)
				return ans
	
	return (-1, -1)


def handmade_AI(arra):
	possible_list = []
	array = arra[:]
	x = first_step(array, 1)
	if x!=(-1, -1):
		return [x]
	x = first_step(array, -1)
	if x!=(-1, -1):
		return [x]

	for i1 in range(0, 15):
		for j1 in range(0, 15):
			if array[i1][j1]!=0:
				continue
			array[i1][j1]=1
			chk=0
			for i2 in range(0, 15):
				for j2 in range(0, 15):
					if array[i2][j2]!=0:
						continue
					array[i2][j2]=-1
					if first_step(array, 1)==(-1, -1):
						chk=1
						array[i2][j2]=0
						break
					array[i2][j2]=0
				if chk==1:
					break
			array[i1][j1]=0
			if chk==0:
				possible_list.append([i1, j1])

	print("attack finish", possible_list)
	if len(possible_list)>0:
		return possible_list

	for i in range(0, 15):
		for j in range(0, 15):
			array[i][j] = -array[i][j]

	for i1 in range(0, 15):
		for j1 in range(0, 15):
			if array[i1][j1]!=0:
				continue
			array[i1][j1]=1
			chk=0
			for i2 in range(0, 15):
				for j2 in range(0, 15):
					if array[i2][j2]!=0:
						continue
					array[i2][j2]=-1
					if first_step(array, 1)==(-1, -1):
						chk=1
						array[i2][j2]=0
						break
					array[i2][j2]=0
				if chk==1:
					break

			array[i1][j1]=0
			if chk==0:
				possible_list.append([i1, j1])
	print("defense finish", possible_list)
	return possible_list



"""print(handmade_AI([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0,-1,-1, 0, 0, 0, 0, 0],
                   [0, 0, 0, -1, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))"""
