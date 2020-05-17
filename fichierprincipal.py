from tkinter import *
import tkinter.messagebox
import LibBksDatabase


class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Gestion d'une Librairie")
        self.root.geometry("1000x350")
        self.root.config(bg="white")
        root.iconbitmap('images/librairie.ico')

        Mty = StringVar()       # Member type
        Ref = StringVar()       # Reference N°
        Tit = StringVar()       # Title
        fna = StringVar()       # First Name
        sna = StringVar()       # Surname
        Adr1 = StringVar()      # Address1
        Adr2 = StringVar()      # Address2
        pcd = StringVar()       # Post Code
        MNo = StringVar()       # Mobile N°
        BKID = StringVar()      # Book id
        Bkt = StringVar()       # Book Title
        Atr = StringVar()       # Author
        DBo = StringVar()       # Date Borrowed
        Ddu = StringVar()       # Date Due
        sPr = StringVar()       # Days on loan
        LrF = StringVar()       # Late Return Fine
        DoD = StringVar()       # Date Over Due
        DonL = StringVar()      # Selling Price

        #********************* Functions Declaration ***************************************************

        def iExit():
            iExit=tkinter.messagebox.askyesno("Gestion d'une librairie","Confirmez si Vous Souhaitez Sortir")
            if iExit > 0:
                root.destroy()
                return

        def ClearData():
            self.txtMType.delete(0 ,END)
            self.txtBKID.delete(0,END)
            self.txtRef.delete(0,END)
            self.txtBkt.delete(0,END)
            self.txtTit.delete(0 ,END)
            self.txtAtr.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtDdu.delete(0,END)
            self.txtAdr1.delete(0,END)
            self.txtAdr2.delete(0,END)
            self.txtDonL.delete(0,END)
            self.txtLrF.delete(0,END)
            self.txtpcd.delete(0,END)
            self.txtDoD.delete(0,END)
            self.txtMNo.delete(0,END)
            self.txtsPr.delete(0,END)
            self.txtDBo.delete(0,END)

        def addData():
            if (len(Mty.get()) !=0):
                LibBksDatabase.addDataRec(Mty.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),
                                          pcd.get(),MNo.get(),BKID.get(),Bkt.get(),Tit.get(),Atr.get(),DBo.get(),
                                          Ddu.get(),sPr.get(),LrF.get(),DoD.get())
                booklist.delete(0,END)
                booklist.insert(END,(Mty.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),
                                          pcd.get(),MNo.get(),BKID.get(),Bkt.get(),Tit.get(),Atr.get(),DBo.get(),
                                          Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get()))

        def DisplayData():
            booklist.delete(0, END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END, row)

        def SelectedBook(event):
            global sb
            searchBK = booklist.curselection()[0]
            sb=booklist.get(searchBK)

            self.txtMType.delete(0, END)
            self.txtMType.insert(END,sb[1])
            self.txtBKID.delete(0, END)
            self.txtBKID.insert(END, sb[2])
            self.txtRef.delete(0, END)
            self.txtRef.insert(END, sb[3])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sb[4])
            self.txtTit.delete(0, END)
            self.txtTit.insert(END, sb[5])
            self.txtAtr.delete(0, END)
            self.txtAtr.insert(END, sb[6])
            self.txtBkt.delete(0, END)
            self.txtBkt.insert(END, sb[7])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END, sb[8])
            self.txtDdu.delete(0, END)
            self.txtDdu.insert(END, sb[9])
            self.txtAdr1.delete(0, END)
            self.txtAdr1.insert(END, sb[10])
            self.txtAdr2.delete(0, END)
            self.txtAdr2.insert(END, sb[11])
            self.txtDonL.delete(0, END)
            self.txtDonL.insert(END, sb[12])
            self.txtLrF.delete(0, END)
            self.txtLrF.insert(END, sb[13])
            self.txtpcd.delete(0, END)
            self.txtpcd.insert(END, sb[14])
            self.txtDoD.delete(0, END)
            self.txtDoD.insert(END, sb[15])
            self.txtMNo.delete(0, END)
            self.txtMNo.insert(END, sb[16])
            self.txtsPr.delete(0, END)
            self.txtsPr.insert(END, sb[17])
            self.txtDBo.delete(0, END)
            self.txtDBo.insert(END, sb[18])

        def DeleteData():
            if (len(Mty.get()) != 0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()

        def SearchDatabase():
            booklist.delete(0, END)
            for row in LibBksDatabase.SearchData(Mty.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),
                                          pcd.get(),MNo.get(),BKID.get(),Bkt.get(),Tit.get(),Atr.get(),DBo.get(),
                                          Ddu.get(),sPr.get(),LrF.get(),DoD.get()):
                booklist.insert(END,row)

        def update():
            if (len(Mty.get()) != 0):
                LibBksDatabase.dataUpdate(sb[0],Mty.get(), Ref.get(), Tit.get(), fna.get(), sna.get(), Adr1.get(), Adr2.get(),
                                          pcd.get(), MNo.get(), BKID.get(), Bkt.get(), Tit.get(), Atr.get(), DBo.get(),
                                          Ddu.get(), sPr.get(), LrF.get(), DoD.get(), DonL.get())



        # ********************* Frames ***************************************************************

        MainFrame=Frame(self.root)
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=40, pady=8, bg="powder blue", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame,font=("arial",46,"bold"),text=("Gestion d'une Librairie"))
        self.lblTit.grid(sticky=W)

        ButtonFrame= Frame (MainFrame,bd=2,width=1350,height=100,padx=20,pady=20,bg="powder blue",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail= Frame(MainFrame,bd=5,width=1330,height=50,padx=20,relief=RIDGE,bg="Grey")
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=6, width=1200, height=400, padx=20,pady=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=800, height=300, padx=20,relief=RIDGE,
                                   font=("arial",12,"bold"),text="LES INFOS ADHERANTS :",bg="cadet blue")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20,pady=3,relief=RIDGE
                                   ,font=("arial", 12, "bold"), text="DETAILS DES LIVRES :", bg="cadet blue")
        DataFrameRIGHT.pack(side=RIGHT)

        # ********************* Labels and Entrys widgets **********************************************
        self.lblMemberType=Label(DataFrameLEFT,font=("arial", 12, "bold"),text="Type Membre :",padx=2,pady=2,bg="cadet blue")
        self.lblMemberType.grid(row=0,column=0,sticky=W)
        self.txtMType = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = Mty , width=25)
        self.txtMType.grid(row=0, column=1)

        self.lblBKID = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="id livre : ", padx=2, pady=2,bg="cadet blue")
        self.lblBKID .grid(row=0, column=2, sticky=W)
        self.txtBKID = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=BKID, width=25)
        self.txtBKID.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLEFT, font=("arial", 12, "bold"), text=" N° Reference :", padx=2, pady=2, bg="cadet blue")
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblBkt = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Titre du Livre :", padx=2, pady=2, bg="cadet blue")
        self.lblBkt.grid(row=1, column=2, sticky=W)
        self.txtBkt = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Bkt, width=25)
        self.txtBkt.grid(row=1, column=3)

        self.lblTit = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Titre :", padx=2, pady=2,bg="cadet blue")
        self.lblTit.grid(row=2, column=0, sticky=W)
        self.txtTit = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Tit, width=25)
        self.txtTit.grid(row=2, column=1)

        self.lblAtr = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Auteur :", padx=2, pady=2, bg="cadet blue")
        self.lblAtr.grid(row=2, column=2, sticky=W)
        self.txtAtr = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Atr, width=25)
        self.txtAtr.grid(row=2, column=3)

        self.lblfna = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Nom :", padx=2, pady=2, bg="cadet blue")
        self.lblfna.grid(row=3, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=fna, width=25)
        self.txtfna.grid(row=3, column=1)

        self.lblDBo = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date d'Emprunt :", padx=2, pady=2,bg="cadet blue")
        self.lblDBo.grid(row=3, column=2, sticky=W)
        self.txtDBo = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DBo, width=25)
        self.txtDBo.grid(row=3, column=3)

        self.lblsna = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Prénom :", padx=2, pady=6,bg="cadet blue")
        self.lblsna.grid(row=4, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=sna, width=25)
        self.txtsna.grid(row=4, column=1)

        self.lblDdu = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date de Retour :", padx=2, pady=6, bg="cadet blue")
        self.lblDdu.grid(row=4, column=2, sticky=W)
        self.txtDdu = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Ddu, width=25)
        self.txtDdu.grid(row=4, column=3)

        self.lblAdr1 = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Addresse 1 :", padx=2, pady=6, bg="cadet blue")
        self.lblAdr1.grid(row=5, column=0, sticky=W)
        self.txtAdr1 = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Adr1, width=25)
        self.txtAdr1.grid(row=5, column=1)

        self.lblDonL = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Addresse 2 :", padx=2, pady=6,bg="cadet blue")
        self.lblDonL.grid(row=6, column=0, sticky=W)
        self.txtDonL = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DonL, width=25)
        self.txtDonL.grid(row=6, column=1)

        self.lblAdr2 = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Jours de prêt :", padx=2, pady=6,bg="cadet blue")
        self.lblAdr2.grid(row=5, column=2, sticky=W)
        self.txtAdr2 = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Adr2, width=25)
        self.txtAdr2.grid(row=5, column=3)

        self.lblLrF = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="AmendeRetourTardif :", padx=2, pady=6,bg="cadet blue")
        self.lblLrF.grid(row=6, column=2, sticky=W)
        self.txtLrF = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=LrF, width=25)
        self.txtLrF.grid(row=6, column=3)

        self.lblpcd = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Code Postale :", padx=2, pady=2,bg="cadet blue")
        self.lblpcd.grid(row=7, column=0, sticky=W)
        self.txtpcd = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=pcd, width=25)
        self.txtpcd.grid(row=7, column=1)

        self.lblDoD = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date d'échéance::", padx=2, pady=2,bg="cadet blue")
        self.lblDoD.grid(row=7, column=2, sticky=W)
        self.txtDoD = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DoD, width=25)
        self.txtDoD.grid(row=7, column=3)

        self.lblMNo = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="N° Mobile :", padx=2, pady=2,bg="cadet blue")
        self.lblMNo.grid(row=8, column=0, sticky=W)
        self.txtMNo = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=MNo, width=25)
        self.txtMNo.grid(row=8, column=1)

        self.lblsPr = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Prix de vente::", padx=2, pady=2,bg="cadet blue")
        self.lblsPr.grid(row=8, column=2, sticky=W)
        self.txtsPr = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=sPr, width=25)
        self.txtsPr.grid(row=8, column=3)

        # ********************* Listbox and scrollbar *************************************

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky="ns")

        booklist= Listbox(DataFrameRIGHT,width=45,height=12,font=("arial", 12, "bold"),yscrollcommand = scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        # *************************** Buttons  ******************************************

        self.btnAddData = Button(ButtonFrame,text="Ajout",font=("arial",14,"bold"),height=2,width=13,bd=4,command=addData,fg="red")
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData= Button(ButtonFrame, text="Affichage", font=("arial", 14, "bold"), height=2, width=13, bd=4,command=DisplayData,fg="red")
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Effacer", font=("arial", 14, "bold"), height=2, width=13, bd=4,command=ClearData,fg="red")
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Supprimer", font=("arial", 14, "bold"), height=2, width=13, bd=4,command=DeleteData,fg="red")
        self.btnDeleteData.grid(row=0, column=3)

        self.btnUpdateData = Button(ButtonFrame, text="MettreAJour", font=("arial", 14, "bold"), height=2, width=13, bd=4,command=update,fg="red")
        self.btnUpdateData.grid(row=0, column=4)

        self.btnSearchData = Button(ButtonFrame, text="Rechercher", font=("arial", 14, "bold"), height=2, width=13, bd=4,command=SearchDatabase,fg="red")
        self.btnSearchData.grid(row=0, column=5)

        self.btnAddData = Button(ButtonFrame, text="Sortir", font=("arial", 14, "bold"), height=2, width=13, bd=4,command=iExit,fg="red")
        self.btnAddData.grid(row=0, column=6)

if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()

