# -*- encoding: utf-8

import io

import pytest

import filecmp2


def test_file_is_same_as_itself(tmpdir):
    path = tmpdir.join("greeting.txt")
    path.write(b"hello world")

    assert filecmp2.cmp_path_contents(path1=path, path2=path)
    assert filecmp2.cmp_stat(path1=path, path2=path)
    assert filecmp2.cmp_same_file(path1=path, path2=path)


def test_different_files_are_different(tmpdir):
    path1 = tmpdir.join("greeting.txt")
    path1.write(b"hello world")

    path2 = tmpdir.join("name.txt")
    path2.write(b"lexie")

    assert not filecmp2.cmp_path_contents(path1=path1, path2=path2)
    assert not filecmp2.cmp_stat(path1=path1, path2=path2)
    assert not filecmp2.cmp_same_file(path1=path1, path2=path2)


def test_two_files_with_equal_contents_match_contents_but_not_same(tmpdir):
    path1 = tmpdir.join("greeting1.txt")
    path1.write(b"hello world")

    path2 = tmpdir.join("greeting2.txt")
    path2.write(b"hello world")

    assert filecmp2.cmp_path_contents(path1=path1, path2=path2)
    assert filecmp2.cmp_stat(path1=path1, path2=path2)
    assert not filecmp2.cmp_same_file(path1=path1, path2=path2)


def test_comparing_contents_of_file_object_to_itself():
    f = io.BytesIO(b"hello world")

    with pytest.raises(ValueError, match="f1 and f2 are the same stream"):
        filecmp2.cmp_file_contents(f, f)


def test_can_compare_equal_file_like_objects():
    f1 = io.BytesIO(b"hello world")
    f2 = io.BytesIO(b"hello world")

    assert filecmp2.cmp_file_contents(f1, f2)


def test_can_compare_equal_file_like_objects_which_are_text():
    f1 = io.StringIO(u"hello world")
    f2 = io.StringIO(u"hello world")

    assert filecmp2.cmp_file_contents(f1, f2)


def test_mixed_binary_and_text_objects_are_different():
    f1 = io.BytesIO(b"hello world")
    f2 = io.StringIO(u"hello world")

    assert not filecmp2.cmp_file_contents(f1, f2)


def test_compares_large_files():
    # The current buffer used by ``cmp_file_contents`` is 8192 bytes; make sure
    # we can detect differences beyond the end of the first buffer.
    common_prefix = b"padding123" * 8200

    f1 = io.BytesIO(common_prefix + b"1")
    f2 = io.BytesIO(common_prefix + b"2")

    assert not filecmp2.cmp_file_contents(f1=f1, f2=f2)
