import tkinter as tk
def click(touch):
    if touch == "=":
        try:
            result = str(eval(enter.get()))
            enter.delete(0, tk.END)
            enter.insert(tk.END, result)
        except:
            enter.delete(0, tk.END)
            enter.insert(tk.END, "Error")
    elif touch == "C":
        enter.delete(0, tk.END)
    else:
        enter.insert(tk.END, touch)
        
fenetre = tk.Tk()
fenetre.title("Calculator")
fenetre.configure(bg="#f0f0f0")


enter = tk.Entry(fenetre, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
enter.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

boutons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for bouton in boutons:
    action = lambda x=bouton: click(x)
    tk.Button(fenetre, text=bouton, width=5, height=2, font=("Arial", 16),
              command=action, bg="#ffffff", fg="#000000").grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
tk.Button(fenetre, text="C", width=21, height=2, font=("Arial", 16),
          command=lambda: click("C"), bg="#ffcccc").grid(row=row, column=0, columnspan=4, padx=5, pady=10)
fenetre.mainloop()