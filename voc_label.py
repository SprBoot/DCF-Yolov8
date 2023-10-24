# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

sets = ['train', 'val', 'test']  # 如果你的Main文件夹没有test.txt，就删掉'test'
classes = ["rice leaf roller", 'rice leaf caterpillar', 'paddy stem maggot', 'asiatic rice borer', 'yellow rice borer', 'rice gall midge', 'Rice Stemfly', 'brown plant hopper', 'white backed plant hopper', 'small brown plant hopper', 'rice water weevil', 'rice leafhopper',
           'grain spreader thrips', 'rice shell pest', 'grub', 'mole cricket', 'wireworm', 'white margined moth', 'black cutworm', 'large cutworm','yellow cutworm','red spider','corn borer','army worm','aphids','Potosiabre vitarsis',
        'peach borer','english grain aphid','green bug','bird cherry-oataphid','wheat blossom midge','penthaleus major','longlegged spider mite','wheat phloeothrips','wheat sawfly','cerodonta denticornis','beet fly','flea beetle','cabbage army worm',
        'beet army worm','Beet spot flies','meadow moth','beet weevil','sericaorient alismots chulsky','alfalfa weevil','flax budworm','alfalfa plant bug','tarnished plant bug','Locustoidea','lytta polita','legume blister beetle','blister beetle',
        'therioaphis maculata Buckton','odontothrips loti','Thrips','alfalfa seed chalcid','Pieris canidia','Apolygus lucorum','Limacodidae','Viteus vitifoliae','Colomerus vitis','Brevipoalpus lewisi McGregor','oides decempunctata','Polyphagotars onemus latus','Pseudococcus comstocki Kuwana',
        'parathrene regalis','Ampelophaga','Lycorma delicatula','Xylotrechus','Cicadella viridis','Miridae','Trialeurodes vaporariorum','Erythroneura apicalis','Papilio xuthus','Panonchus citri McGregor','Phyllocoptes oleiverus ashmead','Icerya purchasi Maskell',
        'Unaspis yanonensis','Ceroplastes rubens','Chrysomphalus aonidum','Parlatoria zizyphus Lucus','Nipaecoccus vastalor','Aleurocanthus spiniferus','Tetradacus c Bactrocera minax','Dacus dorsalis(Hendel)','Bactrocera tsuneonis','Prodenia litura',
        'Adristyrannus','Phyllocnistis citrella Stainton','Toxoptera citricidus','Toxoptera aurantii','Aphis citricola Vander Goot','Scirtothrips dorsalis Hood','Dasineura sp','Lawana imitata Melichar','Salurnis marginella Guerr','Deporaus marginatus Pascoe','Chlumetia transversa','Mango flat beak leafhopper','Rhytidodera bowrinii white','Sternochetus frigidus','Cicadellidae']  # class names


abs_path = os.getcwd()


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    in_file = open(abs_path + '/Annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open(abs_path + '/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # difficult = obj.find('Difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


for image_set in sets:
    if not os.path.exists(abs_path + '/labels/'):
        os.makedirs(abs_path + '/labels/')

    image_ids = open(abs_path + '/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open(abs_path + '/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(abs_path + '/JPEGImages/%s.jpg\n' % (image_id))  # 要么自己补全路径，只写一半可能会报错
        convert_annotation(image_id)
    list_file.close()

