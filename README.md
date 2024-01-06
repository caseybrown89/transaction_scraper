# Transction Scraper

# Overview

Parse HTML (e.g. a transactions page from your bank) into CSV format for compatibility with tools like YNAB

## Supported pages

1. SoFi CC transactions

_Please PR to add more!_

## General use

1. Open transactions page in desktop browser
1. Load as many transactions onto page as you'd like
1. "Save Page As" from your browser to your local filesystem
1. Parse page using Python script in this repo (see [Help](#help))

Basic example:

```console
(venv) casey@Caseys-MacBook-Pro transaction_scraper % python3 main.py --html-file ~/Documents/sofi_cc_2024-01-06.html --output-file trans.csv
(venv) casey@Caseys-MacBook-Pro transaction_scraper % head -n5 trans.csv
date,payee,memo,outflow,inflow
2024-01-05,Market32 pchopper #250,Groceries,58.56,0
2024-01-04,Aldi 65228,Groceries,100.70,0
2024-01-04,Shopjimmycom,Shopping,27.66,0
2024-01-04,Thrive market,Other,64.15,0
```


# Help

```console
% PYTHONPATH=. python3 main.py --help
usage: Scrape transaction HTML [-h] [--mode MODE] --html-file HTML_FILE [--start-date START_DATE] [--end-date END_DATE] [--output-file-name OUTPUT_FILE_NAME] [--file-encoding FILE_ENCODING]

Produce CSV output from transactions HTML

optional arguments:
  -h, --help            show this help message and exit
  --mode MODE           Transaction parser to use. Available sofi_cc
  --html-file HTML_FILE
                        The HTML file containing Sofi CC transactions
  --start-date START_DATE
                        Include transactions whose date is equal or later than this start date, format YYYY-mm-dd
  --end-date END_DATE   Include transactions whose date is equal or later than this start date, format YYYY-mm-dd
  --output-file-name OUTPUT_FILE_NAME
                        File name of output CSV file
  --file-encoding FILE_ENCODING
                        Encoding to use for input HFML/output CSV files
```

# Testing

```console
% PYTHONPATH=. python3 -m unittest parsers/tests/test*.py
.
----------------------------------------------------------------------
Ran 1 test in 0.032s

OK
```