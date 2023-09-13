from solution_3_14 import copy_file


def test_3_14():
    
    src_filename1 = "../source1.txt"
    src_filename2 = "../source2.txt"
    dest_filename1 = "../destination1.txt"
    dest_filename2 = "../destination2.txt"
    test1 = "This is some sample content in the source file.\nYou can use this file for testing."
    test2 = "File not found."

    with open(src_filename1, 'w') as src_file:
        src_file.write(test1)
        
    copy_file(src_filename1, dest_filename1)
    with open(dest_filename1, 'r') as dest_file1:
        res1 = dest_file1.read()
    assert res1 == test1, "copy_file is not correct"
    #     copy_file(src_filename2, dest_filename2)
    #     with open(dest_filename2, 'r') as dest_file2:
    #         res2 = dest_file2.read()
    #     assert res2 == test2, "copy_file is not correct"
