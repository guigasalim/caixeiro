# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 7

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graphD, graphP, s):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)
	only_path = ""
	size_path = 0
	for i in next_permutation:

		# store current Path weight(cost)
		current_pathweight = 0
		current_path = "A"
		
		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graphD[k][j]
			current_path = current_path + " - " + str(graphP[k][j])
			
			k = j
		current_pathweight += graphD[k][s]
		current_path = current_path + " - " + str(graphP[k][s])
		
		# update minimum
		min_path = min(min_path, current_pathweight)
		if current_pathweight >= min_path:
			
			only_path = current_path
	return str(only_path) + " = " + str(min_path)


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graphD = [[0, 25.7, 15.9, 28, 7.7, 17.5, 12,8], [25,7, 0, 10.9, 5.5, 30.1, 34.6, 18],
			[15.9, 10.9, 0, 13.2, 20.5, 25, 8], [28, 5.5, 13.2, 0, 31.4, 35.9, 18.9], [7.7, 30.1, 20.5, 31.4, 0, 7.1, 6.3],
			[17.5, 34.6, 25, 35.9, 7.1, 0, 10.4], [12.8, 18, 8, 18.9, 6.3, 10.4, 0]]
	graphP=[["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"]]
	s = 0
	print("Baseado na distancia(km): ")
	print(travellingSalesmanProblem(graphD, graphP, s))
	print("---------------------------------------------")
	graphD = [[0, 30, 20, 35, 14, 22, 18], [30, 0, 16, 14, 35, 40, 28],
			[20, 16, 0, 20, 22, 26, 10], [35, 14, 20, 0, 35, 40, 26], [14, 35, 22, 35, 0, 9, 12],
			[22, 40, 26, 40, 9, 0, 20], [18, 28, 10, 26, 12, 20, 0]]
	graphP=[["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"]]
	s = 0
	print("Melhor caso(min): ")
	print(travellingSalesmanProblem(graphD, graphP, s))
	print("---------------------------------------------")
	graphD = [[0, 45, 40, 65, 35, 40, 35], [45, 0, 35, 30, 65, 70, 60],
			[40, 35, 0, 45, 40, 45, 20], [65, 30, 45, 0, 70, 85, 50], [35, 65, 40, 70, 0, 14, 30],
			[40, 70, 45, 85, 14, 0, 45], [35, 60, 20, 50, 30, 45, 0]]
	graphP=[["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"],["A","B","C","D","E","F","G"]]
	s = 0
	print("Pior caso(min): ")
	print(travellingSalesmanProblem(graphD, graphP, s))
	print("---------------------------------------------")