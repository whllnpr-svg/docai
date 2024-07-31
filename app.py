import os
import anthropic
from dotenv import load_dotenv

# 加载当前目录下的.env文件
load_dotenv()
# 从环境变量中获取API密钥
cloud_api_key = os.getenv("api_key")
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=cloud_api_key,
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=4000,
    temperature=0.5,
    system="您是一名熟练的人工智能专家，擅长检查语言信息。请检查下面的文字，并标记其中的错别字、错别词语、错别符号和语法错误。",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Meeting notes:  \n  \nDate: Verona, Italy - Late 16th century  \n  \nAttendees:  \n"
                }
            ]
        }
    ]
)
print(message.content)
