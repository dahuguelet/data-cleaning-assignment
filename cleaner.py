import csv

# Specifying input and output files
csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/cleanme-cleaned.csv', 'w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

#Writing headers 
writer.writeheader()

# Loop for cleaning
for row in reader:
	# Uppercasing first names
	row['first_name'] = row['first_name'].upper()
	# Adding leading zeroes to ZIP codes
	row['zip'] = row['zip'].zfill(5)
	# Deleting non-breaking spaces
	row['city'] = row['city'].replace('&nbsp;',' ')
	# Floating amounts for if statement
	row['amount'] = float(row['amount'])
	# Restricting output to contributions of $1,000+
	if row['amount'] > 1000:
		writer.writerow(row)
