# wi, the wheel installer 

This is a package installer for Python wheel packages. For more information
about wheels, please refer to https://pythonwheels.com/

Besides making the package installation process much faster, wheels allow
you to get rid of a building env on your servers, tools such as compilers
and dev libraries will not be required anymore if all of your dependencies
has wheel packages available.

Speaking of packages available, this tool is an attempt to motivate authors
of libs, frameworks and tools to release their packages in the wheel format.

Please note that this tool isn't a replacement for pip. If you have deps
that don't have wheels package available, you will still have to use pip.

However, this tool makes it easy to fallback to pip when the wheel packages
are not found.

## No idle time

This tool is based on asyncio, in such a way that while packages are being
downloaded, the tool will perform the installation of packages already
downloaded.

## Installation

    $ pip install wi

## Usage

If your packages are listed in a _requirements.txt_ file, you can just run:

    $ wi

If the packages are on a file other than _requirements.txt_, then you should
specify the file path as the sole argument to the command. For example:

    $ wi requirements-staging.txt

The command above will search for wheel packages for every entry in the file.
In case no package is found, the command will output to stdout the package
name and version, in the format _package==version_, meaning you can redirect
the stdout to pip as a fallback for installing the missing packages:

    $ wi | xargs pip install --no-deps

## Demonstration

    (wi) root@personal:~# pip uninstall -y -r requirements.txt &>/dev/null
    (wi) root@personal:~# time pip install --no-cache-dir --no-deps \
       -r requirements.txt &>/dev/null

    real	0m46.714s
    user	0m40.575s
    sys	0m3.077s
    (wi) root@personal:~# pip uninstall -y -r requirements.txt &>/dev/null
    (wi) root@personal:~# time wi &>/dev/null
    
    real	0m2.315s
    user	0m1.680s
    sys	0m0.404s
    
## Contributions

Contributions are welcome. Given this is just the start, the tool is missing
lots of cool stuff. If you have time and are willing to contribute, just
open a ticket and let's discuss it there!

It is also important to share this tool so we can advance with the current
status os python wheels and pip itself.

## Running tests

Minimal tests are present runing tox

    $ pip install tox
    $ tox
