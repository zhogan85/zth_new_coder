import csv

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-like object."""
	#open csv file
	opened_file = open(raw_file)
	
	#read csv file
	csv_data = csv.reader(opened_file,delimiter=delimiter)
	
	#build parsed data
	parsed_data = []
	
	#define headers
	fields = csv_data.next()
	
	#Iterate over each row of the csv file, zip together field->value pairs
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	
	#close csv file
	opened_file.close()
	
	return parsed_data

def main():
	#call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")
	
	#let's see what the data looks like!
	print new_data

if __name__ == "__main__":
	main()

