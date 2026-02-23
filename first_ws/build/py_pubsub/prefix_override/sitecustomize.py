import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/franco/Desktop/Robotica/first_ws/install/py_pubsub'
