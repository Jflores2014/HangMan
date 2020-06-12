import getpass 

print("Welcome to Hangman")

#Have frist player type in a word
Word = getpass.getpass("Enter a word to guess:")
#Store this word in an array
wordList = list(Word)
#Set a guess limit at word%2= # guesses  
guessedLetters = ["_ "]*len(wordList)
done = len(wordList)
guess = 10
if(done>guess):
	guess = done + done%2
gameEnd = False 


while(gameEnd == False):
	print("Enter your Guess:")
	letterGuess = input("")
	if(len(letterGuess)>1):
		print("Only one letter at a time please!")
	if (letterGuess.isalpha() != True):
		print("Please use only letters, try again")
	#Compare if guess is in the array
	if letterGuess in wordList:
		#If guess is correct, reveal that part of the word
		for i in range(len(guessedLetters)):
			if(wordList[i] == letterGuess):
				guessedLetters[i] = letterGuess + " "
				done = done-1
		for i in range(len(guessedLetters)):
			print(guessedLetters[i],end='')
		if(done == 0):
			gameEnd = True
			break
		print("")
		print("Keep Going!")
	
#	If guess is wrong, display error message & take guess # down by one
	else:
		print("Wrong")
		guess =  guess - 1
		#If guess# comes to zero end game
		if(guess<1):
			print("You Lose!")
			gameEnd = True

	
#Once all letters are guessed correctly end game
#	Display A Winner Message 

#Start a new  Game