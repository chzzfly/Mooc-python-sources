# 读取文件，去除空行，写入文件
f = open('C:\\Users\\admin\Downloads\\vocabulary.txt', 'w', encoding='utf-8')
content = []
lines = f.readlines()

for line in lines:
    if line[0] != line[-1]:
        content.append(line)

# set1 = set(lines)

# lines1 = list(set1)

# print(content)
f.seek(0)

f.writelines(content)

f.close()
