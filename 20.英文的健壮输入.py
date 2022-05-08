a = input()

ls = []
for i in range(65, 91):
    ls.append(chr(i))

for i in range(97, 123):
    ls.append(chr(i))

for char in a:
    if char in ls:
        print(char, end='')

# 哇塞，当自己设计程序，解决问题的时候，也太有成就感了吧，看到自己耍点小聪明就能解决问题，我要高兴的飞起来了。