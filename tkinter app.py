
import tkinter as tk
root.title('simple tkinter ap')

root = tk.TK()
root.geometry('200*100')
def say_hello():
    print('Hello,World!')
    
hello_button = tk.Button(root,text="click Me",command=say_Hello)
hello_button.pack(pady=20)
root.mainloop()

