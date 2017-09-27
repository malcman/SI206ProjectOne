import os
import filecmp
import csv
import time

# uniqname: malc
# name: Malcolm Maturen
# SI 206 Project 1

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	dictList = []
	with open(file, 'r') as f:
		inFile = csv.DictReader(f)
		for person in inFile:
			dictList.append(person)
	return dictList

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	person = sorted(data, key = lambda x: x[col])[0]
	return person['First'] + ' ' + person['Last']

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	classCounts = {}
	for d in data:
		classCounts[d['Class']] = classCounts.get(d['Class'], 0) + 1
	classList = [item for item in classCounts.items()]
	classList.sort(key = lambda x: x[1], reverse = True)
	return classList



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	dayCounts = {}
	for person in a:
		day = int(person['DOB'].split('/')[1])
		dayCounts[day] = dayCounts.get(day, 0) + 1
	return max(dayCounts, key = dayCounts.get)


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest integer.
	today = time.strftime("%m/%d/%Y")
	todayList = today.split('/')
	ages = []
	for person in a:
		birthdate = person['DOB'].split('/')
		ages.append(int(todayList[2]) - int(birthdate[2]) - ((int(todayList[0]), int(todayList[1])) < (int(birthdate[0]), int(birthdate[1]))))
	return round(sum(ages) / len(ages))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	fieldNames = ['First', 'Last', 'Email']
	sortedA = sorted(a, key = lambda x: x[col])
	with open(fileName, 'w') as f:
		for person in sortedA:
			f.write('{},{},{},\n'.format(person['First'], person['Last'], person['Email']))

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

