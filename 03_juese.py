# -*- coding:utf-8 -*-
from llmbasic import gpt4_0125_preview
import os

## 读取已经生成的场景
genggai = ''
with open('./result/genggai.rs', 'r', encoding='utf-8') as f:
    genggai =  f.read()
    print('加载梗概:'+genggai)

## 读取大元素
dayuansu = ''
with open('./result/dayuansu.rs', 'r', encoding='utf-8') as f:
    dayuansu =  f.read()
    print('加载大元素:'+dayuansu)

role_list = [
    {"role":"主角","link":[]},
    {"role":"侦探","link":[]},
    {"role":"死者","link":[]},
    {"role":"凶手","link":[]},
    {"role":"配角1","link":[]},
    {"role":"配角2","link":[]},
    {"role":"配角3","link":[]},
    {"role":"配角4","link":[]},
    {"role":"配角5","link":[]}
]
role_info_list = []
with open('./pt/角色.pt', 'r', encoding='utf-8') as f:
    pt = f.read()
    pt = pt.replace('${genggai}',genggai)
    pt = pt.replace('${dayuansu}',dayuansu)

    for role_list_i in role_list:
        print('生成',role_list_i)
        rs_path = './result/juese/'+role_list_i['role']+'.rs'
        if os.path.exists(rs_path):
            with open(rs_path, 'r', encoding='utf-8') as f :
                r_pt = f.read()
                role_info_list.append(r_pt)
            continue

        r_pt = pt.replace('${rolelist}','\n'.join(role_info_list))
        r_pt = r_pt.replace('${role}',role_list_i['role'])
        if role_list_i['link'] :
            r_pt = r_pt.replace('${link}', '该人物和' +  ','.join(role_list_i['link'])+'有关系')
        else:
            r_pt =r_pt.replace('${link}', '')
        print(r_pt)
        result = gpt4_0125_preview(r_pt)
        role_info_list.append(result)
        with open('./result/juese/'+role_list_i['role']+'.rs','w', encoding='utf-8') as f2:
            f2.write(result)
        #break