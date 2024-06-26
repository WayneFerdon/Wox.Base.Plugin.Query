# ----------------------------------------------------------------
# Author: WayneFerdon wayneferdon@hotmail.com
# Date: 2023-04-02 12:21:06
# LastEditors: WayneFerdon wayneferdon@hotmail.com
# LastEditTime: 2023-04-09 23:19:30
# FilePath: \FlowLauncher\Plugins\WoxBasePluginQuery\__init__.py
# ----------------------------------------------------------------
# Copyright (c) 2023 by Wayne Ferdon Studio. All rights reserved.
# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.
# ----------------------------------------------------------------

import os
import sys
pluginDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pluginDir)

from RegexList import *
from LauncherAPI import *
from QueryPlugin import *
from QueryDebug import *