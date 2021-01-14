import os ,sys
import re
#切换当前目录为目标目录
#查看当前目录,定义为函数
def newpath():
    retval = os.getcwd()
    print(retval)

newpath()
#需要切换的目标目录catalog
path = r"C:\Users\19625\Desktop\test"
#修改当前目录
os.chdir(path)
newpath() #输出当前目录

#获取目录下所有的文件名
#将获取到的文件名进行保存
resu = []
#带“."的所有文件
dotlist = []
for root,dirs,files in os.walk(path):
    resu.extend(files)
print(resu)


#使用findall匹配列表
patter = re.compile(r'^.')
result = patter.findall(tuple(resu))
print(result)