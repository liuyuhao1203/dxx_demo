import os
import re
import glob
import json
import time
import threading
from flask import Flask, make_response, jsonify, request

from generate import generate

app = Flask(__name__)

event = threading.Event()

@app.route('/')
def index():
    return "Final Phrase"

@app.route('/create_outline', methods=['post', 'get'])
def create_outline():
    try:
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)
        # 梗概的处理方式与剧本内容相同
        with open(current_directory_path + '/result/' + 'outline.rs', 'r', encoding='utf-8') as pt:
            # pattern = r'```json(.*?)```'
            # matches = re.findall(pattern, pt.read(), re.DOTALL)
            # context = eval(matches[0])
            scriptobj = {}
            # 去除字符串中的Markdown代码块标记以及换行符
            clean_str = pt.read().replace("```json", "").replace("```", "").replace("\n", "").replace("\\n", "")
            try:
                parsed_data = json.loads(clean_str)
                content = parsed_data["content"]
                content_data = json.loads(content)
            except json.JSONDecodeError as e:
                print(f"解析JSON时发生错误: {e}")
            else:
                scriptobj["剧本名称"] = content_data["剧本名称"]
                scriptobj["主角名称"] = content_data["主角名称"]
                scriptobj["剧本梗概"] = content_data["剧本梗概"]
        
        response = make_response(jsonify(scriptobj))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except Exception as e:
        print("发生异常：", e)
        context = {}
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response



@app.route('/create_main', methods=['post', 'get'])
def create_main():
    try:
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        # 等待下一步生成完，确保大元素文件已经存在
        file_path = current_directory_path + '/result/' + 'role.rs'
        while not os.path.exists(file_path):
            time.sleep(1)
        # 大元素的处理方式与剧本内容相同
        with open(current_directory_path + '/result/' + 'main_element.rs', 'r', encoding='utf-8') as pt:
            # pattern = r'```json(.*?)```'
            # matches = re.findall(pattern, pt.read(), re.DOTALL)
            # context = eval(matches[0])
            scriptobj = []
            # 去除字符串中的Markdown代码块标记以及换行符
            clean_str = pt.read().replace("```json", "").replace("```", "").replace("\n", "").replace("\\n", "")
            try:
                parsed_data = json.loads(clean_str)
                content = parsed_data["content"]
                content_data = json.loads(content)
            except json.JSONDecodeError as e:
                print(f"解析JSON时发生错误: {e}")
        
        response = make_response(jsonify(content_data))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except Exception as e:
        print("发生异常：", e)
        context = []
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

@app.route('/create_role', methods=['post', 'get'])
def create_role():
    try:
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        # 等待下一步生成完，确保角色文件已经存在
        file_path = current_directory_path + '/result/' + 'story_line.rs'
        while not os.path.exists(file_path):
            time.sleep(1)

        with open(current_directory_path + '/result/' + 'role.rs', 'r', encoding='utf-8') as pt:
            pattern = r'```json(.*?)```'
            matches = re.findall(pattern, pt.read(), re.DOTALL)
            context = eval(matches[0])
        
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except Exception as e:
        print("发生异常：", e)
        context = []
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response


@app.route('/create_storyline', methods=['post', 'get'])
def create_storyline():
    try:
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        # 等待下一步生成完，确保故事线文件已经存在
        file_path = current_directory_path + '/result/' + 'script_00.rs'
        while not os.path.exists(file_path):
            time.sleep(1)

        with open(current_directory_path + '/result/' + 'story_line.rs', 'r', encoding='utf-8') as pt:
            pattern = r'```json(.*?)```'
            matches = re.findall(pattern, pt.read(), re.DOTALL)
            context = eval(matches[0])
        
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except Exception as e:
        print("发生异常：", e)
        context = []
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response


@app.route('/get_script_list', methods=['post', 'get'])
def get_script_list():
    
    # list = ['script_00', 'script_01', 'script_02', 'script_03', 'script_0401'\
    #             , 'script_0402', 'script_0403', 'script_05', 'script_06']
    list = ['开场','场1','场2','场3','场4','场5','场6']
    response = {
        "code": 0,
        "success": True,
        "data": list
    }
    return response

@app.route('/create_script', methods=['post', 'get'])
def create_script():
    try:
        data = request.get_json()
        
        script_name = data['script_name']
        name_map = {'开场':'script_00','场1':'script_01','场2':'script_02','场3':'script_03','场4':'script_04','场5':'script_05','场6':'script_06'}
        script_file_name = name_map[script_name]
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        file_path = current_directory_path + '/result/' + script_file_name + '.rs'
        while not os.path.exists(file_path):
            time.sleep(1)

        # 等待两秒确保文件写完
        time.sleep(2)

        scriptobj = {}
        with open(current_directory_path + '/result/' + script_file_name + '.rs', 'r', encoding='utf-8') as pt:
            # context = eval(pt.read())
            # content = context['content']
            # pattern = r'```json(.*?)```'
            # matches = re.findall(pattern, content, re.DOTALL)
            # rsp = {"success": True, "content": matches[0]}

            clean_str = pt.read().replace("```json", "").replace("```", "")
            try:
                parsed_data = json.loads(clean_str)
                content = parsed_data["content"]
                # 进一步解析content中的JSON
                content_data = json.loads(content)
            except json.JSONDecodeError as e:
                print(f"解析JSON时发生错误: {e}")
            else:
                scriptobj["场次"] = script_name
                scriptobj["时间"] = content_data["时间"]
                scriptobj["地点"] = content_data["地点"]
                scriptobj["剧本内容"] = content_data["剧本内容"]
                scriptobj["元素"] = content_data["元素"]
            rsp = {"success": True, "content": scriptobj} 

        return rsp
        
        response = make_response(jsonify(rsp))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except Exception as e:
        print("发生异常：", e)
        context = {}
        response = make_response(jsonify(context))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response


@app.route('/update_bg', methods=['post', 'get'])
def update_bg():
    try:
        data = request.get_json()
    
        backgroud = data['backgroud']
        desc = data['desc']

        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        with open(current_directory_path + '/pt/' + 'outline_old.pt', 'r', encoding='utf-8') as f:
            pt = f.read() 
            pt = pt.replace('backgroud', backgroud)
            pt = pt.replace('desc', desc)
        with open(current_directory_path + '/pt/' + 'outline.pt', 'w', encoding='utf-8') as f2:
            f2.write(pt)

        return {"success": True}
    except Exception as e:
        print("发生异常：", e)
        return {"success": False}
    

@app.route('/start', methods=['post', 'get'])
def start():
    try:
        print("开始创作")
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)
        directory = current_directory_path + '/result'
        file_pattern = '*.rs' 
        files_to_delete = glob.glob(os.path.join(directory, file_pattern))

        if files_to_delete:
            for file_path in files_to_delete:
                os.remove(file_path)
                print(f"Deleted {file_path}")
        else:
            print("No files found to delete.")
        
        # 设置事件为未设置状态
        event.clear()

        file_generation_thread = threading.Thread(target=generate, args=(0, event))
        file_generation_thread.start()

        # 等待第一个文件生成，故事梗概生成好之后返回，方便前端继续执行
        event.wait()

        # ret = generate()

        file_path = current_directory_path + '/result/' + 'outline.rs'
        if os.path.exists(file_path):
            return jsonify({"message": "第一个文件已生成", "success": True}), 200
        else:
            return jsonify({"message": "第一个文件生成失败", "success": False}), 500

        # return {"success": True}
    except Exception as e:
        print("发生异常：", e)
        return {"success": False}
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8005)
