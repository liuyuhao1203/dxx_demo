# -*- coding: utf-8 -*-
from llmbasic import get_completion_from_messages
import json

def generate_part():
    with open('./result/' + 'context_script_05.rs', 'r', encoding='utf-8') as pt:
        context = eval(pt.read())
    # gen_type = ['script_0401','script_0402','script_0403']
    gen_type = ['script_06']
    for item in gen_type:
        with open('./pt/' + item +'.pt', 'r', encoding='utf-8') as f:
            pt = f.read()
            context.append({"role": "user", "content": pt})
        response = get_completion_from_messages(context,model="gpt-4o-2024-05-13")
        context.append({"role": "assistant", "content": response})
        with open('./result/' + item + '.rs','w', encoding='utf-8') as f2:
            f2.write(response)
        print(response)
    with open('./result/' + 'context_' + item + '.rs','w', encoding='utf-8') as ct:
        ct.write(str(context))

def generate():
    context = [
        {"role": "system", "content": "你是一个专业的编剧，擅长使用美国编剧教父麦基研发三幕式结构来编写剧本的内容。在创作剧本内容时，人物间的对话内容要占到全部内容的80%以上。"}
    ]
    # 基础要素列表，顺序为：梗概、大元素、角色、支线
    gen_type = ['outline', 'main_element', 'role', 'story_line', 'script', 'script_00', 'script_01', 'script_02', 'script_03']
    for item in gen_type:
        if item == 'script':
            with open('./pt/' + item +'.pt', 'r', encoding='utf-8') as f:
                script_pt = f.read()
                context.append({"role": "system", "content": script_pt})
            continue
        with open('./pt/' + item +'.pt', 'r', encoding='utf-8') as f:
            pt = f.read()
            context.append({"role": "user", "content": pt})
        # response = get_completion_from_messages(context) 
        response = get_completion_from_messages(context,model="gpt-4o-2024-05-13")
        # response = get_completion_from_messages(context,model="gpt-4-turbo")
        context.append({"role": "assistant", "content": response})
        with open('./result/' + item + '.rs','w', encoding='utf-8') as f2:
            f2.write(response)
    # context.append({"role": "user", "content": "你还记得元素类型包括哪些吗？"})
    # response = get_completion_from_messages(context,model="gpt-4o-2024-05-13")
    # print(response)
    with open('./result/' + 'context.rs','w', encoding='utf-8') as ct:
        ct.write(str(context))
        
if __name__ == '__main__':
    generate_part()
    exit(0)
    generate()
    print("=== Generate Success ===")
    gen_type = ['outline', 'main_element', 'role', 'story_line', 'script_00', 'script_01', 'script_02', 'script_03']
    with open('./result/' + '汇总.rs','w', encoding='utf-8') as f2:
        for item in gen_type:
            with open('./result/' + item +'.rs', 'r', encoding='utf-8') as f:
                rs = f.read()
                f2.write(rs)
