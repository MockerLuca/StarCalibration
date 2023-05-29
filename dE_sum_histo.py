import ROOT
import numpy as np

def dEBSH(calibration_file, dE_strips_num, E_strips_num, bins_num, channel_i, channel_f,noise):
	output_file = open("histo_BiParBSum_matrix.dat", "wb")
	root_file = ROOT.TFile.Open(calibration_file)
	tree = root_file.T
	entries = tree.GetEntries()
	histo_matrix= np.empty(dE_strips_num,dtype=object)
	for i in range(0,dE_strips_num):
		dE_strip= str(i)
		for j in range(0,E_strips_num):
			E_strip=str(j)
			hname='histo_'+dE_strip+'_sum'
			histo_matrix[i]=(ROOT.TH2F(hname, hname, bins_num, channel_i, channel_f, bins_num, channel_i, channel_f))
	
	n=0
	while n<entries:
		tree.GetEntry(n)
		i=0
		while i < tree.dEB_multis: 
			strip_dE=tree.dEB_Channels[i]
			value_dE=tree.dEB_Values[i]
			j=0
			while j< tree.EB_multis:
				strip_E=tree.EB_Channels[j]
				value_E=tree.EB_Values[j]
				#ene_E=slope[strip_E]*value_E + offset[strip_E]
				if value_dE>noise:
					histo_matrix[strip_dE].Fill(ene_E, value_dE)
					j+=1
				else:
					j+=1
			i+=1
		n+=1
	np.save(output_file, histo_matrix)
	return histo_matrix
	
def dEASH(calibration_file, dE_strips_num, E_strips_num, bins_num, channel_i, channel_f,noise):
	output_file = open("histo_BiParASum_matrix.dat", "wb")
	root_file = ROOT.TFile.Open(calibration_file)
	tree = root_file.T
	entries = tree.GetEntries()
	histo_matrix= np.empty(dE_strips_num,dtype=object)
	for i in range(0,dE_strips_num):
		dE_strip= str(i)
		for j in range(0,E_strips_num):
			E_strip=str(j)
			hname='histo_'+dE_strip+'_sum'
			histo_matrix[i]=(ROOT.TH2F(hname, hname, bins_num, channel_i, channel_f, bins_num, channel_i, channel_f))
	
	n=0
	while n<entries:
		tree.GetEntry(n)
		i=0
		while i < tree.dEA_multis: 
			strip_dE=tree.dEA_Channels[i]
			value_dE=tree.dEA_Values[i]
			j=0
			while j< tree.EA_multis:
				strip_E=tree.EA_Channels[j]
				value_E=tree.EA_Values[j]
				if value_dE>noise:
					histo_matrix[strip_dE].Fill(value_E, value_dE)
					j+=1
				else:
					j+=1
			i+=1
		n+=1
	np.save(output_file, histo_matrix)
	return histo_matrix
