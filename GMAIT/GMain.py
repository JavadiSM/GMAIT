import http.server  
import socketserver  
import webbrowser  
import os
from controller import *


class Constants:
    CODE_FUNC: dict = {
        0: end_program,         # function to exit the program
        1: regMul,              # function for regular multiplication
        2: regMulII,            # another regular multiplication function
        3: divGame,             # division game function
        4: divGameII,           # second division game function
        5: MixedArr,            # mixed array function
        6: MixedArrII,          # second mixed array function
        7: polyEval,            # polynomial evaluation function
        8: DetGame,             # determinant game function
        9: EigenValGame,        # eigenvalue game function
        10: DiscGame,           # discrete game function
        11: rootGame,           # root game function
        12: PFD,                # partial fraction decomposition function
        13: IntegralGame,       # integral game function
        14: regMulDig,          # regular multiplication (digital) function
        15: FourierSeries,      # Fourier series function
        16: EquationSystem,     # equation system function
        17: Mean,               # mean calculation function
        18: Stdev,              # standard deviation function
        19: diffeq,             # differential equation function
        20: PolyDet,            # polynomial determinant function
        21: PolyDetFourier,     # polynomial determinant with Fourier series function
        22: curvatureGame,      # curvature game function
        23: TGame,              # T game function
        24: LineIntegralGame,   # line integral game function
        25: DiverganceGame,     # divergence game function
        26: LineIntegralSc      # line integral with scalar function
    }
