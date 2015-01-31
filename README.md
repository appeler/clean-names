### Clean Names

Takes a csv file with column 'Name' (containing 'dirty names.' For instance, lastname firstname.) and returns all the columns of the original csv file + 'uniqid', 'FirstName', 'MiddleInitial/Name', 'LastName', 'RomanNumeral', 'Title', 'Suffix'. By default, it takes out duplicate names.

#### License

Scripts are released under the [MIT License][].

#### Usage

Main: process\_names.py process\_names.py calls names.py

#### COMMAND LINE OPTIONS

Usage: process\_names.py [options]  
  
Options:  
    -h, --help show this help message and exit  
    -o OUTFILE, --out=OUTFILE  
                  Output file in CSV (default: cfscores\_output.csv)  
     -c COLUMN, --column=COLUMN  
                  Column name in CSV that contains Names (default: Name)  
     -a, --all    Export all names (do not take duplicate names out)  
                  (default: False)

#### EXAMPLES

chdir WhereTheScriptsAre  
python process\_names.py -a sample\_input.csv  

#### NOTE

Use the script to fix names in CF-Scores from [Database on Ideology, Money in Politics, and Elections][].

  [MIT License]: https://github.com/soodoku/Clean-Names/License%20for%20Scripts.md
  [Database on Ideology, Money in Politics, and Elections]: http://data.stanford.edu/dime
