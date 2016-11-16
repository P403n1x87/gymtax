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

import sys
import session

from phonetic import Phonetic

class Phase(Phonetic):
    def __init__(self, desc = None):
        if sys.version_info.major == 3:
            super().__init__("Entering " + ("a new phase" if desc == None else desc) )
        else:
            super(Phase, self).__init__("Entering " + ("a new phase" if desc == None else desc) )

        #self._evt_list = []
        self.midway = False
        self.countdown = 0

    def add_events(self, evt_list):
        #self._evt_list += evt_list
        self += evt_list

    def alter_session(self):
        session.midway = self.midway
        session.countdown = self.countdown

    def do(self):
        self.alter_session()
        self.speak()
        session.sleep(3)
        for evt in self:
            evt.do()

    #def __iter__(self):
    #    return iter(self._evt_list)

class WarmUp(Phase):
    def __init__(self):
        if sys.version_info.major == 3:
            super().__init__("warm up")
        else:
            super(WarmUp, self).__init__("warm up")

        self.midway = False
        self.countdown = 0

class Activity(Phase):
    def __init__(self):
        if sys.version_info.major == 3:
            super().__init__("activity")
        else:
            super(Activity, self).__init__("activity")

        self.midway = True
        self.countdown = 5

class CoolDown(Phase):
    def __init__(self):
        if sys.version_info.major == 3:
            super().__init__("cool down")
        else:
            super(CoolDown, self).__init__("cool down")

        self.midway = False
        self.countdown = 0
