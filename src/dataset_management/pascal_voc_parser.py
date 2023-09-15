"""
Project: ak_sw_benchmarker Azure Kinect Size Estimation https://github.com/juancarlosmiranda/ak_size_weight_sim/

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda/
Date: February 2022
Description:
    Contains methods to manage PASCAL VOC files

Use:

"""

from lxml import etree as ET


class PascalVocParser:
    class_label_name = "Obj_"

    def __init__(self, config_param):
        pass
    # TODO: 16/02/2023 CHECK CONVERSION FROM STRING TO INTEGER
    @staticmethod
    def readXMLFromFile(file_to_parse_path):
        a_label_list = []
        bounding_boxes_list = []
        # ---------------------------------
        xml_tree = ET.parse(file_to_parse_path)
        xml_body = xml_tree.getroot()

        for record in xml_body.iter('object'):
            label_element = record.find('name').text
            bbox_element = record.find('bbox')
            xmin = int(bbox_element.find('xmin').text)
            ymin = int(bbox_element.find('ymin').text)
            xmax = int(bbox_element.find('xmax').text)
            ymax = int(bbox_element.find('ymax').text)
            a_box_list = [xmin, ymin, xmax, ymax]
            bounding_boxes_list.append(a_box_list)
            a_label_list.append(label_element)

        return bounding_boxes_list, a_label_list

    @staticmethod
    def create_labeled_XML_files(self):
        pass
        raise NotImplementedError("Can't use yet!")
    # todo: implement ths method
    # todo: fix test of pascal_voc_parser, add label_list control

# todo: methods from dataset manager used in .XML files must be migrated to this file