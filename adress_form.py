from future.moves import tkinter as tk

window = tk.Tk()
fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Адрес', 'Описание']
frm_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frm_frame.pack()
for item in fields:
    label = tk.Label(master=frm_frame, text=item)
    entry = tk.Entry(master=frm_frame, width=50)
    label.grid(row=fields.index(item), column= 0,sticky='e')
    entry.grid(row=fields.index(item), column=1,)
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
btn_submit = tk.Button(master=frm_buttons, text='Отправить')
btn_submit.pack(side=tk.RIGHT,pady=5,padx=5)
btn_clear = tk.Button(master=frm_buttons, text='Очистить')
btn_clear.pack(side=tk.RIGHT,pady=5,padx=5)

window.mainloop()


