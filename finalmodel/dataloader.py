# def load_dataset(size):
def unzip(zipfile):
    with ZipFile(zipfile, 'r') as zip:
        zip.printdir()
        zip.extractall()
        print('Done!')


def load_dataset():
  # if size == 100:

  #   cm = [x for x in os.walk('CM100')][0][2]
  #   hs = [x for x in os.walk('HS100')][0][2]
  #   hc = [x for x in os.walk('HC100')][0][2]

  # elif size == 200:
  #   cm = [x for x in os.walk('CM200')][0][2]
  #   hs = [x for x in os.walk('HS200')][0][2]
  #   hc = [x for x in os.walk('HC200')][0][2]

  # elif size == 224:
  #   cm = [x for x in os.walk('CM224')][0][2]
  #   hs = [x for x in os.walk('HS224')][0][2]
  #   hc = [x for x in os.walk('HC224')][0][2]

  # else:
  #   return 'invalid size'
  cm = [x for x in os.walk('CM100')][0][2]
  hs = [x for x in os.walk('HS100')][0][2]
  hc = [x for x in os.walk('HC100')][0][2]

  # cm = ['CM100/' + cm[x] for x in range(len(cm))]
  # hs = ['HS100/' + hs[x] for x in range(len(hs))]
  # hc = ['HC100/' + hc[x] for x in range(len(hc))]


  cm = ['CM100/' + cm[x] for x in range(len(cm))]
  hs = ['HS100/' + hs[x] for x in range(len(hs))]
  hc = ['HC100/' + hc[x] for x in range(len(hc))]

  cm_label = [0]*len(cm)
  hs_label = [1]*len(hs)
  hc_label = [2]*len(hc)

  dataset = cm+hs+hc
  labels = cm_label + hs_label + hc_label

  return dataset, label

def read_images(dataset):
    images = []

    for filepath in dataset:
        images.append(cv2.imread(filepath))

    return images
