import tkinter
from tkinter import ttk,messagebox
import pyodbc
import tkcalendar


def welcome():
    root = tkinter.Tk()
    root.title('Database2 - Social Application')
    root.geometry('300x300')
    root['padx']=20
    LOG_btn = tkinter.Button(root,text='Loign',command=LOGAction)
    LOG_btn.grid(row=1,column=1,pady=20)
    REG_btn = tkinter.Button(root,text='Register',command=REGAction)
    REG_btn.grid(row=2,column=1,pady=20)
    root.mainloop()

def LOGAction():
    loginUI()

def REGAction():
    Register()

con = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-JKAAB6J\SQLEXPRESS;'
                      'Database=Social;'
                      'Trusted_Connection=yes;')
cursor = con.cursor()

## REGISTER Window & Button
def regBtnAction():
    if (fnameinput.get()=='' or emailinput.get() == '' or useinput.get() =='' or pasinput.get() ==''):
        messagebox.showerror('Error, Fill Required fields',parent=main_window)
    else:
        try:
            cursor.execute(
                'insert into users(F_Name,L_Name,Email,Username,Password,Gender,Birth_Date,Address,bio) values(?,?,?,?,?,?,?,?,?);',(fnameinput.get(),lnameinput.get(),emailinput.get(),useinput.get(),pasinput.get(),genderinput.get(),birthinput.get(),addressinput.get(),bioinput.get())
            )
            con.commit()
            messagebox.showinfo("Successful Registeration",parent=main_window)
        except Exception as es:
            messagebox.showerror('Error due to',str(es),parent=main_window)
def Register():
    global main_window
    main_window = tkinter.Tk()
    main_window.title('Database2 - Social Application')
    main_window['padx']=20
    main_window.geometry('350x480')
    fname_input=tkinter.StringVar()
    lname_input=tkinter.StringVar()
    use_input=tkinter.StringVar()
    pas_input=tkinter.StringVar()
    email_input=tkinter.StringVar()
    gender_input=tkinter.StringVar()
    address_input=tkinter.StringVar()
    bio_input=tkinter.StringVar()

    title=tkinter.Label(main_window,text='Registeration',font=('arial',16,'bold'))
    title.grid(row=0,column=0,pady=20)

    info_fname= tkinter.Label(main_window,text='First Name *')
    info_fname.grid(row=1,column=0)
    global fnameinput
    fnameinput=tkinter.Entry(main_window,textvariable=fname_input)
    fnameinput.grid(row=1,column=1)

    info_lname=tkinter.Label(main_window,text='Last Name')
    info_lname.grid(row=2,column=0,pady=20)
    global lnameinput
    lnameinput=tkinter.Entry(main_window,textvariable=lname_input)
    lnameinput.grid(row=2,column=1)
    
    info_email=tkinter.Label(main_window,text='Email *')
    info_email.grid(row=3,column=0)
    global emailinput
    emailinput=tkinter.Entry(main_window,textvariable=email_input)
    emailinput.grid(row=3,column=1)

    info_use=tkinter.Label(main_window,text='Username *')
    info_use.grid(row=4,column=0,pady=20)
    global useinput
    useinput=tkinter.Entry(main_window,textvariable=use_input)
    useinput.grid(row=4,column=1)

    info_pas=tkinter.Label(main_window,text='Password *')
    info_pas.grid(row=5,column=0)
    global pasinput
    pasinput=tkinter.Entry(main_window,textvariable=pas_input)
    pasinput.grid(row=5,column=1)

    info_gender=tkinter.Label(main_window,text='Gender')
    info_gender.grid(row=6,column=0,pady=20)
    global genderinput
    genderinput=ttk.Combobox(main_window,textvariable=gender_input)
    genderinput['values']=("Female","Male")
    genderinput.grid(row=6,column=1)

    info_birth=tkinter.Label(main_window,text='Birth Data')
    info_birth.grid(row=7,column=0)
    global birthinput
    birthinput=tkcalendar.DateEntry(main_window)
    birthinput.grid(row=7,column=1)

    info_address=tkinter.Label(main_window,text='Address')
    info_address.grid(row=8,column=0,pady=20)
    global addressinput
    addressinput=tkinter.Entry(main_window,textvariable=address_input)
    addressinput.grid(row=8,column=1)

    info_bio=tkinter.Label(main_window,text='bio')
    info_bio.grid(row=9,column=0)
    global bioinput
    bioinput=tkinter.Entry(main_window,textvariable=bio_input)
    bioinput.grid(row=9,column=1)

    reg_btn = tkinter.Button(main_window,text='Register',command=regBtnAction)
    reg_btn.grid(row=10,column=1,pady=20)

    main_window.mainloop()


## LOGIN Window & Button
def loginUI():
    main_window = tkinter.Tk()
    main_window.title('Database2 - Social Application')
    main_window.geometry('300x300')
    main_window['padx']=20
    user_input=tkinter.StringVar()
    pass_input=tkinter.StringVar()
    
    info_label=tkinter.Label(main_window,text='Login',font=('arial',16,'bold'))
    info_label.grid(row=0,column=0,pady=20)
    
    info_user= tkinter.Label(main_window,text='Username')
    info_user.grid(row=1,column=0)
    global userinput
    userinput=tkinter.Entry(main_window,textvariable=user_input)
    userinput.grid(row=1,column=1)

    info_pass=tkinter.Label(main_window,text='Password')
    info_pass.grid(row=2,column=0,pady=20)
    global passinput
    passinput=tkinter.Entry(main_window,textvariable=pass_input)
    passinput.grid(row=2,column=1)

    login_btn = tkinter.Button(main_window,text='Login',command=logBtnAction)
    login_btn.grid(row=3,column=1)

    main_window.mainloop()
# end of loginUI function

def logBtnAction():
    if (passinput.get() =='' or userinput.get() =='' ):
        messagebox.showerror('Empty fields')
    else:
        try:
            cursor.execute('select * from users where Username= ? and Password= ?',(userinput.get(),passinput.get()))
            username = cursor.fetchone()
            print(username )
            if (username is not None ):
                messagebox.showinfo("Successful Login")
                post() ####################################
            else:
                messagebox.showerror('Not found, Try again') 
        except Exception as es:
            messagebox.showerror('Error due to',str(es))
# end of loginBtnAction function

#home page and Post Button and Search:
def post():
    global main_window
    main_window = tkinter.Tk()
    main_window.title('Database2 - Social Application')
    main_window['padx']=20
    main_window.geometry('300x380')
    post_input=tkinter.StringVar()
    global postinput
    postinput=tkinter.Entry(main_window,textvariable=post_input)
    postinput.grid(row=1,column=1,padx=10,pady=10,ipadx=50, ipady=40)
    post_btn = tkinter.Button(main_window,text='Post',command=postBtnAction)
    post_btn.grid(row=2,column=1,pady=5,ipadx=20)
    home_btn = tkinter.Button(main_window,text='Go to home page',command=homeBtnAction)
    home_btn.grid(row=3,column=1,ipadx=60,pady=20)
    info_search=tkinter.Label(main_window,text='Search with Username or Email:')
    info_search.grid(row=4,column=1,pady=5,sticky='W')
    Search = tkinter.StringVar()
    global search_entry
    search_entry = tkinter.Entry(main_window,bd = 2, textvariable = Search, bg='#FAFAFA')
    search_entry.grid(row=5,column=1,pady=2,ipadx=60)
    search_btn = tkinter.Button(main_window,text='Search',command=searchBtnAction)
    search_btn.grid(row=6,column=1,pady=5,ipadx=20)
    messages_btn = tkinter.Button(main_window,text='Messages',command=messagesBtnAction)
    messages_btn.grid(row=7,column=1,ipadx=60,pady=20)
    main_window.mainloop()

#Post Button
def postBtnAction():
    if postinput.get()!= "":
        if len(postinput.get())<1000:
            try:
                postBtnAction.count+=1
                cursor.execute(
                    'insert into posts(id, content, user_name) values(?,?,?);',(postBtnAction.count,postinput.get(),userinput.get())
                )
                con.commit()
            except Exception as es:
                messagebox.showerror('Error due to',str(es))
        else:
            messagebox.showerror("Exceed 1000 Letters")
    else:
        messagebox.showerror("Empty post")

################################################################################

# Messages Button 

def messagesBtnAction():
    messages_window = tkinter.Tk()
    messages_window.title('Database2 - Social Application')
    messages_window['padx']=20
    messages_window.geometry('370x400')
    cursor.execute(
        'select count(username) from users where username <> ?',(userinput.get())
    )
    friends_num = cursor.fetchone()[0]
    if friends_num != 0:
        friends_list = []
        cursor.execute(
            'select dbo.concat_Name(f_name,l_name),username from users where username <> ?',(userinput.get())
        )
        for each_username in range(friends_num):
            friends_list.append(cursor.fetchone())
        for c,friend in zip(range(friends_num),friends_list):
            name = friend[0]
            uname = friend[1]

            info_Name=tkinter.Label(messages_window,text=name,font=('arial',10))
            info_Name.grid(row=c,column=0,pady=10,sticky='W',padx=10)

            cursor.execute('EXEC number_of_messages ?, ?',(userinput.get(),uname))
            number_of_messages = str(cursor.fetchone()[0])

            info_Name=tkinter.Label(messages_window,text=number_of_messages,font=('arial',10))
            info_Name.grid(row=c,column=1,sticky='W',padx=10)

    messages_window.mainloop()


#Searh Button 
def searchBtnAction():
    if (len(search_entry.get())>=3):

        cursor.execute(
            'EXEC  searchRes_num ?',(search_entry.get())
        )
        Res_num = cursor.fetchone()[0]
        print('++++++++++++++++++++++++++++++++++++',Res_num)
        if (Res_num != 0):
            chat1_window = tkinter.Tk()
            chat1_window.title('Database2 - Social Application')
            chat1_window['padx']=20
            chat1_window.geometry('370x400')

            cursor.execute(
                'EXEC  searchRes ?',(search_entry.get())
            )
            global search_list
            search_list = []
            for Res in range(0,Res_num):
                search_list.append(cursor.fetchone()[0])

            
            for searchNum,item in zip(range(0,len(search_list)),search_list):   
                cursor.execute(
                    'EXEC searchRes_info ?',(item)
                ) 
                l = cursor.fetchone()
                F_Name = l[0]
                L_Name = l[1]
                U_name = l[2]
                print(F_Name,L_Name,U_name)
                
                info_F_Name=tkinter.Label(chat1_window,text=F_Name+' '+L_Name,font=('arial',10))
                info_F_Name.grid(row=searchNum,column=0,pady=10,sticky='W',padx=10)

                globals()['chat_btn'+str(searchNum)]= tkinter.Button(chat1_window,text='Start Chatting', command=lambda b='chat_btn'+str(searchNum): chatBtnAction(b))
                globals()['chat_btn'+str(searchNum)].grid(row=searchNum,column=2,pady=10,padx=10,ipadx=40)

                print(search_list)
                chat1_window.mainloop()
        else:
            messagebox.showerror("No Users are Found")
    else:
        messagebox.showerror("Less than 3 chars")

#Start Chat Button 
def chatBtnAction(var):
    searchNum = int(var[len(var)-1:])
    chat_username = search_list[searchNum]
    cursor.execute(
        'EXEC searchRes_info ?',(chat_username)
    ) 
    l = cursor.fetchone()
    global F_Name
    F_Name = l[0]
    global L_Name
    L_Name = l[1]
    global To_U_name
    To_U_name = l[2]
    print(F_Name,L_Name,To_U_name)

    chat_window = tkinter.Tk()
    chat_window.title(F_Name + ' ' + L_Name + ' Chat')
    chat_window['padx']=20
    chat_window.geometry('360x200')

    chat_input= tkinter.StringVar()
    global chatinput
    chatinput=tkinter.Entry(chat_window,textvariable=chat_input)
    chatinput.grid(row=1,column=0,ipadx=100,pady= 20)

    send_btn = tkinter.Button(chat_window,text='Send',command=sendBtnAction)
    send_btn.grid(row=2,column=0,sticky='E')

    refresh_btn = tkinter.Button(chat_window,text='Refresh Messages',command=refreshBtnAction)
    refresh_btn.grid(row=3,column=0,ipadx=100,pady= 30)

 #Send Message Button
def sendBtnAction():
    if chatinput.get()!='':
        sendBtnAction.count+=1
        cursor.execute('EXEC send_message ?,?,?,?;',(sendBtnAction.count,chatinput.get(),userinput.get(),To_U_name))
        con.commit()
    else:
        messagebox.showerror("Empty Message")

#Refresh Messages Button
def refreshBtnAction():
    cursor.execute('EXEC number_of_messages ?, ?',(userinput.get(),To_U_name))
    messages_num = cursor.fetchone()[0]
    if messages_num is not None:
        chat_window = tkinter.Tk()
        chat_window.title(F_Name + ' ' + L_Name + ' Chat')
        chat_window['padx']=20
        chat_window.geometry('370x400')

        cursor.execute('EXEC get_all_messages ?, ?',(userinput.get(),To_U_name))
        messages_list = []
        print(messages_num)
        for messages_counter in range(messages_num):
            messages_list.append(cursor.fetchone())
            print(messages_list[messages_counter])
        count = 0
        print(messages_list)
        for  num,message_row in zip(range(len(messages_list)),messages_list):
            count += 1
            if messages_list[num][2] == userinput.get():
                info_F_Name=tkinter.Label(chat_window,text=messages_list[num][1],font=('arial',10),borderwidth=2,relief="groove",anchor='w')
                info_F_Name.grid(row=count,column=0,pady=5,sticky='W',padx=10,ipadx=100)
            elif messages_list[num][2] == To_U_name:
                info_F_Name=tkinter.Label(chat_window,text=messages_list[num][1],font=('arial',10),borderwidth=2,relief="groove",anchor='e')
                info_F_Name.grid(row=count,column=0,pady=5,sticky='E',padx=10,ipadx=100)


## Home Page & Like - Comment Buttons

#Go to Home page Button 
like_dict=dict()
def homeBtnAction():
    global main_window
    main_window = tkinter.Tk()
    main_window.title('Database2 - Social Application')
    main_window['padx']=20
    main_window.geometry('500x400')
    cursor.execute('select count(id) from posts')
    posts_num = cursor.fetchone()[0]
    comment_input=tkinter.StringVar()
    global commentinput
    if posts_num is not None:
        for i,j in zip(range(posts_num,0,-1),range(1,posts_num+1)):
            cursor.execute('select content from posts where id=?',(i))
            post_content = cursor.fetchone()[0]
            info_post=tkinter.Label(main_window,text=post_content,borderwidth=2,relief="groove")
            info_post.grid(row=(j*2)-1,column=0,pady=10,columnspan=4,ipadx=130,ipady=20)
            globals()['like_btn'+str(i)]= tkinter.Button(main_window,text='Like',command=lambda b='like_btn'+str(i): likeBtnAction(b))
            globals()['like_btn'+str(i)].grid(row=j*2,column=0,pady=3,padx=3)
            globals()['commentinput'+str(i)]=tkinter.Entry(main_window)#,textvariable=comment_input)
            globals()['commentinput'+str(i)].grid(row=j*2,column=2,ipadx=20,padx=3)
            globals()['comment_btn'+str(i)]= tkinter.Button(main_window,text='Comment',command=lambda b='comment_btn'+str(i) :commentBtnAction(b))
            globals()['comment_btn'+str(i)].grid(row=j*2,column=3,padx=3)
    main_window.mainloop()

#Like Button Action 
def likeBtnAction(var):
    postnum = int(var[len(var)-1:])
    cursor.execute('select * from likes where post_id= ? and user_name= ?',(postnum,userinput.get()))
    liked = cursor.fetchone()
    print(liked)
    if (liked is None):
        likeBtnAction.count+=1
        cursor.execute('insert into likes(id, user_name, post_id) values(?,?,?);',(int(likeBtnAction.count),userinput.get(),postnum))
        con.commit()

#Comment Button Action
def commentBtnAction(var):
    postnum = int(var[len(var)-1:])
    if globals()['commentinput'+str(postnum)].get() !='':
        commentBtnAction.count+=1
        cursor.execute('insert into comments(id, content, user_name, post_id) values(?,?,?,?);',(int(commentBtnAction.count)+1,globals()['commentinput'+str(postnum)].get(),userinput.get(),postnum))
        con.commit()
    else:
        messagebox.showinfo("Empty comment")


cursor.execute('select max(id) from posts')
postBtnAction.count = cursor.fetchone()[0]
if postBtnAction.count is None:
    postBtnAction.count = 0

cursor.execute('select max(id) from likes')
likeBtnAction.count = cursor.fetchone()[0]
if likeBtnAction.count is None:
    likeBtnAction.count = 0

cursor.execute('select max(id) from comments')
commentBtnAction.count = cursor.fetchone()[0]
if commentBtnAction.count is None:
    commentBtnAction.count = 0

cursor.execute('select max(id) from chats')
sendBtnAction.count = cursor.fetchone()[0]
if sendBtnAction.count is None:
    sendBtnAction.count = 0

welcome()
