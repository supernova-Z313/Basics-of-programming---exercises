# ahmadreza zabihi chashmi   S.N=400521342
import sqlite3

con = sqlite3.connect('second_Q.db')
cur = con.cursor()

# cur.execute("""CREATE TABLE users(
#     Username TEXT,
#     Password TEXT
#     )""")

def add_user(username, password):
    con = sqlite3.connect('second_Q.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
    con.commit()
    

def delete(username):
    con = sqlite3.connect('second_Q.db')
    cur = con.cursor()
    cur.execute('DELETE FROM users WHERE username=' , username)
    con.commit()
    con.close
    
def change(password1 , password2):
    delete(password1)
    add_user(password2)  
    return  


# add_user('ahmad', '400521342')

con.commit()
con.close()


# input('Enter a key to exit:')
