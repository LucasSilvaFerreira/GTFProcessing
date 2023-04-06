from setuptools import setup

setup(
    name="GTFProcessing",
    version="0.0.1",
    py_modules=["GTFProcessing"],
    install_requires=["pandas", "gtfparse==1.3.0", "tqdm"]
)

