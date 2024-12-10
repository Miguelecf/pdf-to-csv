import os
import PyPDF2
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_text_from_pdf(pdf_file_path):
    text_data = []
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            text_data.append({'Archivo': os.path.basename(pdf_file_path), 'Página': page_num + 1, 'Contenido': text})
    return text_data

def process_pdfs_to_csv(input_folder, output_csv):
    all_text_data = []

    # Iterar sobre todos los archivos PDF en la carpeta
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            text_data = extract_text_from_pdf(pdf_path)
            all_text_data.extend(text_data)

    # Convertir los datos a un DataFrame
    df = pd.DataFrame(all_text_data)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(output_csv, index=False, encoding='utf-8')

def select_folder():
    folder_selected = filedialog.askdirectory(title="Seleccionar Carpeta con PDFs")
    if folder_selected:
        output_csv = filedialog.asksaveasfilename(
            title="Guardar archivo CSV",
            defaultextension=".csv",
            filetypes=[("Archivo CSV", "*.csv")]
        )
        if output_csv:
            try:
                process_pdfs_to_csv(folder_selected, output_csv)
                messagebox.showinfo("Éxito", f"Datos guardados en {output_csv}")
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema: {str(e)}")
        else:
            messagebox.showwarning("Cancelado", "No seleccionaste un archivo para guardar el CSV.")
    else:
        messagebox.showwarning("Cancelado", "No seleccionaste una carpeta.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Extract PDF to CSV")
root.geometry("400x200")

# Etiqueta y botón
label = tk.Label(root, text="Selecciona una carpeta con PDFs para procesar:", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Seleccionar Carpeta", command=select_folder, font=("Arial", 12))
button.pack(pady=10)

# Iniciar la aplicación
root.mainloop()