import matplotlib.pyplot as plt
import numpy as np

#(11) Matplotlib 여러 곡선 그리기
#35 기본
x = np.arange(0, 2, 0.2)
plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g-.')
plt.show()

#36 스타일 지정하기
x = np.arange(0, 2, 0.2)
plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=1)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.show()

#(12) Matplotlib 그리드 설정하기
#37 기본 사용
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.grid(True)
plt.show()

#38 축 지정하기
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
# plt.grid(True, axis='x')
plt.grid(True, axis='y')
plt.show()

#39 스타일 설정하기
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.grid(True, axis='y', color='red', alpha=0.5, linestyle='--')
plt.show()


#(13) Matplotlib 눈금 표시하기
#40 기본 사용
x = np.arange(0, 2, 0.2)
plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=1)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.xticks([0, 1, 2])
plt.yticks(np.arange(1,6))
plt.show()

#40-1 기본 사용
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.tick_params(axis='both', direction='in', length=3, pad=6, labelsize=14)
plt.title('Graph Title')

plt.show()

#41 눈금 스타일 설정하기
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='red', marker = '*', linewidth = 2)
plt.plot(x, x**3, color='green', marker = '^', markersize=9)
plt.xticks(np.arange(0, 2, 0.2), labels = ['Jan', '', 'Mar', '', 'May', '', 'July', '', 'Sep', ''])
plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))
plt.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=14,
                labelcolor = 'blue', top=True)
plt.tick_params(axis='y', direction='inout', length=10, pad=15, labelsize=14,
                width=2, color = 'springgreen')
plt.show()

#(14) Matplotlib 타이틀 설정하기
#42 기본사용
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='red', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^',markersize=9)
plt.tick_params(axis='both', direction='in', length=3, pad=6, labelsize=14)
plt.title('Graph Title')
plt.show()

#43 위치와 오프셋 지정하기
x = np.arange(0, 2, 0.2)

#step1 - fig 사용
fig,ax = plt.subplots(figsize = (7, 7))
ax.plot(x, x, 'bo')
ax.plot(x, x**2, color = '#e35F62', marker = '*', linewidth = 2)
ax.plot(x, x**3, color = 'forestgreen', marker = 'o')
ax.tick_params(axis = 'both', direction='in', length=3, pad = 6, labelsize=12)
ax.set_title('Graph Title', loc='right', pad = 18)
plt.show()

#step2 - plt 사용
plt.plot(x, x, 'bo')
plt.plot(x, x**2, color = '#e35F62', marker = '*', linewidth = 2)
plt.plot(x, x**3, color = 'forestgreen', marker = 'o')
plt.tick_params(axis = 'both', direction='in', length=3, pad = 6, labelsize=12)
plt.title('Graph Title', loc='right', pad = 18)
#plt.tilte loc 는 위치 지정 ('left', 'right', 'center')
#pad 는 타이틀과 그래프간의 간격
plt.show()

#44 폰트 지정하기
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='red', marker = '^', linewidth = 3)
plt.plot(x, x**3, color='green', marker = '*', markersize = 5)

plt.tick_params(axis = 'both', direction='in', length=3, pad = 6, labelsize = 12)
plt.title('Graph Title', loc='right', pad=20)

title_font = {'fontsize':12, 'fontweight':'bold'}
# title_font 안에 fontsize 는 12로 지정, fontweight는 'bold'로 설정
# fontsize는 smaller 이나 x-large 로 상대적인 설정도 가능하며,
# fontweight는 [normal, bold, heavy, light, ultrabold, ultralight] 설정 가능
plt.title('Graph Title', fontdict=title_font, loc='left', pad=20)
plt.show()

#45 타이틀 얻기
x = np.arange(0, 2, 0.3)
plt.plot(x, x, 'ro')
plt.plot(x, x**2, color='blue', marker='*', linewidth=2)
plt.plot(x, x**3, color='green', marker='^', markersize=5)
plt.tick_params(axis='both', direction='in', length=3, pad=6, labelsize=12)
title_right = plt.title('Graph Title', loc = 'right', pad=20)
title_font = {'fontsize':13, 'fontweight':'heavy'}
title_left = plt.title('Graph Title', fontdict=title_font, loc='left', pad=20)

print(title_left.get_position())
print(title_left.get_text())
#get_position(), get_text() 사용해서 텍스트의 위치와 문자열을 알 수 있다.
print(title_right.get_position())
print(title_right.get_text())

plt.show()

#(15) Matplotlib 수평선/수직선 표시하기
#axhline(): 수평선, axvline(): 수직선을 표시
#hlines(): 지정한 점을 따라 수평선, vlines(): 수직선 표시
# Keyword: plt.axhline(), plt.hlines(), plt.axvline(),  plt.vlines(), 수직선, 수평선

#46 수평선 그리기 - axhline()->점선, hlines()->일직선
x = np.arange(0, 4, 0.5)
plt.plot(x, x + 1, 'r*')
plt.plot(x, x**2 - 4, 'g--')
plt.plot(x, -2*x + 3, 'b:')

plt.axhline(4.0, 0.1, 0.9, color='lightgray', linestyle='--', linewidth=2)
#axhline()함수는 첫번째인자(4.0)는 y값으로 수평선의 위치하고,
#두,세번째는 xmin, xmax 값으로 0에서 1사이의 값입력 0은 왼쪽 끝, 1은 오른쪽 끝
plt.hlines(-0.62, 1.0, 2.5, color='gray', linestyle='solid', linewidth=3)
#hline()함수에서 y, xmin, xmax, 순서대로 입력하면, 점(xmin, y)와 점 (xmax, y) 따라 수평선 표시
plt.show()

#47 수직선 그리기 - axhline(), vlines()
x = np.arange(0, 4, 0.5)
plt.plot(x, x + 1, 'bo')
plt.plot(x, x**2 - 4, 'r--')
plt.plot(x, -2*x + 3, 'g:')

plt.axvline(1.0, 0.2, 0.8, color='black', linestyle = '--', linewidth=2)
#axvline()함수 첫번째 인자는 x값으로 수직선의 위치가 된다.
#두,세번째 인자는 ymin, ymax 값으로 0에서 1사이의 값 입력 하고, 0은 아래쪽 끝, 1은 위쪽 끝
plt.vlines(1.8, -3.0, 2.0, color='gray', linestyle='solid', linewidth=3)
#vlines()함수에 x, ymin, ymax를 순서대로 입력하면 점(x,ymin), 점(x, ymax)따른 수평선
plt.show()