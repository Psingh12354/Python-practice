from collections import Counter
s = 'lkseropewdssafsdfafkpwe'
print('original string'+s)
print('Most common elements are')
print(Counter(s).most_common(4))
