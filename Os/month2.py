# import os 
# import shutil

# #Create a new directory
# if not os.path.isdir("Test_directory"):
#     os.mkdir("test_directory")

# #Change the current working directory to the new directory
# os.chdir("test_directory")
# print("Current working directory: ", os.getcwd())

# #Create a text file in the directory
# with open("example.txt", "w") as file:
#     file.write("This is a text file.")

# #list files in the current directory
# print("Files in the directory:", os.listdir())

# #Copy the file
# shutil.copy("example.txt", "copy_example.txt")

# #Move the copied filke to a new location(renaming it in the process)
# shutil.move("copy_example.txt", "../moved_example.txt")

# #Go back to the parent directory
# os.chdir("..")
# #remove the test directory and its contents
# shutil.rmtree("test_directory")
# os.remove("moved_example.txt")#remove the moved file
# print("cleanup completed!")

# import subprocess
# import os
# # result=subprocess.run(["echo","hello, world"],capture_output=True,text=True)
# # print("command output", result.stdout)
# command=["Is"]if os.name !="nt" else ["dir"]
# result=subprocess.run(command,capture_output=True,text=True,shell=True)
# print("files in current directory:")
# print(result.stdout)

# #check for error (e.g.,invalid command)
# result=subprocess.run(["fake_command"],capture_output=True,text=True)
# if result.returncode !=0:
#     print("error",result.stderr)


# import os
# import shutil

# #Define the directory to organiize
# directory = "./example_directory"

# #Create the directory and some text files
# os.makedirs(directory, exist_ok=True)
# with open(os.path.join(directory, "file1.txt"), "w") as f:
#     f.write("Text file content")
# with open(os.path.join(directory, "file2.txt"), "w") as f:
#     f.write("Image file content")
# with open(os.path.join(directory, "file3.txt"), "w") as f:
#     f.write("Audio file content")

# #Function to organize files by type
# def organize_files_by_type(directory):
#     #Get a list of all files in the directory
#     for file_name in os.listdir(directory):
#         file_path = os.path.join(directory, file_name)
#         #Skip directories
#         if os.path.isdir(file_path):
#             continue
#         #Get the file extension
#         file_extension = file_name.split(".")[-1]
#         #Create a folder for the file type f it doesnot exist
#         type_folder = os.path.join(directory, file_extension)
#         os.makedirs(type_folder, exist_ok=True)
#         #Move the file to the appropriate folder
#         shutil.move(file_path, os.path.join(type_folder, file_name))
#         print(f"Moved {file_name} to {type_folder}/")

# #Call the functioin
# organize_files_by_type(directory)

# #Display organized structure

# for root, dirs, files in os.walk(directory):
#     print(f"\nIn {root}:")
#     for dir_name in dirs:
#         print(f"Directory: {dir_name}")
#     for file_name in files:
#         print(f"Directory: {file_name}")

# #Clean up
# #shutil.rmtree(directory)

# #create a zip file
# import shutil
# from datetime import datetime
# import os

# def create_backup(directory_path):
#     if not os.path.isdir(directory_path):
#         print(f"error:the directory '{directory_path}'does not exits.")
#         return
#     timestamp=datetime.datetime.now().strftime("%y%m%d_%h%m%s")
#     backup_name=f"backup_{timestamp}"
#     shutil.make_archive(backup_name, 'zip',directory_path)
#     print(f"backup created:{backup_name}.zip")


# Example usage
# create_backup("./example_directory")

# import subprocess
# import os
# def list_running_process(output_file):
#      try:
#         command=['tasklist'if os.name=='nt'else['ps','aux']]
#         result=subprocess.run(command,captutre_output=True,text=True)
#         with open(output_file,'w')as file:
#             file.write(result.stdout)
#         print(f"process list saved to '{output_file}'")
#      except Exception as e:
#         print(f"error:{e}")
# list_running_process("process_list.txt")


# import os
# import shutil
# from datetime import datetime, timedelta

# def file_cleanup(directory, days):
#     archive_folder = os.path.join(directory, "Archive")
#     os.makedirs(archive_folder, exist_ok=True)
    
#     # Calculate the cutoff date
#     cutoff_date = datetime.now() - timedelta(days=days)
    
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path):
#             file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
#             if file_mtime < cutoff_date:
#                 shutil.move(file_path, archive_folder)
#                 print(f"Moved: {filename}")

#     confirm = input(f"Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
#     if confirm == 'yes':
#         shutil.rmtree(archive_folder)
#         print("Archive folder deleted.")
#     else:
#         print("Archive folder retained.")
# file_cleanup('/path/to/directory', 30)  
# import os
# import platform
# import subprocess

# def system_diagnostics_report(output_file):
#     cwd = os.getcwd()

#     # Get disk usage (current directory)
#     disk_usage = subprocess.getoutput(f"du -sh {cwd}")

#     # Get system information
#     os_info = platform.uname()

#     report = f"""
# System Diagnostics Report
# ==========================
# Current Working Directory: {cwd}

# Disk Usage:
# {disk_usage}

# System Information:
# - System: {os_info.system}
# # - Node Name: {os_info.node}
# # - Release: {os_info.release}
# # - Version: {os_info.version}
# # # - Machine: {os_info.machine}
# # - Processor: {os_info.processor}
# # """

# #     # Save the report to a file
# #     with open(output_file, "w") as file:
# #         file.write(report)

# #     print(f"Report saved to {output_file}")

# # # Usage
# # output_file = input("Enter the file path to save the report (e.g., diagnostics.txt): ")
# # system_diagnostics_report(output_file)

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# #email credentials
# sender_email="prakritikhatri746@gmail.com"
# recevier_email="ruman.metahorizon@gmail.com"
# password="pqpo cgwx pbsb rwkr"
# message=MIMEMultipart()
# message["from"]=sender_email
# message["to"]=recevier_email
# message["subject"]="test email"
# body="hello, this is a test email send from python"
# message.attach(MIMEMultipart(body,"plain"))
# try:
#   with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email,password)
#         server.sendmail(sender_email,recevier_email,message.as_string())
#         print("emeil sent successfully!")
# except Exception as e:
#     print(f"error:{e}")

import schedule
import time
def send_notification():
    print("this is your schedule notification!")
    schedule.every(10).seconds.do(send_notification)
    print("scheduler started.press ctrl+c to stop")
    while True:
        schedule.run_pending()
        time.sleep(1)