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
            r'\usepackage{mathtext}',
            r'\usepackage{graphicx}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T2A]{fontenc}',
            r'\usepackage[main=russian,english]{babel}',
            ]

data = np.genfromtxt('experiment3.csv', delimiter=';')

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.plot(data[13,1:],data[12,1:],color='#FF7800',marker='o',lw=1,ms=2, label=r'detector off')
ax.errorbar(data[13,1:],data[12,1:],yerr=80,fmt='.',color='#FF7800')
ax.plot(data[10,1:],data[9,1:],color='#133CAC',marker='o',lw=1,ms=2, label=r'detector on')
ax.errorbar(data[10,1:],data[9,1:],yerr=80,fmt='.',color='#133CAC')
ax.set_ylabel(r'$U$, mv')
ax.set_xlabel(r'$f$, kHz')
ax.grid()
plt.tight_layout()
ax.legend(loc=5)
plt.savefig('exp3с.pdf')