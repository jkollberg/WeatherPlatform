# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:37:38 2021

@author: Johan
"""

from api import smhi_api

api = smhi_api()
 
api.parameters = api._GetParameters()
api.forecast = api._GetPointForecast(57.005,12.432)

api.referenceTime = api.forecast['referenceTime']

params,cols = api.parseParams()

df = api.parseForecast()