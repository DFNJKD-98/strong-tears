import json

with open('./jsonFileList/myfav.json', 'r', encoding='utf-8') as f:
    content = f.read()

jsonText = json.loads(content)
length = jsonText['cdlist'][0]['songnum'] | jsonText['data']['cdlist'][0]['songnum']
print(length)