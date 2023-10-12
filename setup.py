from setuptools import setup, find_packages

setup(
    name='mediapipe',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    author='Daniel Fiuza & Ibrahim Animashaun',
    package_data={
        'mediapipe': ['modules/pose_landmark/pose_landmark_heavy.tflite',
                      'modules/pose_landmark/pose_landmark_lite.tflite'] 
    }
)
