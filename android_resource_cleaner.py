#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import sys, getopt
import os

inputfile = ''
exceptionfile = ""

def main(argv):

	global inputfile
	global exceptionfile

	try:
      		opts, args = getopt.getopt(argv,"hi:e:",["inputFile=","exceptionFile"])
	except getopt.GetoptError:
		print 'android_resource_cleaner.py -i <inputfile> -'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
         		print 'android_resource_cleaner.py -i <inputFile> -e <exceptionFile>'
        		sys.exit()
     		elif opt in ("-i", "--inputFile"):
         		inputfile = arg
		elif opt in ("-e", "--exceptionFile"):
			exceptionfile = arg


def xmlParser(inputfile,exceptionfile):

	if not inputfile:
		print 'please enter input file path'
		return 

	DOMTree = xml.dom.minidom.parse(inputfile)
	issuesCollection = DOMTree.documentElement
	
	#exception set
	exceptionSet = set()

	# initialize the exception set with file names
	if exceptionfile:
		fileNames = file(exceptionfile).read().split()
		for fileName in fileNames:
			exceptionSet.add(fileName)
		
	# Get all the issues in the collection
	issues = issuesCollection.getElementsByTagName("issue")

	outputFile = open('android_resource_cleaner_output.txt', 'w')

	resourceTotal = 0

	for issue in issues:
		id = issue.attributes["id"]
		id = id.value
		if id == 'UnusedResources':

			if not issue.hasAttribute("errorLine1"):
				locations = issue.getElementsByTagName("location")
				for location in locations:
					resource = location.attributes["file"]
					resource = resource.value
					resourceFileName = resource.split('/')
					resourceFileName = resourceFileName[len(resourceFileName)-1]
					if not resourceFileName in exceptionSet:
						print >> outputFile,'unused resource cleaned ',resource
						os.remove(resource)
						resourceTotal = resourceTotal + 1



	print >> outputFile,"Total resource cleaned = ",resourceTotal
	outputFile.close()
	print 'Clean up is done, complete report is available in android_resource_cleaner_output.txt'
	print 'Total clean up = ',resourceTotal

if __name__ == "__main__":
	main(sys.argv[1:])
	xmlParser(inputfile,exceptionfile)


