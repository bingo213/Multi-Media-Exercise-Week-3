import math

'''hàm prob(n, p) tính xác suất của phân bố geometric ứng vói symbol X = n
   2 tham số đầu vào: n - số lần thực hiện
                      p - xác suất thành công
'''
def prob(n, p):
    return (1-p)**(n-1) * p


'''Hàm infoMeasure(n, p) tính lượng tin có các symbols theo phân bố geometric 
   ứng với symbol X = n
   2 tham số đầu vào: n - số lần thực hiện
                      p - xác suất thành công
'''
def infoMeasure(n, p):
    return -math.log(prob(n,p), 2)


''' Hàm sumProb(n,p) tính giá trị tổng xác suất của các symbol từ 1 đến n
    cho nguồn có các symbol theo phân bố geometric
    Khi tăng giá trị của n lên thì giá trị trả về của hàm sumProb dần tiến đến 1.
'''
def sumProb(n, p):
    s = 0.0
    for i in range (1,n+1):
        s += prob(i, p)
    return s


'''Hàm approxEntropy(n, p) tính giá trị trung bình lượng tin
   của tất cả symbol từ 1 đến n
'''
def approxEntropy(n, p):
    sum = 0.0
    for i in range (1, n+1):
        sum += infoMeasure(i, p)
    return sum/n

