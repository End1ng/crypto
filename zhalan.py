#!/usr/bin/env python
# -*- coding: utf-8 -*-


zlstr = "a o pcrcr6yteSoahTos ehaek,a:rcsht  on:@dgace.no aipl9 cr eepotr_b pFveoe{niur_deddwhahe hn kisf4taocy utuagewi vX1ooearim nvEw  mi Acmeudbbnftninofmeh}Se t 8eaimer"

for x in xrange(len(zlstr)/2):
    r = ""
    for xx in xrange(x+1):
        r += zlstr[xx::x+1]
    print r
