'''
Created on 15 Jul 2020

@author: d035331
'''

import argparse
import codecs
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="SPA SPOOL Pre-Wrangler")

    parser.add_argument("-s", "--spoolfile", type=str, help="|String| The name of the SPOOL output file to be converted")
    parser.add_argument("-w", "--wranglefile", type=str, help="|String| The name of the file to be created, which will be used in wrangler ingestion")
    
    args = parser.parse_args()

    spoolfile = ""
    if args.spoolfile:
        spoolfile = args.spoolfile
    else:
        print("--spoolfile argument missing from arguments: %s.  Script needs the name of the SPOOL output file to be converted" %args)
        sys.exit()
        
    wranglefile = ""
    if args.wranglefile:
        wranglefile = args.wranglefile
    else:
        print("--wranglefile argument missing from arguments: %s.  Script needs the name of the output file, which will be wrangled" %args)
        sys.exit()


    rawReadLoc = codecs.open(spoolfile, "r", "utf-8")
    rawAllLines = rawReadLoc.readlines()
    rawReadLoc.close
    
    n = 0
    kept = 0
    skipped = 0
    skipLines = []
    wranglerLines = []
    
    for eachReadLine in rawAllLines:
        try:
            rawLine = rawAllLines[n]
        except IndexError:
            break
        
        if n == 0:
            #The first line will be ascii art.  Note it as a skip pattern and continue
            skipLines.append(eachReadLine)
            skipped = skipped + 1
        elif n == 1:
            #The second line is the first instance of a header row.  Note it in the skip pattern and add it to the output list
            skipLines.append(eachReadLine)
            wranglerLines.append(eachReadLine)
            kept = kept + 1
        else:
            if eachReadLine not in skipLines:
                wranglerLines.append(eachReadLine)
                kept = kept + 1
            else:
                skipped = skipped + 1
                
        n = n+1
                
    outWriteLoc = codecs.open(wranglefile, "w", "utf-8")
    outAllLines = outWriteLoc.writelines(wranglerLines)
    outWriteLoc.close
    
    print("Wrote contents of SPOOL file %s to SAP Analytics Cloud friendly wrangle file %s." %(spoolfile, wranglefile)) 
    print("Wrote %s lines and dropped %s." %(kept, skipped)) 