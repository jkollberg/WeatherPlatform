# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 09:58:44 2021

@author: Johan
"""

import matplotlib.pyplot as plt

def plot_HumidTemp(df_in, hours):
    """
    Parameters
    ----------
    df : DataFrame with datetime as index (UTC format)
    hours: How many hours ahead do we want to plot.

    """
    
    # Getting only interested times, and saving in DataFrame.
    delta = df_in.index[hours] - df_in.index[0]  
    df = df_in.loc[df_in.index[0]:(df_in.index[0]+delta),:]
    
    
    
    fig, ax = plt.subplots(nrows = 3, ncols = 1, figsize=(7,9))
    
    plt.subplot(3,1,1)
    plt.plot(df['t'], 'r', label = 'Temperature (C)')
    plt.legend()
    
    plt.subplot(3,1,2)
    plt.plot(df['r'], 'c', label = 'Relative Humidity (%)')
    plt.legend()
    
    plt.subplot(3,1,3)
    plt.plot(df['pmean'], 'b', label = 'Mean Percipitation (mm/h)')
    plt.legend()
    
    # plt.xticks(rotation=30)
    # plt.plot(df.r)
    # plt.plot(df.t)
    
    
    return 