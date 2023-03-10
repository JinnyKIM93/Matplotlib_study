import numpy as np
import matplotlib.pyplot as plt

#(16)Matplotlib 막대그래프 그리기
#막대그래프(Bar graph, Bar chart)

#48 기본
x = np.arange(3)
years = ['2018', '2020', '2022']
values = [100, 300, 700]
#years는 x축에 표시될 연도, values는 막대그래프의 y값
fig, ax = plt.subplots(figsize=(7, 7))

ax.bar(x, values) #values이 y값으로 입력
ax.set_xticks(x, years) #x축에 눈금 레이블로 years 입력
plt.show()

#49 색상 지정하기
x = np.arange(3)

#step1 바 다 같은 색으로 지정
years = ['2018', '2019', '2020']
values = [100, 500, 800]
fig, ax = plt.subplots(figsize=(7,7))
ax.set_xticks(x, years)
# ax.bar(x, values, color='y') # 노랑색
# ax.bar(x, values, color='C2') # 초록색
# ax.bar(x, values, color='dodgerblue')  # 파랑색
ax.bar(x, values, color='#e35f62') # 빨강색
plt.show()

#step2 bar 마다 다르게 색 지정
years = ['2018', '2019', '2020']
values = [100, 500, 800]
colors = ['y', 'dodgerblue', 'C2']
# 원하는 색을 각각 써주면 입력되어 출력된다.
fig, ax = plt.subplots(figsize=(7,7))
ax.bar(x, values, color=colors)
ax.set_xticks(x, years)
plt.show()

#50 막대폭 지정하기
x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 500, 800]
colors = ['y', 'dodgerblue', 'C2']

fig, ax = plt.subplots(figsize=(7,7))
ax.bar(x, values, color=colors, width=0.6)
ax.set_xticks(x, years)
plt.show()

#51 스타일꾸미기
x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 500, 800]
colors = ['y', 'dodgerblue', 'C2']

fig, ax = plt.subplots(figsize=(7,7))
ax.bar(x, values, align='edge',edgecolor='lightgray', color=colors,
       linewidth=5, tick_label=years)
plt.show()

#(17) Matplotlib 수평 막대그래프 그리기
#52 기본사용
#harh() 함수 사용,  keyword:plt.barh()
y = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]
plt.barh(y, values)
plt.yticks(y, years)
plt.show()

#53 색상 지정하기
#step1 바 다 같은 색으로 지정
y = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]
plt.barh(y, values, color='y')
# plt.barh(y, values, color='dodgerblue')
# plt.barh(y, values, color='C2')
# plt.barh(y, values, color='#e35f62')
plt.yticks(y, years)
plt.show()

#step2 bar 마다 다른 색 지정
y = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]
colors = ['y', 'dodgerblue', 'C2']
plt.barh(y, values, color=colors)
plt.yticks(y, years)
plt.show()

#54 막대 높이 지정하기
y = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.barh(y, values, height=0.4)
#막대의 높이를 0.4/0.6/0.8/1.0으로 지정 가능, 디폴트는 0.8이다.
plt.show()

#55 스타일 꾸미기
y = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.barh(y, values, align = 'edge', edgecolor='#eee',
         linewidth=5, tick_label=years)
#align 은 눈금과 막대의 위치를 조절, 디폴트는 'center', 'edge'로 설정하며 막대의 아래쪽 끝에 눈금이 표시
#edgecolor는 막대의 테두리 색, linewidth 테두리의 두께 지정
#tick_label 리스트 또는 어레이 형태로 지정, 틱에 문자열을 순서대로 나타낼 수 있다.
plt.show()

#(18) Matplotlib 산점도 그리기
#56 기본사용
#keyword:plt.scatter(), scatter plot()

np.random.seed(0)

n = 50 # numpy의 random 모듈에 포함된 rand()함수를 사용해서 0,1 범위에 난수 각 50개씩 생성
x = np.random.rand(n)
y = np.random.rand(n)
plt.scatter(x, y)
plt.show()

#57 색상과 크기 지정하기
#step1
np.random.seed(0)
n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30 * np.random.rand(n))**2
colors = np.random.rand(n)

fig, ax = plt.subplots(figsize = (7,7))
ax.scatter(x, y, s = area, c=colors)
# scatter()에서 s,c파라미터는 각각 마커의 크기와 색상을 지정
#마커의 크기는 size **2의 형태로 지정 = plot()함수에 markersize=20으로 지정하는 것과 같다.
plt.show()

#step2
fig, ax = plt.subplots(figsize = (7, 7))
ax.plot([1], [1], 'o', markersize=20, c='r')
ax.scatter([2], [1], s = 20**2, c='b')

ax.text(0.5, 1.05, 'plot(markersize=20)', fontdict={'size':14})
ax.text(1.6, 1.05, 'scatter(s=20**2)', fontdict={'size':14})
ax.axis([0.4, 2.6, 0.8, 1.2])
plt.show()

#58 투명도와 컬러맵 설정하기
np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30 * np.random.rand(n))**2
colors = np.random.rand(n)

plt.scatter(x, y, s = area, c = colors, alpha=0.5, cmap='Spectral')
#alpha값은 마커의 투명도를 지정, 0~1사이의 값을 입력한다.
plt.colorbar()
plt.show()

#(19) Matplotlib 3차원 산점도 그리기
#Keyword:scatter(), 3Dscatterplot
#59 기본사용
from mpl_toolkits.mplot3d import Axes3D #3차원 그래프 그리기 위해
n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50 #범위 지정
cmin, cmax = 0, 2 #각각 다른 색으로 표현

xs = np.array([(xmax - xmin) * np.random.random_sample() + xmin for i in range(n)])
ys = np.array([(ymax - ymin) * np.random.random_sample() + ymin for i in range(n)])
zs = np.array([(zmax - zmin) * np.random.random_sample() + zmin for i in range(n)])
color = np.array([(cmax- cmin) * np.random.random_sample() + cmin for i in range(n)])
#위와 동일한 다른 방법
# xs = (xmax - xmin) * np.random.rand(n) + xmin
# ys = (xmax - xmin) * np.random.rand(n) + ymin
# zs = (xmax - xmin) * np.random.rand(n) + zmin
# color = (xmax - xmin) * np.random.rand(n) + cmin

fig, ax = plt.subplots(figsize = (7, 7))
ax = fig.add_subplot(111, projection = '3d') #3D axes 만들기 위해서 입력
ax.scatter(xs, ys, zs, c = color, marker = '*', s = 15, cmap = 'Greens')
plt.show()

#(20) Matplotlib 히스토그램 그리기
#Keyword : plt.hist(), histogram
#60 기본사용
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
fig, ax = plt.subplots(figsize = (7, 7))
ax.hist(weight)
plt.show()

#61 구간 개수 지정하기
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

fig, ax = plt.subplots(figsize = (7, 7))
ax.hist(weight, label = 'bins=10') # bins 값을 지정 하지 않아서 기본값인 10으로 지정
ax.hist(weight, bins=30, label = 'bins=30') # bins 값을 30으로 지정
ax.legend()
plt.show()

#62 누적 히스토그램 그리기
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
fig, ax = plt.subplots(figsize = (7, 7))
ax.hist(weight, cumulative=True, label='cumulative=True')
ax.hist(weight, cumulative=False, label='cumulative=False')
ax.legend(loc='upper left')
plt.show()

#63 히스토그램 종류 지정하기
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
        80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
weight2 = [52, 67, 84, 66, 58, 78, 71, 57, 76, 62, 51, 79,
        69, 64, 76, 57, 63, 53, 79, 64, 50, 61]

plt.hist((weight, weight2), histtype='bar')
plt.title('histtype - bar')
plt.figure()

plt.hist((weight, weight2), histtype='barstacked')
plt.title('histtype - barstacked')
plt.figure()

plt.hist((weight, weight2), histtype='step')
plt.title('histtype - step')
plt.figure()

plt.hist((weight, weight2), histtype='stepfilled')
plt.title('histtype - stepfilled')
plt.show()

#64 NumPy 난수의 분포 나타내기
a = 2.0 * np.random.randn(10000) + 1.0
# 어레이 a는 표준편차 2.0, 평균 1.0
b = np.random.standard_normal(10000)
# 어레이 b는 표준정규분포
c = 20.0 * np.random.rand(5000) - 10.0
# 어레이 c는 -10.0에서 10.0상에 균일한 분포를 갖는 5000개의 임의의 값
plt.hist(a, bins=100, density=True, alpha=0.7, histtype='step')
#density=True 밀도함수가 되어서 막대의 아래 면적이 1이 된다.
plt.hist(b, bins=50, density=True, alpha=0.5, histtype='stepfilled')
plt.hist(c, bins=100, density=True, alpha=0.9, histtype='step')
plt.show()