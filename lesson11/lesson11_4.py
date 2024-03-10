import csv


students = [{'國文': 90, '數學': 88, '英文': 61},
            {'國文': 98, '數學': 85, '英文': 63},
            {'國文': 86, '數學': 99, '英文': 85},
            {'國文': 52, '數學': 52, '英文': 71},
            {'國文': 53, '數學': 58, '英文': 98},
            {'國文': 54, '數學': 66, '英文': 54},
            {'國文': 94, '數學': 67, '英文': 70},
            {'國文': 69, '數學': 87, '英文': 89},
            {'國文': 100, '數學': 75, '英文': 100},
            {'國文': 100, '數學': 100, '英文': 100}]




#建立file實體,這個實體會自動close()-> with....as
fileName = input('請輸入檔案名稱:')
csvName = f'{fileName}.csv'
with open(csvName,mode='w',encoding='utf-8',newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=['國文','數學','英文'])
    writer.writeheader()
    writer.writerows(students)

print(f'{csvName}存檔完成')