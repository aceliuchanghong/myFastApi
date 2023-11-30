from openai import OpenAI
import httpx


def read_properties(filename):
    properties = {}
    with open(filename, 'r') as f:
        for line in f:
            if "=" in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                properties[key.strip()] = value.strip()
    return properties


def talkToGpt(prompt, stream=False):
    # 读取param.properties文件
    properties = read_properties('../param.properties')

    if properties.get('need_proxy') == 'Y':
        proxy_host = properties.get('proxyHost')
        proxy_port = properties.get('proxyPort')
        http_client = httpx.Client(proxies=f"http://{proxy_host}:{proxy_port}")
        client = OpenAI(http_client=http_client)
    else:
        client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            # {"role": "system", "content": system_init},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        stream=stream,
        # finish_reason="stop"
    )
    if not stream:
        return completion.choices[0].message.content
    else:
        final_output = ""
        for chunk in completion:
            if chunk is not None and chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                yield content
                final_output += content
        return final_output


for content in talkToGpt("你好,帮我写一首诗,每句需要:看,满,花,水,结尾", stream=True):
    print(content, end="")
