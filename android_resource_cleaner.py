#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import sys, getopt
import os

def main(argv):
	inputfile = ''
	try:
      		opts, args = getopt.getopt(argv,"hi:",["inputFile="])
	except getopt.GetoptError:
		print 'android_resource_cleaner.py -i <inputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
         		print 'android_resource_cleaner.py -i <inputfile>'
        		sys.exit()
     		elif opt in ("-i", "--inputFile"):
         		inputfile = arg
		
	return inputfile


def xmlParser(file):
	DOMTree = xml.dom.minidom.parse(file)
	issuesCollection = DOMTree.documentElement

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
					resource = location.attribute["file"]
					resource = resource.value
					print >> outputFile,'unused resource cleaned ',resource
					os.remove(resource)
					resourceTotal = resourceTotal + 1



	print >> outputFile,"Total resource cleaned = ",resourceTotal
	outputFile.close()
	print 'Clean up is done, complete report is available in android_resource_cleaner_output.txt'
	print 'Total clean up = ',resourceTotal

if __name__ == "__main__":
	input = main(sys.argv[1:])
	xmlParser(input)


