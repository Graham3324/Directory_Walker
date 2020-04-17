import os
import shutil


class Dir_Holder:
    def __init__(self):
        self.uniques = {}
        self.duplicates = {}

    def additem(self, item):
        if item in self.uniques:
            if item in self.duplicates:
                pass
            else:
                self.duplicates.update(item)
        else:
            self.uniques.update(item)


class Dir_Walker:
    def __init__(self, path):
        self.base_path = path
        self.uniqueitems = {}
        self.duplicateitems = {}
        self.walked_directories = {}

    def run(self):
        items = os.listdir(self.base_path)

        print("Walking directory " + self.base_path)

        for entry in items:
            current_item = self.base_path + "/" + entry
            if os.path.isdir(current_item):
                subdir = Dir_Walker(current_item)
                returned_uniques, returned_duplicates = subdir.run()
                for piece in returned_uniques.items():
                    if piece[0] in self.uniqueitems:
                        if piece[0] in self.duplicateitems:
                            pass
                        else:
                            self.duplicateitems.update([piece])
                    else:
                        self.uniqueitems.update([piece])
                for piece in returned_duplicates.items():
                    if piece[0] in self.duplicateitems:
                        pass
                    else:
                        self.duplicateitems.update([piece])
            else:
                print("Processing file " + current_item)
                file_name = current_item
                current_type = "file"
                output_list = file_name.split("/")
                output_name = output_list[len(output_list) - 1]

                if output_name not in self.uniqueitems.keys():
                    self.uniqueitems.update([(entry, (file_name, current_type))])

        return self.uniqueitems, self.duplicateitems


start_directory = "/Users/grahamsayers/Desktop/Python_Work/projects/Directory_Walker"
new_walker = Dir_Walker(start_directory)

new_walker.run()

for file_name, file_tuple in new_walker.uniqueitems.items():

    destination = (
        "/Users/grahamsayers/Desktop/Python_Work/projects/DW_Output" + "/" + file_name
    )

    try:
        shutil.copyfile(file_tuple[0], destination)
        print("Copied to : " + destination)
    except shutil.SameFileError:
        print("Already exists")
    except:
        print("Something else")
