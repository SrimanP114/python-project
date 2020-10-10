haystack = input("Enter a word\n")
needle = input("Enter a word to search:\n")
a = len(needle)
b = len(haystack)
if needle in haystack:
    needle = list(needle)
    haystack = list(haystack)
    for x in range(b-1):
        if needle[0:a] == haystack[x : a]:
            print(x)
            break
        a = a + 1
else:
    print(-1)
