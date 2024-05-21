# def find_max_multiple(number):
#     if number % 60 == 0:
#         return 576000  # 返回最大的倍数，也就是这个数本身
#     elif   number % 24 == 0:
#         return 230000
#     elif number % 12 == 0:
#         return 110000
#     elif number % 6 == 0:
#         return 57600
#     elif number % 3 == 0:
#         return 28800
#
#     else:
#         return 9600  # 如果不是60的倍数，返回None或其他标识值


def find_max_multiple(number):
    multiples = [60, 24, 12, 6, 3]
    for multiple in multiples:
        if number % multiple == 0:
            return multiple
    return None


def process_numbers():
    # 从键盘获取输入的数字，以空格分隔
    input_str = input("请输入一组用空格分隔的数字: ")
    # 将输入的字符串分割成数字列表
    numbers = list(map(int, input_str.split()))

    # 处理每个数字
    for num in numbers:
        # 用9600除之后向下取整
        floored_num = num // 9600 + 1
        # 判断是否是60、24、12、6或3的倍数，并返回最大倍数
        max_multiple = find_max_multiple(floored_num)
        if max_multiple == 60:
            maxtime = (floored_num * 9600 + 28800 - num) // 320 + 1
            normaltime = (floored_num * 9600 - num) // 320 + 1
            mintime = max((floored_num * 9600 - 28800 - num) // 320 + 1,0)
            print(f"数字 {num}，将要做57.6w维保,最晚要在{maxtime}天后做，正常应该在{normaltime}天后做，最早应该在{mintime}天后做")
        elif max_multiple == 24:
            maxtime = (floored_num * 9600 + 10000 - num) // 320 + 1
            normaltime = (floored_num * 9600 - num) // 320 + 1
            mintime = max((floored_num * 9600 - 10000 - num) // 320 + 1, 0)
            print(f"数字 {num}，将要做23w维保,最晚要在{maxtime}天后做，正常应该在{normaltime}天后做，最早应该在{mintime}天后做")
        elif max_multiple == 12:
            maxtime = (floored_num * 9600 + 5000 - num) // 320 + 1
            normaltime = (floored_num * 9600 - num) // 320 + 1
            mintime = max((floored_num * 9600 - 5000 - num) // 320 + 1, 0)
            print(f"数字 {num}，将要做11w维保,最晚要在{maxtime}天后做，正常应该在{normaltime}天后做，最早应该在{mintime}天后做")
        elif max_multiple == 6:
            maxtime = (floored_num * 9600 + 3000 - num) // 320 + 1
            normaltime = (floored_num * 9600 - num) // 320 + 1
            mintime = max((floored_num * 9600 - 3000 - num) // 320 + 1, 0)
            print(f"数字 {num}，将要做5.76w维保,最晚要在{maxtime}天后做，正常应该在{normaltime}天后做，最早应该在{mintime}天后做")
        elif max_multiple == 3:
            maxtime = (floored_num * 9600 + 2500 - num) // 320 + 1
            normaltime = (floored_num * 9600 - num) // 320 + 1
            mintime = max((floored_num * 9600 - 2500 - num) // 320 + 1, 0)
            print(f"数字 {num}，将要做2.88w维保,最晚要在{maxtime}天后做，正常应该在{normaltime}天后做，最早应该在{mintime}天后做")
        else:
            maxtime = (floored_num * 9600 + 1200 - num) // 320 + 1
            normaltime = (floored_num * 9600 - num) // 320 + 1
            mintime = max((floored_num * 9600 - 1200 - num) // 320 + 1, 0)
            print(f"数字 {num} ，将要做9600维保,最晚要在{maxtime}天后做，正常应该在{normaltime}天后做，最早应该在{mintime}天后做")


# 调用函数处理数字
process_numbers()