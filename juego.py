from tkinter import *
import random
import math

enemigos = []
puntuacion = int(0)
def mover(e):
    global puntuacion
    if e.keysym == 'Up':
        if player.winfo_y() >= 0:
            player.place(x=player.winfo_x(), y=player.winfo_y()-10)
    elif e.keysym == 'Down':
        if player.winfo_y() <= 500:
            player.place(x=player.winfo_x(), y=player.winfo_y()+10)
    elif e.keysym == 'Left':
        if player.winfo_x() >= 0:
            player.place(x=player.winfo_x()-10, y=player.winfo_y())
    elif e.keysym == 'Right':
        if player.winfo_x() <= 500:
            player.place(x=player.winfo_x()+10, y=player.winfo_y())

def generarComida():
    food.place_forget()
    foodX = random.randint(0, 50)
    foodY = random.randint(0, 50)
    food.place(x=foodX*10, y=foodY*10)
    generarEnemigo()

def generarEnemigo():
    enemyX = random.randint(0, 50)
    enemyY = random.randint(0, 50)
    new_enemy = Label(app, text='👾', fg="#ae00ff", font=(30), bg="#000000")
    new_enemy.place(x=enemyX * 10, y=enemyY * 10)
    enemigos.append(new_enemy)

def moverEnemigo(enemy):
    jugador_x = player.winfo_x()
    jugador_y = player.winfo_y()
    enemigo_x = enemy.winfo_x()
    enemigo_y = enemy.winfo_y()

    dx = jugador_x - enemigo_x
    dy = jugador_y - enemigo_y
    distancia = math.sqrt(dx**2 + dy**2)

    if distancia > 0:
        dx /= distancia
        dy /= distancia

        enemy.place(x=enemigo_x + dx * 2, y=enemigo_y + dy * 2)

def verificarComidaYJugador():
    global puntuacion
    if player.winfo_x() == food.winfo_x() and player.winfo_y() == food.winfo_y():
        puntuacion += 1
        labelResultado.config(text=f"Puntuacion: {puntuacion}")
        generarComida()

    for enemy in enemigos:
        if abs(player.winfo_x() - enemy.winfo_x()) < 10 and abs(player.winfo_y() - enemy.winfo_y()) < 10:
            app.quit()

    app.after(100, verificarComidaYJugador)

app = Tk()

labelResultado = Label(app, text='Puntuación: ' + str(puntuacion))
labelResultado.place(x=0, y=500)
player = Label(app, text='🧑‍💼', fg="blue", font=(30), bg="#000000")
player.place(x=0, y=0)

food = Label(app, text='🍎', fg="red", font=(30), bg="#000000")
generarComida()

enemigos = []
generarEnemigo()

app.geometry('564x564')
app.config(bg='#000000')

app.bind('<Key>', mover)

verificarComidaYJugador()

def moverEnemigosCiclo():
    for enemy in enemigos:
        moverEnemigo(enemy)
    app.after(100, moverEnemigosCiclo)

moverEnemigosCiclo()

app.mainloop()
