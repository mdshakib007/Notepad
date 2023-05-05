import tkinter as tk 
from datetime import datetime

class Clock:
    """this class contains a simple digital Clock"""
    def __init__(self, master):
        self.master = master
        self.master.title('Clock')
        
        self.time_label = tk.Label(master, font=('Arial', 25), fg='black', bg='white')
        self.time_label.pack(padx=50, pady=20)
        
        self.date_label = tk.Label(master, font=('Arial', 18), fg='black', bg='white')
        self.date_label.pack(padx=50, pady=10)
        
        #update time
        self.update_time()      
        
    def update_time(self):
        current_time = datetime.now().strftime('%I:%M:%S %p') #get current time
        current_date = datetime.now().strftime('%B %d, %Y') #get current date
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.master.after(200, self.update_time) #set 200 milisecond updatetime
        
        
def main():
    root = tk.Tk()
    root.geometry('400x200')
    root.maxsize(400,200)
    root.minsize(400,200)
    root.configure(bg='white')
    clock = Clock(root)      
    root.mainloop()
    
if __name__ == '__main__':
    main()
