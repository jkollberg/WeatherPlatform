# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 11:53:02 2021

@author: Johan
"""

import requests
import pandas as pd

class smhi_api:
    def __init__(self):
        self.entrypoint = 'https://opendata-download-metfcst.smhi.se'
        
    def _GetPointForecast(self, lat, lon):
        self.endpoint = '/api/category/pmp3g/version/2/geotype/point/lon/' + str(lon) + '/lat/' + str(lat) + '/data.json'
            
        response = requests.get(self.entrypoint + self.endpoint)
        # Add error handling, use response to check [200]               

        self.forecast = response.json()
        return self.forecast
 
        
    def _GetParameters(self):
        self.endpoint = '/api/category/pmp3g/version/2/parameter.json'
        
        response = requests.get(self.entrypoint + self.endpoint)        
        # Add error handling, use response to check [200]
        
        self.parameters = response.json()
        return self.parameters
    
    def parseParams(self):
        """
        Returns...
            1: dataframe of parameters as is.
            2: list of parameter labels (column headers)
        """        
        
        df_params = pd.json_normalize(self.parameters['parameter'])
        list_params = [parameter['name'] for parameter in self.parameters['parameter']]        
        
        return df_params, list_params
    
    def parseForecast(self):
        """
        Returns...
            Dataframe of prased response.
        """
        params = ['time','pcat','pmean','t','wd','ws','r']
        df = pd.DataFrame(columns = params)
        
        new_row = {'pcat': 999, 'pmean':999, 't': 999, 'wd':999, 'ws':999, 'r':999}
        
        df['time'] = pd.to_datetime(df['time'])
        df.set_index('time', inplace=True)
        
        for houritem in self.forecast['timeSeries']:
            time = houritem['validTime']
            new_row['time'] = time
                
            for item in houritem['parameters']:
                name = item['name']
                values = item['values'][0]
                
                # unit = item['unit']
                # level = item['level']
                # levelType = item['levelType']
                
                if name in params:
                    new_row[name] = values
                                                 
            
            df = df.append(new_row,ignore_index=True)
            df[['pmean','t','wd','ws','r']] = df[['pmean','t','wd','ws','r']].astype('float')
            
        df['time'] = pd.to_datetime(df['time'],format="%Y-%m-%dT%H:%M:%SZ")
        df.set_index('time',inplace=True)
            
        return df