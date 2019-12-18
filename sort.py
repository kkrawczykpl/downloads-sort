import os


def main():
    folder_to_sort = input("Sort files in folder (path): ")
    change_location = input("Change files location? (True or False): ")

    if change_location == "True":
        folder_destination = input("Location (path): ")
    else:
        folder_destination = folder_to_sort

    sort(folder_to_sort, folder_destination)


def sort(folder_to_sort, folder_destination):
    for filename in os.listdir(folder_to_sort):
        subfolder = choose_subfolder(filename)
        check_if_folder_exists(folder_destination + '\\' + subfolder + '\\')
        src = folder_to_sort + '\\' + filename
        src_destination = folder_destination + '\\' + subfolder + '\\' + filename
        os.rename(src, src_destination)


def choose_subfolder(filename):
    if filename.lower().endswith(('.mp3', '.wav', '.aac', '.wma', '.flac', '.ogg', '.alac')):
        return 'Music'
    elif filename.lower().endswith(('.avi', '.mov', '.mkv', '.mp4', '.flv', '.wmv')):
        return 'Videos'
    elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
        return 'Images'
    elif filename.lower().endswith(('.psd', '.ai', '.eps')):
        return 'Graphic Projects'
    elif filename.lower().endswith(('.pdf', '.doc', '.docx', '.odt', '.ppt', '.pptx')):
        return 'Documents'
    elif filename.lower().endswith(('.html', '.css', '.js')):
        return 'Web Development'
    elif filename.lower().endswith(('.zip', '.rar')):
        return 'Archives'
    elif filename.lower().endswith('.txt'):
        return 'Texts'
    elif filename.lower().endswith(('.csv', '.xlm', '.ods', '.ots', '.tsv', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xlt')):
        return 'Spreadsheets'
    else:
        return ''


def check_if_folder_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


main()
