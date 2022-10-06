import tkinter as tk
from tkinter import messagebox

### Création de fonctions

def fQuit():
    return app.destroy()

def show_error_window():
    messagebox.showerror("ERREUR", "Veuillez sélectionner des dimmensions non nulles")

def toContinue():
    if(var_entryX.get() == 0 or var_entryY.get() == 0 or var_scaleX.get() == 0 or var_scaleY.get() == 0):
       return show_error_window()
    else :
        next_window = tk.Toplevel(app)
        next_window.title("Autre fenetre")
        next_window.geometry("560x480")
        next_window.resizable(False, False)

### Fenetre principale - choix des dimensions

#----------------------------------------------------------------------------------------------------

app = tk.Tk()
app.title("Détection de fissures")
app.geometry("560x480")
app.resizable(False, False)


### Création des variables

var_entryX = tk.IntVar()
var_entryY = tk.IntVar()
var_scaleX = tk.IntVar()
var_scaleY = tk.IntVar()


#----------------------------------------------------------------------------------------------------

frame = tk.LabelFrame(app, text="Taille du mur à scanner(cm)")
scale_x = tk.Scale(frame, from_ = 0, to = 1000, tickinterval = 500, orient="horizontal", length = 200, variable = var_scaleX)
scale_y = tk.Scale(frame, from_ = 0, to = 1000, tickinterval = 500, orient="vertical", length = 200, variable = var_scaleY)

frame2 = tk.LabelFrame(app, text="Taile des images(cm)")
entryX = tk.Entry(frame2, textvariable = var_entryX)
entryY = tk.Entry(frame2, textvariable = var_entryY)
labelX = tk.Label(frame2, text ="X(cm)")
labelY = tk.Label(frame2, text ="Y(cm)")

quit_button = tk.Button(app, text = "Quit", command = fQuit)
continue_button = tk.Button(app, text = "Continue", command = toContinue)


frame.pack(fill = "x")
scale_x.pack()
scale_y.pack(side = "left")


frame2.pack(fill = "x")
entryX.pack()
entryY.pack()
labelX.place(x = 350, y = 0)
labelY.place(x = 350, y = 17)

quit_button.place(x = 10, y = 440)
continue_button.place(x = 480, y = 440)
app.mainloop()