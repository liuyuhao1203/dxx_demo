# -*- coding: utf-8 -*-
from llmbasic import gpt4_0125_preview

## 待加入更多场景
with open('./pt/梗概.pt', 'r', encoding='utf-8') as f:
    result = gpt4_0125_preview(f.read() )
    with open('./result/genggai.rs','w',encoding='utf-8') as f2:
        f2.write(result)
