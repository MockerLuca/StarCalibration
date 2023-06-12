import ROOT
import numpy as np
from get_histo import *
from gaus_fit import *
from dE_sum_histo import *
from lin_fit import*
import os

os.chdir('/home/luca/Desktop/pesquisa/star_calibration/data_files/')
c = ROOT.TCanvas()
i=11 #dE
j=0 #E

calibration_files=['119Sn_run053_part001.root', '119Sn_run053_part002.root', '119Sn_run053_part003.root', '119Sn_run053_part004.root', '119Sn_run053_part005.root', '119Sn_run053_part006.root']

detector=0 #A=0 ; B=1

make_1d_histo=0    #true=1 ; false=0
make_2d_histo=0    #true=1 ; false=0
make_2dSum_histo=0 #true=1 ; false=0
make_gaus_fit=0    #true=1 ; false=0

plot_1d_histo=0    #true=1 ; false=0
plot_2d_histo=0    #true=1 ; false=0
plot_2dSum_histo=0 #true=1 ; false=0
plot_gaus_fit=0    #true=1 ; false=0
plot_lin_fit=1	    #true=1 ; false=0

if make_1d_histo==1:
	GHEA1D(calibration_files, 16, 1024, 1024, 4096,300)
	GHEB1D(calibration_files, 16, 1024, 1024, 4096,300)
elif make_1d_histo==0:
	print(make_1d_histo)

if make_2d_histo==1:
	GHB2D('119Sn_run038_part001.root','EA_LinFitPar.dat', 16, 16, 1024, 0, 1024,300)
	GHA2D('119Sn_run038_part001.root','EB_LinFitPar.dat', 16, 16, 1024, 0, 1024,300)
elif make_2d_histo==0:
	print(make_2d_histo)

if make_2dSum_histo==1:
	dEASH('119Sn_run038_part001.root','EA_LinFitPar.dat', 16, 16, 1024, 0, 1024,300)
	dEBSH('119Sn_run038_part001.root','EB_LinFitPar.dat', 16, 16, 1024, 0, 1024,300)
elif make_2dSum_histo==0:
	print(make_2dSum_histo)
	
if plot_1d_histo==1:
	if detector==0:
		data_file= np.load(open('histoEA_matrix.dat', 'rb'),allow_pickle=True)
		data_file[j].Draw()
	elif detector==1:
		data_file= np.load(open('histoEB_matrix.dat', 'rb'),allow_pickle=True)
		data_file[j].Draw()
elif plot_1d_histo==0:
	print(plot_1d_histo)

if plot_2d_histo==1:
	if detector==0:
		data_file= np.load(open('histo_BiParA_matrix.dat', 'rb'),allow_pickle=True)
		data_file[i][j].Draw('colz')
	elif detector==1:
		data_file= np.load(open('histo_BiParB_matrix.dat', 'rb'),allow_pickle=True)
		data_file[i][j].Draw('colz')
elif plot_2d_histo==0:
	print(plot_2d_histo)

if plot_2dSum_histo==1:
	if detector==0:
		data_file= np.load(open('histo_BiParASum_matrix.dat', 'rb'),allow_pickle=True)
		data_file[i].Draw('colz')
	elif detector==1:
		data_file= np.load(open('histo_BiParBSum_matrix.dat', 'rb'),allow_pickle=True)
		data_file[i].Draw('colz')
elif plot_2dSum_histo==0:
	print(plot_2dSum_histo)

if make_gaus_fit==1:
	GS1D(16, 6, 'histoEA_matrix.dat', 'A')
	GS1D(16, 6, 'histoEB_matrix.dat', 'B')
elif make_gaus_fit==0:
	print(make_gaus_fit)

if plot_gaus_fit==1:
	if detector==0:
		fit_file= np.load(open('EAFitMatrix.dat', 'rb'),allow_pickle=True)
		data_file= np.load(open('histoEA_matrix.dat', 'rb'),allow_pickle=True)
		data_file[j].Draw()
		data_file[j].Fit(fit_file[j],'R')
	elif detector==1:
		fit_file= np.load(open('EBFitMatrix.dat', 'rb'),allow_pickle=True)
		data_file= np.load(open('histoEB_matrix.dat', 'rb'),allow_pickle=True)
		data_file[j].Draw()
		data_file[j].Fit(fit_file[j],'R')
elif plot_gaus_fit==0:
	print(plot_gaus_fit)

if plot_lin_fit==1:
	if detector==0:
		fit_parameters= FitPar('histoEA_matrix.dat','EAFitMatrix.dat',16,'A')
		linear_fit= LinFit('EAGausFitPar.dat', 16, 4,'A')
		linear_fit[0][j].Draw("AP*")
		linear_fit[0][j].GetXaxis().SetLimits(0, 4096)
		linear_fit[0][j].GetYaxis().SetRangeUser(0, 8)
		linear_fit[0][j].Fit(linear_fit[1][j])
	elif detector==1:
		fit_parameters= FitPar('histoEB_matrix.dat','EBFitMatrix.dat',16,'B')
		linear_fit= LinFit('EBGausFitPar.dat', 16, 4,'B')
		linear_fit[0][j].Draw("AP*")
		linear_fit[0][j].GetXaxis().SetLimits(0, 4096)
		linear_fit[0][j].GetYaxis().SetRangeUser(0, 8)
		linear_fit[0][j].Fit(linear_fit[1][j])
elif plot_lin_fit==1:
	print(plot_lin_fit)

#spec= ROOT.TSpectrum()
#peaks=spec.Search(data_file[j], 10,"",0.0075 )
#temp=spec.GetPositionX()
#peaks_pos=np.empty((4))
#for j in range(0, len(peaks_pos)):
#	peaks_pos[j]=temp[j]
#peaks_pos=np.sort(peaks_pos)
#print(peaks_pos)

