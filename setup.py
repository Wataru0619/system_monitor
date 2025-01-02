from setuptools import setup

package_name = 'system_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'psutil'],
    zip_safe=True,
    maintainer='wataru',
    maintainer_email='s23c1072kg@s.chibakoudai.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'system_info_publisher = system_monitor.system_info_publisher:main',
        ],
    },
)
