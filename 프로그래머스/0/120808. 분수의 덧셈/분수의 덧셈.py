import math
def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1*denom2+denom1*numer2
    denom3 = denom1*denom2
    math.gcd(numer3,denom3)
    answer = [numer3/math.gcd(numer3,denom3),denom3/math.gcd(numer3,denom3)]
    return answer