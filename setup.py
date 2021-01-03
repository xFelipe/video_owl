import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Video Owl',
    version='0.1',
    author='Felipe Gomes Duarte',
    author_email='xfelipegd@gmail.com',
    description='Persiste vídeos e playlists do youtube.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xFelipe/video_owl',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)