import tkinter as tk
from tkinter import messagebox
import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    augmented_matrix = np.column_stack((A, b)) 
    steps = []  

    for i in range(n):
        max_row = np.argmax(np.abs(augmented_matrix[i:n, i])) + i
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]  
        steps.append(f"الخطوة {i+1}: تبديل الصف {max_row+1} مع الصف {i+1} لتقليل الخطأ العددي")

        for j in range(i+1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]
            steps.append(f"الخطوة {i+1}.{j+1}: حذف المتغير x{i+1} من الصف {j+1}")
            steps.append(f"المصفوفة بعد العملية:\n{augmented_matrix}")

    solution = np.zeros(n)
    for i in range(n-1, -1, -1):
        solution[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, :-1], solution)) / augmented_matrix[i, i]
        steps.append(f"التعويض العكسي للمتغير x{i+1}: x{i+1} = {solution[i]:.2f}")

    return solution, steps

def gauss_jordan_elimination(A, b):
    n = len(A)
    augmented_matrix = np.column_stack((A, b))  
    steps = [] 

    for i in range(n):
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        steps.append(f"الخطوة {i+1}: تطبيع الصف {i+1} بحيث يصبح العنصر المحوري 1")
        steps.append(f"المصفوفة بعد التطبيع:\n{augmented_matrix}")
        
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]  # حذف باقي العناصر في العمود
                steps.append(f"الخطوة {i+1}.{j+1}: حذف المتغير x{i+1} من الصف {j+1}")
                steps.append(f"المصفوفة بعد العملية:\n{augmented_matrix}")
    
    solution = augmented_matrix[:, -1]
    for i in range(n):
        steps.append(f"الحل للمتغير x{i+1}: {solution[i]:.2f}")

    return solution, steps

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

        solution, steps = gaussian_elimination(coefficients, results)
        show_solution(solution, "Gaussian Elimination", steps)
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

        solution, steps = gauss_jordan_elimination(coefficients, results)
        show_solution(solution, "Gauss-Jordan Elimination", steps)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_solution(solution, method, steps):
    result_window = tk.Toplevel(root)
    result_window.title(f"Results of {method}")
    result_window.geometry("600x600")

    canvas = tk.Canvas(result_window, bg="#f7f7f7")
    scrollbar = tk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
    steps_frame = tk.Frame(canvas, bg="#f7f7f7")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=steps_frame, anchor="nw")
    
    title_label = tk.Label(steps_frame, text=f"Results of {method}", font=("Helvetica", 16, "bold"), bg="#f7f7f7")
    title_label.grid(row=0, columnspan=2, pady=10)

    row = 1
    for step in steps:
        step_label = tk.Label(steps_frame, text=step, font=("Helvetica", 12), anchor="w", justify="left", bg="#f7f7f7")
        step_label.grid(row=row, column=0, sticky="w", pady=2)
        row += 1

    result_label = tk.Label(steps_frame, text="Final Results:\n", font=("Helvetica", 14, "bold"), bg="#f7f7f7")
    result_label.grid(row=row, columnspan=2, pady=5)
    row += 1

    for i, value in enumerate(solution):
        result_text = f"x{i+1} = {value:.2f}"
        result_label = tk.Label(steps_frame, text=result_text, font=("Helvetica", 12), bg="#f7f7f7")
        result_label.grid(row=row, column=0, sticky="w", pady=2)
        row += 1

    steps_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    close_btn = tk.Button(result_window, text="Close", command=result_window.destroy, bg="#d9534f", font=("Helvetica", 14, "bold"), fg="white")
    close_btn.pack(pady=20)

def setup_entries(num):
    for widget in frame1.winfo_children():
        widget.destroy()

    title_label = tk.Label(frame1, text="Enhanced Equation Solver", font=("Helvetica", 18, "bold"), fg="#008CBA")
    title_label.grid(row=0, columnspan=num*2, pady=20)

    for i in range(num):
        for j in range(num):
            tk.Label(frame1, text=f"a{i+1}{j+1}", font=("Helvetica", 14)).grid(row=i+1, column=2*j, padx=10, pady=10)
            globals()[f'a{i+1}{j+1}_entry'] = tk.Entry(frame1, width=8, font=("Helvetica", 14))
            globals()[f'a{i+1}{j+1}_entry'].grid(row=i+1, column=2*j+1, padx=10, pady=10)

    for i in range(num):
        tk.Label(frame1, text=f"b{i+1}", font=("Helvetica", 14)).grid(row=num+1, column=2*i, padx=10, pady=10)
        globals()[f'b{i+1}_entry'] = tk.Entry(frame1, width=8, font=("Helvetica", 14))
        globals()[f'b{i+1}_entry'].grid(row=num+1, column=2*i+1, padx=10, pady=10)

    solve_gauss_btn = tk.Button(frame1, text="Solve using Gaussian Elimination", command=solve_gauss, bg="#5bc0de", font=("Helvetica", 14, "bold"))
    solve_gauss_btn.grid(row=num+2, column=0, columnspan=num, pady=20, sticky="ew")

    solve_gauss_jordan_btn = tk.Button(frame1, text="Solve using Gauss-Jordan Elimination", command=solve_gauss_jordan, bg="#5cb85c", font=("Helvetica", 14, "bold"))
    solve_gauss_jordan_btn.grid(row=num+2, column=num, columnspan=num, pady=20, sticky="ew")

    back_btn = tk.Button(frame1, text="Back", command=show_initial_screen, bg="#d9534f", font=("Helvetica", 14, "bold"), fg="white")
    back_btn.grid(row=num+3, column=0, columnspan=num*2, pady=10, sticky="ew")

def show_initial_screen():
    for widget in frame1.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(frame1, text="Welcome to the Enhanced Equation Solver!", font=("Helvetica", 18, "bold"), fg="#008CBA")
    welcome_label.grid(row=0, columnspan=6, pady=20)

    instructions_label = tk.Label(frame1, text="Please select the number of variables for your system of equations:", font=("Helvetica", 14))
    instructions_label.grid(row=1, columnspan=6, pady=10)

    button_frame = tk.Frame(frame1)
    button_frame.grid(row=2, columnspan=6, pady=20)

    tk.Button(button_frame, text="2 Variables", font=("Helvetica", 14), command=lambda: [num_vars.set(2), setup_entries(2)]).grid(row=0, column=0, padx=20, pady=10)
    tk.Button(button_frame, text="3 Variables", font=("Helvetica", 14), command=lambda: [num_vars.set(3), setup_entries(3)]).grid(row=0, column=1, padx=20, pady=10)
    tk.Button(button_frame, text="4 Variables", font=("Helvetica", 14), command=lambda: [num_vars.set(4), setup_entries(4)]).grid(row=0, column=2, padx=20, pady=10)

root = tk.Tk()
root.title("Enhanced Equation Solver")
root.geometry("800x600")

num_vars = tk.IntVar()

frame1 = tk.Frame(root, padx=20, pady=20)
frame1.pack(fill=tk.BOTH, expand=True)

show_initial_screen()

root.mainloop()

