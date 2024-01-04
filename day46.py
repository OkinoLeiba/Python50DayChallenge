#python challenge day46
# Day 46: Create a DataFrame  
# Create  a  Dataframe  using  pandas.  You  are  going  to  create  a 
# code  to  put  the  following  into  a  Dataframe.  You  will  use  the 
# information  in  the  table  below.  Basically,  you  are  going  to 
# recreate this table using pandas. Use the information in the table 
# to recreate the table. 
 
# year Title genre 
# 2009 Brothers Drama 
# 2002 Spider-Man Sci-fi 
# 2009 WatchMen Drama 
# 2010 Inception Sci-fi 
# 2009 Avatar Fantasy 
 
# Extra Challenge: Website Data with Pandas  
# Create a code that extracts data from  a website. You will extract a 
# table from the website. And from that table you will extract columns 
# about the data types in Python and their mutability. You will extract 
# information from the following website: 
# https://en.wikipedia.org/wiki/Python_(programming_language) 
# The following table (next page) is what you will extract from the 
# website. 




def data_frame() -> None:
    import pandas as pd, numpy as np
    
    data_dict = {"year":[2009, 2002, 2009, 2010, 2009],  "Title":["Brothers", "Spider-Man", "WatchMen", "Inception", "Avatar"], "genre":["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy" ]}

   
 
    df1 = pd.DataFrame(data_dict)
    
    # df2 = pd.DataFrame(np.array([[2009, 2002, 2009, 2010, 2009], ["Brothers", "Spider-Man", "WatchMen", "Inception", "Avatar"], ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"]]),
    #                    columns=["year", "Title", "genre"])
    
    df_web = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)", match="Summary of Python 3's built-in types")
    
    print(df1)
    print(df_web[0:2])
 
  
data_frame() 