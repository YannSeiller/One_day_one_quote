## Give a daily quote , quote inspire by reading 

import pandas as pd
import numpy as np
from tkinter import *


class Quotes():

	def printQuote(self):
		Quotes = pd.read_csv('Citastr.csv', sep=',')
		N = len(Quotes.index)
		i = np.random.randint(0,N)
		citastr = Quotes.iloc[i,0]
		auteur = Quotes.iloc[i,1]
		return citastr, auteur

def callback():
	Quotes = pd.read_csv('Citastr.csv', sep=',')
	citation = str(entree_citation.get())
	auteur = str(entree_auteur.get())
	df = pd.DataFrame([[citation,auteur]],columns=['Citation','Auteur'])
	Quotes = Quotes.append(df,ignore_index=True)
	#Quotes.to_csv('Citastr.csv',sep=',')
	entree_citation.delete(0,END)
	entree_auteur.delete(0,END)
	

wdinput = Tk()
value = StringVar() 
value.set("texte par défaut")
label1 = Label(wdinput, text = "Citation")
label1.pack()
entree_citation = Entry(wdinput, textvariable=str, width=30)
entree_citation.pack()
label2 = Label(wdinput, text = "Auteur")
label2.pack()
entree_auteur = Entry(wdinput, textvariable=str, width=30)
entree_auteur.pack()
bouton=Button(wdinput, text="Ajouter", command=callback)
bouton.pack()
bouton=Button(wdinput, text="Fermer", command=wdinput.quit)
bouton.pack()
 

"""
fenetre = Tk()
Quote = Quotes()
citation,auteur = Quote.printQuote()
label1 = Label(fenetre, text = citation)
label2 = Label(fenetre,text = auteur)
label1.pack()
label2.pack()
""" 

wdinput.mainloop()
