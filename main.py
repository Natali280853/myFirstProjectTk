import tkinter as tk
def add_task():
    task = task_entry.get()
    if task:
        task_ListBox1.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def del_task():
    sel_task = task_ListBox1.curselection()
    if sel_task:
        task_ListBox1.delete(sel_task)

def move_selected_items():
    selected_indices = task_ListBox1.curselection()
    selected_items = [task_ListBox1.get(i) for i in selected_indices]
    for item in selected_items:
        task_ListBox2.insert(tk.END, item)
        task_ListBox1.delete(task_ListBox1.get(0, tk.END).index(item))
    color_list_items()

def color_list_items():
    for index in range(task_ListBox2.size()):
        item = task_ListBox2.get(index)
        if item:
          task_ListBox2.itemconfig(index, bg="SeaGreen", fg="white")


root = tk.Tk()
root.wm_title("Список задач")
root.iconbitmap(default="VIEW1.ico")
root.geometry("300x650+400+200")

root.configure(background="grey84")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

text1 = tk.Label(frame, text="Введите задачу:")
text1.pack(pady=5)

task_entry = tk.Entry(frame, width=30, bg="gray92")
task_entry.pack(pady=10)  #padx - влево/вправо

add_task_button = tk.Button(frame, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)
del_task_button = tk.Button(frame, text="Удалить задачу", command=del_task)
del_task_button.pack(pady=5)
mark_task_button = tk.Button(frame, text="Отметить задачу", command=move_selected_items)
mark_task_button.pack(pady=5)

text2 = tk.Label(frame, text="Актуальные задачи:")
text2.pack(pady=5)

task_ListBox1 = tk.Listbox(frame, selectmode='multiple', width=40, height=10)
task_ListBox1.pack(padx=10, pady=10)

text3 = tk.Label(frame, text="Выполненные задачи:")
text3.pack(pady=10)

task_ListBox2 = tk.Listbox(frame, width=40, height=10, bg="ghost white")
task_ListBox2.pack(padx=10, pady=10)

root.mainloop()
