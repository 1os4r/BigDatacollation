import sys

# 接收每行输出的字符串
for line in sys.stdin:

	# 去除换行符，回车符空白等字符串
    line = line.replace("\r", "").replace(" ", "").replace("\n", "")
    # print(line)

    # 使用|分割字符串
    list = line.split("|")
    # 判断长度是否为5
    if len(list) == 5:
    	# 使用|连接并输出
        print("|".join(list))
