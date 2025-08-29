# file_organizer.py
import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self, directory_path):
        self.directory = Path(directory_path)
        self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
            'videos': ['.mp4', '.mov', '.avi', '.mkv'],
            'audio': ['.mp3', '.wav', '.flac'],
            'archives': ['.zip', '.rar', '.7z'],
            'code': ['.py', '.js', '.html', '.css', '.java']
        }
    
    def organize_files(self):
        if not self.directory.exists():
            print("Directory does not exist!")
            return
        
        for file_path in self.directory.iterdir():
            if file_path.is_file():
                self.move_file_to_category(file_path)
        
        print("File organization completed! ✅")
    
    def move_file_to_category(self, file_path):
        file_extension = file_path.suffix.lower()
        category = 'others'
        
        for cat, extensions in self.file_types.items():
            if file_extension in extensions:
                category = cat
                break
        
        category_folder = self.directory / category
        category_folder.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(file_path), str(category_folder / file_path.name))
        except Exception as e:
            print(f"Error moving {file_path.name}: {e}")

def main():
    target_directory = input("Enter directory path to organize: ")
    organizer = FileOrganizer(target_directory)
    organizer.organize_files()

if __name__ == "__main__":
    main()