class Univariate():
    def quanQual(dataset):
      quan=[]
      qual=[]
      for columnName in dataset.columns:
         # print(columnName)
         if(dataset[columnName].dtype=='O'):
           # print("qual")
           qual.append(columnName)
         else:
           # print("quan") 
           quan.append(columnName)
      return quan,qual



def Univariate(dataset,quan):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25th","Q2:50th","Q3:75th","Q4:100th","IQR","1.5","Lesser","Greater","Min","Max"],columns=quan)
    for columnName in quan:
        descriptive[columnName]["Mean"]=dataset[columnName].mean()
        descriptive[columnName]["Median"]=dataset[columnName].median()
        descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
        descriptive[columnName]["Q1:25th"]=dataset.describe()[columnName]["25%"]
        descriptive[columnName]["Q2:50th"]=dataset.describe()[columnName]["50%"]
        descriptive[columnName]["Q3:75th"]=dataset.describe()[columnName]["75%"]
        descriptive[columnName]["Q4:100th"]=dataset.describe()[columnName]["max"]
        descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75th"]-descriptive[columnName]["Q1:25th"]
        descriptive[columnName]["1.5"]=1.5*descriptive[columnName]["IQR"]
        descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25th"]-descriptive[columnName]["1.5"]
        descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75th"]+descriptive[columnName]["1.5"]
        descriptive[columnName]["Min"]=dataset[columnName].min()
        descriptive[columnName]["Max"]=dataset[columnName].max()
        return descriptive

def freqTable(columnName,dataset):
    freqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative_frequency","Cummulative_frequency"])
    freqTable["Unique_values"]=dataset[columnName].value_counts().index
    freqTable["Frequency"]=dataset[columnName].value_counts().values
    freqTable["Relative_frequency"]=(freqTable["Frequency"]/103)
    freqTable["Cummulative_frequency"]=freqTable["Relative_frequency"].cumsum()
    return freqTable

def univariate(columnName,dataset):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25th","Q2:50th","Q3:75th","Q4:100th","IQR","1.5","Lesser","Greater","Min","Max","Skewness","Kurtosis","Var","STD"],columns=quan)
    for columnName in quan:
        descriptive[columnName]["Mean"]=dataset[columnName].mean()
        descriptive[columnName]["Median"]=dataset[columnName].median()
        descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
        descriptive[columnName]["Q1:25th"]=dataset.describe()[columnName]["25%"]
        descriptive[columnName]["Q2:50th"]=dataset.describe()[columnName]["50%"]
        descriptive[columnName]["Q3:75th"]=dataset.describe()[columnName]["75%"]
        descriptive[columnName]["Q4:100th"]=dataset.describe()[columnName]["max"]
        descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75th"]-descriptive[columnName]["Q1:25th"]
        descriptive[columnName]["1.5"]=1.5*descriptive[columnName]["IQR"]
        descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25th"]-descriptive[columnName]["1.5"]
        descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75th"]+descriptive[columnName]["1.5"]
        descriptive[columnName]["Min"]=dataset[columnName].min()
        descriptive[columnName]["Max"]=dataset[columnName].max()
        descriptive[columnName]["Skewness"]=dataset[columnName].skew()
        descriptive[columnName]["Kurtosis"]=dataset[columnName].kurtosis()
        descriptive[columnName]["Var"]=dataset[columnName].var()
        descriptive[columnName]["STD"]=dataset[columnName].std()
    return descriptive