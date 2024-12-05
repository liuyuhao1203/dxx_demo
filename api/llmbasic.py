import openai
from openai import OpenAI
import os
import json
import requests


def gpt4_1106_preview(pt):
  client = OpenAI()
  msg =[
      {"role": "system", "content": """你现在是一个专业的编剧，擅长使用美国编剧教父麦基研发三幕式结构来编写剧本的内容。"""},
      {"role": "user", "content": pt}
    ]
  ppt=""" """
  response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages = msg,
      temperature=0,
      #frequency_penalty=frequency_penalty
  )
  # return response.choices[0].message.content
  print("+++输出+++")
  print(response.choices[0].message.content)


def gpt4_0125_preview(pt):
  # client = OpenAI()
  client = OpenAI()
  msg =[
      {"role": "system", "content": """你现在是一个专业的编剧，擅长使用美国编剧教父麦基研发三幕式结构来编写剧本的内容。"""},
      {"role": "user", "content": pt}
    ]
  ppt=""" """
  response = client.chat.completions.create(
      model="gpt-4-0125-preview",
      messages = msg,
      temperature=0,
      #frequency_penalty=frequency_penalty
  )
  return response.choices[0].message.content

def get_completion_from_messages(messages, model='gpt-4-0125-preview', temperature=0):
  client = OpenAI()
  
  response = client.chat.completions.create(
    model = model,
    messages = messages,
    temperature = temperature,
  )

  return response.choices[0].message.content

def get_completion_from_messages_grok(messages, model='grok-beta', temperature=0):
  url = 'https://api.x.ai/v1/chat/completions'

  data = {
    "messages": messages,
    "model": model,
    "temperature": temperature
  }
  # 将数据转换为JSON格式
  json_data = json.dumps(data)

  # 设置请求头，指定发送JSON数据
  headers = {
      'Content-Type': 'application/json',
      'Authorization': ''
  }
  response = requests.post(url, data=json_data, headers=headers)
  
  return response.json()['choices'][0]['message']['content']

if __name__ == '__main__':
  messages = [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and nothing else."
    }
  ]
  get_completion_from_messages_grok(messages)