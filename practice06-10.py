import matplotlib.pyplot as plt
import numpy as np

#(06) Matplotlib 선 종류 지정하기
#19 선 종류 지정하기
plt.plot([1, 2, 3], [4, 4, 4], '-', color='b', label='Solid')
plt.plot([1, 2, 3], [3, 3, 3], '--', color='b',label='Dashed')
plt.plot([1, 2, 3], [2, 2, 2], ':', color='b', label='Dotted')
plt.plot([1, 2, 3], [1, 1, 1], '-.', color='b', label='Dash-dot')
plt.axis([0.9, 3.1, 0.5, 5.1])
# axis_range = plt.axis()
# print(axis_range)
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.legend(loc='upper right', fontsize=10, ncol=4)
plt.show()

#20 linestyle(위랑 같은 것)
plt.plot([1, 2, 3], [4, 4, 4], linestyle='solid', color='r', label='Solid')
plt.plot([1, 2, 3], [3, 3, 3], linestyle='dashed', color='r',label='Dashed')
plt.plot([1, 2, 3], [2, 2, 2], linestyle='dotted', color='r', label='Dotted')
plt.plot([1, 2, 3], [1, 1, 1], linestyle='dashdot', color='r', label='Dash-dot')
plt.axis([0.9, 3.1, 0.5, 5.1])
# axis_range = plt.axis()
# print(axis_range)
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.legend(loc='upper right', fontsize=10, ncol=4)
plt.show()

#21 튜플을 사용해서 선 그리기
plt.plot([1, 2, 3], [4, 4, 4], linestyle=(0, (1, 1)), color='C0', label='(0, (1, 1))')
plt.plot([1, 2, 3], [3, 3, 3], linestyle=(0, (1, 5)), color='C0', label='(0, (1, 5))')
plt.plot([1, 2, 3], [2, 2, 2], linestyle=(0, (5, 1)), color='C0', label='(0, (5, 1))')
plt.plot([1, 2, 3], [1, 1, 1], linestyle=(0, (3, 5, 1, 5)), color='C0', label='(0, (3, 5, 1, 5))')
plt.axis([0.9, 3.1, 0.5, 5.1])
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.legend(loc='upper left', fontsize=10, ncol=2)
plt.show()

#22 선 끝 모양 지정하기
plt.plot([1, 2, 3], [4, 4, 4], linestyle='solid', linewidth=10,
      solid_capstyle='butt', color='C0', label='solid+butt')
plt.plot([1, 2, 3], [3, 3, 3], linestyle='solid', linewidth=10,
      solid_capstyle='round', color='g', label='solid+round')

plt.plot([1, 2, 3], [2, 2, 2], linestyle='dashed', linewidth=10,
      dash_capstyle='butt', color='r', label='dashed+butt')
plt.plot([1, 2, 3], [1, 1, 1], linestyle='dashed', linewidth=10,
      dash_capstyle='round', color='C1', label='dashed+round')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis([0.8, 3.2, 0.5, 5.0])
plt.legend(loc='upper center', ncol=2)
plt.tight_layout()
plt.show()

#(07) Matplotlib 마커 지정하기
#23 마커 지정하기
plt.plot([1, 2, 3, 4], [3, 5, 7, 10], 'bo')
#'bo' blue, 'o' circle
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

#24 선/마커 동시에 나타내기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], 'bo-') #실선
plt.plot([1, 2, 3, 4], [3, 5, 7, 10], 'r*--') #점선
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

#25 marker 파라미터 사용하기
plt.plot([4, 5, 6], marker='H')
plt.plot([3, 4, 5], marker='d')
plt.plot([2, 3, 4], marker='x')
plt.plot([1, 2, 3], marker=11)
plt.plot([0, 1, 2], marker='$z$')
plt.show()

#(08) Matplotlib 색상 지정하기
#26 포맷 문자열 사용하기
plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], 'r')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], 'g')
plt. plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], 'b')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

#27 color 키워드 인자 사용하기
plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], color='limegreen')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color='violet')
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color='dodgerblue')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

#28 Hex code 사용하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], color='#e35f62',
         marker='o', linestyle='--')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

#(09) Matplotlib 그래프 영역 채우기
#29 기본사용 - fill_between()
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y[1:3], alpha=0.5)
plt.show()

#30 기본사용 - fill_betweenx()
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_betweenx(y[2:4], x[2:4], alpha=0.5)
plt.show()

#31 두 그래프 사이 영역 채우기
x = [1, 2, 3, 4]
y1 = [2, 3, 5, 10]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y1[1:3], y2[1:3], color='lightgray', alpha=0.5)
plt.show()

#32 다각형 영역 채우기 fill()
x = [1, 2, 3, 4]
y1 = [2, 3, 5, 10]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill([1.9, 1.9, 3.1, 3.1], [1.0, 4.0, 6.0, 3.0],
         color='lightgray', alpha=0.5)
plt.show()

#(10) Matplotlib 축 스케일 지정하기
#33 X축 스케일 지정하기
x = np.linspace(-10, 10, 100)
y = x ** 3

plt.plot(x, y)
plt.xscale('symlog')
plt.show()

#34 Y축 스케일 지정하기
x = np.linspace(0, 5, 100)
y = np.exp(x)

plt.plot(x, y)
plt.yscale('linear')
# plt.yscale('log')
plt.show()
