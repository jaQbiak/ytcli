from setuptools import setup, find_packages

setup(
    name="ytcli",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "pytube"
    ],
    entry_points="""
    [console_scripts]
    ytcli=ytcli:ytcli
    """
)
