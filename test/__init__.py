import os
import sys

test_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(test_path)
src_path = base_path + "\\src"
sys.path.append(test_path)
sys.path.append(src_path)
