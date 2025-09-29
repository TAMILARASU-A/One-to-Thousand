"""Anagram_Check"""
str1=input("Enter the 1st string:")
str2=input("Enter the 2nd string:")

if len(str1)!=len(str2):
    print("The given strings are not an Anagram...!")
elif sorted(str1)==sorted(str2):
    print("The given strings are Anagram...!")
