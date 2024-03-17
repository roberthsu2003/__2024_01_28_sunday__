import random

def getSuggestion(bmi:float) -> str:
    '''計算建議：給入bmi:float，傳回suggest:str'''
    if bmi<18.5:
        suggest=('體重過輕')
    elif bmi<24:
        suggest=('身材正常')
    elif bmi<27:
        suggest=('體重稍重')
    elif bmi<30:
        suggest=('輕度肥胖')
    elif bmi<35:
        suggest=('中度肥胖')
    else:  
        suggest=('重度肥胖')
    return suggest

def getBMI(height:float,weight:float,)->float:
    '''計算BMI，給入height:float及weight:float，傳回bmi:float'''
    bmi=weight/((height/100)**2)
    return bmi

def homework(member:int):
    for i in range(0,member):
        with open('names.txt',encoding='utf-8') as file:
            names: str = file.read()
            name_list: list[str] = names.split(sep='\n')
            XXX=random.choice(name_list)
            height=random.randint(100,190)
            weight=random.randint(40,99)
            bmi=getBMI(height,weight)
            suggest=getSuggestion(bmi)
            print(f'{XXX},身高：{height}cm,體重：{weight}kg,BMI：{bmi:.2f},所屬範圍:{suggest}')

homework(10)