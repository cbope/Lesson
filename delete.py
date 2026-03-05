import os
# os.remove("delete.me")

file_to_be_deleted = "delete.me"
folder_to_be_deleted = "deleteme"

# if os.path.exists(file_to_be_deleted):
#     os.remove(file_to_be_deleted)
# else: print("The file does not exist")

# if os.path.exists(folder_to_be_deleted):
#     os.rmdir(folder_to_be_deleted)
# else: print("The folder does not exist")

def clean_up():
    if os.path.exists(file_to_be_deleted):
        os.remove(file_to_be_deleted)
    if os.path.exists(folder_to_be_deleted):
        os.rmdir(folder_to_be_deleted)

clean_up()

