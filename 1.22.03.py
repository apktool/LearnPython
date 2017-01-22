# ci|params.py

class Parameters(dict):
    __getattr__=dict.get
    __setattr__=dict.__setattr__
    __delattr__=dict.__delattr__

    def copy(self):
        res=Parameters()
        for key, value in self.items():
            res[key]=value
        return res

params=Parameters()
temp=params.copy()
print(temp)
