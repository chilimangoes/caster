#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

"""
Command-module for Notepad++

"""


#---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, MappingRule,
                       Dictation, IntegerRef, Mouse,
                       Key, Text, Repeat, Pause)
from caster.lib.dfplus.state.short import R

class CommandRule(MappingRule):

    mapping = {
            "next tab [<n>]":                       R(Key("c-pgdown") * Repeat(extra="n"), rdescript="Notepad++: Next Tab"),
            "prior tab [<n>]":                      R(Key("c-pgup") * Repeat(extra="n"), rdescript="Notepad++: Prior Tab"),
            "close tab [<n>]":                      R(Key("c-w") * Repeat(extra="n"), rdescript="Notepad++: Close Tab"),
            
            "stylize <n2>":                         R(Mouse("right")+Key("down:6/5, right")+(Key("down") * Repeat(extra="n2"))+Key("enter"), rdescript="Notepad++: Stylize"),
            "remove style":                         R(Mouse("right")+Key("down:6/5, right/5, down:5/5, enter"), rdescript="Notepad++: Remove Style"),
            
            "preview in browser":                   R(Key("cas-r"), rdescript="Notepad++: Preview In Browser"),
            # requires function list plug-in:
            "function list":                        R(Key("cas-l"), rdescript="Notepad++: Function List"),
        }
    extras = [
              Dictation("text"),
              IntegerRef("n", 1, 100),
              IntegerRef("n2", 1, 10),
              
             ]
    defaults = {"n": 1}

#---------------------------------------------------------------------------

context = AppContext(executable="notepad++")
grammar = Grammar("Notepad++", context=context)
grammar.add_rule(CommandRule())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
