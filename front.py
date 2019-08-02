from tkinter import*
import tkinter.messagebox as ms 
from tkinter import ttk
import sqlite3
from PIL import ImageTk
import random
import time
import string

import tkinter.simpledialog 
from tkinter.simpledialog import Dialog
#import tkinter.messagebox as ms

import database





with sqlite3.connect("paris_sportifs.db") as db:
	cursur = db.cursor()
cursur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL\
    			,password TEXT NOT NULL, compte INTEGER NOT NULL)")

cursur.execute("SELECT * FROM users")
db.commit()
db.close()


listeEquipe = ["Réal Madrid","FC Barcelona","AS Roma","FC Juventus",\
			   "Atlético Madrid","FC Liverpol","Porto","Ajax",\
			   "FC Arsenal","Villaréal","Man Red","Man City","Chelsea","Naple","PSG","FC Lion","Aston"
			  ]
longu = len(listeEquipe)
listeCote = [1.5,1.4,1.5,1.6,1.2,1.9,1.8,2.1,2.16,2.15,2.5,2.4,2.9,3.5,4.5,5,6.5,8.9,9.0,10.7,10.4,18.6]


		
def genererCode(nb_caratere):
	caracteres = string.ascii_letters + string.digits
	aleatoire = [random.choice(caracteres) for _ in range(nb_caratere)]
	code = ''.join(aleatoire)
	return code 


class Ecran:

	def __init__(self, master):

		self.master = master
		self.name = StringVar()
		self.new_username = StringVar()
		self.new_password = StringVar()
		self.username = StringVar()
		self.password = StringVar()
		self.widgetFonc()


	def log(self):
		self.username.set("")
		self.password.set("")
		self.crf.pack_forget()
		self.head['text'] = "   CONNEXION   "
		self.logf.pack()

	def cr(self):
		self.new_username.set("")
		self.new_password.set("")
		self.head['text'] = "   CREATION DE COMPTE  "
		self.logf.pack_forget()
		self.crf.pack()


	def login(self):
		with sqlite3.connect("paris_sportifs.db") as db:
			cursur = db.cursor()
		find_user = ("SELECT * FROM users WHERE username = ? AND password = ?")
		cursur.execute(find_user, [(self.username.get()), (self.password.get())])
		results = cursur.fetchall()


		if results and self.username.get() != "" and self.password.get() != "":
			self.app()
			for row in results:
				if row[1] == "David":
					ms.showinfo("Administrateur","Vous êtes identifier en tant que administrateur")
		else:
			ms.showerror("oops!!",  "Veillez remplir les champs svp !")


	def new_user(self):
		with sqlite3.connect("paris_sportifs.db") as db:
			cursur = db.cursor()
		find_user = ("SELECT * FROM users WHERE username = ?")
		cursur.execute(find_user, [(self.username.get())])
		if cursur.fetchall():
			ms.showerror("Oooooops!", "username déjà existant dans la base de données")
		else:
			ms.showinfo("success!!", "Votre compte a bien été créer")
			self.log()
		insert = 'INSERT INTO users(id,compte,username, password) VALUES(NULL,"0",?,?)'
		cursur.execute(insert,[(self.new_username.get()), (self.new_password.get())])
		db.commit()


	def widgetFonc(self):
		self.head = Label(self.master, text=" CONNEXION ", fg="blue", font=('freesansbold',35), pady=40)
		self.head.pack()


		self.logf = Frame(self.master, padx=10, pady=10)
		self.logf.config(bg="grey")

		Label(self.logf, text= " Utilisateur :", font=('freesansbold', 20), bg="grey", fg="white", padx=5, pady=15).grid(sticky=W)
		Entry(self.logf, textvariable= self.username, bd=4, font= ('calibri', 18, 'bold'), width=30).grid(row=0, column=1, sticky=E)
		Label(self.logf, text= " Mot de pass :", font=('freesansbold', 20), bg="grey", fg="white", padx=5, pady=15).grid(row=1, column=0, sticky=W)
		Entry(self.logf, textvariable= self.password, bd=4, font= ('calibri', 18, 'bold'), width=30, show="*").grid(row=1, column=1, sticky=E)
		Label(self.logf, text= "", font=('freesansbold', 20), bg="grey", padx=5, pady=5).grid(row=2, column=0, sticky=W)
		Label(self.logf, text= "", font=('freesansbold', 20), bg="grey", padx=2, pady=5).grid(row=2, column=1, sticky=W)		
		Button(self.logf, text=" Se connecter ", bd=4, font=("monaco", 15, 'bold'),padx=5, pady=5, width=22, command=self.login).grid(row=3, column=0)
		Button(self.logf, text=" Nouveau compte ", bd=4, font=("monaco", 15, 'bold'),padx=5, pady=5,width=22, command=self.cr).grid(row=3, column=1)
		self.logf.pack()

		self.crf = Frame(self.master, padx=10, pady=10)
		self.crf.config(bg="grey")

		Label(self.crf, text= " Utulisateur:", font=('freesansbold', 20), bg="grey", fg="white", padx=5, pady=15).grid(sticky=W)
		Entry(self.crf, textvariable= self.new_username, bd=4, font= ('calibri', 18, 'bold'),width=30).grid(row=0, column=1, sticky=E)
		Label(self.crf, text= "Mot de pass:", font=('freesansbold', 20), bg="grey", fg="white", padx=5, pady=15).grid(row=1, column=0, sticky=W)
		Entry(self.crf, textvariable= self.new_password, bd=4, font= ('calibri', 18, 'bold'), width=30, show="*").grid(row=1, column=1, sticky=E)
		Label(self.crf, text= "", font=('freesansbold', 20), bg="grey", padx=5, pady=5).grid(row=2, column=0, sticky=W)
		Label(self.crf, text= "", font=('freesansbold', 20), bg="grey", padx=2, pady=5).grid(row=2, column=1, sticky=W)	
		Button(self.crf, text=" Connexion ", bd=4, font=("monaco", 15, 'bold'),padx=5, pady=5, width=22, command=self.log).grid(row=3, column=0)
		Button(self.crf, text=" créer compte ", bd=4, font=("monaco", 15, 'bold'),padx=5, pady=5, width=22, command=self.new_user).grid(row=3, column=1)
		self.logf.pack()


	def app(self):
		self.Ecran = Toplevel(self.master)
		self.app = FenetreAcceuil(self.Ecran)

class FenetreAcceuil:

	def __init__(self, master):
		self.master = master
		self.master.title("UNI BETA")
		self.master.geometry("900x600+180+0")
		self.master.configure(background='aqua')
		self.frame = Frame(self.master)
		self.frame.pack()

		#============================================
		#============================================
		self.equipe01 = random.randint(0, longu-1)
		self.equipe02 = random.randint(0, longu-1)


		#===========================================
		self.type = StringVar()
		self.mise = StringVar()
		self.equipe1 = StringVar()
		self.equipe2 = StringVar()
		self.date = StringVar()
		self.cote = StringVar()
		self.result = StringVar()
		self.gain = StringVar()
		self.prono = StringVar()
		self.username = StringVar()
		self.username.set(self.username.get())
		self.compte = StringVar()
		self.date = StringVar()
		self.solde = StringVar()

		self.compte.set(0)
		self.date.set(time.strftime("%d/%m/%Y"))

		#=============================================
		#self.cote.set(2.5)

		self.equipe1.set(listeEquipe[self.equipe01])
		self.equipe2.set(listeEquipe[self.equipe02])
		self.cote.set(random.choice(listeCote))

		#==========================Les cadres=======================================
		self.cadreTitre = Frame(self.frame, width=900, height=50, bd=8, relief=RIDGE)
		self.cadreTitre.pack(side=TOP)
		self.cadreTitre.config(bg="green")

		self.cadreDroit = Frame(self.frame, width=600, height=600, bd=8, relief=RIDGE)
		self.cadreDroit.pack(side=RIGHT)
		self.cadreDroit.config(bg="yellow")

		self.cadreGauche = Frame(self.frame, width=300, height=550, bd=8, relief=RIDGE)
		self.cadreGauche.pack(side=LEFT)
		self.cadreGauche.config(bg="orange")

		self.cadreGaucheHaut = Frame(self.cadreGauche, width=300,height=230,bd=4,relief=RIDGE)
		self.cadreGaucheHaut.pack(side=TOP)
		self.cadreGaucheHaut.config(bg="orange")

		self.cadreGaucheBas = Frame(self.cadreGauche, width=300,height=320,bd=4,relief=RIDGE)
		self.cadreGaucheBas.pack(side=BOTTOM)
		self.cadreGaucheBas.config(bg="orange")

		#==================================================================

		self.lblFrame = LabelFrame(self.cadreGaucheHaut, width=300, height=230, text="Informations perso",font=("arial",14,'bold'))
		self.lblFrame.grid(row=0,column=0)

		self.txtParieur = Label(self.lblFrame, font="arial 12 bold", bd=12, text="Parieur :")
		self.txtParieur.grid(row=0,column=0)

		self.txtParieur = Entry(self.lblFrame, font="arial 12 bold",bd=6, width=25, textvariable=self.username)
		self.txtParieur.grid(row=1,column=0)

		self.txtCompte = Label(self.lblFrame, font="arial 12 bold", bd=12, text=" Compte :")
		self.txtCompte.grid(row=2,column=0)

		self.txtCompte = Entry(self.lblFrame, font="arial 12 bold", bd=6, width=25, textvariable=self.compte)
		self.txtCompte.grid(row=3,column=0)

		self.txtDate = Label(self.lblFrame, font="arial 12 bold", bd=12, text="  Date :")
		self.txtDate.grid(row=4,column=0)

		self.txtDate = Entry(self.lblFrame, font="arial 12 bold", bd=6, width=25, textvariable=self.date)
		self.txtDate.grid(row=5,column=0)

		#=========================================================
		self.logo = Canvas(self.cadreGaucheBas, width=300, height=320)
		self.logo.grid(row=0, column=0)
		self.photo = ImageTk.PhotoImage(file="unibet1.png")
		self.logo.create_image(120,120,image = self.photo)

		#============================================================
		self.txtTitre = Label(self.cadreTitre, bg="orange", font=("arial",18,"bold"), text="                       Bienvenu sur votre application de pari sportif                            ")
		self.txtTitre.grid(row=0,column=0)
		#=====================Cadre droit=====================================

		self.lblType = Label(self.cadreDroit, text="Type pari", bg="yellow", pady=6, padx=5, font=('arial',10,'bold'), fg='grey')
		self.lblType.grid(row=0,column=0)

		self.txtType = ttk.Combobox(self.cadreDroit, font=('arial',12,'bold'), width=20, textvariable=self.type)
		self.txtType['value'] = ("","1N2")
		self.txtType.current("0")
		self.txtType.grid(row=0,column=1)

		self.lblMise = Label(self.cadreDroit, text="  Mise  ", bg="yellow", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		self.lblMise.grid(row=0,column=2)

		# self.txtMise = ttk.Combobox(self.cadreDroit, font=('arial',15,'bold'),textvariable=self.mise)
		# self.txtMise['value'] = ("","1N2")
		# self.txtMise.current("0")
		# self.txtMise.grid(row=0,column=3)

		self.txtMise = Entry(self.cadreDroit, font=('arial',12,'bold'), width=20, textvariable=self.mise)
		#self.txtMise.insert(END,"£")
		self.txtMise.grid(row=0,column=3)

		#=======================================================

		self.lblMacth = Label(self.cadreDroit, text="Match du jour", bg="yellow", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		self.lblMacth.grid(row=1,column=0)

		self.txtEquipe1 = Entry(self.cadreDroit, bd=8, font=('arial',12,'bold'), width=20, textvariable=self.equipe1)
		#self.txtEquipe1.insert(END, "vvvvvvvv")
		self.txtEquipe1.grid(row=1,column=1)

		self.lblVs = Label(self.cadreDroit, text="VS", bg="yellow", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		self.lblVs.grid(row=1,column=2)	

		self.txtEquipe2 = Entry(self.cadreDroit, bd=8, font=('arial',12,'bold'), width=20, textvariable=self.equipe2)
		self.txtEquipe2.grid(row=1,column=3)

		#==================================================================

		self.lblPro = Label(self.cadreDroit, text="Equipe", bg="yellow", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		self.lblPro.grid(row=2,column=0)	

		self.txtPro = ttk.Combobox(self.cadreDroit, font=('arial',12,'bold'), width=20, textvariable=self.prono)
		self.txtPro['value'] = (" ",listeEquipe[self.equipe01],listeEquipe[self.equipe02])

		self.txtPro.current("0")
		self.txtPro.grid(row=2,column=1)

		self.lblRes = Label(self.cadreDroit, text="Parier", bg="yellow", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		self.lblRes.grid(row=2,column=2)

		self.txtRes = ttk.Combobox(self.cadreDroit, font=('arial',12,'bold'), width=20, textvariable=self.result)
		self.txtRes['value'] = (" ","Victoire","Défaite","Egalité")
		self.txtRes.current("0")
		self.txtRes.grid(row=2,column=3)

		#======================================================================================

		self.lblCote = Label(self.cadreDroit, text="Cote Proposéé :", bg="yellow", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		self.lblCote.grid(row=3,column=0)

		self.txtCote = Entry(self.cadreDroit, bd=8, font=('arial',12,'bold'), width=20, textvariable=self.cote)
		#self.txtCote.set(2.5)
		self.txtCote.grid(row=3,column=1)

		# self.lblCoteI = Label(self.cadreDroit, text="2.5", pady=6, font=('arial',10,'bold'), padx=5, fg='grey')
		# self.lblCoteI.grid(row=3,column=1)


		self.btnParier = Label(self.cadreDroit,text="", bg="yellow")
		self.btnParier.grid(row=3,column=2)

		self.btnVider = Button(self.cadreDroit,text="Valider mon pari",bg="aqua",command=self.valider)
		self.btnVider.grid(row=3,column=3)

		#=========================================================================
		self.txtVide = Label(self.cadreDroit,text="", bg="yellow")
		self.txtVide.grid(row=4,column=0)

		self.btnParier = Label(self.cadreDroit, fg="black", bg="yellow",text="Username          Mode            Pronostic         Action         Mise(£)       gain(£)")
		self.btnParier.grid(row=5,column=0, columnspan=2)

		self.list1 = Listbox(self.cadreDroit, height = 22, width = 60)
		#list1.insert(END)
		self.list1.grid(row = 6, column =0, rowspan = 6, columnspan = 2)

		#list1.bind('<<ListboxSelect>>',get_selected_row)


		#now we need to attach a scrollbar to the listbox, and the other direction,too
		sb1 = Scrollbar(self.cadreDroit)
		sb1.grid(row = 5, column = 2, rowspan = 6)
		self.list1.config(yscrollcommand = sb1.set)
		sb1.config(command = self.list1.yview)

		self.b1 = Button(self.cadreDroit, text = "Autres Macth", width = 18, command = self.new_match)
		self.b1.grid(row = 6, column = 3)

		self.b2 = Button(self.cadreDroit, text = "Administration", width = 18, command = self.admin)
		self.b2.grid(row = 7, column = 3)

		self.b3 = Button(self.cadreDroit, text = " Resultat Match ", width = 18, command = "")
		self.b3.grid(row = 8, column = 3)

		self.b3 = Button(self.cadreDroit, text = " Ajouter au compte ", width = 18, command = self.ajouter)
		self.b3.grid(row = 9, column = 3)

		self.b3 = Button(self.cadreDroit, text = " Argent cash ", width = 18, command = self.retrait)
		self.b3.grid(row = 10, column = 3)


		self.soldeJoueur = Label(self.cadreDroit, text = "  Mon solde : ", width = 8 )
		self.soldeJoueur.grid(row = 11, column = 2)

		self.soldeJoueur = Entry(self.cadreDroit, cursor="gumby", textvariable=self.solde, width = 12, font=("Arial",16,"bold"))
		self.soldeJoueur.grid(row = 11, column = 3)

		#================================================================
		# now = default_timer() - start
		# minutes, secondes = divmod(now, 60)
		# hours, minutes = divmod(minutes, 60)
		# str_time = "%d:%02d:%02d" % (hours, minutes, secondes)
		# canvas.itemconfigure(text_clock, text=str_time)
		# Fen.after(1000, updateTime)
		# if minutes == 1:
		# 	ms.showinfo("Info","Il est l'heure bro")

		#====================================================================
		# canvas = Canvas(self.cadreDroit, width=4,height=3,bg="white")
		# canvas.grid(row=10,column=2)
		
		# start = default_timer()
		# text_clock = canvas.create_text(90,50)

	def valider(self):
		cpt = 0

		equipe01 = random.randint(0, longu-1)
		equipe02 = random.randint(0, longu-1)
		

		self.cote.set(random.choice(listeCote))

		self.txtPro['value'] = ("",listeEquipe[equipe01],listeEquipe[equipe02],"Nul")

		self.gain = float(self.cote.get()) * int(self.mise.get())
		self.gain = int(self.gain)
		# ms.showinfo('Information',"Veillez patienter quelques second avant le traitement de votre pari")
		rd = time.sleep(5)
		
		self.gain = float(self.cote.get()) * int(self.mise.get())
		self.gain = int(self.gain)
		# gain += gain
		self.compte.set(self.gain) 

		ScoreTeam1 = random.randint(0,6)
		ScoreTeam2 = random.randint(0,6)

		if ScoreTeam1>ScoreTeam2:
			ms.showinfo("Résultat du match séléctionné","{0} a gagné {1} \
					d'un score de {2} à {3}".format(self.txtEquipe1.get(), self.txtEquipe2.get(), ScoreTeam1,ScoreTeam2))
		
		elif ScoreTeam1<ScoreTeam2:
			ms.showinfo("Résultat des match séléctionnés","{0} a gagné {1} \
					d'un score de {2} à {3}".format(self.txtEquipe2.get(), self.txtEquipe1.get(),ScoreTeam2,ScoreTeam1))
		else:
			ms.showinfo("Résultat des match séléctionnés","Un match nul d'un score de {0} à {1}".format(ScoreTeam1,ScoreTeam2))

		database.insertChoix(self.txtEquipe1.get(),self.txtEquipe2.get(),self.txtPro.get(), self.txtRes.get(),self.txtMise.get(),self.gain)

		database.insertResu(self.txtEquipe1.get(), ScoreTeam1, ScoreTeam2, self.txtEquipe2.get())
		self.list1.insert(END, " " + "David" + "             " + self.type.get() + "             " + self.prono.get() + "             " 
						+ self.result.get() + "        " + self.mise.get() + "            " + str(self.gain) + "\n")
		

	def new_match(self):

		equipe01 = random.randint(0, longu-1)
		equipe02 = random.randint(0, longu-1)

		self.equipe1.set(listeEquipe[equipe01])
		self.equipe2.set(listeEquipe[equipe02])

		self.cote.set(random.choice(listeCote))

		self.txtPro['value'] = ("",listeEquipe[equipe01],listeEquipe[equipe02],"Nul")

	def ajouter(self):

		if self.txtPro['value'] == self.txtEquipe1.get():
			if ScoreTeam1 > ScoreTeam2:
				if self.txtRes.get() == "Victoire":
					self.solde.set(self.gain)
				else:
					self.solde.set(0)

			elif ScoreTeam2 > ScoreTeam1:
				if self.txtRes.get() == "Defaite":
					self.solde.set(self.gain)
				else:
					self.solde.set(0)

			elif ScoreTeam2 == ScoreTeam1:
				if self.txtRes.get() == "Egalité":
					self.solde.set(self.gain)
				else:
					self.solde.set(0)
			else:
				self.solde.set(0)

		elif self.txtPro['value'] == self.txtEquipe2.get():
			if ScoreTeam2 > ScoreTeam1:
				if self.txtRes.get() == "Victoire":
					self.solde.set(self.gain)
				else:
					self.solde.set(0)

			elif ScoreTeam1 > ScoreTeam2:
				if self.txtRes.get() == "Defaite":
					self.solde.set(self.gain)
				else:
					self.solde.set(0)

			elif ScoreTeam2 == ScoreTeam1:
				if self.txtRes.get() == "Egalité":
					self.solde.set(self.gain)
				else:
					self.solde.set(0)
		else:
			self.solde.set(0)



	def retrait(self):
		a = ms.askquestion("Argent cash","Voulez-vous vraiment retirer de l'argent ?")
		
		if a=="yes":
			self.appli()			
		else:
			print("Vous avez cliquer sur non")			


	def appli(self):
		self.fen = Toplevel(self.master)
		self.app = GetPassword(self.fen)

	def admin(self):
		self.fenAdmin = Toplevel(self.master)
		self.appAdmin = Administration(self.fenAdmin)

class Administration:
	def __init__(self,master):

		self.master = master
		self.master.title("Panneaux d'Administration de l'application")
		self.master.geometry("900x660+170+10")
		self.master.configure(bg="aqua")

		self.frame = Frame(self.master)
		self.frame.pack()

	#====================Les cadres=======================================

		self.titleFrame = Frame(self.frame, bd=8, width=900, height=18,relief=SUNKEN)
		self.titleFrame.pack(side=TOP)


		self.cadreHaut = Frame(self.frame, width=900, bd=6, height=250, relief="sunken")
		self.cadreHaut.pack(side=TOP)


		self.cadreBas = Frame(self.frame, width=900, bd=6, height=410, relief="sunken")
		self.cadreBas.pack(side=BOTTOM)


	#==============================Les sous cadres===================================


		self.cadreUser = Frame(self.cadreHaut,width=450,height=250, bd=4, relief=SUNKEN)
		self.cadreUser.pack(side=RIGHT)
		self.cadreUser.config(bg="green")

		self.cadreRetrait = Frame(self.cadreHaut,width=450,height=250, bd=4, relief=SUNKEN)
		self.cadreRetrait.pack(side=LEFT)
		self.cadreRetrait.config(bg="green")

		self.cadreResultat = Frame(self.cadreBas,width=450,height=410, bd=4, relief=SUNKEN)
		self.cadreResultat.pack(side=LEFT)
		self.cadreResultat.config(bg="green")

		self.cadreChoixParieur = Frame(self.cadreBas,width=450,height=410, bd=4, relief=SUNKEN)
		self.cadreChoixParieur.pack(side=LEFT)
		self.cadreResultat.config(bg="green")

	#================================Labelframe=========================================
		self.lblframeUser = LabelFrame(self.cadreUser, width=450, height=250,text="Les utilisateurs enregistrés")
		self.lblframeUser.grid(row=0,column=0)
		self.lblframeUser.config(bg="gold")

		self.lblframeRetrait = LabelFrame(self.cadreRetrait, width=450, height=250,text="Les demandes de retrait effectuées")
		self.lblframeRetrait.grid(row=0,column=0)
		self.lblframeRetrait.config(bg="gold")

		self.lblframeResultat = LabelFrame(self.cadreResultat, width=450, height=390,text="Résultat des match éffectués")
		self.lblframeResultat.grid(row=0,column=0)
		self.lblframeResultat.config(bg="gold")

		self.lblframeChoixParieur = LabelFrame(self.cadreChoixParieur, width=450, height=390,text="Les choix éffectués")
		self.lblframeChoixParieur.grid(row=0,column=0)
		self.lblframeChoixParieur.config(bg="gold")

	#==============================Boutton careUser============================================

		self.btn1 = Button(self.lblframeRetrait, bg="aqua", text="Afficher liste", command=self.afficheDemande, font="Arial 10 bold", width=12)
		self.btn1.grid(row=0, column=4)

		self.btn2 = Button(self.lblframeRetrait, bg="aqua", text="Supprimer", font="Arial 10 bold", width=12)
		self.btn2.grid(row=1, column=4)


	#===================================Listebox demandes =======================================

		self.listRetrait = Listbox(self.lblframeRetrait, height = 18, width = 50)
		#list1.insert(END)
		self.listRetrait.grid(row = 0, column =0, rowspan = 1, columnspan = 2)

		#list1.bind('<<ListboxSelect>>',get_selected_row)


		#now we need to attach a scrollbar to the listbox, and the other direction,too
		self.sb1 = Scrollbar(self.lblframeRetrait,bg="yellow")
		self.sb1.grid(row = 0, column = 3, rowspan = 3)
		self.listRetrait.config(yscrollcommand = self.sb1.set)
		self.sb1.config(command = self.listRetrait.yview)

		#===================================================================================
		# self.btn1 = Button(self.lblframeRetrait, text="Afficher liste", font="Arial 10 bold", width=15)
		# self.btn1.grid(row=0, column=4)

		# self.btn2 = Button(self.lblframeRetrait, text="Supprimer", font="Arial 10 bold", width=15)
		# self.btn2.grid(row=1, column=4)

		#===============================Liste box user===================================================

		self.listUser = Listbox(self.lblframeUser, height = 18, width = 45, font="Arial 8")
		#list1.insert(END)
		self.listUser.grid(row = 0, column =0, rowspan = 1, columnspan = 2)

		#list1.bind('<<ListboxSelect>>',get_selected_row)

		self.scrollBar = Scrollbar(self.lblframeUser)
		self.scrollBar.grid(row = 0, column = 3, rowspan = 3)
		self.listUser.config(yscrollcommand = self.scrollBar.set)
		self.scrollBar.config(command = self.listUser.yview)

		#==============================================================================

		self.btnUser1 = Button(self.lblframeUser, bg="aqua", command= self.afficheUser, text="Afficher liste", font="Arial 10 bold", width=12)
		self.btnUser1.grid(row=0, column=4)

		self.btnUser2 = Button(self.lblframeUser, bg="aqua", text="Supprimer", font="Arial 10 bold", width=12)
		self.btnUser2.grid(row=1, column=4)


		#=================================Liste box des macth efféctués==================================================

		self.listMatch = Listbox(self.lblframeResultat, height = 12, width = 50)
		#list1.insert(END)
		self.listMatch.grid(row = 0, column =0, rowspan = 1, columnspan = 2)

		#list1.bind('<<ListboxSelect>>',get_selected_row)

		self.scrollBarMatch = Scrollbar(self.lblframeResultat)
		self.scrollBarMatch.grid(row = 0, column = 2, rowspan = 3)
		self.listMatch.config(yscrollcommand = self.scrollBarMatch.set)
		self.scrollBarMatch.config(command = self.listMatch.yview)

		#==============================================================================

		self.btnMatch1 = Button(self.lblframeResultat, bg="aqua", command=self.afficheMatch, text="Afficher liste", font="Arial 10 bold", width=15)
		self.btnMatch1.grid(row=1, column=0)

		self.btnMatch2 = Button(self.lblframeResultat, bg="aqua", text="Supprimer", font="Arial 10 bold", width=15)
		self.btnMatch2.grid(row=1, column=1)

		#===================================Liste box des choix effectué============================

		self.listMatchChoisi = Listbox(self.lblframeChoixParieur, height = 12, width = 80)
		#list1.insert(END)
		self.listMatchChoisi.grid(row = 0, column =0, rowspan = 1, columnspan = 2)

		#list1.bind('<<ListboxSelect>>',get_selected_row)

		self.scrollBarMatchChoisi = Scrollbar(self.lblframeChoixParieur)
		self.scrollBarMatchChoisi.grid(row = 0, column = 2, rowspan = 3)
		self.listMatchChoisi.config(yscrollcommand = self.scrollBarMatchChoisi.set)
		self.scrollBarMatchChoisi.config(command = self.listMatchChoisi.yview)

		#==============================================================================

		self.btnMatch1 = Button(self.lblframeChoixParieur, bg="aqua", text="Afficher liste", font="Arial 10 bold", width=12, command=self.afficheMatchChoisi)
		self.btnMatch1.grid(row=1, column=0)

		self.btnMatch2 = Button(self.lblframeChoixParieur, bg="aqua", text="Supprimer", font="Arial 10 bold", width=12)
		self.btnMatch2.grid(row=1, column=1)



	#=======================================================================================

		self.titleAdmin = Label(self.titleFrame, text="\t\t\t PANNEAUX D'ADMINISTRATION DES UTILISATEURS ET DES PARI EFFECTUES\t\t\t\t\t",
						font=("Arial 10 bold"), bg="aqua")
		self.titleAdmin.grid(row=0, columnspan=4)

	def afficheUser(self):
		self.listUser.delete(0, END)
		for row in database.viewUser():
			nomUser = row[0]
			compteUser = row[1]

			self.listUser.insert(END, "   "+ nomUser.upper() +"                  "+ str(compteUser) +"£", str(""))

	def afficheMatch(self):
		self.listMatch.delete(0, END)
		for row in database.viewMatch():
			equipe1 = row[0]
			score1 = row[1]
			score2 = row[2]
			equipe2 = row[3]

			self.listMatch.insert(END, "  "+ equipe1 +"               "+ score1 +"  :   "+ score2 +"              "+ equipe2, str(""))

	def afficheDemande(self):
		self.listRetrait.delete(0, END)
		for row in database.viewDemande():
			nomUser = row[0]
			mont = row[1]
			code = row[2]

			self.listRetrait.insert(END, "    "+nomUser.upper() +"            "+mont+"        "+code, str(""))

	def afficheMatchChoisi(self):
		self.listMatchChoisi.delete(0, END)
		for row in database.viewChoixPari():
			equipe1 = row[0]
			equipe2 = row[1]
			choix = row[2]
			pari = row[3]
			mise = row[4]
			gain = row[5]

			self.listMatchChoisi.insert(END, "  "+ equipe1 +"    vs    " + equipe2 +"         "+ choix +"      "+ pari +"       "+ str(mise) +"     "+ str(gain), str(""))


class GetPassword(Dialog):

	def __init__(self, master):

		self.master = master
		self.master.title("Retrait d'argent")
		self.master.geometry("500x240+290+230")
		self.master.configure(bg='white')
		self.frame = ttk.Frame(self.master)
		self.frame.pack()

		#============Les variables=============================


		self.passw = StringVar()
		self.userN = StringVar()
		self.mont = StringVar()

		self.lbl = Label(self.frame, text="    *Pour des raisons de securité, veillez vous identifier à tavers ce formulaire svp!     ",
					bg='red',pady=8, font="Arial 9 bold")
		self.lbl.grid(row=0, columnspan=2)

		self.lblframe = LabelFrame(self.frame, text="Vos Information pour confirmer la demande", font=("Helvetica",12,'bold'),
						width=498, height=238)
		self.lblframe.grid(row=1,column=0)



		self.user = Label(self.lblframe, text=" Nom ", pady=15, font="Arial 10 bold")
		self.user.grid(row=0,column=0)

		self.userEn = Entry(self.lblframe, textvariable=self.userN, bd=8, width=30)
		self.userEn.grid(row=0,column=1)


		self.passlbl = Label(self.lblframe, text=" Password ", pady=15, font="Arial 10 bold")
		self.passlbl.grid(row=1,column=0)

		self.passEnt = Entry(self.lblframe, textvariable=self.passw, width=30, bd=8)
		self.passEnt.grid(row=1,column=1)

		self.montant = Label(self.lblframe, text=" Montant ", pady=15, font="Arial 10 bold")
		self.montant.grid(row=2,column=0)

		self.montEnt = Entry(self.lblframe, textvariable=self.mont, width=30, bd=8)
		self.montEnt.grid(row=2,column=1)
		self.mont.set("0£")

		self.btnEn = Button(self.lblframe, text="Envoyer", width=15, padx=15, command=self.apply)
		self.btnEn.grid(row=0,column=2)

		self.btnQuit = Button(self.lblframe, text="Quitter", width=15, padx=15, command=self.quitter)
		self.btnQuit.grid(row=1,column=2)

		self.btnQuit = Button(self.lblframe, text="Effacer", width=15, padx=15, command=self.effacer)
		self.btnQuit.grid(row=2,column=2)

	
	def effacer(self):
		self.userN.set("")
		self.passw.set("")
		self.mont.set("")


	def apply(self):

		nom = self.userEn.get()
		passw = self.passEnt.get()
		compt = self.montEnt.get()
		code = genererCode(5)

		if nom !="" and passw != "":
			if compt != "0£":
				database.insertDemande(nom,compt,code)
				self.textMs1 = Label(self.lblframe, text="")
				self.textMs1.grid(row=4, column=0, columnspan=2)

				self.textMs2 = Label(self.lblframe, text="")
				self.textMs2.grid(row=4, column=0, columnspan=2)

				self.textConfirm = Label(self.lblframe, text="Demande effectuée avec success Mr {} code du retrait: {}".format(nom,code), fg="white", bg="green")
				self.textConfirm.grid(row=4, column=0, columnspan=2)

			else:
				self.textConfirm = Label(self.lblframe, text="")
				self.textConfirm.grid(row=4, column=0, columnspan=2)

				self.textMs2 = Label(self.lblframe, text="")
				self.textMs2.grid(row=4, column=0, columnspan=2)
				self.textMs1 = Label(self.lblframe, text="Le montant ne doit pas être 0£", fg="white", bg="green")
				self.textMs1.grid(row=4, column=0, columnspan=2)
		else:
			self.textConfirm = Label(self.lblframe, text="")
			self.textConfirm.grid(row=4, column=0, columnspan=2)

			self.textMs1 = Label(self.lblframe, text="")
			self.textMs1.grid(row=4, column=0, columnspan=2)

			self.textMs2 = Label(self.lblframe, text="Le nom et le mot de passe doivent être indiqués", fg="white", bg="green")
			self.textMs2.grid(row=4, column=0, columnspan=2)
	

	def quitter(self):
		self.quit = ms.askyesno("Retrait","Voulez-vous fermer cette fenêtre ?")
		if self.quit >0:
			self.master.destroy()
			return



if __name__=='__main__':
	root = Tk()
	root.title("Mon application de pari sportif")
	#root.config(bg="tomato3")
	Ecran(root)
	root.geometry("700x450+350+150")
	root.mainloop()
	

