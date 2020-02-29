from requests import get, HTTPError
from sodapy import Socrata
import os

API_BASE = 'data.cityofnewyork.us'
END_POINT = 'nc67-uf89'
APP_KEY = os.environ.get('APP_KEY')

def get_size():
    '''get the number of data point in api'''
    try:
        client = Socrata(API_BASE, APP_KEY)
        return int(client.get(END_POINT, select = 'count(*)')[0]['count'])
    except HTTPError as e:
        print(f'Check Your API TOKEN: {e}')
        raise
    except Exception as e:
        print(f'Something Went Wrong: {e}')
        raise


def get_data(page_size: int, num_pages: int, output_fn = None):
    ''' this gets the data from API,
        either saving the data into output_fn or printing out when output_fn is not provided.
        it takes two required arguments: page_size and num_pages
        and one optional argument: output_fn '''
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
                print(r)
        else:
            with open(output_fn, 'w') as fw:
                for i in range(num_pages):
                    r = client.get(END_POINT, limit = page_size, offset = i*page_size)
                    fw.write( str(r)+'\n')
    except HTTPError as e:
        print(f'Something Went Wrong: {e}')
        raise

