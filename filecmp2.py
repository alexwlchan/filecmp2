#!/usr/bin/env python
# -*- encoding: utf-8

import filecmp
import os


def cmp_file_contents(f1, f2):
    """
    Returns True if the contents of the file-like objects ``f1`` and ``f2``
    are the equal.

    That is, they return the same bytes/text when calling ``read()``.

    Passing in the same file-like object twice is an error.

    """
    # Handle the case where the same stream has been handed in twice.
    #
    # Although they arguably contain the same contents; you can't call
    # read() on them both and get the same bytes/text.  It's probably a
    # sign something has gone wrong, so throw an error.
    if f1 is f2:
        raise ValueError("f1 and f2 are the same stream! %r" % f1)

    # Should this be configurable?
    buffer_size = 8192

    while True:
        buffer1 = f1.read(buffer_size)
        buffer2 = f2.read(buffer_size)
        if buffer1 != buffer2:
            return False

        # Both files are exhausted and there's nothing left to read.
        if not buffer1:
            return True


def cmp_path_contents(path1, path2):
    """
    Returns True if the files at path ``path1`` and ``path2``
    have the same contents.

    That is, the files both contain the same bytes.
    """
    with open(path1, "rb") as f1, open(path2, "rb") as f2:
        return cmp_file_contents(f1, f2)


def cmp_stat(path1, path2):
    """
    Returns True if the os.stat() signature of ``path1`` and
    ``path2`` are the same.
    """
    return filecmp.cmp(path1, path2, shallow=True)


def cmp_same_file(path1, path2):
    """
    Returns True if ``path1`` and ``path2`` point to the same file on disk;
    False if not.
    """
    return os.path.samefile(path1, path2)
