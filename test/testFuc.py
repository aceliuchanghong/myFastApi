from test.gpt_util import talkToGptStream, talkToGpt

for content in talkToGptStream("你好,帮我写一首诗,每句需要:看,满,花,水,结尾"):
    print(content, end="")
print(talkToGpt("100+100是多少?"))
