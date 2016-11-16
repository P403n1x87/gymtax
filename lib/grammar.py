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

gymtax = r"""
session                       = _ "session" _ string _ (phase _)+ "start" _

  phase                       = "enter" _ ( ( ( warmup / activity / cooldown ) _ (event _)+ ) / ( circuits ( ( circuits_run / event ) _)+ ) )

    warmup                    = "warmup"

    activity                  = "activity"

    cooldown                  = "cooldown"

    circuits                  = "circuits" _ circuits_mode? _ (station _)+

      circuits_mode           = "rotate" / "per station"

      station                 = "station" _ card+

        card                  = string _

    circuits_run              = "run" _ natural*

    event                     = _ (exercise / rest / announce) _

      exercise                = _ "exercise" _ string _ duration? _

      rest                    = _ "rest" _ duration? _

      announce                = _ "announce" _ string _ duration? _

string                        = "'" char "'"

  char                        = ~"[^']*"i

duration                      = ( mins? _ secs? ) / "default"

  mins                        = (natural "m")

  secs                        = (natural "s")

natural                       = ~"[0-9]+"i

_                             = ~"\s*"
"""
