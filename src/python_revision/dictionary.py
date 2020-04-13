empty_dict = {}

marks = {"Joel": 80, "Tim": 95}

print(marks["Joel"]) #use key to give values

try:
	kates_grades = marks["Kate"]
except KeyError:
	print("No entry for Kate exist")

#to collect list of keys use - dict.keys()
#for list of entries in values - dict.values()
#for list of (key, val) tuples - dict.items()

#default dict is the great way we want to check entries many times in program
#which don't even exist
from collections import defaultdict

word_counts = defaultdict(int) #word: count
hobby_list = defaultdict(list) #user: hobby_list
biodata = defaultdict(dict) #user:{"City:name", "age: number", "email: address"}

#counter: used to counter frequency of some item and build a dictionary
from collections import Counter
names = ["Anshul", "Hemant", "Anshul"]

word_counts = Counter(names)
print(word_counts)