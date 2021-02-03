# from trigonometry.my_math import sin, cos

from trigonometry import sin, cos


def proove_pifagor():
    list1 = [0.01, 0.02, -0.01, -0.02]
    print([sin(x)**2 + cos(x)**2 for x in list1])


proove_pifagor()

