import os


class ChangeIELTS:
    def __init__(self):
        self.IELTS_path = "/Users/jack/Desktop/IELTS/IELTS books/IELTS 音频/IELTS 12 audio"

    def get_filepaths(self):
        file_paths = []
        # Walk the tree.
        for root, directories, files in os.walk(self):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.

        return file_paths  # Self-explanatory.


def change(path):
    rep1 = path.replace("IELTS ", "")
    rep2 = rep1.replace(" Test", "")
    rep3 = rep2.replace("_S", "")
    final_path = '/Users/jack/Desktop/IELTS/IELTS books/IELTS 音频/IELTS 12 audio/' + rep3
    orginial_path = '/Users/jack/Desktop/IELTS/IELTS books/IELTS 音频/IELTS 12 audio/' + path
    os.rename(orginial_path, final_path)


name_list = ChangeIELTS()
all_name = ChangeIELTS.get_filepaths(name_list.IELTS_path)
print(all_name)
for each in all_name:
    if each[-8:] == "DS_Store":
        os.remove(each)
    else:
        change(each[-21:])
        print(each)

# change("/Users/jack/Desktop/IELTS/IELTS books/IELTS 音频/IELTS 14 audio/C14T2S2.mp3")





