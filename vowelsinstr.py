#Check Vowels and Consonants
n=eval(input("Enter the String"))
l=["a","e","i","o","u"]
for char in n:
    if char in l:
        print("{} is vowel",char)
    elif not char.isalpha():
        print("{} is number",char)
    else:
        print("{} is constants",char)
        
'''
Enter the String"HelloKrishna123"
{} is constants H
{} is vowel e
{} is constants l
{} is constants l
{} is vowel o
{} is constants K
{} is constants r
{} is vowel i
{} is constants s
{} is constants h
{} is constants n
{} is vowel a
{} is number 1
{} is number 2
{} is number 3
'''
