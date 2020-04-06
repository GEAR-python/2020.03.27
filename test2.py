import openpyxl as pyxl
import pandas as pd

#엑셀 파일(WorkBook) 읽기
file_name = "data/측정기록지(2010년1월).xlsx"
wb = pyxl.load_workbook(file_name)

#워크 시트 읽기
#wb.get_sheet_names() # 엑셀 파일의 sheet 이름들 불러오기

# sheet 이름 지정해서 불러오기
#test = wb.get_sheet_by_name('광복동')

#test = wb.active #활성시트 가져오기, 파일 열었을때 default로 열리는 파일.
test = wb.worksheets[0] #시트 순서별로 불러오기

# 셀값 불러오기
# print(test['A1'].value)
# print(test.cell(row=1, column=1).value)
# print(test["A1:C3"])
# print(test.max_column)
# print(test.max_row)
# print(test.dimensions)

pol_data = list()
name = list()
time = list()
date = list()

for r in test.rows:
    if r[0].value == '측 정 소: ' :
        continue
    elif r[0].value == '측정항목: ' :
        name = r[2].value
        print(name)
    elif r[0].value == '측정년월: ' :
        year = (r[1].value)[0:5]
        #month = int((r[2].value)[0:2])
        month = (r[2].value)[0:2]
        print(year, month)
    elif r[0].value == '구 분' :
        #10 이하 시간에는 숫자'0'추가, 10 이상에는 그냥 time 리스트에 저장
        for t in range(1,25):
            if int((r[t].value)[:-1]) < 10 :
                time.append('0'+ (r[t].value)[:-1])
            else:
                time.append((r[t].value)[:-1])
           # time.append((r[t].value)[:-1])
        print(time)
    elif r[0].value == '최소' :
        #if문을 다 거친 pol_data(자료)를 이곳에서 dataframe에 넣어서 저장하기
        if name == 'O₃':
            df = pd.DataFrame(pol_data)
            df.rename(columns={0:name}, inplace=True)
            df.insert(0,'date', date)
        else:
            df[name] = pol_data

        pol_data = list() #자료 항목이 바뀔때 마다 pol_data 리스트를 초기화
        time = list()
       # break
    elif r[0].value == '최대' :
        continue
    elif r[0].value == '평균' :
        continue
    elif r[0].value == None :
        continue
    else :
        #day = int((r[0].value)[:-1])
        #날짜 중 '일'에 숫자 0 붙히기
        if int((r[0].value)[:-1]) < 10 :
            day = '0'+ (r[0].value)[:-1]
        else :
            day = (r[0].value)[:-1]

        #각 오염 농도값을 pol_data 리스트에 추가하기
        for i in range(1,25):
            pol_data.append(r[i].value)
            date.append(str(year)+str(month)+str(day)+str(time[i-1]))
            print(str(year)+str(month)+str(day)+str(time[i-1]), pol_data[i-1])

print("3")

# 각 행의 index를 연월일로 바꾸자 -> 날짜(연월일시간)을 제일 앞 column으로 삽입.
# output 파일로 저장하는 결과 추가
# 월별 파일들을 열어서 하나의 결과로 합치는 코딩 추가
# 사이트별로 결과 뽑기
# 통계변수 뽑아보기
# 그림그리기

print(df)

# index를 date로 바꾸려면 아래 문장 사용해야함.
#df.set_index('date', inplace=True)
#print(df)

df.to_excel('result.xlsx',sheet_name='Sheet1')
