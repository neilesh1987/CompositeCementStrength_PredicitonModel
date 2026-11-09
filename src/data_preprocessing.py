#step2 : Data Preprocessing and Cleaning
from sklearn.preprocessing import StandardScaler, MinMaxScaler,RobustScaler
from sklearn.model_selection import train_test_split

def data_preprocessing(df):
  '''

  Step1: Feature Engineering and Feature Selection

  Step2 : Split the Dataset into independent columns and dependent columns i.e. X and y
  Step 3: Split the Dataset into Seen and Unseen ( Seen Data: train data and Unseen data : test Data)
  Step4: Scaling/Normalizing the data ( StandardScaler/MinScaler/RobustScaler)
  Step5: Return the seen and unseen data
  '''
  #step 1: Feature Engineering and feature selection
  df['Water_to_Cementitious_MaterialsRatio'] = df['Water  (component 4)(kg in a m^3 mixture)'] / (df['Cement (component 1)(kg in a m^3 mixture)'] + df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)'] + df['Fly Ash (component 3)(kg in a m^3 mixture)'])
  df
  #step2 : Split the dataset into X and y
  target_col = 'Concrete compressive strength(MPa, megapascals) '
  X = df.drop(columns = [target_col])
  y = df[target_col]

  #step3 :- Split the Dataset into Seen and Unseen ( Seen Data: train data and Unseen data : test Data)

  X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                  test_size=0.3,
                                                  random_state = 1)


  #step4 : Noramalization/ Scaling Technique
  sc = MinMaxScaler()
  X_train = sc.fit_transform(X_train) # Seen Data (always use fit.transform() for seen data)
  X_test = sc.transform(X_test) # Unseen data (use transform() for seen data)

  return X_train,X_test,y_train,y_test