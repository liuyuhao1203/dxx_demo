# -*- coding: utf-8 -*-
from llmbasic import gpt4_0125_preview

## 读取已经生成的场景
genggai = ''
with open('./result/genggai.rs', 'r', encoding='utf-8') as f:
    genggai =  f.read()
    print('加载梗概:'+genggai)

with open('./pt/大元素.pt', 'r', encoding='utf-8') as f:
    pt = f.read() 
    pt = pt.replace('genggai',genggai)
    result = gpt4_0125_preview(pt)
    with open('./result/dayuansu.rs','w', encoding='utf-8') as f2:
        f2.write(result)
