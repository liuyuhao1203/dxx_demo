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
        if item == 'script_0302':
            merge_script()
            
        # 故事梗概生成完毕
        if num == 2:
            event.set()
    with open(current_directory_path + '/result/' + 'context.rs','w', encoding='utf-8') as ct:
        ct.write(str(context))

    print("=== Generate Success ===")
    return True
        
def merge_script():
    #整合场3
    script_list= ['script_0301', 'script_0302']
    scriptobj = {
        "场次": "场3",
        "时间": "",
        "地点": "",
        "剧本内容": "",
        "元素": []
    }
    content_str = ""
    for item in script_list:
        with open(current_directory_path + '/result/' + item + '.rs', 'r', encoding='utf-8') as pt:

            # 去除字符串中的Markdown代码块标记
            clean_str = pt.read().replace("```json", "").replace("```", "")

            try:
                parsed_data = json.loads(clean_str)
                content = parsed_data["content"]
                # 进一步解析content中的JSON
                content_data = json.loads(content)
            except json.JSONDecodeError as e:
                print(f"解析JSON时发生错误: {e}")
            else:
                if content_data["场次"] == "场3":
                    scriptobj["时间"] = content_data["时间"]
                    scriptobj["地点"] = content_data["地点"]
                content_str += content_data["剧本内容"]
                scriptobj["元素"].extend(content_data["元素"])
        scriptobj["剧本内容"] = content_str
    with open(current_directory_path + '/result/' + 'script_03.rs', 'w', encoding='utf-8') as f4:
        rsp = {"success": 1, "content": '```json' + json.dumps(scriptobj, ensure_ascii=False, indent=4) + '```'}
        f4.write(json.dumps(rsp, ensure_ascii=False, indent=4))

    