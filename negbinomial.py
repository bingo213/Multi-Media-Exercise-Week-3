import math

# Hàm factorial(n) tính n!
def factorial(n):
    res = 1
    if n == 1:
        return 1
    for i in range (1,n+1):
        res *= i
    return res


'''hàm prob(n, p, N) tính xác suất của phân bố negative binomial
   3 tham số đầu vào: n - số lần thực hiện
                      p - xác suất thành công
                      r - số lần thành công
'''
def prob(n, p, r):
    return factorial(n-1)/(factorial(r-1)*factorial(n-r)) * p**r * (1-p)**(n-r)
print(prob(20, 0.6, 5))


'''Hàm infoMeasure(n, p) tính lượng tin có các symbols theo phân bố negative binomial
   3 tham số đầu vào: n - số lần thực hiện
                      p - xác suất thành công
                      r - số lần thành công
'''
def infoMeasure(n, p, r):
    return -math.log(prob(n, p, r), 2)


''' Hàm sumProb(n,p) tính giá trị tổng xác suất của các symbol từ 1 đến n
    cho nguồn có các symbol theo phân bố negative binomial
'''
def sumProb(n, p, r):
    s = 0.0
    for i in range (1,n+1):
        s += prob(i, p, r)
    return s


'''Hàm approxEntropy(n, p) tính giá trị trung bình lượng tin
   của tất cả symbol từ 1 đến n
'''
def approxEntropy(n, p, r):
    sum = 0.0
    for i in range (1, n+1):
        sum += infoMeasure(i, p, r)
    return sum/n