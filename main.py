from src.api import get_data
from sys import argv
import argparse

if __name__=='__main__':
    # Construct the argument parser to get argument from command line
    ap = argparse.ArgumentParser()
    ap.add_argument("--page_size", type=int, default=None)
    ap.add_argument("--num_pages", type=int, default=None)
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    page_size, num_pages, output_fn = args.page_size, args.num_pages, args.output

    if page_size is None:
        print('Page size should be specified!')
        exit()

    get_data(page_size, num_pages, output_fn)

