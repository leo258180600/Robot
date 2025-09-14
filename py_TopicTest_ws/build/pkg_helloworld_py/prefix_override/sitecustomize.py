import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lsp/MyROS/py_TopicTest_ws/install/pkg_helloworld_py'
