# -*- coding:utf-8 -*-

import ng_exceptions
ng_exceptions.hook()

code = """
if True:
    a = 5
    b = 7 *
"""

exec(code)
