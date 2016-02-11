#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.2'


import cmd
import functools
import os
import sys

from polar import Device


__INTRO = """

 _|                                _|                  _|
 _|    _|_|      _|_|    _|_|_|    _|_|_|      _|_|    _|    _|_|
 _|  _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|_|_|_|
 _|  _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|
 _|    _|_|      _|_|    _|_|_|    _|    _|    _|_|    _|    _|_|_|
                         _|
                         _|
                                                           ver. {}
"""


def check_if_device_is_connected(f):
    """
    Decorator. Checks if device is connected before invoking function.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if args[0].device is not None:
            return f(*args, **kwargs)
        else:
            print '[!] Device disconnected.'
            print
    return wrapper


class LoopholeCli(cmd.Cmd):
    """ Loophole command line interface class. """

    __PROMPT = 'loophole({})>'

    def __init__(self):
        """Constructor.
        """
        cmd.Cmd.__init__(self)
        self.prompt = LoopholeCli.__PROMPT.format('no device')
        self.device = None
    # end-of-method __init__

    def do_exit(self, _):
        """Quit.
        """
        if self.device is not None:
            self.device.close()
        sys.exit(0)
    # end-of-method do_exit

    def do_list(self, _):
        """List available Polar devices.
        """
        devs = Device.list()

        if len(devs) > 0:
            for i, dev in enumerate(devs):
                print '{} - {} ({})'.format(i, dev.product_name, dev.serial_number)
        else:
            print '[!] No Polar devices found!'

        print
    # end-of-method do_list

    def do_connect(self, dev_no):
        """Connect Polar device. Run 'list' to see available devices.
        """
        try:
            dev_no = int(dev_no)
            devs = Device.list()
            dev = devs[dev_no]

            self.prompt = LoopholeCli.__PROMPT.format(dev.serial_number)
            self.device = Device(dev)

            print '[+] Device connected.'
            print
        except IndexError:
            print '[!] Device not found. Run \'list\' to see available devices.'
            print
    # end-of-method do_connect

    def do_disconnect(self, _):
        """Disconnect Polar device.
        """
        if self.device is not None:
            self.device.close()
            self.device = None
            self.prompt = LoopholeCli.__PROMPT.format('no device')
            print '[+] Device disconnected.'
            print
    # end-of-method do_disconnect

    @check_if_device_is_connected
    def do_get(self, line):
        """Read file from device.
Usage: get <src> <dest>
        """
        try:
            src, dest = line.strip().split()

            data = self.device.read_file(src)
            with open(dest, 'wb') as outfile:
                outfile.write(bytearray(data))

            print '[+] File \'{}\' saved to \'{}\''.format(src, dest)
            print
        except ValueError:
            print '[!] Invalid command usage.'
            print '[!] Usage: get <source> <destination>'
            print
    # end-of-method do_get

    def do_dump(self, path):
        """Dump device memory.
Usage: dump <path>
        """
        print '[+] Reading files tree...'
        dev_map = self.device.walk(self.device.SEP)

        for directory in dev_map.keys():
            fixed_directory = directory.replace(self.device.SEP, os.sep)
            full_path = os.path.abspath(os.path.join(path, fixed_directory[1:]))

            if not os.path.exists(full_path):
                os.makedirs(full_path)

            d = dev_map[directory]
            files = [e for e in d.entries if not e.name.endswith('/')]
            for file in files:
                with open(os.path.join(full_path, file.name), 'wb') as fh:
                    print '[+] Dumping {}{}'.format(directory, file.name)
                    data = self.device.read_file('{}{}'.format(directory, file.name))
                    fh.write(bytearray(data))

        print '[+] Device memory dumped.'
        print
    # end-of-method do_dump

    @check_if_device_is_connected
    def do_info(self, _):
        """Print connected device info.
        """
        info = self.device.get_info()
        for k, v in info.items():
            print '{:>20s} - {}'.format(k, v)
        print
    # end-of-method do_info

    @check_if_device_is_connected
    def do_walk(self, path):
        """Walk file system.
Usage: walk [path]
        """
        if not path.endswith('/'):
            path += '/'

        fs = self.device.walk(path)
        keyz = fs.keys()
        keyz.sort()

        for k in keyz:
            print k
            d = fs[k]
            files = [e for e in d.entries if not e.name.endswith('/')]
            files.sort()
            for f in files:
                print '{}{} ({} bytes)'.format(k, f.name, f.size)

        print
    # end-of-method do_walk

    pass
# end-of-class Loophole


def main():
    cli = LoopholeCli()
    cli.cmdloop(__INTRO.format(__version__))
# end-of-function main


##
#  Entry point
if __name__ == '__main__':
    main()