from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize
import os
import shutil
PACKAGE = "MyTools"
class CustomBuildExt(build_ext):
    def run(self):
        # 先执行正常的编译
        super().run()
        # 编译完成后，删除源.py文件（保留__init__.py）
        package_dir = PACKAGE
        for root, _, files in os.walk(package_dir):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    py_path = os.path.join(root, file)
                    if os.path.exists(py_path):
                        os.remove(py_path)

# 要编译的文件
def get_py_files():
    py_files = []
    for root, _, files in os.walk(PACKAGE):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                py_files.append(os.path.join(root, file))
    return py_files

setup(
    name=PACKAGE,
    version="1.0.0",
    author="AngryPsyduck",
    author_email="1440156598@qq.com",
    description="Tools",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/extinction057/MyTools",
    packages=find_packages(),
    package_data={
        PACKAGE: ["*.c", "*.h"],  # 只包含 C 文件
    },
    exclude_package_data={
        PACKAGE: ["*.py"],        # 强制排除所有 py 文件
    },
    ext_modules=cythonize(
        get_py_files(),
        compiler_directives={"language_level": "3"},
        build_dir="cython_build",
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["numpy==2.0.2","zernike","scikit-learn","scipy","tqdm","matplotlib","vtk","opencv-python","cython"],
)