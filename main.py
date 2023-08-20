#<-------------------Libraries---------------------------->
import tkinter as tk
from datetime import datetime
from nltk.chat.util import Chat, reflections
#<--------------------------Funtion for get the current time----------------------->
def time():            
    Now=datetime.now()
    current_time = Now.strftime("%H:%M:%S")
    return current_time

#<---------------------------Funtion for get the current day name-------------------->
def day_name():        
    day=datetime.now()
    return day.strftime('%A')

#<---------------Wishing funtion good morning/good afternon/good evening-------------->
def wishing():
    hour=int(datetime.now().hour)
    if (hour>=0 and hour<12):
        return "Good morning sir!"
    elif(hour>=12 and hour<18):
        return "Good afternon sir!"
    else:
        return "Good evening sir!"
    
#<-----------------------------Funtion for showing wishies-------------------------->
    
def wishing_Show_on_tk_window():
    wish=wishing()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, wish+"\n")
    chat_history.config(state=tk.DISABLED)


   
#<--------------------Funtion for main funtionalities for chatbot--------------------->
def Chatbot():          
  set_rules=[
      [
        r"my name is (.*)",
        ["Hello %1,How are you?"]
    ],
    [
    r"hi|Hello|hey",
    ["Hello","hey there"]
    ],
    [
        r"What is time now?",
        ["its"+" "+time()],
    ],
    [
        r"what is day today?",
        ["Today is"+" "+day_name(),],
    ],
    [
        r"How are you?",
        ["Fine! and you"],
    ],
    [
        r"Fine!|i am good|i am doing good",
        ["Great! how can I help you."]
    ],
    
    ]
  test=Chat(set_rules,reflections)
  bot_resp=test.converse(user_input)
  return bot_resp

 #<----------------funtion for get the response for chatbot----------------------------->
def get_query():            
   if Chatbot()==None:
      return "Chatbot: Sorry! I dind't got you"
   return "Chatbot: "+Chatbot()

#<-------------Funtion that used to show the user query and chatbot response on the tkinter text box-------------->
def send_query():            
    global user_input
    user_input=entry.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.config(state=tk.DISABLED)
    

    response = get_query()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, response + "\n", "bold")
    chat_history.config(state=tk.DISABLED)
    chat_history.see("end")

    entry.delete(0, tk.END)

#<-------------------------------------Coding of chatbot User interface-------------------------------------------->
root=tk.Tk()

arrow = tk.PhotoImage(file = r'right-arrow.png')

root.title("Chatbot")
root.geometry("300x400")
root.minsize(300,400)
root.maxsize(300,400)

scroll_bar=tk.Scrollbar(root, orient='vertical')
scroll_bar.pack(side="right",fill='y')

chat_history = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED,borderwidth=1,yscrollcommand=scroll_bar.set, highlightthickness=1,height=22.2,bg="#D0F6E8")
chat_history.pack()
chat_history.tag_configure("bold", font=("Helvetica", 12, "bold"))

scroll_bar.config(command=chat_history.yview)

entry=tk.Entry(root,width=40,borderwidth=1, highlightthickness=1,background="#1CF4A4")
entry.place(x=1,y=366)
entry.bind("<Return>", lambda event: send_query())

Submit_Query=tk.Button(root, image=arrow,borderwidth=0,command = send_query)
Submit_Query.place(x=254,y=364)
wishing_Show_on_tk_window()
root.mainloop()