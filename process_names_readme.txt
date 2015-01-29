# Main: process_names.py
# process_names.py calls names.py

What the program does: 
	It takes a csv file with column 'Name' and returns all the columns of the original csv file + 'uniqid', 'FirstName', 'MiddleInitial/Name', 'LastName', 'RomanNumeral', 'Title', 'Suffix'. By default, it takes out duplicate names.   
	

COMMAND LINE OPTIONS
---------------------

Usage: process_names.py [options] <input file>

Options:
  -h, --help            show this help message and exit
  -o OUTFILE, --out=OUTFILE
                        Output file in CSV (default: cfscores_output.csv)
  -c COLUMN, --column=COLUMN
                        Column name in CSV that contains Names (default:
                        Name)
  -a, --all             Export all names (do not take duplicate names out)
                        (default: False)

EXAMPLES
--------
   chdir WhereTheScriptsAre
   C:\Python27\python.exe process_names.py -a sample_input.csv 
	