import time 
while True : 
	board = ["1" , "2" , "3" , 
			 "4" , "5" , "6" ,
	 		 "7" , "8" , "9" ,]
	global flag,flag1,x
	flag = 0
	flag1 = 1
	x = 1
	def displayboard():#print the board
		print ('  |     |     |     |')
		print("  |  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |  " )
		print ('--|-----|-----|-----|---')
		print("  |  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |  " )
		print ('--|-----|-----|-----|---')
		print("  |  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |  " ) 
		print ('  |     |     |     |')

	def turns(a):#Take a as the indicator is going to play the next move
		turn = int(input("Tell us your next turn(1-9 acceptable) player({}) : ".format(a)))
		turn = turn - 1
		if a == 1 :
			board[turn] = 'X'
		elif a == 2 :
			board[turn] = 'O'
		


	def checkwin():
		if (board[0] == board[1] == board[2] )| (board[3] == board[4]  == board[5]) |( board[6] == board[7]  == board[8]):
			return "end" #check horizentally
		elif (board[0] == board[3] == board[6] )| (board[1] == board[4]  == board[7]) |( board[2] == board[5]  == board[8]):
			return "end" #check parallaly
		elif (board[0] == board[4]  == board[8] )| (board[2] == board[4]  == board[6]) :
			return "end" #check cross



	def play_game():
		global flag,flag1,x
		flag = 0
		flag1 = 1
		x = 1

		x = checkwin();

		while(flag != 9 and x != 'end'):
			displayboard()#display the board we want to play 

			if flag1==1:#check who is gonna play next
				turns(1)
				flag1 = 2
				flag += 1

			elif flag1 == 2:
				turns(2)
				flag1 = 1
				flag += 1

			x = checkwin();
			if x != 'end':
				pass
			elif flag == 9:
				print("Tie!!! Wanna try again?")
			else :
				if flag1 == 1:
					print("The winner is player 2")
				elif flag1 == 2:
					print("The winner is player 1")



	play_game()
	time.sleep(0.3)
	print('_______________________________________________________________________________________________________')
	time.sleep(0.3)
	print('_______________________________________________________________________________________________________')
	time.sleep(0.3)
	print('_______________________________________________________________________________________________________')
	time.sleep(0.3)
	print("___________________________________________STARTING NEW GAME__________________________________________")
	time.sleep(0.3)
	print('_______________________________________________________________________________________________________')
	time.sleep(0.3)
	print('_______________________________________________________________________________________________________')
	time.sleep(0.3)
	print('_______________________________________________________________________________________________________')
	time.sleep(0.3)
