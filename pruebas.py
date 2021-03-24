from galois_field import *
from galois_field.GF import GF, FFElement
from galois_field.fast_polynom import FastPolynom
import constant


irr_poly = FastPolynom({0: 1, 1: 1, 4: 1})
gfield = GF(2, m=4, irr=irr_poly)
e1 = FFElement(gfield, FastPolynom({0: 1, 1: 1}))
e2 = FFElement(gfield, FastPolynom({0: 1, 1: 1}))
e_res = e1 * e2
"""
for i in range(0, constant.Q)
    print(FFElement())
"""
import mymath

myGALOISFIELD = mymath.galoisField(2,4)


#ola.show_polinomials()
#print(gfield.__annotations__)
#print(FFElement.gen_one(gfield))
#print(FFElement(gfield,FastPolynom({4:1})))

print(FFElement(myGALOISFIELD.gfield, FastPolynom({1:1})).inverse())
