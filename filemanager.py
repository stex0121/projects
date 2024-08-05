import os
import shutil

def move_directories_to_folder(base_path, target_folder):
    # Ensure target folder exists
    target_path = os.path.join(base_path, target_folder)
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # Iterate through all items in the base directory
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)

        # Check if the item is a directory
        if os.path.isdir(item_path) and item != target_folder:
            try:
                # Move the directory to the target folder
                shutil.move(item_path, target_path)
                print(f"Moved directory {item} to {target_folder}")
            except PermissionError as e:
                print(f"PermissionError: {e} - Could not move directory {item}")
            except Exception as e:
                print(f"Error: {e} - Could not move directory {item}")

def main():
    base_path = input("Enter Path: ")
    target_folder = input("Enter Target Folder for Directories: ")

    if not os.path.isdir(base_path):
        print(f"The path {base_path} is not a valid directory.")
        return

    # Move directories into the specified folder
    move_directories_to_folder(base_path, target_folder)

    # Handle files (as in the previous version)
    files = os.listdir(base_path)

    for file in files:
        source = os.path.join(base_path, file)

        if os.path.isfile(source):
            try:
                filename, extension = os.path.splitext(file)
                extension = extension[1:]  # Remove the dot from the extension

                if extension == "":  # Skip files without an extension
                    print(f"Skipping file without an extension: {file}")
                    continue

                destination_dir = os.path.join(base_path, extension)

                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                destination = os.path.join(destination_dir, file)
                shutil.move(source, destination)
                print(f"Moved file {file} to {destination_dir}")

            except PermissionError as e:
                print(f"PermissionError: {e} - Could not move file {file}")
            except Exception as e:
                print(f"Error: {e} - Could not process file {file}")
        else:
            print(f"Skipping directory: {file}")

if __name__ == "__main__":
    main()