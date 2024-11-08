import tkinter as tk
from tkinter import messagebox
import numpy as np

def solve_gauss():
    try:
        if num_vars.get() == 2:
            coefficients = np.array([
                [float(a11_entry.get()), float(a12_entry.get())],
                [float(a21_entry.get()), float(a22_entry.get())]
            ])
            results = np.array([float(b1_entry.get()), float(b2_entry.get())])
        elif num_vars.get() == 3:
            coefficients = np.array([
                [float(a11_entry.get()), float(a12_entry.get()), float(a13_entry.get())],
                [float(a21_entry.get()), float(a22_entry.get()), float(a23_entry.get())],
                [float(a31_entry.get()), float(a32_entry.get()), float(a33_entry.get())]
            ])
            results = np.array([float(b1_entry.get()), float(b2_entry.get()), float(b3_entry.get())])
        elif num_vars.get() == 4:
            coefficients = np.array([
                [float(a11_entry.get()), float(a12_entry.get()), float(a13_entry.get()), float(a14_entry.get())],
                [float(a21_entry.get()), float(a22_entry.get()), float(a23_entry.get()), float(a24_entry.get())],
                [float(a31_entry.get()), float(a32_entry.get()), float(a33_entry.get()), float(a34_entry.get())],
                [float(a41_entry.get()), float(a42_entry.get()), float(a43_entry.get()), float(a44_entry.get())]
            ])
            results = np.array([float(b1_entry.get()), float(b2_entry.get()), float(b3_entry.get()), float(b4_entry.get())])

        solution = np.linalg.solve(coefficients, results)
        show_solution(solution, "Gaussian Elimination")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def solve_gauss_jordan():
    try:
        if num_vars.get() == 2:
            coefficients = np.array([
                [float(a11_entry.get()), float(a12_entry.get())],
                [float(a21_entry.get()), float(a22_entry.get())]
            ])
            results = np.array([float(b1_entry.get()), float(b2_entry.get())])
        elif num_vars.get() == 3:
            coefficients = np.array([
                [float(a11_entry.get()), float(a12_entry.get()), float(a13_entry.get())],
                [float(a21_entry.get()), float(a22_entry.get()), float(a23_entry.get())],
                [float(a31_entry.get()), float(a32_entry.get()), float(a33_entry.get())]
            ])
            results = np.array([float(b1_entry.get()), float(b2_entry.get()), float(b3_entry.get())])
        elif num_vars.get() == 4:
            coefficients = np.array([
                [float(a11_entry.get()), float(a12_entry.get()), float(a13_entry.get()), float(a14_entry.get())],
                [float(a21_entry.get()), float(a22_entry.get()), float(a23_entry.get()), float(a24_entry.get())],
                [float(a31_entry.get()), float(a32_entry.get()), float(a33_entry.get()), float(a34_entry.get())],
                [float(a41_entry.get()), float(a42_entry.get()), float(a43_entry.get()), float(a44_entry.get())]
            ])
            results = np.array([float(b1_entry.get()), float(b2_entry.get()), float(b3_entry.get()), float(b4_entry.get())])

        augmented_matrix = np.column_stack((coefficients, results))
        row_reduced_form = np.linalg.inv(coefficients).dot(results)
        show_solution(row_reduced_form, "Gauss-Jordan Elimination")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_solution(solution, method):
    solution_str = f"{method} Solution:\n" + "\n".join([f"x{i+1} = {value:.2f}" for i, value in enumerate(solution)])
    solution_label.config(text=solution_str)

def setup_entries(num):
    for widget in frame1.winfo_children():
        widget.destroy()

    title_label = tk.Label(frame1, text="Enhanced Equation Solver", font=("Helvetica", 18, "bold"))
    title_label.grid(row=0, columnspan=num*2, pady=20)

    for i in range(num):
        for j in range(num):
            tk.Label(frame1, text=f"a{i+1}{j+1}", font=("Helvetica", 14)).grid(row=i+1, column=2*j)
            globals()[f'a{i+1}{j+1}_entry'] = tk.Entry(frame1, width=8, font=("Helvetica", 14))
            globals()[f'a{i+1}{j+1}_entry'].grid(row=i+1, column=2*j+1, padx=10, pady=10)

    for i in range(num):
        tk.Label(frame1, text=f"b{i+1}", font=("Helvetica", 14)).grid(row=num+1, column=2*i)
        globals()[f'b{i+1}_entry'] = tk.Entry(frame1, width=8, font=("Helvetica", 14))
        globals()[f'b{i+1}_entry'].grid(row=num+1, column=2*i+1, padx=10, pady=10)

    solve_gauss_btn = tk.Button(frame1, text="Solve with Gauss", command=solve_gauss, bg="lightblue", font=("Helvetica", 14, "bold"))
    solve_gauss_btn.grid(row=num+2, column=0, columnspan=num, pady=20, sticky="ew")

    solve_gauss_jordan_btn = tk.Button(frame1, text="Solve with Gauss-Jordan", command=solve_gauss_jordan, bg="lightgreen", font=("Helvetica", 14, "bold"))
    solve_gauss_jordan_btn.grid(row=num+2, column=num, columnspan=num, pady=20, sticky="ew")

    back_btn = tk.Button(frame1, text="Back", command=show_initial_screen, bg="red", font=("Helvetica", 14, "bold"), fg="white")
    back_btn.grid(row=num+3, column=0, columnspan=num*2, pady=10, sticky="ew")

    global solution_label
    solution_label = tk.Label(frame1, text="", font=("Helvetica", 16))
    solution_label.grid(row=num+4, columnspan=num*2, pady=20)

def show_initial_screen():
    for widget in frame1.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(frame1, text="مرحبا بكم في برنامج حل المعادلات المحسّن!", font=("Helvetica", 18, "bold"), fg="blue")
    welcome_label.grid(row=0, columnspan=6, pady=20)

    instructions_label = tk.Label(frame1, text="يرجى اختيار عدد المتغيرات لنظام المعادلات الخاص بك:", font=("Helvetica", 14))
    instructions_label.grid(row=1, columnspan=6, pady=10)

    button_frame = tk.Frame(frame1)
    button_frame.grid(row=2, columnspan=6, pady=20)

    tk.Button(button_frame, text="2 متغيرات", font=("Helvetica", 14), command=lambda: [num_vars.set(2), setup_entries(2)]).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(button_frame, text="3 متغيرات", font=("Helvetica", 14), command=lambda: [num_vars.set(3), setup_entries(3)]).grid(row=0, column=1, padx=20, pady=10)
    tk.Button(button_frame, text="4 متغيرات", font=("Helvetica", 14), command=lambda: [num_vars.set(4), setup_entries(4)]).grid(row=0, column=2, padx=20, pady=10)

# Create the main window
root = tk.Tk()
root.title("Enhanced Equation Solver")
root.geometry("800x600")  # Set the window size

num_vars = tk.IntVar()

frame1 = tk.Frame(root, padx=20, pady=20)
frame1.pack(fill=tk.BOTH, expand=True)

show_initial_screen()

root.mainloop()

