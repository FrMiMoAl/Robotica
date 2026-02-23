from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='franco',
    maintainer_email='32112849+FrMiMoAl@users.noreply.github.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pruebita_publicador = py_pubsub.pub:main',
            'pruebita_subcriptor = py_pubsub.sub:main',
            'pruebita_subcriptor_numeros = py_pubsub.SubNumbers:main',
            'pruebita_publicador_numeros = py_pubsub.pubNumbers:main',
        ],
    },
)
