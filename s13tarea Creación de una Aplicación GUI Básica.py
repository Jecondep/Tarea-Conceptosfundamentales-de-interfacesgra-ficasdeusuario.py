import tkinter as tk

class AplicaciónGUI:
    def __init__(self, master):
        self.master = master
        master.title("Aplicación GUI Básica")

        # Crear componentes GUI
        self.etiqueta = tk.Label(master, text="Ingrese sus datos:")
        self.etiqueta.pack()

        self.campo_texto = tk.Entry(master, width=30)
        self.campo_texto.pack()

        self.boton_agregar = tk.Button(master, text="Agregar", command=self.agregar_datos)
        self.boton_agregar.pack()

        self.boton_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar_datos)
        self.boton_limpiar.pack()

        self.lista_datos = tk.Listbox(master, width=30)
        self.lista_datos.pack()

    def agregar_datos(self):
        datos = self.campo_texto.get()
        if datos:
            self.lista_datos.insert(tk.END, datos)
            self.campo_texto.delete(0, tk.END)

    def limpiar_datos(self):
        self.lista_datos.delete(0, tk.END)
        self.campo_texto.delete(0, tk.END)

root = tk.Tk()
mi_gui = AplicaciónGUI(root)
root.mainloop()
