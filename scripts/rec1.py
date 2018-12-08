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
    name = path.abspath('..'+'\\rec\\rec.xlsx')
    df = pd.read_excel(name,sheet_name='1')
    df=df
    U=[]
    f=[]
    for i in df.index:
        U.append(df['U,mV'][i])
        f.append(df['freq, kHz'][i])
    plot(f,U,color= 'darkblue')
    plot(f,U,'r.')
    prop()
    savefig(path.abspath('..'+'\\fig\\exp1.pdf'))
    show()
def task2():
    name = path.abspath('..'+'\\rec\\rec.xlsx')
    df = pd.read_excel(name,sheet_name='2')
    df=df
    U=[]
    f=[]
    for i in df.index:
        U.append(df['U,mV'][i])
        f.append(df['freq,kHz'][i])    
    f=array(f)
    U=array(U)
    ff=f[~isnan(f)]
    UU=U[~isnan(U)]
    g = interpolate.interp1d(ff,UU, kind='linear')
    x=linspace(ff[0],ff[-1],1000)
    plot(ff,UU,color='darkblue')
    plot(ff,UU,'r.',markersize=3)
    prop()
    savefig(path.abspath('..'+'\\fig\\exp2.pdf'))
    show()
def task3(*args):

    name = path.abspath('..'+'\\rec\\rec.xlsx')
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
    A=[]
    DC=[]
    for i in df.index:
        A.append(df['AUin,mVpp'][i])
        DC.append(df['DCout,mV'][i])    
        f1.append(df['freq,kHz'][i])
        U1.append(df['U1,mV'][i])
        U2.append(df['U2,mV'][i])
        f2.append(df['freq,kHz'][i])
        Uon.append(df['on,mV'][i])
        fon.append(df['freq1,kHz'][i])
        Uoff.append(df['off,mV'][i])
        foff.append(df['freq1,kHz'][i])



    figure('detec')
    prop()
    xlabel(r'$U_{\text{вх}}^{max}, \text{мВ}$')
    ylabel(r'$U_{\text{вых}}$, \text{мВ}')
    A=array(A)/2
    A = A[~isnan(A)]
    DC=array(DC)
    DC=DC[~isnan(DC)]
    f=polyfit(A,DC,1)
    f=poly1d(f)
    x=linspace(A[0],A[-1],100)
    plot(x,f(x))
    plot(A,DC,'r.')
    savefig(path.abspath('..'+'\\fig\\exp3a.pdf'))

    figure('12')
    prop()
    plot(f1,U1,'.-',label=r'$R_1C_1$')
    plot(f2,U2,'.-',label=r'$R_2C_2$')
    legend()
    savefig(path.abspath('..'+'\\fig\\exp3b.pdf'))
    figure('on/off')
    prop()
    plot(foff,Uoff,'.-',label=r'$\text{детектор выключен}$')
    plot(fon,Uon,'.-',label=r'$\text{детектор включен}$')
    legend()
    savefig(path.abspath('..'+'\\fig\\exp3c.pdf'))
    show()
########################################################################

task1()
task2()
# task3(1,2,'on','off')