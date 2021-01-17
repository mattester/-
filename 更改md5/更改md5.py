import os

def fileAppend(filename):
    myfile = open(filename,'a')
    myfile.write("#1234")
    myfile.close

while True:
    if __name__ == '__main__':
        filename = input("输入文件名称")
        fileAppend(filename)
        print(filename + 'is changed.')
