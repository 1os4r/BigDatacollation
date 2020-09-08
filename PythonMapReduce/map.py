''''''
import sys

# 定义一个check函数判断是否为空
def check(arr):
    for i in arr:
        if i.strip() == "":
            return False

    return True

# 接收每行输出的字符串
for line in sys.stdin:
    # print(line)
    list = line.split(",")
    # 去除多余的换行符和回车符
    if " \n" in list: list.remove(" \n")
    if "\r\n" in list: list.remove("\r\n")
    if "\n" in list: list.remove("\n")
    if " " in list: list.remove(" ")
    # print(list)
    if check(list):
    	# 使用|连接字符串并输出
        data = "|".join(list)
        print(data)
