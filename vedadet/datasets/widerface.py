import os.path as osp
import xml.etree.ElementTree as ET
import lmdb

import vedacore.fileio as fileio
from vedacore.misc import registry
from .xml_style import XMLDataset

# ---------------------hgy----------------------
@registry.register_module('dataset')
class WIDERFaceDataset(XMLDataset):
    """Reader for the WIDER Face dataset in PASCAL VOC format.

    Conversion scripts can be found in
    https://github.com/sovrasov/wider-face-pascal-voc-annotations
    """
    CLASSES = ('face', )

    def __init__(self, **kwargs):
        super(WIDERFaceDataset, self).__init__(**kwargs)

    def load_annotations(self, ann_file):
        """Load annotation from WIDERFace XML style annotation file.

        Args:
            ann_file (str): Path of XML file.

        Returns:
            list[dict]: Annotation info from XML file.
        """
        data_infos = []
        img_ids = fileio.list_from_file(ann_file)#train.txt
        self.img_ids = img_ids
        path = osp.join(self.img_prefix,'Annotations')
        env = lmdb.open(path)
        with env.begin(write=False) as txn:
            for img_id in img_ids:
                lmdb_xml_label = osp.join(self.img_prefix, 'Annotations',
                                f'{img_id}').replace('/','\\').replace('\\data\\guangyid\\WIDERFace\\','')
                # print(list(lmdb_xml_label))
                bin = txn.get(lmdb_xml_label.encode())
                # print(bin)
                root = ET.fromstring(bin)
                size = root.find('size')
                width = int(size.find('width').text)
                height = int(size.find('height').text)
                folder = root.find('folder').text
                data_infos.append(
                    dict(
                        id=img_id,
                        filename=osp.join(folder, img_id),
                        width=width,
                        height=height))
        return data_infos

        # data_infos = []
        # img_ids = fileio.list_from_file(ann_file)#train.txt
        # self.img_ids = img_ids
        # for img_id in img_ids:
        #     filename = f'{img_id}.jpg'
        #     xml_path = osp.join(self.img_prefix, 'Annotations',
        #                         f'{img_id}.xml')#先通过目录索引.txt文件得到xml文件名字
        #     tree = ET.parse(xml_path)
        #     root = tree.getroot()
        #     size = root.find('size')
        #     width = int(size.find('width').text)
        #     height = int(size.find('height').text)
        #     folder = root.find('folder').text
        #     data_infos.append(
        #         dict(
        #             id=img_id,
        #             filename=osp.join(folder, filename),#再从xml文件中得到图片的路径
        #             width=width,
        #             height=height))

        # return data_infos
