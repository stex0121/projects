import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
folders = {
    'Images': os.path.join(desktop_folder, "Images"),
    'PDFs': os.path.join(desktop_folder, "PDFs"),
    'Excel Files': os.path.join(desktop_folder, "Excel Files"),
    'Music': os.path.join(desktop_folder, "Music"),
    'Videos': os.path.join(desktop_folder, "Videos")
}


for folder in folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)


file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'PDFs': ['.pdf'],
    'Excel Files': ['.xls', '.xlsx'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv']
}

def get_category(file_extension):
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:
            return category
    return None

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_name, file_extension = os.path.splitext(event.src_path)
            category = get_category(file_extension)
            if category:
                destination_folder = folders.get(category)
                if destination_folder:
                    shutil.move(event.src_path, os.path.join(destination_folder, os.path.basename(event.src_path)))
                    print(f"Moved {event.src_path} to {destination_folder}")

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=downloads_folder, recursive=False)
    observer.start()
    print(f"Monitoring {downloads_folder} for new files...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()