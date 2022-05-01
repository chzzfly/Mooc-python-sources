import wordcloud
import jieba

# w = wordcloud.WordCloud()
# w.generate("python and wordcloud")
# w.to_file('test.png')

f = open('hamlet.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
# ls = jieba.lcut(t)
# txt = ' '.join(ls)

# print(txt[0:300])

wd = wordcloud.WordCloud(
    width=800,
    height=600,
)
wd.generate(t)
wd.to_file('hamlet.png')