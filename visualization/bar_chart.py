#showing some data/number for various discrete values

"""
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

from matplotlib import pyplot as plt 

#bar function accept the x cordinate of left side of each bar as input

x = [i+0.1 for i,_ in enumerate(movies)]
#0.1 to shift the bar to the right

plt.bar(x, num_oscars)
plt.title("My favorite movies") 
plt.ylabel("Number of Academy Awards")
plt.xticks([i+0.5 for i, _ in enumerate(movies)], movies)  #xticks accept position, text
plt.show() 
"""

"""
#making a histogram using bar chart
from collections import Counter
from matplotlib import pyplot as plt
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

decile = lambda grade: grade // 10

histogram = Counter([decile(grade) for grade in grades])

plt.bar([10*x-4 for x in histogram.keys()], histogram.values(), width=8)
plt.axis([-5, 105, 0, 5])
plt.title("Grade Count")
plt.ylabel("frequency of grades")
plt.xticks([10*i for i in range(11)])
plt.show()
"""