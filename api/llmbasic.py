import openai
from openai import OpenAI
import os


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
  XAI_API_KEY = ''
  client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
  )
  
  response = client.chat.completions.create(
    model = model,
    messages = messages,
    temperature = temperature,
  )
  return response.choices[0].message.content

if __name__ == '__main__':

  client = OpenAI()

  text = f"""主角苏七月，今年29岁，身高在女性当中偏高，相貌出众。出生于北京一个普通家庭，父母都是大学教授，\
  基因良好的传输到了苏七月当中，但苏七月不爱读书，所以学业未完成，走上社会后跌跌撞撞才明白学业的重要性，\
  好不容易找到了一份在知名律所做实习生的机会，并且通过自己的努力获得了老板赏识，并承诺她给予她一份推荐信去上最好的法学院，\
  而因为金融诈骗案的负责权所引起的凶杀案改变了这一切，主人公苏七月将会如何破局以及如何从中改变自己，是一个巨大的挑战。"""

  genggai = f"""在中国虚构的城市山城，一起凶杀案震惊了这座宁静的城市。死者是一位名叫周明的年轻企业家，他的死引起了广泛的关注。\
  主角林晓，一位年轻的女性平 面设计师，与周明有过一段深厚的友谊。在周明死亡的前夜，林晓因一次意外将一份重要的设计草图遗失在了周明的家中，\
  这份设计草图对林晓来说至关重要，它是她参加 国际设计大赛的作品，关系到她职业生涯的重大转折。第二天，当她返回周明家中寻找草图时，\
  却被卷入了凶杀案的调查中，成为了警方的重要嫌疑人之一。为了证明自己的清白，同时也为了找回那份至关重要的设计草图，林晓决定配合警方的调查。\
  侦探角色由林晓的青梅竹马，李俊扮演。李俊并非职业侦探，而是一名法律顾问，但他对林晓有着深厚的情感，决定利用自己的专业知识和资源帮助林晓洗清嫌疑。\
  在这个过程中，他们发现了周明身边的五位配角各自隐藏的秘密：包括周明的商业伙伴、前女友、竞争对手、私人助理和一个神秘的陌生人。\
  每个人都有可能是凶手，每个人都有自己的动机。随着调查的深入，林晓和李俊逐渐揭开了周明死亡的真相。原来，凶手是周明的竞争对手，\
  因为一场商业纠纷而决定铲除周明。在这个过程中，林晓不仅证明了自己的清白，也找回了那份重要的设计草图。最终，\
  林晓在国际设计大赛中获得了优异的成绩，而李俊也因为这次事件深刻地意识到了对林晓的重要性，两人的关系因此变得更加牢固。"""


  pt = f"""
  你的任务是根据故事梗概来塑造出剧本的角色，根据现有的故事梗概生成每个角色的人物小传，人物小传需要满足以下几点要求：
  1、	符合现代的凶杀悬疑剧。
  2、	简单描述角色的外形、年龄、性别。
  3、 主角的人物小传要展现出人物内在性格的变化或人物弧光，无论变好还是变坏，不要直接出现人物弧光这个描述。
  4、 死者的死因不能是被嫉妒。
  5、 凶手的人物小传要写出他的杀人动机。
  6、 每个角色都要有明显的优点和缺点，是可以用动作展示出来的优缺点，比如在过马路时会扶着老人展示他善良的一面，但不要直接使用这个例子。请设计每个角色的优缺点使得人物更丰富。
  7、 每个角色的人物小传200字。
  8、 剧本中的人物角色一共是9个, 包含主角1个, 死者1个, 侦探1个, 凶手1个, 配角5个。
  9、	角色都是中国人，最好可以确定到一座城市，可以使用真实城市，也可以使用虚拟的城市。

  下面用[]分界符的文本是已经生成的剧本故事梗概，你需要先认真阅读故事梗概，充分理解。
  [{genggai}]
  
  下面用<>分界符的文本是一段写好的人物小传，你需要参照示例，先学习如何写好一个人物小传，然后在充分满足以上要求，根据提供的故事梗概写出每个角色的人物小传。使用JSON格式返回，需要包含三个个key，角色、角色姓名、人物小传。
  <{text}>
  """

  pt = '你知道美国编剧教父麦基研发三幕式结构吗'
  print(pt)


  print(gpt4_0125_preview(pt))

  '''
  #填写修改场次
  story = "场3"
  #填写修改内容
  #correct_con = '重写这场戏，有以下3点要求：1、要求展现出主角与个角色之间的人物关系，例如职业关系、身份关系以及各角色对主角的看法。2、“每个人都有自己的战斗”这个元素不需要每个角色都原封不动的说出来，而是通过正常的交流展示出每个角色对于此元素的体现。3、侦探不在这场戏破案，这场戏主要是展现各角色对于主角的看法'
  correct_con = '重写这场戏，本场戏并不是以破案与推定案件发展为主题的，这场戏主要是展现各角色对于主角的看法，重新生成内容不低于五千个汉字'


  #
  with open('./result/juben/' + story + '.pt', 'r', encoding='utf-8') as f:
    pt_file =  f.read()
    print('加载pt:'+pt_file)
  with open('./result/juben/' + story + '.rs', 'r', encoding='utf-8') as f:
    rs_file =  f.read()
    print('加载rs:'+rs_file)
  msg =[
      {'role': 'system', 'content': "你现在是一个专业的编剧，擅长使用美国编剧教父麦基研发三幕式结构来编写剧本的内容。"},
      {"role": "user", "content": pt_file},
      {"role": "assistant", "content": rs_file},
      {"role": "user", "content": correct_con}
    ]
  
  response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages = msg,
      temperature=0,
      #frequency_penalty=frequency_penalty
  )
  # return response.choices[0].message.content
  
  # print(response.choices[0].message.content)
  result = response.choices[0].message.content
  with open('./result/juben/' + story + '_correct' + '.rs','w', encoding='utf-8') as f_correct:
        f_correct.write(result)
  '''
