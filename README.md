# SAPSPOOLPreWrangler
A converter utility to "prw-wrangle" output created by the SAP ABAP SPOOL command and make data preparation in SAP Analytics Cloud quicker.

The SPOOL command on SAP ABAP systems outputs table content formatted for a printer.  Each page of the printout starts with a three-line header block, which looks something like the following.

+-----+----+-----------+-----------+---------------------------------+----------+----
| Plnt|DSLT|      DSLND|      DSLNQ|Name 1                           |Ship-To
+-----+----+-----------+-----------+---------------------------------+----------+----

It contains the actual header, wrapped in two lines of ascii art.  When the output target is a file, such as a .csv file, these repeating header lines are in the output, even though page formatting is not relevant.  In fact, it is counter productive if opened in a spreadsheet program or ingested into a data wrangling workflow, because header blocks don't have the same semantic meaning or even data type as the columns they represent.  

This utility removed the ascii art and repeat headers, leaving a single header row at the top of the file.

There are two required parameters:
-s or --spoolfile        The name of the SPOOL output file to be converted
-w or --wranglefile      The name of the file to be created, which will be used in wrangler ingestion
