import math
import decimal
from decimal import Decimal as d #dùng decimal thay cho float để tính toán chính xác hơn

# Hàm factorial(n) tính n!
def factorial(n):
    res = d('1')
    if n == 1 or n == 0:
        return 1
    for i in range (1,n+1):
        res *= d(str(i))
    return res


'''hàm prob(n, p, N) tính xác suất của phân bố binomial
   3 tham số đầu vào: n - số lần thành công
                      p - xác suất thành công
                      N - số lần thực hiện
'''
def prob(n, p, N):
    return factorial(N)/(factorial(N-n)*factorial(n)) * d(str(p))**d(str(n)) * d(str((1-p)))**d(str((N-n)))


'''Hàm infoMeasure(n, p) tính lượng tin có các symbols theo phân bố binomial
   3 tham số đầu vào: n - số lần thành công
                      p - xác suất thành công
                      N - số lần thực hiện
'''
def infoMeasure(n, p, N):
    return -d(str(math.log2(prob(n, p, N))))


''' Hàm sumProb(N,p) tính giá trị tổng xác suất của các symbol từ 0 đến N
    cho nguồn có các symbol theo phân bố binomial
    với N là tổng số phép thử
'''
def sumProb(N, p):
    s = d('0')
    for i in range (0,N+1):
        s += prob(i, p, N)
    return s


'''Hàm approxEntropy(N, p) tính giá trị trung bình lượng tin
   của tất cả symbol từ 0 đến N
   với N là tổng số phép thử
'''
def approxEntropy(N, p):
    sum = d('0')
    for i in range (0, N+1):
        sum += (infoMeasure(i, p, N) * prob(i, p, N))
    return sum