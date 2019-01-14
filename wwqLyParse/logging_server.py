#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>

if __name__ == "__main__":
    # try:
    #     from gevent import monkey
    #
    #     monkey.patch_all()
    #     del monkey
    # except Exception:
    #     gevent = None
    import os
    import sys

    _srcdir = os.path.dirname(os.path.realpath(__file__))
    _filepath = os.path.dirname(sys.argv[0])
    sys.path.insert(0, os.path.join(_filepath, _srcdir))

    print(sys.path)
    del sys
    del os

import sys
import os
import logging

LEVEL = logging.INFO
FORMAT = '%(asctime)s{%(name)s}%(filename)s[line:%(lineno)d]<%(funcName)s> pid:%(process)d %(threadName)s %(levelname)s : %(message)s'
DATA_FMT = '%H:%M:%S'
logging.basicConfig(level=LEVEL, format=FORMAT, datefmt=DATA_FMT, stream=sys.stderr)

from common import *
import asyncio

asyncio_helper.patch_logging()


def _handle(data):
    print(data.decode("utf-8"))


# async def test():
#     address_logging = ADDRESS_LOGGING
#     logging.info("listen address:'%s'" % address_logging)
#     aps = AsyncConnectionServer(ADDRESS_LOGGING, _handle, run_directly=True)
#     await aps.run_async()
#
#
# def main():
#     asyncio_helper.run_in_main_async_loop(test()).result()
#
#     threading.main_thread().join()


def main():
    address_logging = ADDRESS_LOGGING
    logging.info("listen address:'%s'" % address_logging)
    ConnectionServer(address_logging, _handle).run()


if __name__ == "__main__":
    asyncio_helper.start_main_async_loop_in_main_thread(main)
