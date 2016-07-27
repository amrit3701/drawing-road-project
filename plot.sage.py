# This file was *autogenerated* from the file plot.sage
from sage.all_cmdline import *   # import sage library
_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_10 = Integer(10); _sage_const_p1 = RealNumber('.1'); _sage_const_15 = Integer(15); _sage_const_0p9 = RealNumber('0.9'); _sage_const_p9 = RealNumber('.9')
import csv

temp = []
f = open('input.csv')
pointer = csv.reader(f, delimiter=',')
parsed = ((float(row[_sage_const_0 ]), float(row[_sage_const_1 ]))
            for row in pointer)
for i in parsed:
    temp.append(i)

a = []
f = open('output.csv')
pointer = csv.reader(f, delimiter=',')
parsed = ((float(row[_sage_const_0 ]), float(row[_sage_const_1 ]))
            for row in pointer)
for i in parsed:
    a.append(i)

b = []
f = open('output2.csv')
pointer = csv.reader(f, delimiter=',')
parsed = ((float(row[_sage_const_0 ]), float(row[_sage_const_1 ]))
            for row in pointer)
for i in parsed:
    b.append(i)

z1 = point(temp, color="red", size=_sage_const_10 , legend_label="input points")
#z2 = line(temp, color="red", thickness=2)

z3 = point(a, color="blue", size=_sage_const_5 , legend_label="distance points")
#z4 = line(a, color="blue", thickness=1)

z5 = point(b, color="black", size=_sage_const_15 , legend_label="section points")

z=z1+z3+z5
z.set_legend_options(back_color=(_sage_const_0p9 ,_sage_const_0p9 ,_sage_const_0p9 ), shadow=False, loc=(_sage_const_p1 ,_sage_const_p9 ))

z.save('plotting.png')