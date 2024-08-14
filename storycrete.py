from llmbasic import gpt4_0125_preview
import os
import json

            
# {
#     "story_id":'开场',
#     "story_content":'开场',
#     "juese":[],
#     "story_list":[],
#     "mid_yuansulist":[],
#     "small_yuansulist":[{"类型":"道具","作用":"表示玄学，暗示事情发展诡异","值":""}]
# }

def storycreate(story_json):
    pt = storycreate_pt(story_json)
    with open('./result/juben/'+story_json['story_id']+'.pt','w', encoding='utf-8') as f_pt:
        f_pt.write(pt)
    result = gpt4_0125_preview(pt)
    with open('./result/juben/'+story_json['story_id']+'.rs','w', encoding='utf-8') as f2:
        f2.write(result)



def storycreate_pt(story_json):
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
    show_juese_list = []
    file_name = os.listdir('./result/juese')
    for file_name_i in file_name:
        
        with open('./result/juese/'+file_name_i, 'r', encoding='utf-8') as f:
            juese =  f.read()
            juese_list.append(file_name_i+':'+juese)
            if file_name_i.replace('.rs','') in story_json['juese']:
                show_juese_list.append(file_name_i.replace('.rs',''))

    ## 读取故事
    story_list = []
    file_name = os.listdir('./result/story')
    for file_name_i in file_name:
        if file_name_i.replace('.rs','') in story_json['story_list']:
            with open('./result/story/'+file_name_i, 'r', encoding='utf-8') as f:
                story =  f.read()
                story_list.append(file_name_i.replace('.rs','') +'的内容:' + '\n' +story)

    ## 读取剧本
    have_story = []
    file_name = os.listdir('./result/juben')
    for file_name_i in file_name:
        with open('./result/juben/'+file_name_i, 'r', encoding='utf-8') as f:
            story =  f.read()
            have_story.append(file_name_i+':'+story)


    mid_yuansulist = []
    for mid_yuansulist_i in story_json['mid_yuansulist']:
        mid_yuansulist.append(json.dumps(mid_yuansulist_i,ensure_ascii=False))

    small_yuansulist = []
    for small_yuansulist_i in story_json['small_yuansulist']:
        small_yuansulist.append(json.dumps(small_yuansulist_i,ensure_ascii=False))

    with open('./pt/场次.pt', 'r', encoding='utf-8') as f:
        pt = f.read()
        pt = pt.replace('${genggai}',genggai)
        pt = pt.replace('${dayuansu}',dayuansu)
        pt = pt.replace('${juese_list}','\n'.join(juese_list))
        pt = pt.replace('${have_story}', '\n'.join(have_story))
        pt = pt.replace('${story_id}', story_json['story_id'])
        pt = pt.replace('${story_content}', story_json['story_content'])
        pt = pt.replace('${show_juese_list}','\n'.join(show_juese_list) if show_juese_list else '无') 
        pt = pt.replace('${story_list}','\n'.join(story_list) if story_list else '无') 
        pt = pt.replace('${mid_yuansulist}','\n'.join(mid_yuansulist)  if mid_yuansulist else '无') 
        pt = pt.replace('${small_yuansulist}','\n'.join(small_yuansulist) if small_yuansulist else '无') 
        print(pt)
        return pt