from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):
    def init(self):
        self.env: Dict[str, Optional[Any]] = {}


dre = DynamicScope


def get_dynamic_re() -> DynamicScope:
    a = inspect.stack()
    print(a)
    dict = {}
    print("created dict :",dict)
    print("Type:", type(dict))
    for i in a:
        print("\n")
        print(i)
        print("LOCALS")
        print(i[0].f_locals.keys())
        print("FREEVARS")
        print(i[0].f_code.co_freevars)
        print("\n")

    # print("break")
    # for i in a:
    #    if(i==0):
    #        continue
    #    else:
    #        #if a.__contains__("abc"):
    #        #    print("THIS IS BAD")
    #        #else:
    #        print("keys of local vars")
    #        print(i[0].f_locals.keys())

    #        #b = list(i[0].f_code.co_freevars)
    #        #list(b)
    #        #enum = enumerate(b)
    #        #for i in enum:
    #        #    print("freevars")
    #        #    print(i[0].b.keys())
    #        #print(i[0].f_locals.keys())
    # print(a[0])

# get_dynamic_re()
