#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2015, Matthew Brennan Jones <matthew.brennan.jones@gmail.com>
# emu_archive is a HTML based front end for video game console emulators
# It uses a MIT style license
# It is hosted at: https://github.com/workhorsy/emu_archive
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os, sys

import ini
import emu_runner
import base_console


class PCSXR(base_console.BaseConsole):
	def __init__(self):
		super(PCSXR, self).__init__('config/pcsxr.json')

	def is_installed(self):
		return os.path.isdir('emulators/pcsxr/')

	def run(self, path, binary):
		os.chdir("emulators/pcsxr/")

		# Figure out if running a game or not
		command = None
		full_screen = False
		if path and binary:
			game_path = self.goodJoin('../../', path + '/' + binary)
			command = '"pcsxr.exe" -nogui -cdfile "' + game_path + '"'
			full_screen = True
		else:
			command = '"pcsxr.exe"'
			full_screen = False

		# Run the game
		runner = emu_runner.EmuRunner(command, 'PCSXR', full_screen, full_screen_alt_enter=True)
		runner.run()
		os.chdir("../..")
