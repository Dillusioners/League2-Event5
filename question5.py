#A Python Program to Check If Two Strings are Anagram
def check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")
check(s1, s2)
