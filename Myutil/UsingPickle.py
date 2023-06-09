# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:28:28 2023

@author: nanik
"""

import pikle
from pathlib import Path
class UsingPickle:
    
    @staticmethod
    def load(filepath: Path)-> object:
        with open(filepath, "rb") as f:
            obj = pikle.load(f)
        return obj
    
    @staticmethod
    def dump(filepath: Path, obj: object)-> None:
        with open(filepath, "wb") as f:
            pikle.dump(obj, f)
