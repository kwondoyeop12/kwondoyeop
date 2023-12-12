
# list_1 = [1, 2, 3, 4, 5, 1, 3]
# list_2 = []
# list_1
# list_2
# len(list_1)
# list_1[3] = 9999
# list_1
# list_1.append(100)
# list_1
# list_1.remove(9999)
# list_1
# list_1.insert(0,777)
# list_1
# list_2 = list_1.copy()
# list_2

# list_1 = [897, 2, 1, 4, 99, 5, 24, 17]
# list_1
# list_1.reverse()
# list_1
# list_1.sort()
# list_1
# list_1.sort(reverse=True)
# list_1






# st.write("파이썬의 세계에 오신 것을 환영합니다")

# grade = 72

# if grade >= 90:
#     'A'
# elif grade >= 80:
#     'B'
# elif grade >= 70:
#     'C'
# elif grade >= 60:
#     'D'
# else:
#     'F'

# a = 5
# if a < 5:
#     'a is smaller than 5'
# elif a >5:
#     'a is larger than 5'
# else:
#     'a is 5'

# a = 3
# for a in range(2,10):
#     ''
#     a, '단입니다.'
#     for i in range(1,10,1):
#         b = str(a) + 'X' + str(i) + '=' + str(a*i)
#         b

# st.write("저는 그런거 잘 모르겠고, 그냥 직진할게요")

# dict_1 = {'name' : '안유진', 
#           'birth' : 2003, 
#           'height' : 173,
#           'weight' : '45kg', 
#           'family' : '상상의 여자친구',
#           'hobby' : '쇼핑, 운동, 독서',
#           'addr' : 'KR'}
# dict_1

# dict_1.update({'job' : 'IDOL', 'hometown' : 'daejeon'})
# dict_1

# del dict_1['name']
# del dict_1['birth']
# del dict_1['addr']
# dict_1

# for key in dict_1.keys():
#     key
# '=========================================================================='
# for v in dict_1.values():
#     v

# '=========================================================================='
# for k, v in dict_1.items():
#     k
#     v

# list_1 = [1, 2, 7, 4, 50, 33]
# s = sum(list_1)
# mx = max(list_1)
# mn = min(list_1)
# s, mx, mn

# list_1

# def sta(arr):
#     sum = 0 # 초기값
#     mx = -1e10
#     mn = 1e10
#     for i in arr:
#         sum = sum + i
#         if mx < i:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     'sum =', sum, 'min =', mn, 'max =', mx

# sta([5, 13, 7, 4, 11])

# s = 0
# for i in range(1, 100+1):
#     s = s + i
    
# s

# list_1 = [5, 13, 7, 4, 11]
# [s1, mx1, mn1] = sta(list_1)
# s1, mx1, mn1

# sta(list_1)
# s = sum(list_1)
# mx = max(list_1)
# mn = min(list_1)

# s, mx, mn

import streamlit as st
import turtle
import numpy as np

# list_1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# a = np.array(list_1)
# for i in range(4):
#     list_1[i] = list_1[1] + 3
# list_1

# a = np.array(list_1)
# a

# a.shape
# s = a.sum(axis=0)
# s
# z = a.min(axis=1)
# z
# a[1, :] = 18
# a
# n = np.ones((10,5))
# n+99
# n = np.full((10,5), 7)

# n = np.eye(5)
# n

# def yser_eye(n):
#     arr = np.zeros((n,n))
#     for i in in range(n):
#         for j in range(n):
#             if i == j:
#                 arr[i, j] = 1

# a = np.zeros(2)
# 'a/n', a
# b = np.zeros((2,2))
# 'b/n', b
# c = np.ones((2,3))
# 'c/n', c
# d = np.full((2,3), 5)
# 'd/n', d
# e = np.eye(3)
# 'e/n', e

# n = 100
# for i in range(1, n+1):
#     if i&7 == 3:
#         i


# n = 3
# arr = np.full((n,n),'    ')
# arr
# for i in range(n):
#     for j in range(n):
#         arr[i,j] = '나머지'
#         if i == j or i + j == n-1:
#             arr[i, j] = '대'

# arr

# a = np.arange(8)
# a
# a.shape = (4, 2)
# a
# b = a.flatten()
# b


# b = b.resize((2,4))
# b

# import os
# os.system('cls')

# a = np.array((1, 10, -5, 2))
# print(abs(a))
# print(np.sqrt(a))
# print(a**0,5)
# print(np.square(a))
# print(a**2)

# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")
# t.width(3)
# t.speed(0)

# t.penup()
# t.goto(-200, 0)
# t.pendown()

# def shape(n):
#     for _ in range(n):
#         t.forward(1 + 5*i)
#         t.left(360/n)

# while True:
#     for i in range(20):
#         shape(5)
#         t.color(( random.random(), random.random(), random.random()) )
#         t.goto(i*20, 0)
#     t.clear

# turtle.done

import os
os.system('cls')

# li = [1, 2, 3, 4]
# li

# for i in range(4):
#     li[i] = li[i] + 3
# li
# li = np.array({1, 2, 3, 4})
# li

import streamlit as st
import pandas as pd

# list1 = list([['한빛', '남자', '20', '180'],
#               ['한결', '남자', '21', '177'],
#               ['김한결', '중성', '51', '155'],
#               ['한라', '여자', '20', '160']])
# n = np.array(list1)
# col_names = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_names, index=['1행', '2행', '3행', '4행'])
# df


# genre = st.radio("선택하시오.", ["오름차순", "내림차순", "기타", "요약"],
#       horizontal=True, index=2)
# number = st.number_input('Insert a number', value=28, step=1)
# df.iloc[3, 2] = number
# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'], ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df.describe())

import streamlit as st

# st.write('Hello, *World!* :sunglasses:')

import os
# os.system('cls')

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# a = 2
# b = -5
# c = 3
# d = -7

# x = []
# y = []
# for i in range(-100, 101, 50):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)

# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('색을 선택하시오-', ('red', 'green', 'blue'))
# with col2:
#     linestyle = st.radio('선의 스타일을 선택하시오-', ('-', '-.', ':'))
# with col3:
#     marker = st.radio('마커를 선택하시오-', ('s', '^', 'o'))
# if 'red' in colar:
#     t = '-.r^'
# if 'green' in colar:
#     t = '-.g^'
# if 'blue' in colar:
#     t = '-.b^'
    
# plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)

# x = []
# y = []
# for i in range(-10, 11, 2):
#     x.append(i)
#     y.append(3*i**3 - 5*i**2 - 7)


# cc = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange', 'yellow'])
# ma = st.radio('마커의 형태를 선택하시오',['o', '^', 's', 'p', 'h'])
# ls = st.radio('선의 형태를 선택하시오',['-', '-.', ':', '--'])

# plt.plot(x,y, color=cc, linestyle=ls, marker=ma)
# st.pyplot(fig)

git init
git add .
git commit -m "Initial commit"



col1, col2 = st.columns(2)
with col1:
    st.image('dream.jpg', width=300)
with col2:
    st.write('판매명 : 토끼, 가격 : 2만원, 맛있음')
    '판매문의(☎️) : 010-5582-5859😁'
    '이메일(📧) : streamlit@konyang.ac.kr'
    '주소(🏤) : 충청남도 논산시 대학로121'
