""" Game fix Dark Souls Prepare To Die Edition
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Needs WMP9, devenum, quartz, dinput and win7 """

    #For main menu, intro and outro playback
    util.protontricks('devenum')
    util.protontricks('quartz')
    util.protontricks("wmp9")

    #In case if someone wishes to use DSfix
    util.protontricks('dinput8')
    util.winedll_override('dinput8', 'n')

    util.protontricks('win7')
