# -*- coding: utf-8 -*-
"""project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wV_BSmTYDsskHhZ8dQSTupeX8b5hi2i1
"""

#pip install streamlit

def main():
  st.title("Twitter Scrapper using snscrape")
  menu=["Dataset"]
  choice=st.sidebar.selectbox("Menu",menu)
  if choice == "Dataset":
    st.subheader("Dataset")
    data_file=st.file_uploader("/content/DC.csv",type=["csv"])
    if data_file is not None:
      st.write(type(data_file))
      file_details={"Batman":data_file.name}
      df=pd.read_csv(data_file)
      st.dataframe(df)

import streamlit as st
