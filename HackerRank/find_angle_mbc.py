from math import degrees, atan2

AB, BC = float(input()), float((input()))
MBC = round(degrees(atan2(AB, BC)))
print((str(MBC)), chr(176), sep='')
