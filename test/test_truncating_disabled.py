# -*- coding:utf-8 -*-

import ng_exceptions
ng_exceptions.hook()
ng_exceptions.MAX_LENGTH = None

def div():
    var = "9" * 150
    return 1 / var


div()
