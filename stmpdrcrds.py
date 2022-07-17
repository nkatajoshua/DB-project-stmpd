import csv

from cs50 import SQL


open("stmpdmusic.db", "w").close()

db = SQL("sqlite:///stmpdmusic.db")

db.execute("CREATE TABLE artists (Artist_id INTEGER, artist_name TEXT, PRIMARY KEY(Artist_id))")

db.execute("CREATE TABLE releases (Artist2_id INTEGER, Track2_id INTEGER, Album2_id INTEGER, Genre2_id INTEGER, FOREIGN KEY(Track2_id) REFERENCES artists(Artist_id), FOREIGN KEY(Album2_id) REFERENCES tracks(Track_id), FOREIGN KEY(Artist2_id) REFERENCES genres(Genre_id), FOREIGN KEY(Genre2_id) REFERENCES albums(Album_id))")

db.execute("CREATE TABLE tracks (Track_id INTEGER, track_name TEXT, PRIMARY KEY(Track_id))")

db.execute("CREATE TABLE albums (Album_id INTEGER, album_name TEXT,PRIMARY KEY(Album_id))")

db.execute("CREATE TABLE genres (Genre_id INTEGER, genre_name TEXT, PRIMARY KEY(Genre_id))")



with open("stmpd.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        Aname = row["Artists"].strip().capitalize()
        Aid = db.execute("INSERT INTO artists (artist_name) VALUES(?)", Aname)
    
        Tname = row["Track"].strip().capitalize()
        Tid = db.execute("INSERT INTO tracks (track_name) VALUES(?)", Tname)
    
        Alname = row["Album"].strip().capitalize()
        Alid = db.execute("INSERT INTO albums (album_name) VALUES(?)", Alname) 
        
        Gname = row["Genre"].strip().capitalize()
        Gid = db.execute("INSERT INTO genres (genre_name) VALUES(?)", Gname)
        
        for id1 in row["Artists"].split(", "):
            db.execute("INSERT INTO releases(Artist2_id,Track2_id,Album2_id,Genre2_id) VALUES((SELECT DISTINCT Artist_id FROM artists WHERE artist_name =?),(SELECT DISTINCT Track_id FROM tracks WHERE track_name =?),(SELECT DISTINCT Album_id FROM albums WHERE album_name =?),(SELECT DISTINCT Genre_id FROM genres WHERE genre_name =?))",Aname,Tname,Alname,Gname)
            
        
           
              

        

        
        
   