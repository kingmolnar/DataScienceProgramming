from solution_4_2 import find_most_frequent_word

def test_4_2():
    sentences = [
    "Sarah asked her friend to lend her a book for her upcoming trip",
    "In the midst of the storm, the sailors battled the raging sea",
    "She wondered if she should call her sister, as she hadn't heard from her in days"
    ]
    output = [('her', 3), ('the', 4), ('she', 3)]

    for i in range(len(sentences)):
        assert find_most_frequent_word(sentences[i]) == output[i], f"Output is incorrect for testcase {i+1}"
