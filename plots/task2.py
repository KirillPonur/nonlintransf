# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)
pgf_with_latex = {
    "pgf.texsystem": "xelatex",         # use Xelatex which is TTF font aware
}

mpl.rcParams.update(pgf_with_latex)
plt.rc('text', usetex=True)
plt.rc('font', family='serif', serif = 'CMU Serif', size = 12)
plt.rcParams['text.latex.preamble'] = [
            r'\usepackage{amsmath}',
            r'\usepackage{amsfonts}',
            r'\usepackage{graphicx}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            r'\usepackage[main=russian,english]{babel}',
            ]

data = np.genfromtxt('experiment2.csv', delimiter=';')

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
fig.subplots_adjust(hspace=0, wspace=0)
ax.plot(data[1,1:],data[0,1:],color='#FF7800',marker='o',lw=1,ms=1)
ax.errorbar(data[1,1:],data[0,1:],yerr=8,fmt='.',color='#FF7800')
ax.set_ylabel(r'$U_k$, mV')
ax.set_xlabel(r'$f_c$, kHz')
ax.grid()
plt.tight_layout()
plt.savefig('exp2.pdf')