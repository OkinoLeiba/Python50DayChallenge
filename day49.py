#python challenge day49
# Day 49: Create a Database  
# For  this  challenge,  you  are  going  to  create  a  database  using 
# Python’s  SQLite.  You  will  import  SQLite  into  your  script. 
# Create a database called movies.db. In that database, you are 
# going  to  create  a  table  called  movies.  In  that  table,  you  are 
# going to save the following movies: 
 
# year title genre 
# 2009 Brothers Drama 
# 2002 Spider Man Sci-fi 
# 2009 WatchMen Drama 
# 2010 Inception Sci-fi 
# 2009 Avatar Fantasy 
 
# a)  Once  you  create  a  table,  run  a  SQL  query  to  see  all  the 
# movies in your table. 
# b) Run another SQL query to select only the movie Brothers 
# from the list. 
# c)  Run  another  SQL  query  to  select  all  movies  that  were 
# released in 2009 from your table. 
# d) Run  another  query  to  select  movies  in  the  fantasy  and 
# drama genre. 
# e)  Run a query to delete all the contents of your table.





def create_database() -> None:
    import sqlite3
    
    con = sqlite3.connect(":memory:")
    con = sqlite3.connect("Movies.db")
    cur = con.cursor()
    # cur.execute("IF EXISTS DROP TABLE Movies")
    cur.execute("DROP TABLE Movies")
    cur.execute("CREATE TABLE Movies(Year, Title, Genre)")
    
    movies_data = [(2009, 'Brothers', 'Drama'), 
          (2002, 'Spider-Man', 'Sci-fi'), 
          (2009, 'WatchMen', 'Drama'), 
          (2010, 'Inception', 'Sci-fi'), 
          (2009, 'Avatar', 'Fantasy')] 
    
    cur.executescript("""
                     INSERT INTO Movies VALUES(2009, "Brothers", "Drama");
                     INSERT INTO Movies VALUES(2002, "Spider Man", "Sci-fi");
                     INSERT INTO Movies VALUES(2009, "WatchMen", "Drama");
                     INSERT INTO Movies VALUES(2010, "Inception", "Sci-fi");
                     INSERT INTO Movies VALUES(2009, "Avatar", "Fantasy");
                      """ 
                      )
    
    cur.executemany('''INSERT INTO Movies VALUES(?, ?, ?);''', movies_data)
    
    con.commit()
    
    row = cur.fetchall() 
    
    cur.execute("SELECT * FROM Movies")
    for row in cur.execute("SELECT * FROM Movies"):
        print(row)
    
    cur.execute("SELECT * FROM Movies WHERE Year = 2009")
    
    cur.execute("SELECT * FROM Movies WHERE Genre IN ('Fantasy', 'Drama')")
    
    cur.execute("DELETE FROM Movies")
    
    cur.execute("DROP TABLE Movies")
    
    cur.close()


create_database()