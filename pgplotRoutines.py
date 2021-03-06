# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:09:54 2020

@author: Seo
"""


import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtCore import Qt
import numpy as np

def pgPlotDeltaFuncs(fig, x, h, color='r', symbol=None):
    '''
    Adds delta function dashed lines to the specified pyqtgraph plot.

    Parameters
    ----------
    fig : PyQtgraph figure.
        
    x : List of x values where the delta functions should be plotted
        
    h : Height of the delta functions to be plotted.
        

    Returns
    -------
    None.

    '''
    for i in range(len(x)):
        if h[i] != 0:
            fig.plot([x[i],x[i]], [0, h[i]], pen=pg.mkPen(color=color, style=Qt.DashLine))
        if symbol is not None:
            fig.plot([x[i]], [h[i]], symbol=symbol, symbolPen=color)
        
def pgPlotSurface(x, y, z, shader='normalColor', autoscale=True, title=None):
    '''
    Adds a new window with a surface plot and a grid item.
    
    Returns
    w = view widget item
    g = grid item
    p = plot item
    '''
    
    # win = pg.GraphicsWindow()
    w = gl.GLViewWidget()
    w.show()
    w.setWindowTitle(title)
    
    g = gl.GLGridItem()
    
    if autoscale == True:
        sx = np.max(np.abs(x))
        sy = np.max(np.abs(y))
        g.scale(sx,sy,1)
        
        w.setCameraPosition(distance=np.max([sx,sy]) * 2)
        
    g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
    w.addItem(g)
    
    p = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader=shader)
    w.addItem(p)
    
    return w, g, p