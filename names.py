#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
from nameparser import HumanName

re_std_suffix = re.compile("(JR|SR|PHD)[^\.]", flags=re.I)

def process_name_list(infile, outfile=None, col="Name", all=False):
    """ Read names and pre-process
        Returns unique names in format "FirstName LastName AnyRomanNumeral" or "FirstName LastName" 
    """
    ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    if outfile:
        try:
            of = open(outfile, 'w', encoding='utf-8')
        except:
            outfile = None
    
    with open(infile, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if outfile:
            writer = csv.DictWriter(of, fieldnames=reader.fieldnames + ['uniqid', 'FirstName', 'MiddleInitial/Name', 'LastName', 'RomanNumeral', 'Title', 'Suffix'])
            writer.writeheader()
        rowid = 0
        allnames = []
        allnameswithid = []
        for r in reader:
            rname = r[col]
            for name in re.split('[&/]', rname):
                name, n = re.subn(r'\s*\(.*\)\s*', ' ', name)
                if n > 0:
                    #print "Remove Parenthesis...", name
                    pass
                name, n = re.subn(r'\s*[\'"].*[\"\']\s*', ' ', name)
                if n > 0:
                    #print "Remove Quote...", name
                    pass
                name = HumanName(name)
                if name.last == '':
                    a = name.suffix.split(',')
                    if len(a) >= 2:
                        name = HumanName(name.first + ', ' + a[1] + ' ' + a[0])
                first = name.first.lower()
                mid = name.middle.lower()
                roman = ""
                title = name.title
                
                last = ""
                suffix_list = []
                for s in name.suffix.split(','):                        
                    if s.strip() in ROMAN:
                        roman = s
                        last = name.last.lower() + ' ' + roman.strip().lower()
                    else:
                        suffix_list.append(s)
                if last == "":
                    last = name.last.lower()
                suffix = ', '.join(suffix_list)
                
                if last == '':
                    print(repr(name))
                    
                # Fixed ROMAN and Title in Middle
                if mid != "":
                    m_list = mid.split()
                    m = m_list[-1].strip()
                    m = m.strip('.')
                    if len(m_list) > 1 and m.upper() in ROMAN:
                        roman = m
                        mid = ' '.join(m_list[:-1])
                        #print rname, "==>", roman, "==>", mid
                    if m in ['mr', 'ms']:
                        title = m
                        mid = ' '.join(m_list[:-1])
                        #print rname, "==>", title, "==>", mid
                        
                # Adhoc fixed for Title
                if title in ['POPE', "BARON", "MAHDI"]:
                    first = title + ' ' + first
                    #print rname, "==>", title, "==>", first
                    title = ""
                
                # Standardize Jr/Sr suffix
                suffix = re_std_suffix.sub(r'\1.', suffix + ' ').strip()
                
                # Standardize Middle Initial
                std_mid = []
                for m in mid.split():
                    if len(m) == 1:
                        m = m + '.'
                    std_mid.append(m)
                mid = ' '.join(std_mid)
                
                if all or (first, mid, last) not in allnames:
                    rowid += 1
                    r['uniqid'] = rowid
                    allnameswithid.append((r['uniqid'], first, mid, last, r['seat'].strip()))
                    allnames.append((first, mid, last))
                    #print "Add...", r['uniqid'], first, "-", mid, "-", last, "-", r['seat'].strip()
                    s = {'FirstName': first.upper(), 'MiddleInitial/Name': mid.upper(), 'LastName': name.last, 'RomanNumeral': roman.upper(), 'Title': title.upper(), 'Suffix': suffix.upper()}
                    t = dict(r, **s)
                    if outfile:
                        writer.writerow(t)
        if outfile:
            of.close()                            
        return allnameswithid
    return None

if __name__ == '__main__':
    pass
