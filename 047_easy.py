import string
from collections import deque

def rotator(n):
    """Return a function which rotates a sequence N places to the right.
    If n is negative, rotate to the left.
    """
    def rotate(s):
        d = deque(s)
        d.rotate(n)
        return ''.join(d)
    return rotate

def caesar(cipher, shift=None):
    if shift is None:
        shift = 0
    shift %= 26

    r = rotator(shift)

    translation_table = string.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        r(string.ascii_lowercase) + r(string.ascii_uppercase))

    return cipher.translate(translation_table)

todays_cipher = """
Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h 
zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol 
thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk 
zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P 
tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk 
ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol 
cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt! 
Olsw! Olsw! P't ilpun ylwylzzlk!
"""

print caesar(todays_cipher, -19)
