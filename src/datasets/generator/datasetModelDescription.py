#!/usr/bin/python3

from userProfileModel.model.prefFnc.prefFncRestriction import PrefFncRestriction #class


class DatasetModelDescription:

  # prefFncRestrs:list<PrefFncRestriction>
  def __init__(self, prefFncRestrs):
     if type(prefFncRestrs) is not list:
        raise ValueError("Argument prefFncRestrs isn't type list.")
     for prefFncRestrI in prefFncRestrs:
        if type(prefFncRestrI) is not PrefFncRestriction:
          raise ValueError("Argument prefFncRestrs don't contain PrefFncRestriction.")
     self.prefFncRestrs = prefFncRestrs

