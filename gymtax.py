#!/usr/bin/env python
#
# This file is part of GymTax.
#
# See file LICENCE or go to http://www.gnu.org/licenses/ for full
# license details.
#
# GymTax is a scripting language interpreter for gym sessions to turn
# your devices into your personal trainer.
#
# Copyright (c) 2016 Gabriele N. Tornetta <phoenix1987@gmail.com>.
# All rights reserved.
#
# GymTax is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GymTax is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GymTax.  If not, see <http://www.gnu.org/licenses/>.

from argparse import ArgumentParser as ArgParse
from lib.session import SessionBuilder

def parse_args():
    p = ArgParse(description="GymTax scripting language for timed gym sessions.")

    p.add_argument('-v', action='store_true', help="Verbose mode. Print text on screen along with speech.")
    p.add_argument('-d', action='store_true', help="Dry run. Used for syntax checking and for returning session statistics like, e.g., the estimated duration.")
    p.add_argument('script', help="the (relative) path to the script to run.")

    return p.parse_args()

if __name__ == "__main__":
    gt = SessionBuilder(parse_args())
    gt.start()
