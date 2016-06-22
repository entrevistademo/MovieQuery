import argparse
import pandas as pd
import csv 
import requests
import zipfile
import urllib2
import io
#Importing libraries necessary to create this program.

#This is python command line tool to query the movie file from URL.

#declare the function that does the bulk of the queries.
def query(field, criteria, file):
	#using pandas to read the zipfile 
	df = pd.read_csv(file.open('dvd_csv.txt'))
	#converts all fields to strings for issues with NAN. 
	df = df.astype(str)
	#the bulk of the search using pandas str.contains function.
	Searches = df[df[field].str.contains(criteria, case=False)]
	#returns to main the dataframe.
	return Searches

def main():
	#declare location of File via URL
	url = "http://hometheaterinfo.com/download/dvd_csv.zip"
	#read the URL as a raw_data file
	raw_data = urllib2.urlopen(url).read()
	#take raw_data and essentially declare it as a zip, using BytesIO of raw_data
	zf = zipfile.ZipFile(io.BytesIO(raw_data))
	#using CSV library read the zipfile and open the content
	r = csv.reader(zf.open('dvd_csv.txt'))
	#declares the header of the file of the CSV (text)
	headers = r.next()


	#using the argParse library to read the arguements from command line.
	parser = argparse.ArgumentParser()
	#declare the arguments needed for this program (column and search and save a variable)
	parser.add_argument("-c","--column",help="Type Column Name from List", 
			choices = headers,type=str)
	parser.add_argument("-s","--search",nargs='+',help="Type what you want to search", type=str)
	#this reads the arguments of the command line
	args=parser.parse_args()
	#declares a variable field to be used with query function
	field =  args.column
	#This is to ensure that whatever is written for the search criteria includes the
	#spaces,  so that it doesn't only search the first word in a title.
	FullString  = ' '.join(args.search)
	#Call Query function to do the heavy lifting.
	results = query(field, FullString, zf)
	#prints the final results of the dataframe.
	print results	



if __name__=='__main__':
	main()

