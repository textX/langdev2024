from setuptools import find_packages, setup

PACKAGE_NAME = "tx-drone"
VERSION="0.1.0"
AUTHOR="textX"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx"]},
    install_requires=["textx_ls_core", "textX-jinja"],
    entry_points={
        "textx_languages": [
            "drone = tx_drone:drone"
        ], 
        "textx_generators": [
            "drone_generator = tx_drone:drone_generator"
        ]
    },
)