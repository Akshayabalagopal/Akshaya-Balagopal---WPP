def method(answer, search_word, replace_word):

    if search_word in answer:
        index=answer.rindex(search_word)
    else:
        index=-1
    print("Index: ",index)

    split=answer.rsplit( )
    print("Split: ", split)

    find=answer.rfind(search_word)
    print("Find: ", find)

    replace=answer.replace(search_word, replace_word)
    print("Replace: ",replace)

    count=answer.count(search_word)
    print("Count: ",count)

sample_answer=input("Enter the string: ")
search_for=input("Enter the word: ")
replace_with=input("Enter the word: ")

method(sample_answer, search_for, replace_with)