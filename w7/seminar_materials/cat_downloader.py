from abc import ABC, abstractmethod

class CatRecognition:
    def prepare():
        image_downloader = ImageDownloader()
        image_downloader.load_image('https://vk.com/image1.png')
        # self.find_cats()
        # self.print_cats()
    pass


class ImageDownloader:
    def load_image(self, url):
        downloader = None
        if url.startswith('https://'):
            downloader = HttpsConnection(url)
            pic = downloader.get()
            self.clean_https_picture(pic)
        elif url.startswith('tcp://'):
            downloader = TcpConnection(url)
            pic = downloader.get()
            self.clean_tcp_picture(pic)
        elif url.startswith('catprot://'):
            downloader = SpecialCatProtocolConnection(url)
            pic = downloader.get()
            self.clean_cat_protocol_picture(pic)

    def clean_https_picture(self):
        pass


class AbstractConnection(ABC):
    @abstractmethod
    def get(self):
        pass


class HttpsConnection(AbstractConnection):
    def get(self):
        # prepare connection
        # find IP
        # load certificates
        pass

class SsshfsConnection(AbstractConnection):
    def get(self):
        pass


class SpecialCatProtocolConnection(AbstractConnection):
    def decompress(self):
        pass

    # def get(self):
    #     pass

