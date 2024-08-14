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

## 读取角色
juese_list = []
file_name = os.listdir('./result/juese')
for file_name_i in file_name:
    with open('./result/juese/'+file_name_i, 'r', encoding='utf-8') as f:
        juese =  f.read()
        juese_list.append(file_name_i+':'+juese)

story_list = [
    {"type":"主线","id":"1","content":"找到死者的死因,"},
    {"type":"支线","id":"1","content":"死者与主角,主要是讲死者和主角的关系，以及死者和主角的羁绊。 "},
    {"type":"支线","id":"2","content":"主角与侦探,主要是讲主角和侦探对于凶杀的探讨，有不信任到信任的过程。"},
    {"type":"支线","id":"3","content":"侦探与真凶的对手戏。"},
    {"type":"支线","id":"4","content":"主角与凶手的对手戏。"},
    {"type":"支线","id":"5","content":"主角与配角4，配角5的对手戏。"},
    {"type":"支线","id":"6","content":"主角与配角3的对手戏。"},
    {"type":"支线","id":"7","content":"配角1与配角2的对手戏。"},
    {"type":"支线","id":"8","content":"主角的单独故事线，主要是讲述了主角为什么会有杀死死者的理由以及主角做的哪些事情导致被误会成凶手的原因。"},
    {"type":"支线","id":"9","content":"侦探与配角们, 主要是讲侦探对于配角们的询问。"},
    {"type":"支线","id":"10","content":"警察线，主要是讲侦探为什么侦查这个案件以及警察之前的配合和协作。"}
]
story_result_list = []
with open('./pt/主线和支线.pt', 'r', encoding='utf-8') as f:
    pt = f.read()
    pt = pt.replace('${genggai}',genggai)
    pt = pt.replace('${dayuansu}',dayuansu)
    pt = pt.replace('${juese_list}', '\n'.join(juese_list))

    for role_list_i in story_list:
        story_id = role_list_i['type']+'_'+role_list_i['id']
        print('生成',story_id)
        rs_path = './result/story/'+story_id+'.rs'
        if os.path.exists(rs_path):
            with open(rs_path, 'r', encoding='utf-8') as f :
                r_pt = f.read()
                story_result_list.append(r_pt)
            continue

        r_pt = pt.replace('${have}','\n'.join(story_result_list))
        r_pt = r_pt.replace('${write}',story_id+':'+role_list_i['content'])
        print(r_pt)
        result = gpt4_0125_preview(r_pt)
        story_result_list.append(result)
        with open('./result/story/'+story_id+'.rs','w',encoding='utf-8') as f2:
            f2.write(result)
        #break