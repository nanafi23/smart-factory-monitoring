
import tkinter as tk
from tkinter import ttk, messagebox
import random
from database import Database

from monitoring import get_status, health_score

def generate():
    temp = random.randint(50, 110)
    vib = random.randint(10, 100)

    status = get_status(temp, vib)
    score = health_score(temp, vib)

    db.insert_reading(temp, vib, status, score)

    lbl_temp.config(text=f"Temperature: {temp} °C")
    lbl_vib.config(text=f"Vibration: {vib}")
    lbl_status.config(text=f"Status: {status}")
    lbl_score.config(text=f"Health Score: {score}%")

    colors = {"NORMAL":"green","WARNING":"orange","CRITICAL":"red"}
    lbl_status.config(fg=colors[status])

def show_history():
    win = tk.Toplevel(root)
    win.title("History")
    win.geometry("700x300")

    tree = ttk.Treeview(
        win,
        columns=("ID","Temp","Vibration","Status","Score"),
        show="headings"
    )

    for c in ("ID","Temp","Vibration","Status","Score"):
        tree.heading(c, text=c)
        tree.column(c, width=120)

    tree.pack(fill="both", expand=True)

    for row in db.fetch_all():
        tree.insert("", tk.END, values=row)

def about():
    messagebox.showinfo(
        "Project Info",
        "Smart Industrial Machine Monitoring System\nPython + SQLite + Tkinter"
    )

def main():
    global root, db, lbl_temp, lbl_vib, lbl_status, lbl_score
    db = Database()
    root = tk.Tk()
    root.title("Smart Industrial Machine Monitoring System")
    root.geometry("650x500")
    
    title = tk.Label(root,text="SMART FACTORY DASHBOARD",
                     font=("Arial",22,"bold"))
    title.pack(pady=15)
    
    frame = tk.LabelFrame(root,text="Machine Information")
    frame.pack(fill="x", padx=20, pady=10)
    
    tk.Label(frame,text="Machine ID: M001").pack(anchor="w")
    tk.Label(frame,text="Location: Production Line A").pack(anchor="w")
    tk.Label(frame,text="Machine Type: CNC Machine").pack(anchor="w")
    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    
    tk.Button(btn_frame,text="Generate Reading",
              command=generate,width=20).grid(row=0,column=0,padx=5)
    
    tk.Button(btn_frame,text="View History",
              command=show_history,width=20).grid(row=0,column=1,padx=5)
    
    tk.Button(btn_frame,text="About",
              command=about,width=20).grid(row=0,column=2,padx=5)
    
    lbl_temp = tk.Label(root,text="Temperature: -",font=("Arial",14))
    lbl_temp.pack(pady=5)
    
    lbl_vib = tk.Label(root,text="Vibration: -",font=("Arial",14))
    lbl_vib.pack(pady=5)
    
    lbl_status = tk.Label(root,text="Status: -",font=("Arial",14,"bold"))
    lbl_status.pack(pady=5)
    
    lbl_score = tk.Label(root,text="Health Score: -",font=("Arial",14))
    lbl_score.pack(pady=5)
    
    root.mainloop()
    db.close()


if __name__ == "__main__":
    main()
