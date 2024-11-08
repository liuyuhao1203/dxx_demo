import re

# 原始文章
article = """
这是一个故事。张三说：“今天天气真好。”李四回答：“是的，非常适合出去郊游。\\n\\n张三说：“去哪呢。”
故事继续进行。张三又说：“我们去公园吧。”李四同意了。
"""

# 要替换的对话内容
old_dialogue = '“是的，非常适合出去郊游。\\n\\n张三说：“去哪呢。”'
new_dialogue = '"好的，我们去郊游1111吧。\\n\\n张三说：“去哪呢111。””'

# 替换对话
# 使用re.escape()对特殊字符进行转义
old_dialogue_escaped = re.escape(old_dialogue)
updated_article = re.sub(old_dialogue_escaped, new_dialogue, article)

print(old_dialogue_escaped)
print(str(updated_article))