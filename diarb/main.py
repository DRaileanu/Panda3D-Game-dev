#!/usr/bin/env python
"""
# Author: Dan Raileanu
# Last Updated: 10/28/2021
#
# This is an attempt to replicate time reversal functionality from Braid game
"""

from direct.showbase.ShowBase import ShowBase


class Diarb(ShowBase):
    def __init__(self):
        # Set up the window, camera, etc.
        ShowBase.__init__(self)
         # Set the background color to black
        self.win.setClearColor((0, 0, 0, 1))
        

app = Diarb()
app.run()