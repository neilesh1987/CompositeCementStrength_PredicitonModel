from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing
# orchestron Layer Design : Entry Point Modeling
def main(): # Function Definition
  df = data_ingestion()
  #Step2: Data preprocessing and cleaning
  X_train,X_test,y_train,y_test = data_preprocessing(df)
  print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)


main()# Function Calling