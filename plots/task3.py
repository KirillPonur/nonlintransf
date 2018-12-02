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
ax.plot(data[0,1:],data[1,1:],color='#FF7800',marker='o',lw=1,ms=2)
ax.errorbar(data[0,1:],data[1,1:],yerr=1,fmt='.',color='#FF7800')
ax.plot([0,2000],[0,544],color='#133CAC',ls='--')
ax.set_ylabel(r'$U_\mathrm{вых}$, mv')
ax.set_xlabel(r'$U_\mathrm{вх}$, mv')
ax.grid()
plt.tight_layout()
plt.savefig('exp3a.pdf')