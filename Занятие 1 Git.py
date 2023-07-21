s = input("Вводи своё слово:")
reverse = s[::-1]

def palindrom(s):
        if s[::1] == reverse:
            return True

        if s[::1] != reverse:
            return False
print (palindrom(s))



