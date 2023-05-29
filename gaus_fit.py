import ROOT
import numpy as np

def GS1D(strip_num, resolution, histo_matrix):
	fit_matrix=np.empty(16, dtype=object)
	output_file = open('fit_matrix1d.dat', 'wb')
	for i in range(0, strip_num):
		data_file= np.load(open(str(histo_matrix), 'rb'),allow_pickle=True)
		spec= ROOT.TSpectrum()
		peaks=spec.Search(data_file[i])
		peaks_pos=spec.GetPositionX()
		
		g1 = ROOT.TF1( 'g1', 'gaus',  peaks_pos[0]-resolution,  peaks_pos[0]+resolution )
		g2 = ROOT.TF1( 'g2', 'gaus',  peaks_pos[1]-resolution, peaks_pos[1]+resolution )
		g3 = ROOT.TF1( 'g3', 'gaus', peaks_pos[2]-resolution, peaks_pos[2]+resolution)
		
		data_file[i].Fit( g1,'R')
		data_file[i].Fit( g2,'R')
		data_file[i].Fit( g3,'R')
		
		par1 = g1.GetParameters()
		par2 = g2.GetParameters()
		par3 = g3.GetParameters()
		
		gaus_sum = ROOT.TF1( 'gaus_sum', 'gaus(0)+gaus(3)+gaus(6)', peaks_pos[0]-(3*resolution), peaks_pos[2]+(3*resolution) )
		gaus_sum.SetParameters(par1[0],par1[1],par1[2], par2[0],par2[1],par2[2],par3[0],par3[1],par3[2])  
		
		fit_matrix[i]=gaus_sum
	np.save(output_file, fit_matrix)
	return fit_matrix
