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

class Event(Phonetic):
    def __init__(self, desc = None, duration = None):
        if sys.version_info.major == 3:
            super().__init__()
        else:
            super(Event, self).__init__()

        self.desc = desc
        self.duration = duration
        self.midway = False
        self.countdown = 0

        session.tot_duration += 0 if self.duration == None else self.duration

    @property
    def duration(self):
        return self._dur

    @duration.setter
    def duration(self, value):
        self._dur = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    @property
    def midway(self):
        return self._midway

    @midway.setter
    def midway(self, value):
        self._midway = value

    @property
    def countdown(self):
        return self._countdown

    @countdown.setter
    def countdown(self, value):
        self._countdown = value

    def do(self):
        self.speak()
        session.sleep(self.duration)

class Exercise(Event):
    def __init__(self, desc, duration):
        if sys.version_info.major == 3:
            super().__init__(desc, duration)
        else:
            super(Exercise, self).__init__(desc, duration)

        self.speech = desc

    def do(self):
        self.speak()
        Rest(10)
        if session.midway and self.duration / 2 > session.countdown:
            self.speak("Go!")
            session.sleep(self.duration / 2.)
            self.speak("Halfway through. Keep pushing! Change side if you need to.")
            session.sleep(self.duration / 2. - self.countdown)
        else:
            session.sleep(self.duration - self.countdown)

        if session.countdown > 0:
            for i in range(session.countdown):
                self.speak(str(session.countdown - i))
                session.sleep(1)

class Rest(Event):
    def __init__(self, duration):
        if sys.version_info.major == 3:
            super().__init__("rest", duration)
        else:
            super(Rest, self).__init__("rest", duration)

class Announce(Event):
    def __init__(self, desc, duration):
        if sys.version_info.major == 3:
            super().__init__(desc, duration)
        else:
            super(Announce, self).__init__(desc, duration)

        self.speech = desc
