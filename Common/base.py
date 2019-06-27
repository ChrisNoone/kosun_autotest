# coding: utf-8

from configparser import ConfigParser
import yaml
import logging
import time
import sys
import requests
import tesserocr
import csv
import traceback
from PIL import Image


class ConfigHelper(object):
    @staticmethod
    def conf_read(section, option):
        conf = ConfigParser()
        configfile = './Common/config.conf'
        conf.read(configfile)
        result = conf.get(section, option)
        return result


class YamlHelper(object):
    @staticmethod
    def yaml_read(file):
        with open(file, mode='r', encoding='utf8') as config:
            result = yaml.load(config.read(), Loader=yaml.FullLoader)
        config.close()
        return result


class Logger(object):
    conf = ConfigHelper()
    log_path = conf.conf_read('log', 'path')
    log_level = conf.conf_read('log', 'level')

    def __init__(self, path=log_path):
        self.file_name = path + 'fusion_automate_log_%s.log' % time.strftime("%Y%m%d", time.localtime())
        self.logger = logging.getLogger()
        # 日志输出的级别
        if self.log_level == 'error':
            self.logger.setLevel(logging.ERROR)
        elif self.log_level == 'warning':
            self.logger.setLevel(logging.WARNING)
        elif self.log_level == 'info':
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')

    def debug(self, message):
        """
        添加信息日志
        :param message:
        :return:
        """
        self._console("debug", message)

    def info(self, message):
        """
        添加信息日志
        :param message:
        :return:
        """
        self._console("info", message)

    def warning(self, message):
        """
        添加警告日志
        :param message:
        :return:
        """
        self._console("warning", message)

    def error(self, message=None):
        """
        添加错误日志
        :param message:
        :return:
        """
        self._console("error", message)

    def _console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.file_name, 'a', encoding='utf8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个SteamHandler,用于输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            # self.logger.error(message)
            # 使用traceback打印报错的详细位置
            self.logger.error(traceback.format_exc())

        # 这两行代码为了避免日志输出重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()
        ch.close()


class CsvHelper(object):
    @staticmethod
    def read_data(f, encoding="utf-8-sig"):
        """
        读csv文件作为普通list
        :param f:
        :return:
        """
        data_ret = []
        with open(f, encoding=encoding, mode='r') as csv_file:
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                data_ret.append(row)
        return data_ret

    @staticmethod
    def read_data_as_dict(f, encoding="utf-8-sig"):
        """
        读csv文件作为普通list
        :param f:
        :return:
        """
        data_ret = []
        with open(f, encoding=encoding, mode='r') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for row in csv_dict:
                data_ret.append(row)
        return data_ret

    @staticmethod
    def write_data(f, data, encoding='utf-8'):
        """
        写入csv文件
        :param f: 文件路径
        :param data: list类型数据,一行数据一个list
        :param encoding:
        """
        with open(f, encoding=encoding, mode='a', newline='') as fp:
            csv_write = csv.writer(fp, dialect='excel')
            csv_write.writerow(data)
        fp.close()


class Captcha(object):
    img_path = './Cache/captcha.png'

    def download_img(self, pic_url):
        """
        通过图片链接，下载图片到本地
        :param pic_url:
        """
        r = requests.get(pic_url)
        with open(self.img_path, 'wb') as f:
            f.write(r.content)
        f.close()

    def get_img(self):
        """
        用Image获取图片文件
        :return: 图片文件
        """
        img = Image.open(self.img_path)
        return img

    @staticmethod
    def grayscale_deal_img(image):
        """
        图片转灰度处理
        :param image:图片文件
        :return: 转灰度处理后的图片文件
        """
        img = image.convert('L')
        # img.show()
        return img

    @staticmethod
    def thresholding_method_img(image):
        """
            图片二值化处理
            :param image:转灰度处理后的图片文件
            :return: 二值化处理后的图片文件
        """
        # 阈值，控制二值化程度，自行调整（不能超过256）
        threshold = 160
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        img = image.point(table, '1')
        # img.show()
        return img

    @staticmethod
    def captcha_tesserocr_crack(image):
        """
            图像识别
            :param image: 二值化处理后的图片文件
            :return: 识别结果
        """
        result = tesserocr.image_to_text(image)
        return result

    def captcha(self, pic_url):
        self.download_img(pic_url)
        image = self.get_img()
        image1 = self.grayscale_deal_img(image)
        image2 = self.thresholding_method_img(image1)
        result = self.captcha_tesserocr_crack(image2)
        return result
