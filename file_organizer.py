import os
import shutil

# File type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Find the category
        category = None
        for key, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                category = key
                break
        if not category:
            category = "Others"

        # Create category folder if not exists
        category_folder = os.path.join(directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Move file
        new_path = os.path.join(category_folder, filename)
        shutil.move(file_path, new_path)

    print("✅ Files have been organized successfully!")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to organize: ").strip()
    organize_files(folder_path)
