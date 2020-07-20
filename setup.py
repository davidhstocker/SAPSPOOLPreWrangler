
'''
Created on July 20, 2020
@author: David Stocker
'''

from distutils.core import setup
setup(
  name = 'SAPSPOOLPreWrangler',
  packages = ['SAPSPOOLPreWrangler'], # this must be the same as the name above
  version = '0.1',
  description = 'A converter utility to prw-wrangle output created by the SAP ABAP SPOOL command and make data preparation in SAP Analytics Cloud quicker.',
  author = 'David Stocker',
  author_email = 'mrdave991@gmail.com',
  url = 'https://github.com/davidhstocker/SAPSPOOLPreWrangler', # use the URL to the github repo
  download_url = 'https://github.com/davidhstocker/ghcndextractor/tarball/0.1', 
  keywords = ['sap', 'wrangling', 'analytics'], # arbitrary keywords
  classifiers = [],
)
