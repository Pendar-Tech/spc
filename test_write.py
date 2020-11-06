#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals, print_function, division
import os
import spc

tfile = 0
tpass = 0

dpath = os.path.join(os.path.dirname(__file__), 'test_data')
mfile = []
rfile = []
lfile = []
for filename in os.listdir(dpath):
    if filename[-3:].lower() == 'spc':
        tfile += 1
        print(filename)
        f1 = spc.File(os.path.join(dpath, filename))

        outfile = os.path.join(dpath, 'spc2', filename + '.spc')
        f1.write_spc(outfile)

        # now, try loading and comparing
        f2 = spc.File(outfile)

        if f1.data_txt() == f2.data_txt():
            print("Pass\n------")
            tpass += 1
        else:
            print("Fail\n------")
            mfile.append(filename)
print("Passed %i of %i tests. " % (tpass, tfile))
print("Did not match ref file: ", mfile)
print("Did not have ref file: ", rfile)
print("Did not load file: ", lfile)
