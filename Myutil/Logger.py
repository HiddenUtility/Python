# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""

from __future__ import annotations
import abc
from typing import Final
from datetime import datetime
from pathlib import Path
import hashlib


####//Interface
class InterfaceLogMaker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, other: object) -> None:
        raise NotImplementedError()
    @abc.abstractmethod
    def out(self, other: object) -> None:
        raise NotImplementedError()
        
####//ParentClass
class Logger(InterfaceLogMaker):
    LOG_NAME:Final = "ProcessLog"
    name: str
    dst: Path
    logs: list[LogData]
    def __init__(self,dst:Path = None, name=""):
        self.dst = dst if dst is not None else Path()
        self.name = self.LOG_NAME if name=="" else name
        self.logs=[]
        
    def write(self, *args: str, debug=False) -> None:
        data = LogData(*args)
        if debug: print(data)
        self.logs.append(data)
        
    def out(self):
        logs = sorted(self.logs)
        filepath = self.dst.parent.joinpath(f"{self.name}.txt")
        with open(filepath, "w") as f:
            [f.write("%s\n" % log) for log in logs]

        
class LogData:
    def __init__(self, *args: str):
        self.datas = [str(v) for v in args]
        self.now = datetime.now()
    def __hash__(self):
        return hash(self._out_log())
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self._out_log()
    def __lt__(self, other):
        if not isinstance(other, LogData):raise TypeError
        return self.now < other.now
    def _timestamp(self):
        return self.now.strftime("%Y/%m/%d %H:%M:%S.%f")
    def _out_log(self):
        return self._timestamp() + ": " + "_".join(self.datas)
    def get_hash(self):
        return hashlib.md5(self._out_log().encode()).hexdigest()
    
    
if __name__ == '__main__':
    
    logmaker = Logger(name="TEST")
    for i in range(10):
        logmaker.write(str(1))
    
    logmaker.out()