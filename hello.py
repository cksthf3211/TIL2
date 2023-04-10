import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint


# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외

rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

rate = 0
sum = 0

for i in range(20):
    subject, score, grade = input().split()
    if grade == "P":
        continue
    rate += float(score) * rating[grade]
    sum += float(score)

print(rate/sum)
