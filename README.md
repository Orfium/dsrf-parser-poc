# dsrf-parser-poc

This is a parser for DSR Flat files using the UGC Profile (Version 1.4). The script parses .tsv files following the Digital Sales Reporting Standard ([DDEX Knowledge Base](https://kb.ddex.net/display/HBK/DDEX+Knowledge+Base)) and creates .csv files for records and compositions, mentioned in the sales/usage reports in order to be given as input in the [Metadata-Linking Service](https://orfium.atlassian.net/wiki/spaces/CMM/pages/1416921138/Metadata-Linking+Service#CSV-Templates). This proof of concept was implemented for the needs of [MMS-695](https://orfium.atlassian.net/browse/MMS-695).

## Prerequisites 

Python 3.10.8

## Usage

An environment variable should be set indicating the relative path of the .tsv file to be parsed under the name FILE. 
```
export FILE=<filename-in-path>
```

Execute:
```
python dsrf_poc.py
```
