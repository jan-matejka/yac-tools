#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

BORDER=2
border = "+".join(["-" * (i+BORDER) for i in [BORDER*-1,8,2,3,BORDER*-1]])

print border
for i in range(0,2**8):
    print "| {0:8b} | {0:2x} | {0:3d} |".format(i)
print border
