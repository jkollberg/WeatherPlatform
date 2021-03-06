# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:37:38 2021

@author: Johan
"""

import matplotlib.pyplot as plt

from api import smhi_api
from utils import plot_HumidTemp

api = smhi_api()
 
api.parameters = api._GetParameters()
api.forecast = api._GetPointForecast(57.71,11.95)

api.referenceTime = api.forecast['referenceTime']

params,cols = api.parseParams()

df = api.parseForecast()

# %% Plotting- and Post Processing

plot_HumidTemp(df,48)