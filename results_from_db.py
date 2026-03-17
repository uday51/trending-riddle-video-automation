import mysql.connector
from make_video import video


def return_matched_keywords(keywords):
 
 
 
 placeholders = ','.join(['%s'] * len(keywords))
 
 

 conn =mysql.connector.connect(
 
  host="localhost",
  user="root",
  password="uday51@$man",
  port=3306,
  database="riddels"
  )
  
 cursor = conn.cursor()
 query =f"select id, riddle from riddles_yt_new where answer in  ({placeholders}) and processed ='no' order by rand() limit 1 "
 cursor.execute(query , keywords)
 
 common_keywords = cursor.fetchone()
 if common_keywords:
  print(common_keywords[0])
  print(common_keywords[1])
  video(common_keywords[1])
  
  riddle_id = common_keywords[0]
  update_query = "update riddles_yt_new   set processed ='yes' where id = %s"
  cursor.execute(update_query, (riddle_id,))
  conn.commit()
 
 cursor.close()
 conn.close()
 
 
 