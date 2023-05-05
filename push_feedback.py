import mysql.connector

class Data:
    '''this class push user's input to the database.'''
    
    @staticmethod
    def insert_into(val1, val2, val3=None):
        db = mysql.connector.connect(
            host='localhost',
            user='root', 
            password='***********', # i am hided my sql password
            database='tkinter_data'
        )
        
        db_cursor = db.cursor()
        
        formula = """
            INSERT INTO report_data (name, email, issue)
            VALUES (%s, %s, %s)
        """
        values = (val1, val2, val3)
        
        db_cursor.execute(formula, values)
        
        db.commit()
        

if __name__ == '__main__':
    d = Data()
    #d.insert_into('Shakib Ahmed', 'shakibahmed.528874@gmail.com', 'no message.')