import numpy as np
import os
import cv2
from cv2 import *
import sys
import time
import json
def main():
    # front = {'f1': 'yellow', 'f2': 'white', 'f3': 'green', 'f4': 'red', 'f5': 'blue', 'f6': 'white', 'f7': 'green', 'f8': 'orange', 'f9': 'yellow'}
    # right = {'r1': 'red', 'r2': 'orange', 'r3': 'yellow', 'r4': 'blue', 'r5': 'yellow', 'r6': 'orange', 'r7': 'blue', 'r8': 'green', 'r9': 'yellow'}
    # back = {'b1': 'red', 'b2': 'red', 'b3': 'blue', 'b4': 'green', 'b5': 'green', 'b6': 'white', 'b7': 'red', 'b8': 'blue', 'b9': 'blue'}
    # left = {'l1': 'orange', 'l2': 'yellow', 'l3': 'orange', 'l4': 'orange', 'l5': 'white', 'l6': 'yellow', 'l7': 'red', 'l8': 'green', 'l9': 'white'}
    # top = {'t1': 'white', 't2': 'blue', 't3': 'green', 't4': 'green', 't5': 'orange', 't6': 'yellow', 't7': 'green', 't8': 'red', 't9': 'white'}
    # bottom = {'bo1': 'orange', 'bo2': 'blue', 'bo3': 'orange', 'bo4': 'white', 'bo5': 'red', 'bo6': 'red', 'bo7': 'white', 'bo8': 'yellow', 'bo9': 'blue'}

    front = {'f1': 'orange', 'f2': 'blue', 'f3': 'blue', 'f4': 'orange', 'f5': 'blue', 'f6': 'blue', 'f7': 'orange', 'f8': 'blue', 'f9': 'blue'}
    right = {'r1': 'yellow', 'r2': 'yellow', 'r3': 'yellow', 'r4': 'yellow', 'r5': 'yellow', 'r6': 'yellow', 'r7': 'yellow', 'r8': 'yellow', 'r9': 'yellow'}
    back = {'b1': 'green', 'b2': 'green', 'b3': 'red', 'b4': 'green', 'b5': 'green', 'b6': 'red', 'b7': 'green', 'b8': 'green', 'b9': 'red'}
    left = {'l1': 'white', 'l2': 'white', 'l3': 'white', 'l4': 'white', 'l5': 'white', 'l6': 'white', 'l7': 'white', 'l8': 'white', 'l9': 'white'}
    top = {'t1': 'green', 't2': 'orange', 't3': 'orange', 't4': 'green', 't5': 'orange', 't6': 'orange', 't7': 'green', 't8': 'orange', 't9': 'orange'}
    bottom = {'bo1': 'blue', 'bo2': 'red', 'bo3': 'red', 'bo4': 'blue', 'bo5': 'red', 'bo6': 'red', 'bo7': 'blue', 'bo8': 'red', 'bo9': 'red'}


    corners = dict()
    edges = dict()

    corners['c1'] = []
    corners['c2'] = []
    corners['c3'] = []
    corners['c4'] = []
    corners['c5'] = []
    corners['c6'] = []
    corners['c7'] = []
    corners['c8'] = []
    temp = {}
    temp_edge = {}
    solved_state = {0:'orange', 1:'blue', 2:'orange', 3:'yellow', 4:'orange', 5:'green', 6:'orange', 7:'white', 8:'red',
           9:'blue', 10:'red',11:'yellow', 12:'red', 13:'green', 14:'red', 15:'white', 16:'blue', 17:'yellow',
           18:'blue', 19:'white', 20:'green', 21:'yellow', 22:'green', 23:'white', 24:'orange', 25:'blue',
           26:'yellow', 27:'orange', 28:'yellow', 29:'green', 30:'orange', 31:'green', 32:'white', 33:'orange',
           34:'white', 35:'blue', 36:'red', 37:'yellow', 38:'blue', 39:'red', 40:'blue', 41:'white', 42:'red',
           43:'white', 44:'green', 45:'red', 46:'green', 47:'yellow'}


    build_corners(corners, 'c1', front['f1'])
    build_corners(corners, 'c1', top['t7'])
    build_corners(corners, 'c1', left['l3'])
    temp['c1'] = ['F', 'U', 'L']

    build_corners(corners, 'c2', front['f3'])
    build_corners(corners, 'c2', top['t9'])
    build_corners(corners, 'c2', right['r1'])
    temp['c2'] = ['F', 'U', 'R']

    build_corners(corners, 'c3', right['r3'])
    build_corners(corners, 'c3', top['t3'])
    build_corners(corners, 'c3', back['b1'])
    temp['c3'] = ['R', 'U', 'B']

    build_corners(corners, 'c4', back['b3'])
    build_corners(corners, 'c4', top['t1'])
    build_corners(corners, 'c4', left['l1'])
    temp['c4'] = ['B', 'U', 'L']

    build_corners(corners, 'c5', front['f7'])
    build_corners(corners, 'c5', bottom['bo1'])
    build_corners(corners, 'c5', left['l9'])
    temp['c5'] = ['F', 'D', 'L']

    build_corners(corners, 'c6', front['f9'])
    build_corners(corners, 'c6', bottom['bo3'])
    build_corners(corners, 'c6', right['r7'])
    temp['c6'] = ['F', 'D', 'R']

    build_corners(corners, 'c7', right['r9'])
    build_corners(corners, 'c7', bottom['bo9'])
    build_corners(corners, 'c7', back['b7'])
    temp['c7'] = ['R', 'D', 'B']

    build_corners(corners, 'c8', back['b9'])
    build_corners(corners, 'c8', bottom['bo7'])
    build_corners(corners, 'c8', left['l7'])
    temp['c8'] = ['B', 'D', 'L']

    edges['e1'] = []
    edges['e2'] = []
    edges['e3'] = []
    edges['e4'] = []
    edges['e5'] = []
    edges['e6'] = []
    edges['e7'] = []
    edges['e8'] = []
    edges['e9'] = []
    edges['e10'] = []
    edges['e11'] = []
    edges['e12'] = []

    edges['e1'].append(front['f2'])
    edges['e1'].append(top['t8'])
    temp_edge['e1'] = ['F', 'U']

    edges['e2'].append(right['r2'])
    edges['e2'].append(top['t6'])
    temp_edge['e2'] = ['R', 'U']

    edges['e3'].append(back['b2'])
    edges['e3'].append(top['t2'])
    temp_edge['e3'] = ['B', 'U']

    edges['e4'].append(left['l2'])
    edges['e4'].append(top['t4'])
    temp_edge['e4'] = ['L', 'U']

    edges['e5'].append(front['f8'])
    edges['e5'].append(bottom['bo2'])
    temp_edge['e5'] = ['F', 'D']

    edges['e6'].append(right['r8'])
    edges['e6'].append(bottom['bo6'])
    temp_edge['e6'] = ['R', 'D']

    edges['e7'].append(back['b8'])
    edges['e7'].append(bottom['bo8'])
    temp_edge['e7'] = ['B', 'D']

    edges['e8'].append(left['l8'])
    edges['e8'].append(bottom['bo4'])
    temp_edge['e8'] = ['L', 'D']

    edges['e9'].append(front['f6'])
    edges['e9'].append(right['r4'])
    temp_edge['e9'] = ['F', 'R']

    edges['e10'].append(right['r6'])
    edges['e10'].append(back['b4'])
    temp_edge['e10'] = ['R', 'B']

    edges['e11'].append(back['b6'])
    edges['e11'].append(left['l4'])
    temp_edge['e11'] = ['B', 'L']

    edges['e12'].append(left['l6'])
    edges['e12'].append(front['f4'])
    temp_edge['e12'] = ['L', 'F']
    cube = dict()
    position = dict()
    p = {'e1':'F', 'e2':'R', 'e3':'B', 'e4':'L', 'e5':'F', 'e6':'R', 'e7':'B', 'e8':'L', 'e9':'F', 'e10':'L', 'e11':'B', 'e12':'L'}

    for pos, color in edges.items():

        if set(color) == set(['yellow', 'orange']):
            for i in range(len(color)):
                if color[i] == 'yellow':
                    position['3'] = temp_edge[pos][i]
                else:
                    position['2'] = temp_edge[pos][i]

    #-----------------------------------------------------------------------------------------------

        elif set(color) == set(['orange', 'blue']):
            for i in range(len(color)):
                if color[i] == 'orange':
                    position['0'] = temp_edge[pos][i]
                else:
                    position['1'] = temp_edge[pos][i]


    #-------------------------------------------------------------------------------------------------

        elif set(color) == set(['orange','green']):
            for i in range(len(color)):
                if color[i] == 'orange':
                    position['4'] = temp_edge[pos][i]
                else:
                    position['5'] = temp_edge[pos][i]


    #---------------------------------------------------------------------------------------------------

        elif set(color) == set(['orange', 'white']):
            for i in range(len(color)):
                if color[i] == 'orange':
                    position['6'] = temp_edge[pos][i]
                else:
                    position['7'] = temp_edge[pos][i]


    #---------------------------------------------------------------------------------------------------

        elif set(color) == set(['red', 'blue']):
            for i in range(len(color)):
                if color[i] == 'red':
                    position['8'] = temp_edge[pos][i]
                else:
                    position['9'] = temp_edge[pos][i]

    #-----------------------------------------------------------------------------------------------------

        elif set(color) == set(['red', 'yellow']):
            for i in range(len(color)):

                if color[i] == 'red':
                    position['10'] = temp_edge[pos][i]
                else:
                    position['11'] = temp_edge[pos][i]

    #-----------------------------------------------------------------------------------------------------------

        elif set(color) == set(['red', 'green']):
            for i in range(len(color)):
                if color[i] == 'red':
                    position['12'] = temp_edge[pos][i]
                else:
                    position['13'] = temp_edge[pos][i]

    #-------------------------------------------------------------------------------------------------------------

        elif set(color) == set(['red', 'white']):
            for i in range(len(color)):
                if color[i] == 'red':
                    position['14'] = temp_edge[pos][i]
                else:
                    position['15'] = temp_edge[pos][i]

    #---------------------------------------------------------------------------------------------------------------

        elif set(color) == set(['blue', 'yellow']):
                for i in range(len(color)):
                    if color[i] == 'blue':
                        position['16'] = temp_edge[pos][i]
                    else:
                        position['17'] = temp_edge[pos][i]

    #---------------------------------------------------------------------------------------------------------------

        elif set(color) == set(['blue', 'white']):
            for i in range(len(color)):
                if color[i] == 'blue':
                    position['18'] = temp_edge[pos][i]
                else:
                    position['19'] = temp_edge[pos][i]

    #------------------------------------------------------------------------------------------------------------------

        elif set(color) == set(['green', 'yellow']):
            for i in range(len(color)):
                if color[i] == 'green':
                    position['20'] = temp_edge[pos][i]
                else:
                    position['21'] = temp_edge[pos][i]

    #------------------------------------------------------------------------------------------------------------------

        elif set(color) == set(['green', 'white']):
            for i in range(len(color)):
                if color[i] == 'green':
                    position['22'] = temp_edge[pos][i]
                else:
                    position['23'] = temp_edge[pos][i]
        else:
            print('color[0], color[1], pos')



    #------------------------------------------------------------------------------------------------------------------
                                            # 	t		l	f
    for pos, corner in corners.items(): # orange white blue 33 34 35

        if set(corner) == set(['orange', 'white', 'blue']):
            for i in range(len(corner)):
                if corner[i] == 'orange':
                    position['33'] = temp[pos][i]
                if corner[i] == 'white':
                    position['34'] = temp[pos][i]
                if corner[i] == 'blue':
                    position['35'] = temp[pos][i]


        elif set(corner) == set(['orange', 'blue', 'yellow']):
            for i in range(len(corner)):
                if corner[i] == 'orange':
                    position['24'] = temp[pos][i]
                if corner[i] == 'blue':
                    position['25'] = temp[pos][i]
                if corner[i] == 'yellow':
                    position['26'] = temp[pos][i]

        elif set(corner) == set(['orange', 'yellow', 'green']):
            for i in range(len(corner)):
                if corner[i] == 'orange':
                    position['27'] = temp[pos][i]
                if corner[i] == 'yellow':
                    position['28'] = temp[pos][i]
                if corner[i] == 'green':
                    position['29'] = temp[pos][i]

        if set(corner) == set(['orange', 'green','white']):
            for i in range(len(corner)):
                if corner[i] == 'orange':
                    position['30'] = temp[pos][i]
                if corner[i] == 'green':
                    position['31'] = temp[pos][i]
                if corner[i] == 'white':
                    position['32'] = temp[pos][i]


        if set(corner) == set(['red', 'yellow', 'blue']):
            for i in range(len(corner)):
                if corner[i] == 'red':
                    position['36'] = temp[pos][i]
                if corner[i] == 'yellow':
                    position['37'] = temp[pos][i]
                if corner[i] == 'blue':
                    position['38'] = temp[pos][i]

        if set(corner) == set(['red', 'blue', 'white']):
            for i in range(len(corner)):
                if corner[i] == 'red':
                    position['39'] = temp[pos][i]
                if corner[i] == 'blue':
                    position['40'] = temp[pos][i]
                if corner[i] == 'white':
                    position['41'] = temp[pos][i]

        if set(corner) == set(['red', 'white', 'green']):
            for i in range(len(corner)):
                if corner[i] == 'red':
                    position['42'] = temp[pos][i]
                if corner[i] == 'white':
                    position['43'] = temp[pos][i]
                if corner[i] == 'green':
                    position['44'] = temp[pos][i]

        if set(corner) == set(['red', 'green', 'yellow']):
            for i in range(len(corner)):
                if corner[i] == 'red':
                    position['45'] = temp[pos][i]
                if corner[i] == 'green':
                    position['46'] = temp[pos][i]
                if corner[i] == 'yellow':
                    position['47'] = temp[pos][i]

    print(position)
    solution(position)

def build_corners(corners, c_no, data):
    corners[c_no].append(data)

def solution(position):
    pos = ''
    a = 0
    while a <= 22:
        print(a)
        print(position[str(a)])
        pos = pos + position[str(a)] + position[str(a+1)] + ' '
        a += 2

    a = 24
    while a <= 46:
        pos = pos + position[str(a)] + position[str(a+1)] + position[str(a+2)] + ' '
        a += 3

    pos = pos.strip()
    print(pos)

    T=[]
    S=[0]*20,'QTRXadbhEIFJUVZYeijf',0
    I='FBRLUD'

    G=[(~i%8,i//8-4)for i in map(ord,'ouf|/[bPcU`Dkqbx-Y:(+=P4cyrh=I;-(:R6')]
    R=range

    def M(o,s,p):
        z=~p/2%-3;k=1
        for i,j in G[p::6]:
            i*=k
            j*=k
            o[i],o[j]=o[j]-z,o[i]+z
            s[i],s[j]=s[j],s[i]
            k=-k

    N=lambda p:sum([i<<i for i in R(4)for j in R(i)if p[j]<p[i]])

    def H(i,t,s,n=0,d=()):
        if i>4:n=N(s[2-i::2]+s[7+i::2])*84+N(s[i&1::2])*6+divmod(N(s[8:]),24)[i&1]
        elif i>3:
            for j in s:l='UZifVYje'.find(j);t[l]=i;d+=(l-4,)[l<4:];n-=~i<<i;i+=l<4
            n+=N([t[j]^t[d[3]]for j in d])
        elif i>1:
            for j in s:n+=n+[j<'K',j in'QRab'][i&1]
        for j in t[13*i:][:11]:n+=j%(2+i)-n*~i
        return n

    def P(i,m,t,s,l=''):
        for j in~-i,i:
            if T[j][H(j,t,s)]<m:return
        if~m<0:print(l);return t,s
        for p in R(6):
            u=t[:];v=s[:]
            for n in 1,2,3:
                M(u,v,p);r=p<n%2*i or P(i,m+1,u,v,l+I[p]+'n')
                if r>1:return r

    s=pos.split()
    o=[-(p[-1]in'UD')or p[0]in'RL'or p[1]in'UD'for p in s]
    s=[chr(64+sum(1<<I.find(a)for a in x))for x in s]
    print(o)
    print(s)

    for i in R(7):
        m=0;C={};T+=C,;x=[S]
        for j,k,d in x:
            h=H(i,j,k)
            for p in R(C.get(h,6)):
                C[h]=d;u=j[:];v=list(k)
                for n in i,0,i:M(u,v,p);x+=[(u[:],v[:],d-1)]*(p|1>n)
        if~i&1:
            while d > 0:
                d=P(i,m,o,s)
                m-=1
            o=d
            s=d
    print(s)
    print('we done')
main()
