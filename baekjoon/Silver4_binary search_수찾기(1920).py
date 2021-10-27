# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
## 1920번 수 찾기

N = int(input())
A = set(map(int, input().split()))
M = int(input())
target = list(map(int,input().split()))

for i in range(M) :
    if target[i] in A :
        print("1")
    else :
        print("0")
