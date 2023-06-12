import ROOT
import numpy as np

def GHB2D(calibration_file, calibration_par, dE_strips_num, E_strips_num, bins_num, channel_i, channel_f,noise):
	root_file = ROOT.TFile.Open(calibration_file)
	tree = root_file.T
	entries = tree.GetEntries()
	
	histo_matrix= np.empty((dE_strips_num,E_strips_num),dtype=object)
	parameters_file=np.load(open(calibration_par, 'rb'),allow_pickle=True)
	for i in range(0,dE_strips_num):
		dE_strip= str(i)
		for j in range(0,E_strips_num):
			E_strip=str(j)
			hname='histo_'+dE_strip+'_'+E_strip
			histo_matrix[i][j]=(ROOT.TH2F(hname, hname, bins_num, channel_i, channel_f, bins_num, channel_i, channel_f))
	
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
				E_ene=(parameters_file[strip_E][2]*value_E) + parameters_file[strip_E][0]
				if value_dE>noise:
					histo_matrix[strip_dE][strip_E].Fill(value_E, value_dE)
					j+=1
				else:
					j+=1
			i+=1
		n+=1
	output_file = open("histo_BiParB_matrix.dat", "wb")
	np.save(output_file, histo_matrix)
	return histo_matrix
	
def GHA2D(calibration_file, calibration_par, dE_strips_num, E_strips_num, bins_num, channel_i, channel_f,noise):
	root_file = ROOT.TFile.Open(calibration_file)
	tree = root_file.T
	entries = tree.GetEntries()
	
	histo_matrix= np.empty((dE_strips_num,E_strips_num),dtype=object)
	parameters_file=np.load(open(calibration_par, 'rb'),allow_pickle=True)
	for i in range(0,dE_strips_num):
		dE_strip= str(i)
		for j in range(0,E_strips_num):
			E_strip=str(j)
			hname='histo_'+dE_strip+'_'+E_strip
			histo_matrix[i][j]=(ROOT.TH2F(hname, hname, bins_num, channel_i, channel_f, bins_num, channel_i, channel_f))
	
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
				E_ene=(parameters_file[strip_E][2]*value_E) + parameters_file[strip_E][0]
				if value_dE>noise:
					histo_matrix[strip_dE][strip_E].Fill(value_E, value_dE)
					j+=1
				else:
					j+=1
			i+=1
		n+=1
	output_file = open("histo_BiParA_matrix.dat", "wb")
	np.save(output_file, histo_matrix)
	return histo_matrix

def GHEB1D(calibration_file, strips_num, bins_num, channel_i, channel_f, noise):
	tree= ROOT.TChain('T')
	for k in range(0, len(calibration_file)):
		tree.AddFile(calibration_file[k])
	entries = tree.GetEntries()
	histo_matrix= np.empty(strips_num, dtype=object)
	for i in range(0, strips_num):
		E_strip=str(i)
		hname='histo_EB_'+E_strip
		h_temp=ROOT.TH1F(hname, hname, bins_num, channel_i, channel_f)
		h_temp.SetDirectory(0)
		histo_matrix[i]=h_temp
	n=0
	while n<entries:
		tree.GetEntry(n)
		i=0
		while i< tree.EB_multis:
			strip_E=tree.EB_Channels[i]
			value_E=tree.EB_Values[i]
			if value_E>noise:
				histo_matrix[strip_E].Fill(value_E)
				i+=1
			else:
				i+=1
		n+=1
	output_file = open("histoEB_matrix.dat", "wb")
	np.save(output_file, histo_matrix)
	return histo_matrix
	
def GHEA1D(calibration_file, strips_num, bins_num, channel_i, channel_f, noise):
	tree= ROOT.TChain('T')
	for k in range(0, len(calibration_file)):
		tree.AddFile(calibration_file[k])
	entries = tree.GetEntries()
	histo_matrix= np.empty(strips_num, dtype=object)
	for i in range(0, strips_num):
		E_strip=str(i)
		hname='histo_EA_'+E_strip
		h_temp=ROOT.TH1F(hname, hname, bins_num, channel_i, channel_f)
		h_temp.SetDirectory(0)
		histo_matrix[i]=h_temp
	n=0
	while n<entries:
		tree.GetEntry(n)
		i=0
		while i< tree.EA_multis:
			strip_E=tree.EA_Channels[i]
			value_E=tree.EA_Values[i]
			if value_E>noise:
				histo_matrix[strip_E].Fill(value_E)
				i+=1
			else:
				i+=1
		n+=1
	output_file = open("histoEA_matrix.dat", "wb")
	np.save(output_file, histo_matrix)
	return histo_matrix



