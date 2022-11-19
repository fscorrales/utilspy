#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: clcoding.com
Youtube source: https://youtu.be/Hn0lnCa8VzI
Purpose: Convert real time currency
Require package: forex_python
"""

import argparse

from forex_python.converter import CurrencyRates

# --------------------------------------------------
def get_args():
    """Get amount, from and to currency from user input"""
    parser = argparse.ArgumentParser(
        description = 'Convert real time currency',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'amount', 
        metavar = 'Amount',
        default = 1,
        help = "Amount to convert",
        type=float)

    parser.add_argument(
        'from_currency', 
        metavar = 'From', 
        default = None,
        help = "From currency",
        type = str)

    parser.add_argument(
        '-t', '--to_currency', 
        metavar = 'To', 
        default = 'USD',
        help = "To currency",
        type = str)

    return parser.parse_args()

# --------------------------------------------------
def convert_currency(amount: float, 
                        from_currency: str,
                        to_currency: str = 'USD'):
    """Convert pdf to tiff"""
    c = CurrencyRates()
    result = c.convert(base_cur = from_currency, dest_cur=to_currency, 
                amount=amount)
    return result
    #convert_currency('EUR', 'USD', 100)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    result = convert_currency(args.amount, 
                            args.from_currency, args.to_currency)
    print(f'${args.amount} {args.from_currency} = ${result} {args.to_currency}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python real_time_currency.py 100 'ARS'