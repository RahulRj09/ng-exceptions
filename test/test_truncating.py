# -*- coding:utf-8 -*-

import ng_exceptions
ng_exceptions.hook()
ng_exceptions.MAX_LENGTH = 10

def div():
    var = "9" * 150
    return 1 / var


div()
