docs = input()
search = input()

count = 0
start = 0

while start < len(docs) - len(search) + 1:
    if docs[start:start+len(search)] == search:
        count += 1
        start += len(search)
    else:
        start += 1

print(count)