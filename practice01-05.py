import matplotlib.pyplot as plt
import numpy as np

#(01) Matplotlib 기본 사용하기
#01 그래프에 별 찍기 (스타일 지정하기)
plt.plot([1, 2, 3, 4], [1, 4, 6, 9], 'b-')  #세번째 인자에 r*, g+ 넣는거에 따라 다른 출력값을 얻는다.
plt.axis([0, 6, 0, 10])  #[xmin, xmax, ymin, ymax]
plt.show()

#02 3가지 모양 찍기 (여러개 그래프 그리기)
fig, ax = plt.subplots(figsize=(5,5))
ax.set_xlim(0, 5)
ax.set_ylim(0, 50)

t = np.arange(0., 5., 0.2)  #0.2는 200ms 간격으로 균일하게

plt.plot(t, t, 'r*', t, t**3, 'bs', t, t**4, 'g^')
plt.show()

#(02) Matplotlib 숫자 입력하기
#03 그래프 그리기
plt.plot([1, 2, 5, 10])
plt.show()

#04 x, y축 지정해서 꺾은선 그래프
plt.plot([1, 2, 5, 10], [3, 6, 8, 15])
plt.show()

#05 dict 지정해서 그래프 그리기 (레이블이 있는 데이터 사용하기)
data_dict = {'data_x' : [1, 2, 3, 4, 5], 'data_y' : [2, 3, 5, 10, 8]}
plt.plot('data_x', 'data_y', data=data_dict)
plt.show()

#(03) Matplotlib 축 레이블 설정하기
#06 라벨 만들기
plt.plot([1, 2, 3, 4], [4, 9, 10, 14])
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.show()

#07 여백만들기(label_pad)
plt.plot([1, 2, 3, 4], [4, 9, 10, 14])
plt.xlabel('X-axis', labelpad=15)
plt.ylabel('y-axis', labelpad=20)
plt.show()

#08 폰트 설정하기
font1 = {'family':'monospace',
         'color':'deeppink',
         'weight':'bold',
         'size':15}

font2 = {'family':'fantasy',
         'color':'skyblue',
         'weight':'normal',
         'size':15}

plt.plot([1, 2, 3, 4], [4, 9, 10, 14])
plt.xlabel('X-label', labelpad=15, fontdict=font1)
plt.ylabel('Y-label', labelpad=15, fontdict=font2)
plt.show()

#09 위치 지정하기
plt.plot([1, 2, 3, 4], [3, 5, 8, 10])
plt.xlabel('X-label', loc='right')
plt.ylabel('Y-label', loc='top')
plt.show()

#(04) Matplotlib 범례(legend) 표시하기
#10 legend 만들기
plt.plot([1, 2, 3, 4], [3, 5, 8, 10], 'r*', label='star*')
plt.xlabel('xlabel', loc='center')
plt.ylabel('ylabel', loc='center')
plt.legend()
plt.show()

#11 위치 지정하기(1)
plt.plot([1, 2, 3, 4], [3, 5, 8, 10], 'r*', label='star*')
plt.xlabel('x_axis', loc='left')
plt.ylabel('y_axis', loc='bottom')
plt.legend(loc=(0.0, 0.5))
plt.show()

#11-1 위치 지정하기(2)
#legend 숫자 입력도 되고, 이름 입력도 된다.
plt.plot([1, 2, 3, 4], [3, 5, 8, 10], 'r*', label='star*')
plt.xlabel('x_axis', loc='left')
plt.ylabel('y_axis', loc='bottom')
plt.legend(loc='upper left')
plt.show()

#12 열 개수를 지정하기 (ncol)
plt.plot([1, 2, 3, 4], [3, 5, 9, 7],  label='Blue square')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6], label='Red star')
plt.xlabel('Xlabel', loc='center')
plt.ylabel('Ylabel', loc='center')
plt.legend(loc='best', ncol=2)  #best?
plt.show()

#13 legend 폰트 지정하기
plt.plot([1, 2, 3, 4], [3, 5, 9, 14],  label='Blue square')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6], label='Red star')
plt.xlabel('Xlabel', loc='center')
plt.ylabel('Ylabel', loc='center')
plt.legend(loc='best', ncol=1, fontsize=15)
plt.show()

#14 legend 테두리 꾸미기
plt.plot([1, 2, 3, 4], [3, 5, 9, 14],  label='Blue square')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6], label='Red star')
plt.xlabel('Xlabel', loc='center')
plt.ylabel('Ylabel', loc='center')
plt.legend(loc='best', ncol=1, fontsize=10, frameon=False, shadow=False)
plt.show()

#(05) Matplotlib 축 범위 지정하기
#15 기본사용 (xlim, ylim, axis 사용가능)
plt.plot([1, 2, 3, 4], [1, 5, 8, 12], c='darkblue', label='chocolate')
plt.xlabel('x_label', loc='center')
plt.ylabel('y_label', loc='center')
plt.xlim(0, 5)
plt.ylim(0, 15)
plt.legend(loc='best', fontsize=10, frameon=True, shadow=False)
plt.show()

#16 axis() 사용하기
plt.plot([1, 2, 3, 4], [1, 5, 8, 12], c='darkblue')
plt.xlabel('x_label', loc='center')
plt.ylabel('y_label', loc='center')
plt.axis([0, 5, 0, 15])  #x, y축의 범위 : [xmin, xmax, ymin, ymax]
plt.show()

#17 옵션 지정하기
#axis() 옵션 ('on', 'off', 'equal', 'scaled',  'tight',  'auto',  'normal',  'image',  'square')
plt.plot([1, 2, 3, 4], [1, 5, 8, 12], c='darkred')  # c 컽러 입력해주기
plt.xlabel('x_label', loc='center')   # loc는 위치를 나타낸다.
plt.ylabel('y_label', loc='center')
plt.axis('scaled')
plt.show()

#18 축범위 얻기
plt.plot([1, 2, 3, 4], [2, 5, 7, 10])
plt.xlabel('x_axis')
plt.ylabel('y_axis')
x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)

axis_range = plt.axis()
print(axis_range)    #xlim, ylim 같은 결과 값이 나온다.

plt.show()
