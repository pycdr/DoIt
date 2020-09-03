import pickle
def dict_to_pickle(data,path="./data.pckl"):
	try:
		with open(path,'wb') as f:
			pickle.dump(data,f)
			f.close()
		return True
	except:
		return False
def pickle_to_dict(path="./data.pckl"):
	data = pickle.load(open(path,'rb'))
	return data
