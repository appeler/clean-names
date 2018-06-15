#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import optparse

import names

DEFAULT_OUTPUT   = "sample_output.csv"

def parse_command_line(argv):
    """Parse command line options
    """
    usage = "Usage: %prog [options] <input file>"                
    parser = optparse.OptionParser(add_help_option=True, usage=usage)
    
    parser.add_option("-o", "--out", action="store", 
                      type="string", dest="outfile", default=DEFAULT_OUTPUT,
                      help="Output file in CSV (default: {0!s})".format(DEFAULT_OUTPUT))
    parser.add_option("-c", "--column", action="store", 
                      type="string", dest="column", default="Name",
                      help="Column name file in CSV contains Name list (default: Name)")
    parser.add_option("-a", "--all", action="store_true", 
                      dest="all", default=False,
                      help="Export all names (not take duplicate names out) (default: False)")
    return parser.parse_args(argv)

if __name__ == "__main__":
    print("{0!s} - r3 (2013/08/25)\n".format((os.path.basename(sys.argv[0]))))    

    (options, args) = parse_command_line(sys.argv)

    if len(args) < 2:
        print("Usage: {0!s} [options] <input file>\n".format((sys.argv[0])))
        sys.exit(-1)
   
    print("Processing and exporting, please wait...")
        
    """Process and export names file
    """
    names.process_name_list(args[1], options.outfile, options.column, options.all)
    
    print("Done.")