import os
from setuptools import find_packages, setup
from setuptools.command.install import install
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


def make_cuda_ext(name, module, sources):
    cuda_ext = CUDAExtension(
        name='%s.%s' % (module, name),
        sources=[os.path.join(*module.split('.'), src) for src in sources]
    )
    return cuda_ext


if __name__ == '__main__':

    setup(
        name='example',
        version='0.0.0',
        description='Examples illustrating how to use c++ and CUDA in python.',
        install_requires=[
            'numpy',
            'torch>=1.1',
        ],
        author='Jeff Wang',
        author_email='wangxiaofeng2020@ia.ac.cn',
        license='Apache License 2.0',
        packages=find_packages(),
        cmdclass={
            'build_ext': BuildExtension,
        },
        ext_modules=[
            CUDAExtension(
                name="cpp_CUDA_code.pointnet_cuda",
                sources=[
                    "cpp_CUDA_code/pointnet_api.cpp",
                    "cpp_CUDA_code/ball_query.cpp",
                    "cpp_CUDA_code/ball_query_gpu.cu",
                ]   
            ),
        ],
    )
