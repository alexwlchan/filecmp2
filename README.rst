filecmp2
========

If you say "two files are the same", you could mean at least three different things:

*  *The files have the same os.stat() signature.*
   (This is the shallow copy done by ``filecmp.cmp()``.)

*  *The files have the same contents. They're byte-for-byte identical.*

*  *They're the same files on disk (modulo hard links).*

You can compare files with `filecmp <https://docs.python.org/3/library/filecmp.html>`_
or `os <https://docs.python.org/3/library/os.html>`_, but it's not always obvious what
sort of comparison you're doing.

Since `explicit is better than implicit <https://www.python.org/dev/peps/pep-0020/>`_,
filecmp2 provides three functions so you can be clear about what you mean by "same":

.. code-block:: python

   def cmp_path_contents(path1, path2):
       """
       Returns True if the files at paths ``path1`` and ``path2``
       have the same contents.
       """


   def cmp_stat(path1, path2):
       """
       Returns True if the os.stat() signature of ``path1`` and ``path2``
       are the same.
       """


   def cmp_same_file(path1, path2):
       """
       Returns True if ``path1`` and ``path2`` point to the same file on disk.
       """

If you have two file-like objects, you can also compare their contents with
``cmp_contents``:

.. code-block:: pycon

   >>> import filecmp2
   >>> import io

   >>> b1 = io.BytesIO(b"hello world")
   >>> b2 = io.BytesIO(b"hello world")
   >>> filecmp2.cmp_contents(b1, b2)
   True

   >>> b1 = io.BytesIO(b"hello world")
   >>> b2 = io.BytesIO(b"the cheese shop")
   >>> filecmp2.cmp_contents(b1, b2)
   False

This is useful if you're dealing with streams that you don't want to write to disk.

I wrote this after discovering that I was using ``filecmp.cmp()`` wrong, and doing
a shallow copy instead of checking the contents of the files.  I don't find the
current API very clear, and reading the Python bug tracker suggests I'm not the only
person who's made this mistake.  Although the docs explain the distinction, it's
lost on somebody who's casually reading the code or reviewing without the docs.

Installation
************

Install from PyPI (``pip install filecmp2``), or copy the single file directly
into your codebase.

License
*******

MIT.
