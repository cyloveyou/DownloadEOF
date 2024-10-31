from setuptools import setup, find_packages

setup(
    name="SentinelOrbit",
    version="1.0",
    packages=find_packages(),
    # 命令行工具
    scripts=[
        "./src/SentinelOrbit.py",
    ],
    install_requires=["requests"],
    include_package_data=True,
    license="MIT",
    description="This is a tool to download Sentinel-1 orbit data from ASF.",
    long_description=open("README.md").read(),
    author="小y同学",
    author_email="3232076199@qq.com",
    url="https://github.com/cyloveyou/SentinelOrbit ",  # 项目主页链接
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
