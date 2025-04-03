from setuptools import setup, find_packages

setup(
    name="CTkExtendedGraph",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["customtkinter", "matplotlib", "numpy"],
    include_package_data=True,
    author="Loris Dante",
    author_email="loris_06@yahoo.de",
    description="CTkExtendedGraph is a CustomTkinter widget for displaying stacked bar charts. Built on Matplotlib, it allows easy integration into Tkinter apps, with features like dynamic data updates, resizability, and customization of categories, colors, and units. Ideal for flexible, interactive data visualization.",
    url="https://github.com/iLollek/CTkExtendedGraph",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
