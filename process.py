import pandas as pd

re = pd.read_csv(r"C:\Users\Lenovo\OneDrive - UGM 365\Skripsi Training\data2.csv") #kl gapakek r error krn \L \U \O dianggep special character
print(re)
print("anjay\t kntl") #tab
print(r"anjay\x kntl") #r itu raw string nganggep semua dalem " " sebagai string
