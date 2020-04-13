#this file is to get familiar with python formating rules

#python uses indentation to delimit code of blocks unlike the curly braces

for i in [2, 3, 4, 5]:
	print(i)
	for j in [1, 2, 3, 4, 5]:
		print(j)
		print(i+j)

print("done looping") 

##making code easier to read by diving in multiple lines
list_of_lists = [[1, 2, 3], [4, 5, 6], [6, 8, 9]]

easier_to_read_list_of_lists = [ [1, 2, 3],
                                 [4, 5, 6],
                                 [6, 8, 9] ]

print(easier_to_read_list_of_lists)