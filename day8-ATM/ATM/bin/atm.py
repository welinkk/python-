# Author:xqkang
# Date:2020/10/9 上午9:34

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import main



if __name__ == '__main__':
    main.run()
