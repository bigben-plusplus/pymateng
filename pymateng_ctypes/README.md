在matlab.json中配置MATLABROOT，即将root修改为本机上的Matlab安装目录。
pymateng.py实现了matlab engine forpyhton，对libeng.dll中的函数提供了以下3种级别的封装。

1. DLL API级别。这一层次的函数和直接调用libeng.dll函数没有太大差别。不建议采用。
2. Python Function API级别。对DLL中的原始函数通过Python函数做了一层封装，使用相对会更加安全。
3. Python Class级别。采用面向对象编程方式，将相关函数封装到一个Python类中，便于调用。

test/test_pymateng.py提供了对这三种级别API的测试。
也可以直接运行python pymateng.py进行测试。

bigben@seu.edu.cn