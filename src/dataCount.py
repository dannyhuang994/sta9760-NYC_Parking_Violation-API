from requests import get, HTTPError
from sodapy import Socrata
import os

# API_BASE = 'data.cityofnewyork.us'
# END_POINT = 'nc67-uf89'
# APP_KEY = os.environ.get('APP_KEY')

def get_size(API_BASE, END_POINT, APP_KEY ):
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
