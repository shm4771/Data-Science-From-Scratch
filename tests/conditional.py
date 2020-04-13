#This is the example to simulate conditional probability 

######Note:- library locations has been changed, will be upadted soon ----

#problem_1: given elder kid is girl, probability that both kids are girls
#problem_2: given that atleast one kid is girl, probability that both kids are girls

import random 

def pick_kid():
	return random.choice(["boy", "girl"])

elder_girl = 0
both_girls = 0
either_girl = 0  #both can be girls too

random.seed(0)
for _ in range(10000):
	young = pick_kid()
	older = pick_kid()

	if (older == "girl"):
		elder_girl += 1

	if (young == "girl" and older == "girl"):
		both_girls += 1

	if(young == "girl" or older == "girl"):
		either_girl += 1

print("Probability that both are girls conditioned upon elder is girl:", both_girls/elder_girl)
print("Probability that both are girls conditioned atleast one is girl:", both_girls/either_girl)

