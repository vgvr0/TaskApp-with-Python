import tkinter as tk
from tkinter import messagebox, colorchooser

class Task:
    def __init__(self, title, color):
        self.title = title
        self.completed = False
        self.color = color

class TaskApp:
    def __init__(self):
        self.tasks = []

        self.ventana = tk.Tk()
        self.ventana.title("Task App")

        self.frame_superior = tk.Frame(self.ventana)
        self.frame_superior.pack()

        self.entry_titulo = tk.Entry(self.frame_superior, width=30)
        self.entry_titulo.pack(side=tk.LEFT)

        self.boton_color = tk.Button(self.frame_superior, text="Color", command=self.elegir_color)
        self.boton_color.pack(side=tk.LEFT)

        self.boton_agregar = tk.Button(self.ventana, text="Agregar tarea", command=self.agregar_tarea)
        self.boton_agregar.pack()

        self.listbox_tareas = tk.Listbox(self.ventana, width=50)
        self.listbox_tareas.pack()

        self.boton_marcar = tk.Button(self.ventana, text="Marcar completado", command=self.marcar_completado)
        self.boton_marcar.pack()

        self.actualizar_listbox_tareas()

        self.ventana.mainloop()

    def agregar_tarea(self):
        titulo = self.entry_titulo.get()
        color = self.boton_color["bg"]

        if titulo:
            tarea = Task(titulo, color)
            self.tasks.append(tarea)
            self.actualizar_listbox_tareas()
            self.entry_titulo.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese un título para la tarea.")

    def marcar_completado(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            tarea = self.tasks[seleccion[0]]
            tarea.completed = not tarea.completed
            self.actualizar_listbox_tareas()

    def elegir_color(self):
        color = colorchooser.askcolor()[1]
        self.boton_color.config(bg=color)

    def actualizar_listbox_tareas(self):
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tasks:
            color = tarea.color
            completado = "✓" if tarea.completed else " "
            self.listbox_tareas.insert(tk.END, f"[{completado}] {tarea.title}", tarea.title)
            self.listbox_tareas.itemconfig(tk.END, bg=color)

task_app = TaskApp()
