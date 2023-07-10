# Joshua Soto
# 1553869

txt = input()
split_txt = txt.split()
join_txt = ''.join(split_txt)
rev_txt = join_txt[::-1]
if rev_txt == join_txt:
    print(txt, 'is a palindrome')
else:
    print(txt, 'is not a palindrome')
