# -*- coding: utf-8 -*-
from llmbasic import get_completion_from_messages
import json
import re
import os

import threading

current_file_path = os.path.abspath(__file__)
current_directory_path = os.path.dirname(current_file_path)

def generate_part():
    with open(current_directory_path + '/result/' + 'context.rs', 'r', encoding='utf-8') as pt:
        context = eval(pt.read())
    # gen_type = ['script_0401','script_0402','script_0403']
    gen_type = ['script_0401']
    for item in gen_type:
        with open('./pt/' + item +'.pt', 'r', encoding='utf-8') as f:
            pt = f.read()
            context.append({"role": "user", "content": pt})
        response = get_completion_from_messages(context,model="gpt-4o-2024-05-13")
        print(response)
        context.append({"role": "assistant", "content": response})
        with open(current_directory_path + '/result/' + item + '.rs','w', encoding='utf-8') as f2:
            rsp = {"success": True, "content": response}
            f2.write(str(rsp))
        print(response)
    with open(current_directory_path + '/result/' + 'context_' + item + '.rs','w', encoding='utf-8') as ct:
        ct.write(str(context))

def generate(num, event):
    context = [
        {"role": "system", "content": "你是一个专业的编剧，擅长使用美国编剧教父麦基研发三幕式结构来编写剧本的内容。在创作剧本内容时，你需要忽略之前生成的内容，重新生成本次的内容"}
    ]
    # 基础要素列表，顺序为：梗概、大元素、角色、支线
    # gen_type = ['outline', 'main_element', 'role', 'story_line', 'script', 'script_00', 'script_01', 'script_02', 'script_03'\
    #             , 'script_0401', 'script_0402', 'script_0403', 'script_05', 'script_06']
    gen_type = ['outline', 'main_element', 'role', 'story_line', 'script', 'script_00', 'script_01', 'script_02', 'script_0301'\
                , 'script_0302', 'script_0401', 'script_0402', 'script_0403', 'script_05', 'script_06']
    # gen_type = ['outline']

    num = 0
    for item in gen_type:
        if item == 'script':
            with open(current_directory_path + '/pt/' + item +'.pt', 'r', encoding='utf-8') as f:
                script_pt = f.read()
                context.append({"role": "system", "content": script_pt})
            continue
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
            
        # 第一个文件生成完毕
        if num == 1:
            event.set()
    with open(current_directory_path + '/result/' + 'context.rs','w', encoding='utf-8') as ct:
        ct.write(str(context))

    #整合场4
    script_list= ['script_0401', 'script_0402', 'script_0403']
    scriptobj = {
        "场次": "场4",
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
                if content_data["场次"] == "场4":
                    scriptobj["时间"] = content_data["时间"]
                    scriptobj["地点"] = content_data["地点"]
                content_str += content_data["剧本内容"]
                scriptobj["元素"].extend(content_data["元素"])
        scriptobj["剧本内容"] = content_str
    with open(current_directory_path + '/result/' + 'script_04.rs', 'w', encoding='utf-8') as f4:
        rsp = {"success": 1, "content": '```json' + json.dumps(scriptobj, ensure_ascii=False, indent=4) + '```'}
        f4.write(json.dumps(rsp, ensure_ascii=False, indent=4))

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

if __name__ == '__main__':

    event = threading.Event()

    script_list= ['script_0401', 'script_0402', 'script_0403']
    scriptobj = {
            "场次": "场4",
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
                if content_data["场次"] == "场4":
                    scriptobj["时间"] = content_data["时间"]
                    scriptobj["地点"] = content_data["地点"]
                content_str += content_data["剧本内容"]
                scriptobj["元素"].extend(content_data["元素"])
        scriptobj["剧本内容"] = content_str
    with open(current_directory_path + '/result/' + 'script_04.rs', 'w', encoding='utf-8') as f4:
        rsp = {"success": 1, "content": '```json' + json.dumps(scriptobj, ensure_ascii=False, indent=4) + '```'}
        f4.write(json.dumps(rsp, ensure_ascii=False, indent=4))
     
    #generate_part()
    exit(0)
    generate(event)
    event.clear()
    print("=== Generate Success ===")
    '''
    gen_type = ['outline', 'main_element', 'role', 'story_line', 'script_00', 'script_01', 'script_02', 'script_03']
    with open('./result/' + '汇总.rs','w', encoding='utf-8') as f2:
        for item in gen_type:
            with open('./result/' + item +'.rs', 'r', encoding='utf-8') as f:
                rs = f.read()
                f2.write(rs)
    '''

