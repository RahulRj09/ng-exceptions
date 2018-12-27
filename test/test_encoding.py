# -*- coding:utf-8 -*-

import ng_exceptions
ng_exceptions.hook()


def _deep(val):
    return 1 / val

def div():
    return _deep("天")


div()
