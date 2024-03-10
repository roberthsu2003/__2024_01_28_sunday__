import pyinputplus as pyip
import random
from pprint import pprint

def get_student(n:int)->list[dict]:
    students:list[dict] = []
    for _ in range(n):
        student:dict[str,int] = {}
        for subject in ['國文','英文','數學']:
            student[subject] = random.randint(50,100)
        students.append(student)
    return students

nums = pyip.inputInt("請輸入學生數量:")
stus = get_student(n=nums)
pprint(stus)