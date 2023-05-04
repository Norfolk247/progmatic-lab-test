def from10to3(num):
    res = 0
    i = 0
    while num > 0:
        res += (num % 3)*(10**i)
        i+=1
        num = num // 3
    return res

def brute():
    i = 0
    nums = []
    while i < 3**9:
        nums.append((9-len(str(from10to3(i))))*'0'+str(from10to3(i)))
        i+=1
    return nums

def check(nums):
    res = 0
    prev = '+9'
    for i in range(len(nums)):
        match nums[i]:
            case '0':
                prev += str(8-i)
            case '1':
                res += int(prev)
                prev = '-'+str(8-i)
            case '2':
                res += int(prev)
                prev = '+'+str(8-i)
    res += int(prev)
    if res == 200:
        return True
    return False

def answer(nums):
    res = '9'
    for i in range(9):
        match nums[i]:
            case '0':
                res += str(8-i)
            case '1':
                res = res + '-' + str(8-i)
            case '2':
                res = res + '+' + str(8-i)
    return res

for i in brute():
    if check(i):
        print(answer(i))