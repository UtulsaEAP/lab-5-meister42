"""
Name: Henry Holman
Lab Time: Thursday 2pm


"""



def fibonacci(start_num):
    #write your code here
    old = 0
    now = 1
    new = 0
    fiblist = [0, 1]
    i = 0
    for i in range(0, start_num):
        new = old + now
        old = now
        now = new
        fiblist.append(new)
        i += 1

    fibonum = fiblist[start_num]
    return fibonum
    



if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')