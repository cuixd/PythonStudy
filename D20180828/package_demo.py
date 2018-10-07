# 引入自定义的包中的模块
import D20180827.getAllDir

'''
包的本质是一个目录，但是在目录的基础上有两点要求：
1、包名不能以数字开头，即目录不能以数字开头
2、包中必须要包含一个__init__.py文件，使用PyCharm来创建一个Package时会自动创建该文件，
    如果是自己手动添加Package，则需要手动创建该文件，作用是用来限定包中的哪些模块
    可以被其他程序引入，默认为空，表示包中的全部模块都可被引入
'''

# 调用模块中的方法
D20180827.getAllDir.getAllDirByQueueScope("/Users/cuixiaodong/PycharmProjects/PythonStudy/D20180824/1")