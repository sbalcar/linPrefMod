#!/usr/bin/python3

from userProfileModel.userProfileModel import UserProfileModel #class

from userProfileModel.model.prefFnc.prefFncs import PrefFncX #class
from userProfileModel.model.prefFnc.prefFncs import PrefFncY #class
from userProfileModel.model.aggrFnc.aggrFnc import AggrFnc #class

from geometry.point import Point #class


def getUserProfileModel01():
    idealX = 0.4
    idealY = 0.7
    prefFncX=PrefFncX([Point(0, 0), Point(idealX, 1), Point(1, 0)])
    prefFncY=PrefFncY([Point(0, 0), Point(1, idealY), Point(0, 1)])
    aggrFnc = AggrFnc([2,1])
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);


def getUserProfileModel02():
    idealX = 0.5
    idealY = 0.6
    prefFncX=PrefFncX([Point(0, 0), Point(idealX, 1), Point(1, 0)])
    prefFncY=PrefFncY([Point(0, 0), Point(1, idealY), Point(0, 1)])
    aggrFnc = AggrFnc([2,1])
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);

def getUserProfileModelExample01():
    idealX = 1.5
    idealY = 0.3
    prefFncX=PrefFncX([Point(0, 0), Point(idealX, 1), Point(2, 0)])
    prefFncY=PrefFncY([Point(0, 0), Point(1, idealY), Point(0, 1.25)])
    prefFncX=prefFncX.exportRefractedPrefFncX();
    prefFncY=prefFncY.exportRefractedPrefFncY();
    aggrFnc = AggrFnc([2,1])
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);



def getUserProfileModelExample02():
    idealX = 0.5
    idealY = 0.9
    prefFncX=PrefFncX([Point(0, 0), Point(idealX, 1), Point(2, 0)])
    prefFncY=PrefFncY([Point(0, 0), Point(1, idealY), Point(0, 1.25)])
    prefFncX=prefFncX.exportRefractedPrefFncX();
    prefFncY=prefFncY.exportRefractedPrefFncY();
    aggrFnc = AggrFnc([0.5, 1])
    return UserProfileModel(prefFncX, prefFncY, aggrFnc);

