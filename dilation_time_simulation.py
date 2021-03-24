from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['toolbar'] = "None"

from matplotlib.widgets import Slider, RadioButtons
from math import *
import scipy.constants as const

lorentz = 1
dict = {}

class SnaptoCursor(object):
	def __init__(self, ax):
	
		self.ax = ax
		self.ly = ax.axvline(color='k', ymax=0.825, ymin=0.335)
		[radio_2.labels[i].set_x(-0.32) for i in range(len(radio_2.labels))]
		self.txt_3 = ax.text(0.1,0.58,'',transform = ax.transAxes, fontsize = 12)

			
	def mouse_move(self, event):
	
		if not event.inaxes:
			return
		x = event.xdata
		self.ly.set_xdata(x)
			
		try:		
			self.txt_1.remove()		
			self.txt_2.remove()		
		except:
			pass
			

		
		if radio_2.value_selected == 'Seconde' : 
			scale = 1
			
			if x/9 - 0.2 > 0.75 : self.txt_1 = ax.text(0.75, 0.845, '', transform = ax.transAxes, fontsize = 12)
			elif x/9 - 0.2 > -0.15 : self.txt_1 = ax.text(x/9 - 0.2, 0.845, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_1 = ax.text(-0.15, 0.845, '', transform = ax.transAxes, fontsize = 12)
			
			if x/9 - 0.276 > 0.67 : self.txt_2 = ax.text(0.67, 0.297, '', transform = ax.transAxes, fontsize = 12)			
			elif x/9 - 0.276 > -0.15 : self.txt_2 = ax.text(x/9 - 0.275, 0.297, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_2 = ax.text(-0.15, 0.297, '', transform = ax.transAxes, fontsize = 12)	
					
		elif radio_2.value_selected == 'Minute' : 
			scale = 60
			
			if x/9 - 0.2 > 0.67 : self.txt_1 = ax.text(0.67, 0.845, '', transform = ax.transAxes, fontsize = 12)
			elif x/9 - 0.2 > -0.15 : self.txt_1 = ax.text(x/9 - 0.2, 0.845, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_1 = ax.text(-0.15, 0.845, '', transform = ax.transAxes, fontsize = 12)
			
			if x/9 - 0.276 > 0.596 : self.txt_2 = ax.text(0.596, 0.297, '', transform = ax.transAxes, fontsize = 12)			
			elif x/9 - 0.276 > -0.15 : self.txt_2 = ax.text(x/9 - 0.276, 0.297, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_2 = ax.text(-0.15, 0.297, '', transform = ax.transAxes, fontsize = 12)	
							
		elif radio_2.value_selected == 'Heure' :
			scale = 60*60
			
			if x/9 - 0.2 > 0.598 : self.txt_1 = ax.text(0.598, 0.845, '', transform = ax.transAxes, fontsize = 12)
			elif x/9 - 0.2 > -0.15 : self.txt_1 = ax.text(x/9 - 0.2, 0.845, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_1 = ax.text(-0.15, 0.845, '', transform = ax.transAxes, fontsize = 12)
			
			if x/9 - 0.276 > 0.531 : self.txt_2 = ax.text(0.531, 0.297, '', transform = ax.transAxes, fontsize = 12)			
			elif x/9 - 0.276 > -0.15 : self.txt_2 = ax.text(x/9 - 0.276, 0.297, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_2 =  ax.text(-0.15, 0.297, '', transform = ax.transAxes, fontsize = 12)
			
		elif radio_2.value_selected == 'Jour' : 
			scale = 60*60*24
			
			if x/9 - 0.2 > 0.53 : self.txt_1 = ax.text(0.53, 0.845, '', transform = ax.transAxes, fontsize = 12)
			elif x/9 - 0.2 > -0.15 : self.txt_1 = ax.text(x/9 - 0.2, 0.845, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_1 = ax.text(-0.15, 0.845, '', transform = ax.transAxes, fontsize = 12)
			
			if x/9 - 0.276 > 0.451 : self.txt_2 = ax.text(0.451, 0.297, '', transform = ax.transAxes, fontsize = 12)			
			elif x/9 - 0.276 > -0.15 : self.txt_2 = ax.text(x/9 - 0.276, 0.297, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_2 = ax.text(-0.15, 0.297, '', transform = ax.transAxes, fontsize = 12)
			
		else : 
			scale = 60*60*24*365
			
			if x/9 - 0.2 > 0.45 : self.txt_1 = ax.text(0.45, 0.845, '', transform = ax.transAxes, fontsize = 12)
			elif x/9 - 0.2 > -0.15 : self.txt_1 = ax.text(x/9 - 0.2, 0.845, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_1 = ax.text(-0.15, 0.845, '', transform = ax.transAxes, fontsize = 12)
			
			if x/9 - 0.276 > 0.378 : self.txt_2 = ax.text(0.378, 0.297, '', transform = ax.transAxes, fontsize = 12)			
			elif x/9 - 0.276 > -0.15 : self.txt_2 = ax.text(x/9 - 0.276, 0.297, '', transform = ax.transAxes, fontsize = 12)
			else : self.txt_2 = ax.text(-0.15, 0.297, '', transform = ax.transAxes, fontsize = 12)
		
		
		if x < 10 : 
			self.txt_1.set_text('Temps vécue par le Terrien : %s ' % affichage_temps(x*scale))	
			self.txt_2.set_text('Pour le Terrien, le Voyageur a vielli de : %s ' % affichage_temps(scale*x/lorentz))
			self.txt_3.set_text('Pour le Terrien, il y a donc une différence de : %s' % affichage_temps(x*scale-scale*x/lorentz))

		fig.canvas.draw_idle()	
		plt.draw()
		
def choix_vitesse(label):
	vitesse = ''
	for lettre in label:	
		if not lettre == 'm' : vitesse+=lettre
		else : break
	
	v.set_val(int(vitesse.replace(" ","")))
	update(int(vitesse.replace(" ","")))
	
def affichage_temps(chaine):
	global lorentz
	
	minute,seconde = divmod(chaine,60)
	heure,minute = divmod(minute,60)
	jour,heure = divmod(heure,24)
	annee,jour = divmod(jour,365)
				
	sequence = ''
	
	if annee > 0 and annee < 2 : sequence += '%d année ' % annee
	elif annee : sequence += '%d années ' % annee
	if jour > 0 and jour < 2 : sequence += '%d jour ' % jour
	elif jour: sequence += '%d jours ' % jour
	if heure > 0 and heure < 2 : sequence += '%d heure ' % heure
	elif heure : sequence += '%d heures ' % heure
	if minute > 0 and minute < 2 : sequence += '%d minute ' % minute
	elif minute : sequence += '%d minutes ' % minute
	if seconde >= 0 and seconde < 2 : sequence += '%1.9f seconde' % seconde
	else : sequence += '%1.9f secondes' % seconde

	return sequence
		
def ecriture(chaine):
	chaine = str(chaine)
	counter = 0
	percent = 0
	apres_point = ''
	nombre = ''
	avant_point = ''
	dot = False
	
	for separateur in chaine:
		if dot : apres_point += separateur
		else : avant_point += separateur
		if separateur == '.' and not dot : dot = True
		
	if dot : avant_point = avant_point[:len(avant_point)-1]
	
	for i in range (3 - int(len(apres_point))) : apres_point += '0'	
		
	for chiffre in reversed(avant_point):
		if counter % 3 == 0 : nombre += ' '		
		counter += 1
		nombre += chiffre
		
	percent = (int(avant_point) / const.c)*100
	nombre = nombre[::-1] + '.' + apres_point[:3] + ' m/s\n%.9f' % percent + ' % de c' 
	
	return nombre 

def circle_color():

	if v.val == 1 : radio_1.value_selected = '1m/s : Marche'
	if v.val > 11082 : radio_1.activecolor = 'white'
	else : radio_1.activecolor = 'red'
		
	for i,p in enumerate(radio_1.circles):
		if radio_1.value_selected == dict[i] : color = radio_1.activecolor
		else : color = radio_1.ax.get_facecolor()
		p.set_facecolor(color)		
	
def update(val):
	global note
	global lorentz
	global test
	
	circle_color()
	
	lorentz = 1 / (sqrt(1 - ((v.val**2)/(int(const.c)**2))))
	l.set_xdata(np.arange(0,387170,1*lorentz))
	l.set_ydata(np.array([1.25]*len(np.arange(0,387170,1*lorentz))))
	v.valtext.set_text(ecriture(v.val))
	for i, a in enumerate(note):
		a.remove()
	note[:] = []
	note = [ax.annotate(i,xy=(i*lorentz,1.13),xytext=(-3,5), textcoords='offset points') for i in range(10)]
	fig.canvas.draw_idle()	

fig = plt.figure('Simulation de la dilatation du temps en fonction de la vitesse')
ax = plt.subplot()

axis_x_1 = np.arange(0,387170,1)
axis_x_2 = np.arange(0,20,1)
axis_y_1 = np.array([1.25]*len(axis_x_1))
axis_y_2 = np.array([2.25]*len(axis_x_2))

l, = plt.plot(axis_x_1, axis_y_1, '|-k')
plt.plot(axis_x_2, axis_y_2,'|-')

ax.set_ylim(0,3)
ax.set_xlim(0,9) 
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.tick_params(size = 0)
[ax.spines[i].set_visible(False) for i in ('right','left','top','bottom')]
[ax.annotate(i,xy=(i,2.25),xytext=(-3,5), textcoords='offset points') for i in range(10)]
note = [ax.annotate(i,xy=(i,1.13),xytext=(-3,5), textcoords='offset points') for i in range(10)]
	
box_1 = plt.axes([0.2,0.1,0.6,0.05], facecolor = 'lightgoldenrodyellow')
v = Slider(box_1, 'Vitesse', 1, int(const.c) - 0.001, valinit=1, valstep=0.001, valfmt='%.3f', color = 'black')
if v.val : 	v.valtext.set_text(ecriture(v.val))
v.on_changed(update)

box_2 = plt.axes([0.007,0.1,0.1,0.9],frameon=False,aspect='equal')
radio_1 = RadioButtons(box_2,("1m/s : Marche","10m/s : Usain Bolt","30m/s : Voiture","250m/s : Avion","300m/s : Mur du son","3 000m/s : Fusée","11 082m/s : Apollo 10" ),activecolor='red')
for i in range(7) : dict[i] = radio_1.labels[i].get_text()
radio_1.on_clicked(choix_vitesse)	

box_3 = plt.axes([0.96,0.1,0.1,0.9],frameon=False,aspect='equal')
radio_2 = RadioButtons(box_3,("Seconde","Minute","Heure","Jour","Année"),activecolor='red')

cursor = SnaptoCursor(ax)
plt.connect('motion_notify_event', cursor.mouse_move)
plt.show()