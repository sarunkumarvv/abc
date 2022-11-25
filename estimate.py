

                    tab3_5.grid_columnconfigure(0,weight=1)                   
                    tab3_5.grid_rowconfigure(0,weight=1)

                    est_frame = Frame(tab3_5)
                    est_frame.grid(row=0,column=0,sticky='nsew')

                    def est_responsive_widgets(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget

                        dcanvas.coords("ctree1",dwidth/12,dheight/1.8)
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14
                        y2 = dheight/3.505

                        dcanvas.coords("cpoly1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("chline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                        dcanvas.coords("clabel1",dwidth/2.5,dheight/8.00)

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.8


                        dcanvas.coords("cpoly2",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("cbutton1",dwidth/2.1,dheight/2.4)
                        dcanvas.coords("cbutton2",dwidth/1.59,dheight/2.4)
                        dcanvas.coords("cbutton3",dwidth/1.28,dheight/2.26)
                        dcanvas.coords("ccombo1",dwidth/1.179,dheight/1.52)


                    est_canvas=Canvas(est_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

                    est_frame.grid_rowconfigure(0,weight=1)
                    est_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(est_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=est_canvas.yview)
                    est_canvas.bind("<Configure>", est_responsive_widgets)
                    est_canvas.config(yscrollcommand=vertibar.set)
                    est_canvas.grid(row=0,column=0,sticky='nsew')

                    est_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly1"))

                    label_1 = Label(est_canvas,width=12,height=1,text="ESTIMATE", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = est_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("clabel1"))

                    est_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("chline"))

                    
                    est_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly2"))



                    fgthi = ttk.Style()
                    fgthi.configure('mystyle105.Treeview.Heading', background='#2f516f',State='DISABLE')

                    est_scrollbar = Scrollbar(est_frame,orient="vertical")

                    est_tree = ttk.Treeview(est_canvas, columns = (1,2,3,4,5,6,7), height = 10, show = "headings",style='mystyle105.Treeview',yscrollcommand=est_scrollbar.set)
                    est_tree.heading(1)
                    est_tree.heading(2, text="Date")
                    est_tree.heading(3, text="Estimate No")
                    est_tree.heading(4, text="Referance No")
                    est_tree.heading(5, text="Customer Name")
                    est_tree.heading(6, text="Status")
                    est_tree.heading(7, text="Amount")
                    
                    est_tree.column(1, width = 50)
                    est_tree.column(2, width = 200)
                    est_tree.column(3, width = 220)
                    est_tree.column(4, width = 150)
                    est_tree.column(5, width = 150)
                    est_tree.column(6, width = 200)
                    est_tree.column(7, width = 150)
                    window_label_4 = est_canvas.create_window(0, 0, anchor="nw", window=est_tree,tags=('ctree1'))

                    est_scrollbar.config(command=est_tree.yview)
                    est_scrollbar.grid(row=0,column=2,sticky='ns')

                    sql_pr="select * from auth_user where username=%s"
                    sql_pr_val=(nm_ent.get(),)
                    fbcursor.execute(sql_pr,sql_pr_val,)
                    pr_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (pr_dtl[0],)
                    fbcursor.execute(sql, val,)
                    cmp_dtl=fbcursor.fetchone()

                    c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                    c_val_1 = (cmp_dtl[0],)
                    fbcursor.execute(c_sql_1,c_val_1,)
                    c_data_1 = fbcursor.fetchall()

                    count0 = 0
                    for i in c_data_1:
                        if True:
                            est_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                        else:
                            pass
                    count0 += 1


                    def new_estimate():
                        est_frame.grid_forget()
                        est_frame_1 = Frame(tab3_5)
                        est_frame_1.grid(row=0,column=0,sticky='nsew')

                        def est_responsive_widgets2(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("acpoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.45


                            dcanvas.coords("acpoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


                        est_canvas_1=Canvas(est_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                        est_frame_1.grid_columnconfigure(0,weight=1)
                        est_frame_1.grid_rowconfigure(0,weight=1)

                        
                        vertibar=Scrollbar(est_frame_1, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=est_canvas_1.yview)

                        est_canvas_1.bind("<Configure>", est_responsive_widgets2)
                        est_canvas_1.config(yscrollcommand=vertibar.set)
                        est_canvas_1.grid(row=0,column=0,sticky='nsew')
                        
                        def sales_add_new_cus():
                            title = comb_est_1.get()
                            firstname = entry_est_f1.get()
                            lastname = entry_est_l2.get()
                            company = entry_est_com3.get()
                            location = est_loc4.get()
                            gsttype = comb_est_g2.get()
                            gstin = entry_est_gin5.get()
                            panno = entry_est_pan6.get()
                            email = entry_est_em7.get()
                            website = entry_est_web8.get()
                            mobile = entry_est_mob9.get()
                            street = entry_est_10.get()
                            city = entry_est_12.get()
                            state = entry_est_13.get()
                            pincode = entry_est_p12.get()
                            country = entry_est_c13.get()
                            shipstreet = entry_est_11.get()
                            shipcity = entry_est_14.get()
                            shipstate = entry_est_15.get()
                            shippincode = entry_est_pin.get()
                            shipcountry = entry_est_c15.get()

                            usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usr_val = (nm_ent.get(),)
                            fbcursor.execute(usr_sql,usr_val)
                            usr_data = fbcursor.fetchone()

                            cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmp_val = (usr_data[0],)
                            fbcursor.execute(cmp_sql,cmp_val)
                            cmp_data = fbcursor.fetchone()
                            cid = cmp_data[0]

                            if chk_str_1.get() == True:

                                est_sql = "INSERT INTO app1_customer (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                est_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid)
                                fbcursor.execute(est_sql,est_val)
                                finsysdb.commit()

                                #----------Refresh Insert Tree--------#

                                for record in est_tree.get_children():
                                        est_tree.delete(record)

                                sql_pr="select * from auth_user where username=%s"
                                sql_pr_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pr,sql_pr_val,)
                                pr_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtl=fbcursor.fetchone()

                                c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                                c_val_1 = (cmp_dtl[0],)
                                fbcursor.execute(c_sql_1,c_val_1,)
                                c_data_1 = fbcursor.fetchall()

                                count0 = 0
                                for i in c_data_1:
                                    if True:
                                        est_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                    else:
                                        pass
                                count0 += 1

                                
                                est_frame_1.destroy()
                                est_frame.grid(row=0,column=0,sticky='nsew')

                            else:
                                pass
                        

                        est_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                        label_1 = Label(est_canvas_1,width=15,height=1,text="ESTIMATE", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = est_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                        est_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                        est_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

#edit

#                        prvbackbtn0 = Button(est_canvas_1, bd=0,text = '<<<Back',foreground='#fff',background='#2f516f',height=1,width=10,font=subheadingfont5, command = editemp_back)
#                        est_canvas_1.create_window(0,0,anchor="nw",window=prvbackbtn0,tags=("prvbackbtn"))

#end
                        label_1 = Label(est_canvas_1,width=20,height=1,text="choose customer", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_1 = est_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))
                      

#edit
                        est_comb_3 = ttk.Combobox(est_canvas_1,font=('arial 10'))
                        est_comb_3['values'] = ("Choose customer",)
                        est_comb_3.current(0)
                        window_est_comb_3 = est_canvas_1.create_window(120, 350, anchor="nw", width=110,height=30,window=est_comb_3,tags=('aclabel2'))
                        est_comb_3.bind("<<ComboboxSelected>>",edit_delete_currency)
#end


                        est_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))


                      
                    btn1=Button(est_canvas,text='New Estimate', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=new_estimate)
                    window_btn1 = est_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton2"))

                    def edit_delete_customer(event):
                        if est_comb_1.get() == 'Edit':
                            est_frame.grid_forget()
                            est_eframe_1 = Frame(tab3_5)
                            est_eframe_1.grid(row=0,column=0,sticky='nsew')

                            def eest_responsive_widgets2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("acpoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                                dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.45


                                dcanvas.coords("acpoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                                dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                                dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                                dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                                dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                                dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                                dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                                dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                                dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                                dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                                dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                                dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                                dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                                dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                                dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                                dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                                dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                                dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                                dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                                dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                                dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                                dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                                dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                                dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                                dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                                dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                                dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                                dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                                dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                                dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                                dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                                dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                                dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                                dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                                dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                                dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                                dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                                dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                                dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                                dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                                dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                                dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                                dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                                dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                                dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                                dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                                dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                                dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                                dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                                dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


                            est_ecanvas_1=Canvas(est_eframe_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                            est_eframe_1.grid_columnconfigure(0,weight=1)
                            est_eframe_1.grid_rowconfigure(0,weight=1)

                            
                            vertibar=Scrollbar(est_eframe_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=est_ecanvas_1.yview)

                            est_ecanvas_1.bind("<Configure>", eest_responsive_widgets2)
                            est_ecanvas_1.config(yscrollcommand=vertibar.set)
                            est_ecanvas_1.grid(row=0,column=0,sticky='nsew')

                            c_editid = est_tree.item(est_tree.focus())["values"][4]
                            print(c_editid)
                            c_editid_1 = est_tree.item(est_tree.focus())["values"][5]
                            print(c_editid_1)

                            sql_u = 'select * from auth_user where username=%s'
                            val_u = (nm_ent.get(),)
                            fbcursor.execute(sql_u,val_u)
                            pr_dtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtl=fbcursor.fetchone()
                            print(cmp_dtl)

                            sql = 'select * from app1_customer where panno = %s and email = %s and cid_id = %s'
                            val =  (c_editid,c_editid_1,cmp_dtl[0],)
                            fbcursor.execute(sql,val)
                            edit_cus = fbcursor.fetchone()
        

                            def sales_edit_new_cus():
                                title = comb_eest_1.get()
                                firstname = entry_eest_1.get()
                                lastname = entry_eest_2.get()
                                company = entry_eest_3.get()
                                location = eest_4.get()
                                gsttype = comb_eest_2.get()
                                gstin = entry_eest_5.get()
                                panno = entry_eest_6.get()
                                email = entry_eest_7.get()
                                website = entry_eest_8.get()
                                mobile = entry_eest_9.get()
                                street = entry_eest_10.get()
                                city = entry_eest_12.get()
                                state = entry_eest_13.get()
                                pincode = entry_eest_p12.get()
                                country = entry_eest_c13.get()
                                shipstreet = entry_eest_11.get()
                                shipcity = entry_eest_14.get()
                                shipstate = entry_eest_15.get()
                                shippincode = entry_eest_pin14.get()
                                shipcountry = entry_eest_co15.get()

                                usre_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usre_val = (nm_ent.get(),)
                                fbcursor.execute(usre_sql,usre_val)
                                usre_data = fbcursor.fetchone()

                                cmpne_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpne_val = (usre_data[0],)
                                fbcursor.execute(cmpne_sql,cmpne_val)
                                cmpne_data = fbcursor.fetchone()
                                cid = cmpne_data[0]

                                if echk_str_1.get() == True:

                                    est_sql = "UPDATE app1_customer set title=%s,firstname=%s,lastname=%s,company=%s,location=%s,gsttype=%s,gstin=%s,panno=%s,email=%s,website=%s,mobile=%s,street=%s,city=%s,state=%s,pincode=%s,country=%s,shipstreet=%s,shipcity=%s,shipstate=%s,shippincode=%s,shipcountry=%s,cid_id=%s where panno=%s and email = %s"
                                    est_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,c_editid,c_editid_1)
                                    fbcursor.execute(est_sql,est_val)
                                    finsysdb.commit()

                                    #----------Refresh Insert Tree--------#

                                    for record in est_tree.get_children():
                                            est_tree.delete(record)

                                    sql_pr_1="select * from auth_user where username=%s"
                                    sql_pr1_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_pr_1,sql_pr1_val,)
                                    pr_dtl_1=fbcursor.fetchone()

                                    sql_2 = "select * from app1_company where id_id=%s"
                                    val_2 = (pr_dtl_1[0],)
                                    fbcursor.execute(sql_2, val_2,)
                                    cmp_dtl_2=fbcursor.fetchone()

                                    c_sql_2 = "SELECT * FROM app1_customer where cid_id=%s"
                                    c_val_2 = (cmp_dtl_2[0],)
                                    fbcursor.execute(c_sql_2,c_val_2,)
                                    c_data_2 = fbcursor.fetchall()

                                    count1 = 0
                                    for i in c_data_2:
                                        if True:
                                            est_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                        else:
                                            pass
                                    count1 += 1

                                    est_eframe_1.destroy()
                                    est_frame.grid(row=0,column=0,sticky='nsew')

                                else:
                                    pass


                            est_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                            label_1 = Label(est_ecanvas_1,width=15,height=1,text="EDIT CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                            est_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                            est_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))


                            label_1 = Label(est_ecanvas_1,width=20,height=1,text="sample", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                            est_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                            comb_eest_1 = ttk.Combobox(est_ecanvas_1, font=('arial 10'))
                            comb_eest_1['values'] = ("Mr","Mrs","Miss","Ms",)
                            comb_eest_1.current(0)
                            window_comb_eest_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_eest_1, tags=("accombo1"))
                            comb_eest_1.delete(0,'end')
                            comb_eest_1.insert(0, edit_cus[1])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                            entry_eest_1=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_1, tags=("acentry1"))
                            entry_eest_1.delete(0,'end')
                            entry_eest_1.insert(0, edit_cus[2])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                            entry_eest_2=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_2, tags=("acentry2"))
                            entry_eest_2.delete(0,'end')
                            entry_eest_2.insert(0, edit_cus[3])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                            entry_eest_3=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_3 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_3, tags=("acentry3"))
                            entry_eest_3.delete(0,'end')
                            entry_eest_3.insert(0, edit_cus[4])


                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                            eest_4=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_eest_4 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=eest_4, tags=("acentry4"))
                            eest_4.delete(0,'end')
                            eest_4.insert(0, edit_cus[5])


                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                            comb_eest_2 = ttk.Combobox(est_ecanvas_1, font=('arial 10'))
                            comb_eest_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                            comb_eest_2.current(0)
                            window_comb_eest_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_eest_2, tags=("accombo2"))
                            comb_eest_2.delete(0,'end')
                            comb_eest_2.insert(0, edit_cus[6])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

                            def gst_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                entry_eest_5.config(fg="white")
                                return True

                            def gst_invalidate():
                                entry_eest_5.config(fg="red")

                            

                            entry_eest_5=Entry(est_ecanvas_1,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                            eval_gst = (est_ecanvas_1.register(gst_validate), '%P')
                            eival_gst = (est_ecanvas_1.register(gst_invalidate),)
                            entry_eest_5.config(validate='focusout', validatecommand=eval_gst, invalidcommand=eival_gst)
                            window_entry_eest_5 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_5, tags=("acentry5"))
                            entry_eest_5.delete(0,'end')
                            entry_eest_5.insert(0, edit_cus[7])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                            def pan_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                entry_eest_6.config(fg="white")
                                return True

                            def pan_invalidate():
                                entry_eest_6.config(fg="red")


                            entry_eest_6=Entry(est_ecanvas_1,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                            eval_pan = (est_ecanvas_1.register(pan_validate), '%P')
                            eival_pan = (est_ecanvas_1.register(pan_invalidate),)
                            entry_eest_6.config(validate='focusout', validatecommand=eval_pan, invalidcommand=eival_pan)
                            window_entry_eest_6 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_6, tags=("acentry6"))
                            entry_eest_6.delete(0,'end')
                            entry_eest_6.insert(0, edit_cus[8])

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                            def email_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                entry_eest_7.config(fg="white")
                                return True

                            def email_invalidate():
                                entry_eest_7.config(fg="red")

                            entry_eest_7=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f')
                            eval_email = (est_ecanvas_1.register(email_validate), '%P')
                            eival_email = (est_ecanvas_1.register(email_invalidate),)
                            entry_eest_7.config(validate='focusout', validatecommand=eval_email, invalidcommand=eival_email)
                            window_entry_eest_7 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_7, tags=("acentry7"))
                            entry_eest_7.delete(0,'end')
                            entry_eest_7.insert(0, edit_cus[9])


                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                            entry_eest_8=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_8 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_8, tags=("acentry8"))
                            entry_eest_8.delete(0,'end')
                            entry_eest_8.insert(0, edit_cus[10])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))
                            

                            entry_eest_9=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_9 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_9, tags=("acentry9"))
                            entry_eest_9.delete(0,'end')
                            entry_eest_9.insert(0, edit_cus[11])

                            label_1 = Label(est_ecanvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                            window_label_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                            entry_eest_10=Entry(est_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_10 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_eest_10, tags=("acentry10"))
                            entry_eest_10.delete(0,'end')
                            entry_eest_10.insert(0, edit_cus[12])


                            label_1 = Label(est_ecanvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                            window_label_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                            echk_str = StringVar()
                            echkbtn1 = Checkbutton(est_ecanvas_1, text = "Same As Billing Address", variable = echk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            echkbtn1.select()
                            window_echkbtn_1 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn1, tags=("accheck1"))

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                            entry_eest_11=Entry(est_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_11 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_eest_11, tags=("acentry11"))
                            entry_eest_11.delete(0,'end')
                            entry_eest_11.insert(0, edit_cus[17])

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                            entry_eest_12=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_12 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_12, tags=("acentry12"))
                            entry_eest_12.delete(0,'end')
                            entry_eest_12.insert(0, edit_cus[13])
                            
                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                            entry_eest_13=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_13 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_13, tags=("acentry13"))
                            entry_eest_13.delete(0,'end')
                            entry_eest_13.insert(0, edit_cus[14])

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                            entry_eest_14=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_14 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_14, tags=("acentry14"))
                            entry_eest_14.delete(0,'end')
                            entry_eest_14.insert(0, edit_cus[18])

                            label_2 = Label(est_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                            entry_eest_15=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_15 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_15, tags=("acentry15"))
                            entry_eest_15.delete(0,'end')
                            entry_eest_15.insert(0, edit_cus[19])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                            entry_eest_p12=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_p12 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_p12, tags=("acentry16"))
                            entry_eest_p12.delete(0,'end')
                            entry_eest_p12.insert(0, edit_cus[15])
                            
                            label_2 = Label(est_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                            entry_eest_c13=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_c13 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_c13, tags=("acentry17"))
                            entry_eest_c13.delete(0,'end')
                            entry_eest_c13.insert(0, edit_cus[16])

                            label_2 = Label(est_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                            entry_eest_pin14=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_pin14 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_pin14, tags=("acentry18"))
                            entry_eest_pin14.delete(0,'end')
                            entry_eest_pin14.insert(0, edit_cus[20])

                            label_2 = Label(est_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                            entry_eest_co15=Entry(est_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_eest_co15 = est_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_eest_co15, tags=("acentry19"))
                            entry_eest_co15.delete(0,'end')
                            entry_eest_co15.insert(0, edit_cus[21])

                            echk_str_1 = BooleanVar()
                            echkbtn2 = Checkbutton(est_ecanvas_1, text = "Agree to terms and conditions", variable = echk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            window_echkbtn_2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn2,tags=("accheck2"))

                            def ec_back_1_():
                                est_eframe_1.grid_forget()
                                est_frame.grid(row=0,column=0,sticky='nsew')

                            ec_bck_btn1=Button(est_ecanvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ec_back_1_)
                            window_ec_bck_btn1 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=ec_bck_btn1,tags=('acbutton3'))

                            eest_btn2=Button(est_ecanvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_edit_new_cus)
                            window_eest_btn2 = est_ecanvas_1.create_window(0, 0, anchor="nw", window=eest_btn2,tags=("acbutton1"))

                        elif est_comb_1.get() == 'Delete':
                            est_del = messagebox.askyesno("Delete Customer","Are you sure to delete this customer?")

                            if est_del == True:
                                est_id_1 = est_tree.item(est_tree.focus())["values"][4]
                                est_id_2 = est_tree.item(est_tree.focus())["values"][5]

                                sql_u = 'select * from auth_user where username=%s'
                                val_u = (nm_ent.get(),)
                                fbcursor.execute(sql_u,val_u)
                                u_dtl = fbcursor.fetchone()

                                sql_c = 'select * from app1_company where id_id=%s'
                                val_c = (u_dtl[0],)
                                fbcursor.execute(sql_c,val_c)
                                c_dtl = fbcursor.fetchone()

                                sql = 'delete from app1_customer where panno=%s and email=%s and cid_id=%s'
                                val = (est_id_1,est_id_2,c_dtl[0],)
                                fbcursor.execute(sql,val)
                                finsysdb.commit()

                                #----------Refresh Insert Tree--------#

                                for record in est_tree.get_children():
                                        est_tree.delete(record)

                                sql_pr="select * from auth_user where username=%s"
                                sql_pr_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pr,sql_pr_val,)
                                pr_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtl=fbcursor.fetchone()

                                c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                                c_val_1 = (cmp_dtl[0],)
                                fbcursor.execute(c_sql_1,c_val_1,)
                                c_data_1 = fbcursor.fetchall()

                                count0 = 0
                                for i in c_data_1:
                                    if True:
                                        est_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                    else:
                                        pass
                                count0 += 1

                            else:
                                pass
                        else:  
                            pass

                    

                    est_comb_1 = ttk.Combobox(est_canvas,font=('arial 10'))
                    est_comb_1['values'] = ("Actions","Edit","Delete")
                    est_comb_1.current(0)
                    window_est_comb_1 = est_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=est_comb_1,tags=('cbutton3'))
                    est_comb_1.bind("<<ComboboxSelected>>",edit_delete_customer)
