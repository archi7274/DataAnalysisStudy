import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Ex_CEOSalary.csv')
# print(data.head())/
# CEO들의 연봉을 나타낸 데이터
# sales : 매출 , salary : 연봉 , 매출이 높아지면 연봉이 높아져야 함
# 선형 데이터, 선형 회귀, 상관 관계 분석, 범주형 데이터

# 상관 계수 뽑기
data['industry'] = data['industry'].replace([1,2,3,4], ['Service','IT','Finance','Others'])
# 상관 계수 함수 pandas corr
# print(data.corr())


# print(data.corr(method='pearson'))

# print(data.corr(method='spearman'))

# print(data.corr(method='kendall'))


# industry가 salary에 영향을 미친다.
# plt.scatter(data['sales'],data['salary'])
# plt.show()

# 상관 계수 확인, 낮다..
# plt.scatter(data['roe'],data['salary'], alpha=0.3)
# plt.show()

# print(data['salary'].describe())

# print(data.groupby('industry')['salary'].describe())


#  이상치 처리

data = pd.read_csv('Ex_CEOSalary.csv')

print(data.head())

# data.boxplot(column='salary', return_type='both')

# data.boxplot(column='')

# Salary 변수의 이상치 처리
# 1 사분위와 3사분위의 값 알아내기 300 - 2100 ; 1400 중간값

print(data['salary'].mean())

print(data['salary'].quantile(q = 0.25)) # 1사분위
Q1 = data['salary'].quantile(q = 0.25)

print(data['salary'].quantile(q = 0.75)) # 3사분위
Q3 = data['salary'].quantile(q = 0.75)

IQR = Q3 - Q1
print(IQR)

data_IQR = data[(data['salary'] < Q3 + IQR * 1.5) & (data['salary'] > Q1 - IQR*1.5)]
data_IQR.hist()

# sales 와 salary 의 이상치를 모두 처리한 데이터 셋

Q1_sales = data['sales'].quantile(q=0.25)
Q3_sales = data['sales'].quantile(q=0.75)
IQR_sales = Q3_sales - Q1_sales
data_IQR = data[(data['salary'] < Q3 + IQR * 1.5) & (data['salary'] > Q1 - IQR*1.5) 
& (data['sales'] < Q3_sales + IQR_sales * 1.5) & (data['sales'] > Q1_sales - IQR_sales * 1.5)]
# 상관계수 출력
print(data_IQR.corr())

plt.scatter(data_IQR['sales'], data_IQR['salary'] alpha=0.5)
plt.show()

