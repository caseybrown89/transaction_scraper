"""
Parses transactions from Sofi CC desktop HTML
"""

from datetime import datetime

from bs4 import BeautifulSoup

def parse(lines):
    soup = BeautifulSoup(lines, 'html.parser')

    pending = soup.find_all("button", {"data-qa" : "pending-transaction-item"})
    posted = soup.find_all("button", {"data-qa" : "posted-transaction-item"})
    count = 0
    for transaction in pending + posted:
        count += 1
        if count % 2 == 1:
            # duplicate transaction entry
            continue

        jump_parent_div = transaction.parent.parent
        tran_date = jump_parent_div.find("p").text
        parsed_datetime = datetime.strptime(tran_date, '%m/%d/%Y')

        tran_merchant, tran_category, tran_amount = [
            p.text.strip() for p in jump_parent_div.find("div").find_all("p")
        ]

        tran_type = 'inflow' if tran_amount[0] == '-' else 'outflow'
        inflow, outflow = 0, 0
        amt_cleaned = tran_amount[tran_amount.find('$') + 1:].replace(',', '')

        if tran_type == 'inflow':
            inflow = amt_cleaned
        else:
            outflow = amt_cleaned

        yield [parsed_datetime, tran_merchant, tran_category, outflow, inflow]
