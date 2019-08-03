def generateStrings (sigma, lengthOfSigma, maximumLengthOfString) :
	stringList = sigma	
	tempStringList = sigma
	for i in range(maximumLengthOfString-1) :
		currentListSize = len(tempStringList)
		for j in range(currentListSize):	
			for k in range(lengthOfSigma) :
				tempStringList.append(tempStringList[j] + sigma[k])
		tempStringList = tempStringList[currentListSize:]
		for j in tempStringList :
			stringList.append(j)
	return stringList

def main():
	lengthOfSigma=int(input("How many terminals are there in sigma?: "))
	print "length is: ",lengthOfSigma
	sigma=[]
	maximumLengthOfString=int(input("What is the maximum length of the string?: "))
	print "length is: ",maximumLengthOfString
	for i in range(lengthOfSigma) :
		sigma.append(input("Enter alphabet: "))
	sigma = list(set(sigma))	
	print sigma
	lengthOfSigma=len(sigma)
	stringList = generateStrings(sigma, lengthOfSigma, maximumLengthOfString)
	print stringList
	fileDiscriptor = open("output.txt", 'w')
	fileDiscriptor.truncate(0)
	for i in stringList :
		print i
		fileDiscriptor.write(i+"\n")
	fileDiscriptor.close()	

if __name__ == "__main__":
	main()
