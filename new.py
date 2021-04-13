import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def meaning(w):
	if w in data:
		return data[w.lower()]
	elif len(get_close_matches(w,data.keys()))>0:
		ch =input("Did you mean %s instead: " %get_close_matches(w,data.keys())[0])
		if ch.lower()=='yes' or ch.lower()=='y':
			return meaning(get_close_matches(w,data.keys())[0])
		else:
			return "The word doesnt exist"
	else:
		return "The word doesnt exist"


while True:
	word=input("Enter Word: ")
	print(meaning(word))
	ch =input("Want to continue? ")
	if ch.lower()=='yes' or ch.lower()=='y':
	else: 
		break
