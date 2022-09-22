from Dyanmic_Scope import get_dynamic_re
from typing import Any
import unittest


class UnitTests(unittest.TestCase):


    def test_skeleton_example(self):
        def outer():
            a = "outer_a"
            b = "outer_b"
            c = "outer_c"
            d = "outer_d"
            e = "outer_e"

            def inner1():
                a = "inner1_a"
                b = "inner1_b"
                return inner3("parameter1_d")

            def inner2():
                a = "inner2_a"
                b = "inner2_b"
                return inner3("parameter2_d")

            def inner3(d: Any):
                e = "inner3_e"
                get_dynamic_re()

            dre = inner1()
            self.assertEquals(
                dre["a"], "inner1_a", "Your reference environment had the incorrect value for a variable.")
            self.assertEquals(
                dre["d"], "parameter1_d", "Your reference environment had the incorrect value for a variable.")
            self.assertEquals(
                dre["e"], "inner3_e", "Your reference environment had the incorrect value for a variable.")
            dre = inner2()
            self.assertEquals(
                dre["a"], "inner2_a", "Your reference environment had the incorrect value for a variable.")
            self.assertEquals(
                dre["d"], "parameter2_d", "Your reference environment had the incorrect value for a variable.")
            self.assertEquals(
                dre["e"], "inner3_e", "Your reference environment had the incorrect value for a variable.")
            return inner3
        a = "module_a"
        b = "module_b"
        c = "module_c"
        inner3_ref = outer()
        dre = inner3_ref("module_parameter_d")
        self.assertEquals(
            dre["a"], "module_a", "Your reference environment had the incorrect value for a variable.")
        self.assertEquals(
            dre["b"], "module_b", "Your reference environment had the incorrect value for a variable.")
        self.assertEquals(
            dre["c"], "module_c", "Your reference environment had the incorrect value for a variable.")
        self.assertEquals(dre["d"], "module_parameter_d",
                          "Your reference environment had the incorrect value for a variable.")
        self.assertEquals(
            dre["e"], "inner3_e", "Your reference environment had the incorrect value for a variable.")

