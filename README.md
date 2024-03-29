# Transction Scraper

# Overview

Parse HTML (e.g. a transactions page from your bank) into CSV format for compatibility with tools like YNAB

## Supported banks and pages

1. SoFi, credit card transactions page - mode `sofi_cc`

_Please PR to add more!_

## General use

1. Open the transactions page in a desktop browser and get it to your desired state (e.g. scroll to load set of transactions)
1. "Save Page As" from your browser to your local filesystem, note the path
1. If necessary, clone/download this repo and setup
1. Execute Python script from this repo with desired options (see [Help](#help))

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

# Setup & Execution Options

## Setup

Create virtualenv, use it, and install dependencies:

```console
python3 -m venv trans_venv
source trans_venv/bin/activate
pip install -r requirements.txt
```

## Execution options

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
  --end-date END_DATE   Include transactions whose date is equal or prior to this end date, format YYYY-mm-dd
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