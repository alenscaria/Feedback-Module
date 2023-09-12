import pandas as pd


#read data from excel file
# df = pd.read_excel('feedback.xlsx')     #df - dataframe containing data
# print(df)


data={'Name':["Alen","Alex","Alan"],'Department':["Comp. Sci","Electro.","IT"]}
df=pd.DataFrame(data)
df.to_excel('out.xlsx',index=False,sheet_name="Students")
