#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""TC77: Serially accessible digital temperature sensor particularly suited for low cost and small form-factor applications."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Microchip"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from TC77_constants import *

# name:        TC77
# description: Serially accessible digital temperature sensor particularly suited for low cost and small form-factor applications.
# manuf:       Microchip
# version:     0.1
# url:         http://ww1.microchip.com/downloads/en/DeviceDoc/20092B.pdf
# date:        2016-08-17


# Derive from this class and implement read and write
class TC77_Base:
	"""Serially accessible digital temperature sensor particularly suited for low cost and small form-factor applications."""
	# Register CONFIG
	# Select either Shutdown, Continuous Conversion or Test modes: 
	
	def setCONFIG(self, val):
		"""Set register CONFIG"""
		self.write(REG.CONFIG, val, 16)
	
	def getCONFIG(self):
		"""Get register CONFIG"""
		return self.read(REG.CONFIG, 16)
	
	# Bits CONFIG
	# Register TEMP
	# holds the temperature conversion data. 
	
	def setTEMP(self, val):
		"""Set register TEMP"""
		self.write(REG.TEMP, val, 16)
	
	def getTEMP(self):
		"""Get register TEMP"""
		return self.read(REG.TEMP, 16)
	
	# Bits TEMP
	# the 13 bit tws complement data from the temperature conversion 
	# Bits FLAG_COMPLETE
	# Bit 2 is set to a logic1 after
	#           completion of the first temperature conversion following a power-up or reset event.
	#           Bit 2 is set to a logic 0 during the time needed to complete the first
	#           temperature conversion. Therefore, the status of bit 2 can be monitored to indicate
	#           that the TC77 has completed the first temperature conversion. 
	
	# Bits unused_0
	# Bits 0 and 1 are undefined and will be tri-state outputs during a read sequence. 
	# Register M_ID
	# Manufacture's identification code 
	
	def setM_ID(self, val):
		"""Set register M_ID"""
		self.write(REG.M_ID, val, 16)
	
	def getM_ID(self):
		"""Get register M_ID"""
		return self.read(REG.M_ID, 16)
	
	# Bits ID
	# Bits unused_0
	# bits 7:2 are set to0 
	# Bits unused_1
	# Bits 1:0 are undefined and will be tri- state outputs during a read sequence 
