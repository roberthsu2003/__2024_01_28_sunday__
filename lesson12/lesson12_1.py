import pyinputplus as pyip
import random
import csv

def get_student(n:int)->list[dict]:
    students:list[dict] = []
    for _ in range(n):
        student:dict[str,int] = {}
        for subject in ['國文','英文','數學']:
            student[subject] = random.randint(50,100)
        students.append(student)
    return students

def save_csvfile(fn:str,data:list[dict[str,int]]):
    '''
    儲存為csv檔
    參數fn:str -> 檔案名稱
    參數data:list[dict] -> dict內的key,必需是[國文,數學,英文]
    '''
    with open(fn,mode='w',encoding='utf-8',newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=['國文','數學','英文'])
        writer.writeheader()
        writer.writerows(data)
    print(f'{fn}存檔完成')

def main():
    nums = pyip.inputInt("請輸入學生數量:")
    stus = get_student(n=nums)
    fileName = input('請輸入檔案名稱:')
    csvName = f'{fileName}.csv'
    save_csvfile(fn=csvName,data=stus)


main()