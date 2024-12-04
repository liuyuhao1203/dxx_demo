# -*- coding: utf-8 -*-
from micro_correct import MicroCorrect
from llmbasic import get_completion_from_messages
import json
import re
import os

import threading

current_file_path = os.path.abspath(__file__)
current_directory_path = os.path.dirname(current_file_path)

def generate(num, event):
    context = []
    with open('./pt/' + 'level1.pt', 'r', encoding='utf-8') as f:
        pt = f.read()
        context.append({"role": "system", "content": pt})
    # 基础要素
    gen_type = ['level1_5']

    num = 0
    for item in gen_type:
        with open('./pt/' + item +'.pt', 'r', encoding='utf-8') as f:
            pt = f.read()
            print("=============")
            print(pt)
            context.append({"role": "user", "content": pt})
        response = get_completion_from_messages(context,model="gpt-4o-2024-05-13")
        context.append({"role": "assistant", "content": response})
        with open('./result/' + item + '.rs','w', encoding='utf-8') as f2:
            # 剧本内容、故事梗概、大元素可能存在换行符，需要特殊处理
            if item.startswith("script") or item == "outline" or item == "main_element":
                rsp = {"success": 1, "content": response}
                f2.write(json.dumps(rsp, ensure_ascii=False, indent=4))
            else:
                f2.write(response)
        num += 1
            
            event.set()
    with open(current_directory_path + '/result/' + 'context.rs','w', encoding='utf-8') as ct:
        ct.write(str(context))

    print("=== Generate Success ===")
    return True