import re
import tkinter as tk

def analizar(entrada):
    identificador = []

    for token in ["for", "do"]:
        matches = re.findall(rf"\b{token}\b", entrada)

        for match in matches:
            identificador.append(f"<Reservada\t{token}\tSimbolo\t{token}")
            entrada = entrada.replace(match, " ", 1)
    
    matches = re.findall(r"[()]", entrada)

    for match in matches:
        identificador.append(f"<Parentesis en cierre {match}>")
        entrada = entrada.replace(match, " ", 1)
    
    entrada = entrada.strip()

    if len(entrada) > 0:
        identificador.append("<No definido>\t{}".format(entrada))
        
    return identificador
    
def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    entrada = codigo.split("\n")
    token_totales = []

    for i, linea in enumerate(entrada):
        tokens_linea = analizar(linea)

        for token in tokens_linea:
            token_totales.append((i+1, token))

    resultado_texto.delete("1.0", tk.END) 

    for numero_linea, token in token_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n{token}\n")

    numero_reservadas = len([token for numero_linea, token in token_totales if token.startswith("<Reservada")])
    resultado_texto.insert(tk.END, f"\nPalabra reservada: {numero_reservadas}")

ventana = tk.Tk()
ventana.geometry("540x650")
ventana.title("Analizador Léxico")
ventana.config(bg="white")

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=40, y=50)
entrada_texto.configure(insertbackground="black")

resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
resultado_texto.place(x=40, y=320)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#121b29", fg="white", command=analizar_codigo)
boton_analizar.place(x=150, y=580)

boton_borrar = tk.Button(ventana, text="Borrar", font=("Arial", 12), bg="#121b29", fg="white", command=lambda: entrada_texto.delete("1.0", tk.END))
boton_borrar.place(x=280, y=580)

ventana.mainloop()
