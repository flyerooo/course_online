# course_online
安装xadmin是参考https://coding.imooc.com/lesson/78.html#mid=1996
即直接下载源码
先在setting中加入：
sys.path.insert(1, os.path.join(BASE_DIR, 'extra_apps'))
如果还报错：则安装如下包
(xadmin所需的依赖要装上，可以先pip install xadmin，再pip uninstall xadmin，这样那些依赖包就装好了)
pip install future six 
pip install  django_import_export