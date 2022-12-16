s = input()
t = input()

sorted_s = sorted(s)
sorted_t = sorted(t, reverse=True)

print('Yes') if sorted_s < sorted_t else print('No')

