from itertools import product
from lists import subDict
from lists import dummyCharacters
from lists import numbersOnly

def fullSub(password):
	letters = []
	for val in password:
		if val in subDict.keys():
			letters.append(subDict[val])
		else:
			letters.append(val)
	return [''.join(item) for item in product(*letters)]

def basicSub(password, numbers=False):
	numCombos = [''.join(p) for n in range(1,5) for p in product(numbersOnly, repeat=n)]
	characterList = numCombos if numbers else dummyCharacters
	passwords = []
	middle = password[1:]
	replacements = product(subDict[password[0]], characterList)
	for val in replacements:
		passwords.append(val[0] + middle + val[1])
	return passwords

def appendNumbers(password):
	return basicSub(password, True)