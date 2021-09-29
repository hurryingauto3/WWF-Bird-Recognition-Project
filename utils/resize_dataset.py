from PIL import Image
from os import walk, rename

def get_filenames(path):
    files = [x[2] for x in walk(path)]
    files = files[0]
    return files

def resize_images(files, src, dest, code):
    count = 0

    for img in files:
        print(img)
        count += 1
        im = Image.open(src+img)
        im = im.resize((50,50))
        im.save(dest+code+str(count)+'.jpg')

src1 = 'HS\\'
dest1 = 'HS50\\'
code1 = 'HS'

src2 = 'HC\\'
dest2 = 'HC50\\'
code2 = 'HC'

src3 = 'CM\\'
dest3 = 'CM50\\'
code3 = 'CM'

files1 = get_filenames(src1)
files1.sort()

files2 = get_filenames(src2)
files2.sort()

files3 = get_filenames(src3)
files3.sort()

resize_images(files1, src1, dest1, code1)
print('done')
resize_images(files2, src2, dest2, code2)
print('done')
resize_images(files3, src3, dest3, code3)
print('done')

