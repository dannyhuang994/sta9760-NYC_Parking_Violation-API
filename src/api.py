from requests import get, HTTPError
from sodapy import Socrata
from src.dataCount import get_size
import os

API_BASE = 'data.cityofnewyork.us'
END_POINT = 'nc67-uf89'
APP_KEY = os.environ.get('APP_KEY')

def get_data(page_size: int, num_pages = None, output_fn = None):
    ''' get the data from API,
        either save the data into output_fn or print when output_fn is not provided.
        when num_pages is not specified, we will continue reading data until the end of database'''
    if num_pages is None:
        total = get_size(API_BASE,END_POINT,APP_KEY )
        num_pages = (total // page_size) + 1

    try:
        client = Socrata(API_BASE, APP_KEY)
    except HTTPError as e:
        print(f'Check URL: {e}')
        raise
    except Exception as e:
        print(f'Something Went Wrong: {e}')
        raise

    try:
        if output_fn is None:
            for i in range(num_pages):
                r = client.get(END_POINT, limit = page_size, offset = i*page_size)
                for item in r:
                    print(item)
        else:
            with open(output_fn, 'w') as fw:
                for i in range(num_pages):
                    r = client.get(END_POINT, limit = page_size, offset = i*page_size)
                    for item in r:
                        fw.write( str(item)+'\n')
    except Exception as e:
        print(f'Something Went Wrong with: {e}')
        raise

