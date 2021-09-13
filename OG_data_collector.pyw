import tkinter as tk
import main

def send_args_to_main():
    Type = str(Entry_OG_Type.get())
    Volume = str(Entry_OG_Volume.get())
    Weight = str(Entry_OG_Weight.get())
    Store = str(Entry_OG_Store.get())
    Entry_OG_Type.delete( '0', tk.END )
    Entry_OG_Volume.delete( '0', tk.END )
    Entry_OG_Weight.delete( '0', tk.END )
    Entry_OG_Store.delete( '0', tk.END )
    main.OG_Autofill(StringOGType=Type, StringVolume=Volume, stringWeight=Weight, StringTrip=Store)

OG_data_collector = tk.Tk()
OG_data_collector.title("Параметры автозаполнения")
OG_data_collector.geometry('420x120+700+300')
Frame = tk.Frame(master=OG_data_collector)

Label_OG_Type = tk.Label(master=OG_data_collector, text="Что едет?: ")
Entry_OG_Type = tk.Entry(master=OG_data_collector, width=20)
Label_OG_Type_description = tk.Label(master=OG_data_collector, text="    (Например: AS IS, EXTW, KOROBA)", fg="grey")

Label_OG_Volume = tk.Label(master=OG_data_collector, text="Объём: ")
Entry_OG_Volume = tk.Entry(master=OG_data_collector, width=20)
Label_OG_Volume_description = tk.Label(master=OG_data_collector, text="    в метрах кубических", fg="grey")

Label_OG_Weight = tk.Label(master=OG_data_collector, text="Вес: ")
Entry_OG_Weight = tk.Entry(master=OG_data_collector, width=20)
Label_OG_Weight_description = tk.Label(master=OG_data_collector, text="    в килограммах", fg="grey")

Label_OG_Store = tk.Label(master=OG_data_collector, text="Стор: ")
Entry_OG_Store = tk.Entry(master=OG_data_collector, width=20)
Label_OG_Store_description = tk.Label(master=OG_data_collector, text="    Например: 480", fg="grey")

Button_Fill = tk.Button(master=OG_data_collector, text="Заполнить OG в CNS", width=20, command=send_args_to_main)



Label_OG_Type.grid(row=0, column=0, sticky='w')
Entry_OG_Type.grid(row=0, column=1)
Label_OG_Type_description.grid(row=0, column=2, sticky='w')

Label_OG_Volume.grid(row=1, column=0, sticky='w')
Entry_OG_Volume.grid(row=1, column=1)
Label_OG_Volume_description.grid(row=1, column=2, sticky='w')

Label_OG_Weight.grid(row=2, column=0, sticky='w')
Entry_OG_Weight.grid(row=2, column=1)
Label_OG_Weight_description.grid(row=2, column=2, sticky='w')

Label_OG_Store.grid(row=3, column=0, sticky='w')
Entry_OG_Store.grid(row=3, column=1)
Label_OG_Store_description.grid(row=3, column=2, sticky='w')

Button_Fill.grid(row=4, column=1)

Frame.grid()

OG_data_collector.mainloop()