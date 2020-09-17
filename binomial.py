import math

# Hàm factorial(n) tính n!
def factorial(n):
    res = 1
    if n == 1:
        return 1
    for i in range (1,n+1):
        res *= i
    return res


'''hàm prob(n, p, N) tính xác suất của phân bố binomial
   3 tham số đầu vào: n - số lần thành công
                      p - xác suất thành công
                      N - số lần thực hiện
'''
def prob(n, p, N):
    return factorial(N)/(factorial(N-n)*factorial(n)) * p**n * (1-p)**(N-n)


'''Hàm infoMeasure(n, p) tính lượng tin có các symbols theo phân bố binomial
   3 tham số đầu vào: n - số lần thành công
                      p - xác suất thành công
                      N - số lần thực hiện
'''
def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)


''' Hàm sumProb(n,p) tính giá trị tổng xác suất của các symbol từ 1 đến n
    cho nguồn có các symbol theo phân bố binomial
'''
def sumProb(n, p, N):
    s = 0.0
    for i in range (1,n+1):
        s += prob(i, p, N)
    return s


'''Hàm approxEntropy(n, p) tính giá trị trung bình lượng tin
   của tất cả symbol từ 1 đến N
'''
def approxEntropy(n, p, N):
    sum = 0.0
    for i in range (1, n+1):
        sum += infoMeasure(i, p, N)
    return sum/N