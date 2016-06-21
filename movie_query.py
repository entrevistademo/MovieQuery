import argparse
import pandas as pd
import csv 

def query(field, criteria):
	df = pd.read_csv('orgdvd.csv')
	df = df.astype(str)
	Searches = df[df[field].str.contains(criteria, case=False).fillna(False)]
	return Searches

def main():
	
	with open('dvdv1.csv') as f:
		f_csv = csv.reader(f)
		headers=next(f_csv)
		f.close()

	parser = argparse.ArgumentParser()
	parser.add_argument("-c","--column",help="Type Column Name from List", 
			choices = headers,type=str)
	parser.add_argument("-s","--search",nargs='+',help="Type what you want to search", type=str)
	args=parser.parse_args()
	field =  args.column
	FullString  = ' '.join(args.search)
	MainSearch =  FullString.lower()
	results = query(field, FullString)
	print results	
#	print "The "+ str(args.num) + "th fib number is " + str(result)

if __name__=='__main__':
	main()

