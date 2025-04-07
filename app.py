import os,shutil
path = input( "Enter path: ").strip().replace("\\", "/")
if not path.endswith("/"):
    path += "/"
file_name = os.listdir(path)
print(file_name)
folder_name = ["jpg_files", "jpeg_files", "png_files", "pdf_files", "docx_files", "txt_files","mp4_files","mp3_files","py_files", "js_files", "html_files", "css_files","xls_files", "xlsx_files", "csv_files"]
for loop in range (0,len(folder_name)):
     if not os.path.exists(path + "/"+ folder_name [loop]): 
         os.makedirs (path + "/"+ folder_name[loop])

# LOGIC --- ORGANIZING THE FILES 
for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf_files/" + file):
        shutil.move(path + file , path + "pdf_files/" + file)
    if ".txt" in file and not os.path.exists(path + "txt_files/" + file):
        shutil.move(path + file , path + "txt_files/" + file)
    if ".docx" in file and not os.path.exists(path + "docx_files/" + file):
        shutil.move(path + file , path + "docx_files/" + file)
    if ".jpg"  in file and not os.path.exists(path + "jpg_files/" + file):
        shutil.move(path + file , path + "jpg_files/" + file)
    if ".jpeg" in file and not os.path.exists(path + "files.jpeg/" + file):
        shutil.move(path + file , path + "files.docx/" + file)
    if ".png" in file and not os.path.exists(path + "png_files/" + file):
        shutil.move(path + file , path + "png_files/" + file)
    if ".mp4"  in file and not os.path.exists(path + "mp4_files/" + file):
        shutil.move(path + file , path + "mp4_files/" + file)
    if ".mp3" in file and not os.path.exists(path + "mp3_files/" + file):
        shutil.move(path + file , path + "mp3_files/" + file)
    if ".html" in file and not os.path.exists(path + "html_files/" + file):
        shutil.move(path + file , path + "html_files/" + file)
    if ".css" in file and not os.path.exists(path + "css_files/" + file):
        shutil.move(path + file , path + "css_files/" + file)
    if ".js" in file and not os.path.exists(path + "js_files/" + file):
        shutil.move(path + file , path + "js_files/" + file)
    if ".py" in file and not os.path.exists(path + "py_files/" + file):
        shutil.move(path + file , path + "py_files/" + file)
    if ".xls" in file and not os.path.exists(path + "xls_files/" + file):
        shutil.move(path + file , path + "xls_files/" + file)
    if ".xlsx" in file and not os.path.exists(path + "xlsx_files/" + file):
        shutil.move(path + file , path + "xlsx_files/" + file)
    if ".csv" in file and not os.path.exists(path + "csv_files/" + file):
        shutil.move(path + file , path + "csv_files/" + file)




        




