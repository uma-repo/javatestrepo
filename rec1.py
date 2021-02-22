import pymysql
conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "Pass@123", 
        db='uma', 
        ) 
mycursor = conn.cursor()
sell_qty = 0
buy_qty = 0
sell_prc = 0
buy_prc = 0
sell_dt = 0
buy_dt = 0
buy_remain = 0
sell_remain = 0
mycursor.execute("SHOW TABLES")
mycursor.execute("select * from myscript where Remaining >0 AND Action = 'SELL' limit 1")
for x in mycursor:
  print(x)
  sell_dt = x[0]
  sell_qty = x[2]
  sell_prc = x[4]
  print(sell_dt)
  print(sell_qty)
  print(sell_prc)
  print(sell_remain)

mycursor.execute("select * from myscript where Remaining >0 AND Action = 'BUY' limit 1")
for x in mycursor:
  print(x)
  buy_dt = x[0]
  buy_qty = x[2]
  buy_prc = x[4]
  print(buy_dt)
  print(buy_qty)
  print(buy_prc)
  print(buy_remain)

if(buy_qty >= sell_qty):
   buy_remain = buy_qty - sell_qty
   print("buy-remain is")
   print(buy_remain)
   print("sell-remain is")
   sell_remian = 0
   print(sell_remain)

else:
  sell_remain = sell_qty - buy_qty
  print("sell-remain is")
  print(sell_remain)
  buy_remian = 0
  print("buy-remain is")
  print(buy_remain)