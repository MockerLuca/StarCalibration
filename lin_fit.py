import ROOT
import numpy as np

def FP(histo_matrix,fit_matrix1d,E_strips_num):
	data_file= np.load(open(histo_matrix, 'rb'),allow_pickle=True)
	fit_file= np.load(open(fit_matrix1d, 'rb'),allow_pickle=True)
	output_file = open('fit_parameters_EA.dat', 'wb')
	fit_par_matrix= np.empty((16,9))
	for j in range(0, E_strips_num):
		data_file[j].Fit(fit_file[j],'R')
		par=fit_file[j].GetParameters()
		errors=fit_file[j].GetParErrors()
		temp= np.array([float(4.672), par[1], errors[1], float(5.480), par[4], errors[4], float(5.788), par[7], errors[7]])
		for k in range(0,len(temp)):
			fit_par_matrix[j][k]=temp[k]
	np.save(output_file, fit_par_matrix)
	return fit_par_matrix


