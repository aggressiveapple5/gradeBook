def average_rows(grid):
	rowAverage = 0
	rowAverages = []
	rows = 0
	for row in grid:
		rowAverage = 0.0
		rows = 0.0
		for number in row:
			rowAverage += number
			rows += 1
		rowAverages.append(rowAverage / rows)
		
	return rowAverages


gradeBook = [[95, 100, 93, 32, 7],
             [1, 2, 3, 4, 5],
             [80, 81, 82, 83, 84]]


rowAverages = average_rows(gradeBook)

classAverage = 0.0
students = 0.0
for student in rowAverages:
	classAverage += student
	students += 1
classAverage = classAverage / students



classAverage = round(classAverage, 2)







print("Student Averages: {}".format(rowAverages))
print("Class Average: {}".format(classAverage))           
             
             
             
             