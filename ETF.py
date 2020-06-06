#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:04:14 2020

@author: jonathanbrooks
"""
'''
from airflow import DAG
import airflow
'''
#!/usr/bin/env python
import json
import pandas as pd
#webbrowser.open('https://inventwithpython.com/')

#response = requests.get("https://financialmodelingprep.com/developer/docs/")
#print(response.status_code)
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
To fix this, please verify that your firewall or antivirus allows Python processes to open ports in your system, or restart Spyder.    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/quotes/etf?apikey=8f326671b95132e9ba8198ded4d3f06a")
print(get_jsonparsed_data(url))
df = pd.DataFrame(get_jsonparsed_data(url))
#We only want the ETFS that have a positive percent change from the day before
df = df.query('changesPercentage > 0')

print(df)
df.to_excel("/users/jonathanbrooks/ETFS.xlsx",
             sheet_name='Sheet_name_1')  









