//A program to Sort Words in Alphabetic Order.
String = input("Enter the sentence you want to sort")
while String == "":
    String = input("Enter your sentence again correctly")


def sorter(word_given):
    word_list = word_given.split()
    word_list.sort()

    print("The Words which have been sorted are: ")

    for word in word_list:
        print(word, " ")


sorter(String)
