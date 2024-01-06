"""
Reads in HTML file and produces parsed CSV output
"""

from datetime import datetime
import argparse
import csv

from parsers.sofi_cc import parse as sofi_cc_parser

if __name__ == "__main__":
    transaction_parser_funcs = {
        'sofi_cc': sofi_cc_parser
    }

    arg_parser = argparse.ArgumentParser(
        prog='Scrape transaction HTML',
        description='Produce CSV output from transactions HTML'
    )

    arg_parser.add_argument('--mode', default='sofi_cc',required=False,
                            help='Transaction parser to use. Available ' \
                            f'{",".join(transaction_parser_funcs)}')
    arg_parser.add_argument('--html-file', required=True,
                        help='The HTML file containing Sofi CC transactions')
    arg_parser.add_argument('--start-date', required=False,
                        help='Include transactions whose date is equal or later than this ' \
                        'start date, format YYYY-mm-dd')
    arg_parser.add_argument('--end-date', required=False,
                        help='Include transactions whose date is equal or later than this ' \
                        'start date, format YYYY-mm-dd')
    arg_parser.add_argument('--output-file-name', required=False, default='cc_trans_out.csv',
                        help='File name of output CSV file')
    arg_parser.add_argument('--file-encoding', default='utf-8',
                        help='Encoding to use for input HFML/output CSV files')
    args = arg_parser.parse_args()

    if args.mode not in transaction_parser_funcs:
        raise TypeError(f"Unknown mode option: f{args.mode}")
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d') if args.start_date else None
    end_date = datetime.strptime(args.end_date, '%Y-%m-%d') if args.end_date else None

    # parse
    with open(args.html_file, 'r', encoding=args.file_encoding) as html_file:
        html_lines = "\n".join(html_file.readlines())
        parsed_transactions = transaction_parser_funcs[args.mode](html_lines)


    # filter and write
    with open(args.output_file_name, 'w', newline='', encoding=args.file_encoding) as csv_file_out:
        fieldnames = ['date', 'payee', 'memo', 'outflow', 'inflow']
        tran_writer = csv.DictWriter(csv_file_out, delimiter=',',quotechar='|',
                                     quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)

        tran_writer.writeheader()
        for tran in parsed_transactions:
            dicted = dict(zip(fieldnames, tran))            
            if start_date or end_date:
                if start_date and dicted['date'] < start_date:
                    continue # tran before start date
                if end_date and dicted['date'] > end_date:
                    continue # tran date after end date
            dicted['date'] = dicted['date'].strftime("%Y-%m-%d")
            tran_writer.writerow(dicted)
