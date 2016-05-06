from math import *
#Importing library math to use function 'tan'
def polysum(n,s):
    '''
    input     n: number of sides of polygon
              s: length of each side                         
    return float number --> area + perimeter**2
    '''
    area = (0.25*n*(s**2))/(tan(pi/n))
    perimeter = n*s
    return round(area +(perimeter**2),4)