import random
import time
num = random.randint(1,9)
userguess = 0
userguesses = []
print "Let's take a try at guessing a number between 1 and 9. \
Once you take a guess, I will tell you if you are too low, too high, or on the mark. \
Once you've got the number, we'll look at how many guesses it took."
time.sleep(2)
while num!=userguess:
	while True:
		try:
			userguess = int(raw_input("Take a guess between 1 and 9: "))
			while userguess not in range (1,10):
				userguess = int(raw_input("Take a guess between 1 and 9: "))
			if userguess<num:
				print "Too low! Try again."
			elif userguess>num:
				print "Too high! Try again."
			userguesses.append(userguess)
			break
		except:
			print "Not a valid numeric entry."
time.sleep(2)
print "Got it! You guessed the correct number",num,"after",len(userguesses),"tries!"
time.sleep(5)
