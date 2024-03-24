import requests
from pydantic import BaseModel,Field,RootModel
import io
import csv

csv_url = 'https://raw.githubusercontent.com/roberthsu2003/python/master/pydantic/%E5%AD%B8%E7%94%9F%E5%88%86%E6%95%B8.csv'
res = requests.get(url=csv_url)
if res.ok:
    print('下載成功')
else:
    print('下載失敗')

class Scores(BaseModel):
    姓名:str
    國文:int = Field(alias='科目1')
    英文:int = Field(alias='科目2')
    數學:int = Field(alias='科目3')
    地理:int = Field(alias='科目4')
    歷史:int = Field(alias='科目5')
  
class Student(RootModel):
    root:list[Scores]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
    
csv_url:str = res.text
csv_file = io.StringIO(csv_url)
dict_reader = csv.DictReader(csv_file)
csv_data = list(dict_reader)

csv_root = Student.model_validate(csv_data)
json_str = csv_root.model_dump_json()

with open('新學生分數.csv',mode='w',encoding='utf-8',newline='') as file:
    dict_writer = csv.DictWriter(file,fieldnames=list(Scores.model_fields.keys()))
    dict_writer.writeheader()
    for site in csv_root:
        dict_writer.writerow(site.model_dump())
print('生成csv檔')       

with open('新學生分數.json',mode='w',encoding='utf8') as jsonFile:
    jsonFile.write(json_str)
print('生成json檔')