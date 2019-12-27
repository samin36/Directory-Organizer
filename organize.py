import os
from shutil import move

file_to_dir = {
    '.jpg'  :   './Images',
    '.png'  :   './Images',
    '.gif'  :   './Images',
    '.ico'  :   './Images',
    '.doc'  :   './Documents/Word',
    '.docx' :   './Documents/Word',
    '.ppt'  :   './Documents/PowerPoint',
    '.pptx' :   './Documents/PowerPoint',
    '.pdf'  :   './Documents/PDF',
    '.txt'  :   './Documents/Text',
    '.zip'  :   './Documents/Zip',
    '.exe'  :   './Applications'
}

file_names = [file_name for file_name in os.listdir('.') if os.path.isfile(file_name)]
for current_file in file_names:
    file_name, file_extension = os.path.splitext(current_file)
    
    destination_dir = file_to_dir.get(file_extension, -1)
    if destination_dir != -1:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        move(current_file, destination_dir)

