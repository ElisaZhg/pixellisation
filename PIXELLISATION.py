##Importation des modules##
from tkinter import Tk, Scale, IntVar, Menu, Canvas
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
#from tkinter.filedialog import asksaveasfile

#2 images simultanées? et image avant/après
#lorsque aucune image, montrer un tableau blanc écrit charger une image



def pixel(img, img2):
    #valeurs de largeur et longueur
     #longueur
    width = img.size[0] #largeur
    height= img.size[1]
    # initialisation d'une nouvelle image
    pixels = img2.load()
    
    # taille de la case pixelisée dépendant de la valeur choisie par l'utilisateur
    pixel_size = select() 
    #création Gros Pixel par Gros Pixel l'Image Pixelisée
    for i in range(0, img.size[0], pixel_size):
        for j in range(0, img.size[1], pixel_size): # For every row
            # On calcule la moyenne de tous les pixels du Gros Pixel
            r=0 # moyenne du rouge
            g=0 # moyenne du vert
            b=0 # moyenne du bleu
            n=0 # compteur de pixel par case
        
            # On vérifie que xmax et ymax ne sortent pas de l'image
            #pour que sur les bords, les gros pixels ne sortent pas de l'image sinon erreur out of range?
            xmax= i+pixel_size
            ymax= j+pixel_size
            if i+pixel_size> width:
                xmax= width
            if j+pixel_size> height:
                ymax= height
           
            # On parcours chaque pixels de la Case à pixeliser
            for x in range(i, xmax):
                for y in range(j, ymax):
                    n+=1
                    pixel= img.getpixel((x,y))
                    r+= pixel[0]
                    g+= pixel[1]
                    b+= pixel[2]
       
            # On fait la moyenne des couleurs des pixels de la Case à pixeliser
            r= int(r*1.0/n)
            g= int(g*1.0/n)
            b= int(b*1.0/n)
       
            # On crée la case pixelisé avec les couleurs moyennes
            for x in range(i, xmax): #entre i et i+pixel_size
                for y in range(j, ymax): #entre j et pixel_size
                   pixels[x, y]= (r, g, b) 

#global image_name
image_name="inconnu"

def name(name): #Sinon erreur fichier parcours
    indice=0
    for i in range(len(name)):
        if name[i]=="/":
            indice=i+1
    return name[indice:]

def openfile():
    global image_name
    image_name= name(filedialog.askopenfilename())
    
#def SaveFile():
   
def select():
    return value.get()

def valider():
    if image_name != "inconnu":
        img= Image.open(image_name)
        width = img.size[0] #largeur
        height= img.size[1]
        img2= Image.new('RGB', (width,height), color= 'white')
        pixel(img, img2)
        img2.show()#CANVAS

    else:
        print ("ERREUR. Aucun fichier")

root = Tk() # Création de la fenêtre racine
root.title("Pixellisation") #nom de la fenetre
value = IntVar(root) 

"""
def canvas_change():
    global img
    photo = ImageTk.PhotoImage(img)
    zone_image = Canvas(root) # crée un canevas de dimensions ajustées à celles de l'image
    zone_image.create_image(0,0, anchor = "se", image= ) # association image/widget
    zone_image.pack() # placement du widget
"""

#Barre d'outils
menubar= Menu(root)
root.config(menu= menubar)
menufichier= Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)

menufichier.add_command(label="Ouvrir", command = openfile) #Bouton ouvrir l'image
menufichier.add_separator() #ligne séparatrice
#menufichier.add_command(label="Enregistrer", command = SaveFile) #Bouton enregistrement

#Bouton variable SCALE
scale = Scale(root, variable= value,from_= 3, to= 60,
              orient= 'horizontal', len=200)
scale.pack()

#Bouton validation de scale
bouton_valider = ttk.Button(root, text="Valider", command = valider)  # <------
bouton_valider.pack()
    
# Lancement de la boucle principale
root.mainloop() 