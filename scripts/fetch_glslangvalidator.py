#!/usr/bin/env python3
#
# Copyright (c) 2018 The Khronos Group Inc.
# Copyright (c) 2018 Valve Corporation
# Copyright (c) 2018 LunarG, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Mark Lobodzinski <mark@lunarg.com>


# This script will download the latest glslang release binary and extract the
# glslangValidator binary needed by the samples.
#
# It takes as its lone argument the filname (no path) describing the release
# binary name from the glslang github releases page.

# 第一步：将glslang-master-windows-x64-Release.zip文件存放至根目录glslang里面
# 第二步：python ./fetch_glslangvalidator.py

import sys
import os
import shutil
import ssl
import subprocess
import urllib.request
import zipfile

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.join(SCRIPTS_DIR, '..')

if __name__ == '__main__':
    GLSLANG_FILENAME = "glslang-master-windows-x64-Release.zip"
    GLSLANG_OUTFILENAME = os.path.join(REPO_DIR, "glslang", GLSLANG_FILENAME)
    GLSLANG_VALIDATOR_PATH = os.path.join(REPO_DIR, "glslang", "bin")
    GLSLANG_VALIDATOR_FULL_PATH = os.path.join(REPO_DIR, "glslang", "bin", "glslangValidator")
    GLSLANG_DIR = os.path.join(REPO_DIR, "glslang")

    if os.path.isdir(GLSLANG_DIR):
        if os.path.isdir(GLSLANG_VALIDATOR_PATH):
            dir_contents = os.listdir(GLSLANG_VALIDATOR_PATH)
            for afile in dir_contents:
                if "glslangValidator" in afile:
                    print("   Using glslangValidator at %s" % GLSLANG_VALIDATOR_PATH)
                    sys.exit();
    else:
        os.mkdir(GLSLANG_DIR)
    print("   Unzipping glslangValidator binary from glslang releases dir")
    sys.stdout.flush()

    zipped_file = zipfile.ZipFile(GLSLANG_OUTFILENAME, 'r')
    namelist = zipped_file.namelist()
    for afile in namelist:
        if "glslangValidator" in afile:
            EXE_FILE_PATH = os.path.join(GLSLANG_DIR, afile)
            zipped_file.extract(afile, GLSLANG_DIR)
            os.chmod(EXE_FILE_PATH, 0o775)
            break
    zipped_file.close()
    sys.exit();
