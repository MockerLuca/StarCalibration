import ROOT
import numpy as np
from get_histo import *
from gaus_fit import *
from dE_sum_histo import *
from lin_fit import*
c = ROOT.TCanvas()
i=3
j=7

#GHEA1D('119Sn_run042_part001.root', 16, 1024, 0, 2048,200)
#GHEB1D('119Sn_run042_part001.root', 16, 1024, 0, 2048,200)

#GHB2D('119Sn_run038_part001.root', 16, 16, 1024, 0, 2048,300)
#GHA2D('119Sn_run038_part001.root', 16, 16, 1024, 0, 2048,300)

#dEASH('119Sn_run038_part001.root', 16, 16, 1024, 0, 2048,300)
#dEBSH('119Sn_run038_part001.root', 16, 16, 1024, 0, 2048,300)

#data_file= np.load(open('histoEA_matrix.dat', 'rb'),allow_pickle=True)
#data_file= np.load(open('histoEB_matrix.dat', 'rb'),allow_pickle=True)

#data_file= np.load(open('histo_BiParA_matrix.dat', 'rb'),allow_pickle=True)
#data_file= np.load(open('histo_BiParB_matrix.dat', 'rb'),allow_pickle=True)
#data_file[i][j].Draw('colz')

#projx=data_file[i][j].ProjectionX('projx',0, 2048)
#projx.Draw()
#projy=data_file[i][j].ProjectionY('projy',0, 2048)
#projy.Draw()

#data_file= np.load(open('histo_BiParASum_matrix.dat', 'rb'),allow_pickle=True)
#data_file= np.load(open('histo_BiParBSum_matrix.dat', 'rb'),allow_pickle=True)
#data_file[i].Draw('colz')

#GS1D(16, 10, 'histoEA_matrix.dat')
#fit_file= np.load(open('fit_matrix1d', 'rb'),allow_pickle=True)
#GS1D(16, 10, 'histoEB_matrix.dat')
#fit_file= np.load(open('fit_matrix1d', 'rb'),allow_pickle=True)

#data_file[j].Fit(fit_file[j],'R')
#c.Draw()

fit_parameters= FP('histoEA_matrix.dat','fit_matrix1d',16)
print(fit_parameters[1])

