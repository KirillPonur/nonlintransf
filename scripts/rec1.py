from pylab import *
from matplotlib import rc
import os.path as path
import pandas as pd
from scipy import interpolate
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')
def prop():
    grid(which='major', linestyle='-')
    grid(which='minor', linestyle=':')
    minorticks_on()
    ylabel(r'$U,\text{мВ}$',fontsize=16)
    xlabel(r'$\nu, \text{кГц}$',fontsize=16)

def task1():
    name = path.abspath('..'+'\\rec\\experiment.xlsx')
    df = pd.read_excel(name,sheet_name='1')
    df=df
    U=[]
    f=[]
    for i in df.index:
        U.append(df['U(mV)'][i])
        f.append(df['frec(kHz)'][i])
    plot(f,U,color= 'darkblue')
    plot(f,U,'r.')
    prop()
    show()

def task2():
    name = path.abspath('..'+'\\rec\\experiment.xlsx')
    df = pd.read_excel(name,sheet_name='2')
    df=df
    U=[]
    f=[]
    for i in df.index:
        U.append(df['U(mV)'][i])
        f.append(df['frec(kHz)'][i])    
    f=array(f)
    U=array(U)
    ff=f[~isnan(f)]
    UU=U[~isnan(U)]
    g = interpolate.interp1d(ff,UU, kind='cubic')
    x=linspace(ff[0],ff[-1],1000)
    plot(x,g(x),color='darkblue')
    plot(ff,UU,'r.')
    prop()
    show()

def task3(*args):

    name = path.abspath('..'+'\\rec\\experiment.xlsx')
    df = pd.read_excel(name,sheet_name='3')
    df=df
    U1=[]
    f1=[]
    U2=[]
    f2=[]
    Uon=[]
    fon=[]
    Uoff=[]
    foff=[]
    for i in df.index:
        U1.append(df['u1(mv)'][i])
        f1.append(df['frec1(kHz)'][i])
        U2.append(df['u2(mv)'][i])
        f2.append(df['frec2(kHz)'][i])
        Uon.append(df['U(detec=on)(mv)'][i])
        fon.append(df['frec(kHz)'][i])
        Uoff.append(df['U(detec=off)(mv)'][i])
        foff.append(df['frec(kHz)'][i])

    U=array([U1,U2,Uon,Uoff])
    f=array([f1,f2,fon,foff])
    for counter,value in enumerate(args):
        figure(value)
        prop()
        ff=f[counter][~isnan(f[counter])]
        UU=U[counter][~isnan(U[counter])]
        g = interpolate.interp1d(ff,UU, kind='cubic')
        x=linspace(ff[0],ff[-1],1000)
        plot(x,g(x),color='darkblue')
        plot(ff,UU,'r.')

    show()
########################################################################

task1()
task2()
task3(1,2,'on','off')