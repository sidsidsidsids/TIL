
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        ans = num1 / num2
    except:
        ans = '0으로 나눌 수 없습니다.'
    return ans
    