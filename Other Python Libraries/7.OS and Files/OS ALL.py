
import os


print(dir(os))

folder =  "/Users/benjaminbrooke/.cache/kagglehub/datasets/aryashah2k/breast-ultrasound-images-dataset/versions/1/Dataset_BUSI_with_GT"

print(os.listdir(folder))
#['.DS_Store', 'malignant', 'benign', 'normal']



if 'Test_data' not in os.listdir(folder):
    os.makedirs(f'{folder}/Test_data')


print(os.stat(f'{folder}/benign'))
#os.stat_result(st_mode=16877, st_ino=20786378, st_dev=16777232, st_nlink=893, st_uid=501, st_gid=20, st_size=28576, st_atime=1763222136, st_mtime=1763222123, st_ctime=1763222123)


for dirpath, dirnames, filenames in os.walk(folder):
    print("Current Path:", dirpath)
    print("Dictionaries:", dirpath)
    print("Files:", dirpath)




for files in os.listdir('/Users/benjaminbrooke/PycharmProjects/Python/Other Python Libraries/7.OS and Files/Data'):
    print(files)

"""
Third.txt
First.txt
Second.txt
"""








