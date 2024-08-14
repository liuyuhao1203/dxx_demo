import os
import re
import glob
from flask import Flask, make_response, jsonify, request

from generate import generate

app = Flask(__name__)

@app.route('/')
def index():
    return "Final Phrase"

@app.route('/create_outline', methods=['post', 'get'])
def create_outline():
    try:
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        with open(current_directory_path + '/result/' + 'outline.rs', 'r', encoding='utf-8') as pt:
            pattern = r'```json(.*?)```'
            matches = re.findall(pattern, pt.read(), re.DOTALL)
            context = eval(matches[0])
        
        response = make_response(jsonify(context))
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

        with open(current_directory_path + '/result/' + 'main_element.rs', 'r', encoding='utf-8') as pt:
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

@app.route('/create_role', methods=['post', 'get'])
def create_role():
    try:
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

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
        script_name = name_map[script_name]
        current_file_path = os.path.abspath(__file__)
        current_directory_path = os.path.dirname(current_file_path)

        with open(current_directory_path + '/result/' + script_name + '.rs', 'r', encoding='utf-8') as pt:
            context = eval(pt.read())
            content = context['content']
            pattern = r'```json(.*?)```'
            matches = re.findall(pattern, content, re.DOTALL)
            #rsp = eval(matches[0])
            rsp = {"success": True, "content": matches[0]}

            json_rsp = eval(str(rsp))
            print (eval(json_rsp['content']))

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
        ret = generate()
        return {"success": True}
    except Exception as e:
        print("发生异常：", e)
        return {"success": False}
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8006)
