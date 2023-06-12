import ROOT
from array import array
import numpy as np

def GS1D(strip_num, resolution, histo_matrix, detector):
	file_label='E'+str(detector)+'FitMatrix.dat'
	fit_matrix=np.empty(16, dtype=object)
	output_file = open(file_label, 'wb')
	for i in range(0, strip_num):
		data_file= np.load(open(str(histo_matrix), 'rb'),allow_pickle=True)
		spec= ROOT.TSpectrum()
		peaks=spec.Search(data_file[i], 10,"",0.0075 )
		temp=spec.GetPositionX()
		peaks_pos=np.empty((4))
		for j in range(0, len(peaks_pos)):
			peaks_pos[j]=temp[j]
		peaks_pos=np.sort(peaks_pos)
		
		g1 = ROOT.TF1( 'g1', 'gaus',  peaks_pos[0]-resolution,  peaks_pos[0]+resolution )
		g2 = ROOT.TF1( 'g2', 'gaus',  peaks_pos[1]-resolution, peaks_pos[1]+resolution )
		g3 = ROOT.TF1( 'g3', 'gaus', peaks_pos[2]-resolution, peaks_pos[2]+resolution)
		
		if i==2 or i==9:
			g4 = ROOT.TF1( 'g4', 'gaus', peaks_pos[3]-(resolution/2), peaks_pos[3]+(resolution/2))
		elif i==6 or i==12:
			g4 = ROOT.TF1( 'g4', 'gaus', peaks_pos[3]-(resolution/3), peaks_pos[3]+(resolution/3))
		else:
			g4 = ROOT.TF1( 'g4', 'gaus', peaks_pos[3]-(resolution), peaks_pos[3]+(resolution))

		data_file[i].Fit( g1,'R')
		data_file[i].Fit( g2,'R+')
		data_file[i].Fit( g3,'R+')
		data_file[i].Fit( g4,'R+')
		
		par1 = g1.GetParameters()
		par2 = g2.GetParameters()
		par3 = g3.GetParameters()
		par4 = g4.GetParameters()
		
		par=array( 'd', 12*[0.] )
		
		par[0], par[1], par[2]=par1[0], par1[1], par1[2]
		par[3], par[4], par[5]=par2[0], par2[1], par2[2]
		par[6], par[7], par[8]=par3[0], par3[1], par3[2]
		par[9], par[10], par[11]=par4[0], par4[1], par4[2]
		
		gaus_sum = ROOT.TF1( 'sum', 'gaus(0)+gaus(3)+gaus(6)+gaus(9)', peaks_pos[0]-(8*resolution), peaks_pos[3]+(8*resolution) )
		gaus_sum.SetParameters(par)  
		
		fit_matrix[i]=gaus_sum
	np.save(output_file, fit_matrix)
	return fit_matrix
