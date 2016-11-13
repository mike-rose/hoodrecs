# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 15:19:01 2016

@author: Owner
"""
import requests
url='https://data.raleighnc.gov/resource/emea-ai2t.json?'
token= '$$app_token=nPun54jdIHWiqnKk7HUdQyDo1'
fullpath= url+token


crime = requests.get(fullpath)
if crime.status_code == 200:
    data = crime.json()
else:
    print(crime.status_code)


