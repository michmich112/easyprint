
LIST = 0
DICT = 1
TUPL = 2

spaces = 0
CustomSpacing = 2

def returnType(inputValue):
	global LIST,DICT,TUPL
	a = inputValue.__class__
	if a == list:
		return LIST
	elif a == dict:
		return DICT
	elif a == tuple:
		return TUPL
	else:
		return None

def eprint(inputValue):
	global LIST,DICT,TUPL,spaces,CustomSpacing
	tmp = returnType(inputValue)
	if tmp == None:
		try:
			print(' '*spaces + str(inputValue))
		except UnicodeEncodeError:
			print(inputValue)
	elif tmp == LIST:
		print(' '*spaces + '[')
		spaces += 1*CustomSpacing
		for element in inputValue:
			eprint(element)
		spaces -= 1*CustomSpacing
		print(' '*spaces + ']')
	elif tmp == DICT:
		print(' '*spaces + '{')
		spaces += 1*CustomSpacing
		k = inputValue.keys()
		for key in k:
			if returnType(inputValue.get(key)) == None:
				try:
					print(' '*spaces + key + ' : ' + str(inputValue.get(key)))
				except UnicodeEncodeError:
					print(' '*spaces + key + ' : ' ,inputValue.get(key))
			else:
				print(' '*spaces + key + ' :')
				eprint(inputValue.get(key))
		spaces -= 1*CustomSpacing
		print(' '*spaces + '}')
	elif tmp == TUPL:
		print(' '*spaces + '(')
		spaces += 1*CustomSpacing
		for element in inputValue:
			eprint(element)
		spaces -= 1*CustomSpacing
		print(' '*spaces + ')')




