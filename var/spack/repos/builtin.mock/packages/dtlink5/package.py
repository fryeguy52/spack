# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Dtlink5(Package):
    """Simple package which acts as a link dependency"""

    homepage = "http://www.example.com"
    url = "http://www.example.com/dtlink5-1.0.tar.gz"

    version("1.0", md5="0123456789abcdef0123456789abcdef")
