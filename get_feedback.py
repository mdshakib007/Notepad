import tkinter as tk
import tkinter.messagebox as tmsg
import push_feedback as pft

class ReportGUI:
    def __init__(self, master):
        self.master = master
        master.geometry('430x430')
        master.title('Give Feedback')
        master.maxsize(490, 430)
        master.minsize(490, 430)

        tk.Label(master, text='Give Us Feedback_', font='monospace 25 bold').grid(
            row=0, column=1, columnspan=2, pady=20)

        tk.Label(master, text='Name', font='monospace 12 bold').grid(row=1, column=0, pady=10)
        tk.Label(master, text='Email', font='monospace 12 bold').grid(row=2, column=0, pady=10)
        tk.Label(master, text='Message', font='monospace 12 bold').grid(row=3, column=0, pady=10)

        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.name_entry = tk.Entry(master, textvariable=self.name, width=40)
        self.email_entry = tk.Entry(master, textvariable=self.email, width=40)
        self.message_entry = tk.Text(master, width=40, height=5)

        self.name_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.message_entry.grid(row=3, column=1)

        b1 = tk.Button(master, text='Submit', relief='groove', command=self.submit_report,
                       font='monospace 10 bold', border=5)
        b1.grid(row=4, column=1, pady=10)

    def submit_report(self):
        name_data = self.name_entry.get()
        email_data = self.email_entry.get()
        report_data = self.message_entry.get(1.0, tk.END).replace('\n', ' ')
        if name_data == '':
            tmsg.showerror('Error', 'Name cannot be empty!')
        elif email_data == '':
            tmsg.showerror('Error', 'Email cannot be empty!')
        else:
            insertdata = pft.Data()
            insertdata.insert_into(name_data, email_data, report_data)
            tmsg.showinfo('Submitted', 'Your report submitted successfully.')
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.message_entry.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    ReportGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

