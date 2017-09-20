#!/usr/bin/env python

# Copyright (c) 2016-Present Pivotal Software, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os
import sys

def read_version_file():
    with open('version') as vfile:
        return vfile.read()

setup(
    name='cf_platform_eng',
    version=read_version_file(),
    description='A toy python package',
    url='http://github.com/cf-platform-eng/test-python-package',
    license='Apache 2.0',
    packages=['cf_platform_eng'],
    zip_safe=False)