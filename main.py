# -*- coding: utf-8 -*-

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os


class Image2Word(object):
    '''
    put input file to folder input
    '''
    INPUT_FOLDER = 'input'
    OUTPUT_FOLDER = 'output'

    def __init__(self, input_file):
        self.filename = input_file
        self.input_path = os.path.join(self.INPUT_FOLDER, self.filename)
        self.output_path = os.path.join(
            self.OUTPUT_FOLDER, os.path.splitext(self.filename)[0] + '.txt')

    def transfer(self):
        try:
            im = Image.open(self.input_path)
            text = pytesseract.image_to_string(im)  # lang 指定中文简体

            with open(self.output_path, 'w+') as f:
                f.write(text)
                print("==finish==")
        except Exception as ex:
            print(ex)
