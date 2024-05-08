#Problem 4.5 (!!!Klar)
import os
import datetime

non_convention_name = []
config_file = False
backup_file = False

input_directory = input("Enter a path to a directory: ")
content_of_directory = os.listdir(input_directory)
print()

#Gets the date of all the files and creates an absolute path. 
for file in content_of_directory:
    full_file_path = os.path.join(input_directory, file)
    time = os.path.getctime(full_file_path)
    date = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d")

    if file == "config.xml":
        config_file = True
    
    if file == f"backup-config-{date}.xml":
        backup_file = True
    elif file != "config.xml" and file != f"backup-config-{date}.xml":
        non_convention_name.append(file)
        config_file = False
        backup_file = False

if config_file == True and backup_file == True:
    print(f"""'{input_directory}' only contains files with the this naming scheme: 
config.xml
backup-config-YYYY-MM-DD.xml""")
elif config_file == False and backup_file == False:
    print(f"""'{input_directory}' containts files that don't follow the naming shceme.
Names of these files are: """)
    for file_names in non_convention_name:
        print(file_names)