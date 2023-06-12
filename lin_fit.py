import ROOT
import numpy as np

def FitPar(histo_matrix,fit_matrix1d,E_strips_num, detector):
	data_file= np.load(open(histo_matrix, 'rb'),allow_pickle=True)
	fit_file= np.load(open(fit_matrix1d, 'rb'),allow_pickle=True)
	file_label='E'+str(detector)+'GausFitPar.dat'
	output_file = open(file_label, 'wb')
	
	fit_par_matrix= np.empty((16,12))
	for j in range(0, E_strips_num):
		data_file[j].Fit(fit_file[j],'R')
		par=fit_file[j].GetParameters()
		errors=fit_file[j].GetParErrors()
		temp= np.array([float(4.672), par[1], errors[1], float(5.480), par[4], errors[4], float(5.788), par[7], errors[7], float(7.660), par[10], errors[10]])
		for k in range(0,len(temp)):
			fit_par_matrix[j][k]=temp[k]
	np.save(output_file, fit_par_matrix)
	return fit_par_matrix

def LinFit(fit_par_file, strips_num, peaks_num, detector):
	GraphVec= np.empty(strips_num, dtype=object)
	LinFitVec= np.empty(strips_num, dtype=object)
	ParMatrix=np.empty((16,4))
	
	file_label='E'+str(detector)+'_LinFitPar.dat'
	data_file= np.load(open(fit_par_file, 'rb'),allow_pickle=True)
	output_file = open(file_label, 'wb')
	for i in range(0, strips_num):
		LinFitVec[i]=ROOT.TF1('pol1','pol1')
		GraphVec[i]=ROOT.TGraph(peaks_num)
		j=0
		k=0
		while k< peaks_num:
			energy=data_file[i][j]
			j+=1
			channel=data_file[i][j]
			j+=1
			channel_error=data_file[i][j]
			j+=1
			GraphVec[i].SetPoint(k, channel, energy)
			k+=1
	
	for i in range(0, strips_num):
		GraphVec[i].Fit(LinFitVec[i])
		par=LinFitVec[i].GetParameters()
		errors=LinFitVec[i].GetParErrors()
		temp=np.array([par[0], errors[0], par[1], errors[1]])
		for j in range(0, len(temp)):
			ParMatrix[i][j]=temp[j]
	np.save(output_file, ParMatrix)
	return GraphVec, LinFitVec
