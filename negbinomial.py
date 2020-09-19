import math
import decimal
from decimal import Decimal as d

# Hàm factorial(n) tính n!
def factorial(n):
    res = d('1')
    if n == 1 or n == 0:
        return 1
    for i in range (1,n+1):
        res *= d(str(i))
    return res


'''hàm prob(n, p, r) tính xác suất của phân bố negative binomial
   3 tham số đầu vào: n - symbol đang cần tính xác suất
                      p - xác suất thành công
                      r - số lần thành công
'''
def prob(n, p, r):
    if n < r:
        return 0
    return factorial(n-1)/(factorial(r-1)*factorial(n-r)) * d(str(p))**d(str(r)) * d(str((1-p)))**d(str((n-r)))


'''Hàm infoMeasure(n, p) tính lượng tin có các symbols theo phân bố negative binomial
   3 tham số đầu vào: n - số lần thực hiện
                      p - xác suất thành công
                      r - số lần thành công
'''
def infoMeasure(n, p, r):
    if n < r:
        return 0
    return -d(str(math.log(prob(n, p, r), 2)))


''' Hàm sumProb(n,p) tính giá trị tổng xác suất của các symbol từ r đến N
    cho nguồn có các symbol theo phân bố negative binomial
    với N là tổng số phép thử
'''
def sumProb(N, p, r):
    s = d('0')
    for i in range (r,N+1):
        s += prob(i, p, r)
    return s
    

'''Hàm approxEntropy(N, p, r) tính giá trị trung bình lượng tin
   của tất cả symbol từ r đến N
'''
def approxEntropy(N, p, r):
    sum = d('0')
    for i in range (r, N+1):
        sum += infoMeasure(i, p, r) * prob(i, p, r)
    return sum
print(approxEntropy(400, 0.2, 10))
