# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:46:21 2016

@author: ajea6201
"""
#第一次作業(10/12)畫出+C-C，+P-P，任一選擇權策略
#######第一題##########
#K=30,S=30
#S=10~50
#C=3
#payoff of buy and sell a call
import numpy as np #陣列的package
x=np.arange(10,51) #R的seq,只是不包括最後的數字
K=30 #履約價
C=2 #權利金
y1_C=np.maximum(np.subtract(x,K),0)-C 
#np.subtract相減,矩陣的加減乘除皆需透過外面一個程式碼包著
#若想要陣列裡的每一個元素都比大小,只能用p.maximum,不可用np.max
y2_C=-y1_C
import matplotlib.pyplot as mb #畫圖的package
mb.subplot(211) 
#把圖併在一起，第一個數字表示上下幾張圖，第二個數字為左右幾張圖
#第三個數字為接下來是第幾張圖
mb.plot(x,y1_C,label="Buy Call")
mb.plot(x,y2_C,label="Sell Call")
#想要畫多條線，多寫幾個plot就對了
mb.legend(loc='upper left')
mb.ylabel("payoff")
#mb.xlabel("St")
mb.title("Buy and Sell a Call")
mb.show

########第二題############
#payoff of buy and sell a put
P=2
y1_P=np.maximum(np.subtract(K,x),0)-P
y2_P=-y1_P
mb.subplot(212)
mb.plot(x,y1_P,label="Buy Put")
mb.plot(x,y2_P,label="Sell Put")
mb.legend(loc='upper right') #圖例在右上角
mb.ylabel("payoff")
mb.xlabel("St")
mb.title("Buy and Sell a Put")

###########第三題###########
#畫BullSpread 買一個call(K低)賣一個call(K高)
K1=25
K2=35
C1=6 #價內較貴
C2=2 #價外較便宜
y1_C1=np.maximum(np.subtract(x,K1),0)-C1
y1_C2=-np.maximum(np.subtract(x,K2),0)+C2
y1_bull=y1_C1+y1_C2
mb.plot(x,y1_C1,label="Buy low K Call")
mb.plot(x,y1_C2,label="Sell high K Call")
mb.plot(x,y1_bull,label="Bull Spread")
mb.legend(loc='upper left')
mb.ylabel("payoff")
mb.xlabel("St")
mb.title("Bull Spread")
mb.show