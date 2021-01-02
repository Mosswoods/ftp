# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import wget
import os

class Ftp:
    def mkdir(self, path):   # 创建下载文件夹
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path + " is created successfully!")
            return True
        else:
            return False

    @staticmethod
    def static_download(url):  # 从网站上获取文件下载列表
        filename = wget.download(url)
        return filename

    @staticmethod
    def static_readTxt(filename, url):    # 根据文件下载列表完成下载
        with open(filename, "r") as f:
            for line in f.readlines():
                columns = line.split()
                print(columns[-1])
                full_url = url+str(columns[-1])
                wget.download(full_url)
                print(columns[-1] + " is downloaded successfully!")

    def main(self):
        dir_path = os.path.abspath(__file__).replace('\\', '/').rsplit('/', 2)[0] + '/datasets/GSE150nnn/GSE150123/matrix/'
        ftp.mkdir(dir_path)
        os.chdir(dir_path)

        # root_url = 'ftp://ftp.genome.jp/pub/kegg/medicus/drug/gif/'
        root_url = 'ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE150nnn/GSE150123/matrix/'
        txt = Ftp.static_download(root_url)
        Ftp.static_readTxt(txt, root_url)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ftp = Ftp()
    ftp.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
