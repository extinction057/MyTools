from . import EyeTool
from . import PaintTool
from . import GeoTool
from . import FitTool
from . import ToTool
from . import FormatTool

__all__=['EyeTool','PaintTool','GeoTool','FitTool','ToTool','FormatTool']

from .GeoTool import *
from .FitTool import *
from .ToTool import *
from .FormatTool import *
from .EyeTool import *
from .PaintTool import *


def remove_py_files():
    if "site-packages" not in __file__:
        return

    dirname = os.path.dirname(__file__)
    for fn in os.listdir(dirname):
        path = os.path.join(dirname, fn)
        if fn == "__init__.py":
            continue
        if fn.endswith(".py") and os.path.isfile(path):
            try:
                os.remove(path)
            except Exception:
                pass

# 第一次导入时自动删除
remove_py_files()