import sys

# 获取命令行终端的未知参数列表第一个为脚本名称
arglist = sys.argv
print(arglist)

for arg in sys.argv:
    print(arg)

# 在PyCharm中设置命令行参数的方法：Run - Edit Configurations - Parameters
# 也可以通过命令行终端来运行脚本 添加位置参数

'''
192-169-30-129:10.图片读取、sys模块、package cuixiaodong$ pwd
/Users/cuixiaodong/PycharmProjects/PythonStudy/10.图片读取、sys模块、package
192-169-30-129:10.图片读取、sys模块、package cuixiaodong$ python3 sys_module.py cuixd 33 dba
['sys_module.py', 'cuixd', '33', 'dba']
sys_module.py
cuixd
33
dba
192-169-30-129:10.图片读取、sys模块、package cuixiaodong$
'''

# 获取python的path
print(sys.path)