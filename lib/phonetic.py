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

droid  = None
espeak = None
verbose = False

try:
    import androidhelper as android
    droid = android.Android()

except:
    # import pyttsx
    #
    # try :
    #     espeak = pyttsx.init()
    #     espeak.setProperty('voice', 'en-scottish')
    #
    # except:
    #     espeak = None
    from subprocess import call

    class espeak():
        @staticmethod
        def say(what):
            call(["espeak", "-v", "en-scottish", '"{}"'.format(what)])

        @staticmethod
        def runAndWait():
            pass

class Phonetic(list):
    def __init__(self, what = ""):
        if sys.version_info.major == 3:
            super().__init__()
        else:
            super(Phonetic, self).__init__()

        self.speech = what

    @property
    def speech(self):
        return self._speech

    @speech.setter
    def speech(self, what):
        self._speech = what

    def speak(self, text = None):
        global espeak
        global verbose

        if verbose: # or (droid == None and espeak == None):
            print(self.speech if text is None else text)

        if droid:
            droid.ttsSpeak(self.speech if text is None else text)

        elif espeak:
            espeak.say(self.speech if text is None else text)
            espeak.runAndWait()
