#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
#import cartopy as ct

def read_data(fname,mode):
    dic={}
    is_dataset = False
    try:
        infile = open(fname,mode)
        while True:
            line = infile.readline()
            if not line:
                break
            if line[0].startswith('#'):
                continue
            elif is_dataset == False:
                dic[line] = []
                name = line 
                is_dataset = True
            elif is_dataset == True:
                if line == '\n':
                    is_dataset = False
                    continue
                dic[name].append(line)
        infile.close()
    except IOError:
        print('Sorry,fail to open file!')
    else:
        print('Succeed to open file!')
    return dic


def split(dic):
#    data_xy = {}
    a = 0
    data_x = [[] for f in range(len(list(dic.values())))]
    data_y = [[] for f in range(len(list(dic.values())))]
        #data_xy[i]= []
        #data_xy[i].append([])
        #data_xy[i].append([])
    for i in list(dic.values()):
        a = a + 1
        if len(list(dic.values())) == 1:
            t = i
            t = t.replace('[','')
            t = t.replace(']','')
            t = t.replace('(','')
            t = t.replace(')','')
            for j in range(len(t)):
                data_x[a-1].append(float(t[::2]))
                data_y[a-1].append(float(t[1::2]))
        else:
            for j in range(len(i)):
                t = i[j]
                t = t.replace('(','')
                t = t.replace('[','')
                t = t.replace(')','')
                data_x[a-1].append(float(t.split(', ')[0]))
                data_y[a-1].append(float(t.split(', ')[1]))
    return data_x,data_y

def draw(data_x,data_y):
    for i in range(len(data_x)-1):
        plt.plot(data_x[i],data_y[i],'b')
#        plt.legend(('line1','line2','line3','line4','line5','line6','line7','line8','line9','line10'),ncol = 2)
#        plt.xlabel('X')
#        plt.ylabel('Y')
#        plt.title('My Plot_task1')
    plt.show()
    
data = read_data('natural_neighbourhoods.dat','r')
data_x, data_y = split(data)
draw(data_x,data_y)

