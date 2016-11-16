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

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

from phase import *
from event import *
from grammar import gymtax
from circuits import *

import time
import phonetic

midway        = False
countdown     = 0
phs_list      = []
duration      = 60
rest          = 15
tot_duration  = 0

sleep = time.sleep

def add_phases(phase_list):
    global phs_list
    phs_list += phase_list

def get_phases():
    global phs_list
    return phs_list

def fmt_tot_duration():
    global tot_duration

    m, s = divmod(tot_duration, 60)
    h, m = divmod(m, 60)

    return ("%dh" % h if h > 0 else "") + ("% 2dm" % m if m > 0 else "") + ("% 2ds" % s if s > 0 or (h + m == 0) else "")

class SessionBuilder(NodeVisitor):
    def __init__(self, args):
        self._args = args

        self.dur           = None
        self.phase         = None
        self.dur_list      = []
        self.str_list      = []
        self.evt_list      = []
        self.phs_list      = []
        self.num_list      = []
        self.crd_list      = []
        self.sta_list      = []
        self.circuits      = None
        self.circuits_mode = None

        self.grammar = Grammar(gymtax)

        with open(self._args.script) as fin:
            self.parse(fin.read().lower())

    def start(self):
        global sleep

        if self._args.d:
            sleep = lambda x: None
            phonetic.droid = phonetic.espeak = phonetic.verbose = None

        if self._args.v:
            phonetic.verbose = True

        for phs in get_phases():
            phs.do()

        print "Session '{}' terminated. Estimated total duration: {}".format(self.str_list.pop(), fmt_tot_duration())

    def get_duration(self):
        global duration

        return self.dur_list.pop() if self.dur_list else duration

    def get_rest(self):
        global rest

        return self.dur_list.pop() if self.dur_list else rest

    def default_phase_factory(self, phs):
        self.phase = phs()

    def visit_char(self, n, vc):
        self.str_list.append(n.text)

    def visit_natural(self, n, vc):
        self.num_list.append( int(n.text) )

    def visit_secs(self, n, vc):
        self.dur = int(self.num_list.pop()) + (0 if self.dur == None else self.dur)

    def visit_mins(self, n, vc):
        self.dur = int(self.num_list.pop()) * 60 + (0 if self.dur == None else self.dur)

    def visit_duration(self, n, vc):
        if self.dur != None:
            self.dur_list.append(self.dur)
            self.dur = None

    def visit_exercise(self, n, vc):
        self.evt_list.append( Exercise(self.str_list.pop(), self.get_duration()) )

    def visit_rest(self, n, vc):
        self.evt_list.append( Rest(self.get_rest()) )

    def visit_announce(self, n, vc):
        self.evt_list.append( Announce(self.str_list.pop(), self.get_duration()) )

    def visit_warmup(self, n, vc):
        self.phase = WarmUp()

    def visit_activity(self, n, vc):
        self.phase = Activity()

    def visit_cooldown(self, n, vc):
        self.phase = CoolDown()

    def visit_circuits_mode(self, n, vc):
        self.circuits_mode = CircuitsMode[n.text]

    def visit_card(self, n, vc):
        self.crd_list.append(self.str_list.pop())

    def visit_station(self, n, vc):
        self.sta_list.append(Station(self.crd_list))
        self.crd_list = []

    def visit_circuits(self, n, vc):
        self.phase = Circuits(self.circuits_mode, self.sta_list)
        #self.cir_list.append(self.phase)
        self.sta_list      = []
        self.circuits_mode = None

    def visit_circuits_run(self, n, vc):
        self.evt_list.append(CircuitsRunner(self.phase, self.num_list.pop() if self.num_list else 0) )

    def visit_phase(self, n, vc):
        self.phase.add_events(self.evt_list)
        self.evt_list = []
        self.phs_list.append(self.phase)
        self.phase = None

    def visit_session(self, n, vc):
        add_phases(self.phs_list)

    def generic_visit(self, n, vc):
        pass
