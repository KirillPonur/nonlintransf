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
            r'\usepackage[main=russian,english]{babel}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            ]

data = np.genfromtxt('experiment1.csv', delimiter=';')

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.plot(data[1,1:],data[0,1:],color='#FF7800',marker='o',lw=1,ms=2)
ax.errorbar(data[1,1:],data[0,1:],yerr=1,fmt='.',color='#FF7800')
ax.set_ylabel(r'$U$, mV')
ax.set_xlabel(r'$f$, kHz')
ax.grid()
plt.tight_layout()
plt.show()
# plt.savefig('exp1.pdf')