import tkinter as tk
import main
window = tk.Tk()
window.geometry("200x200")

btnFillOG = tk.Button(window, text="Заполнить OG", command=main.OG_Autofill)

btnFillOG.pack(expand=1)




window.mainloop()