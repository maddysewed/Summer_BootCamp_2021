import random
words = [['м','о','р','е'],['д','о','м'],['с','а','д'],['к','о','т'],['п','о','л','е'],['с','т','о','л'],['о','к','н','о'],['к','о','д'],['з','а','м','о','к'],['н','о','с'],['р','е','к','а'],['н','о','ч','ь'],['с','ы','н']]
a = random.choice(words)
b = list(a)
i = j = times = 0
for b[i] in b:
    b[i] = '_'
    print(b[i], end = ' ')
    i += 1
for times in range(10):
    i = j = k = 0
    letter = input('\nEnter a letter - ') 
	#список индексов одной буквы    
    cnt = []        
    if letter in a:
        for a[k] in a:
            if a[k] == letter:
                cnt += str(k)
            k += 1
        for cnt[j] in cnt:
            b[int(cnt[j])] = letter
        print(*b)
        if b == a:
            print('\nGOOD JOB')
            break
    else:
        print('There is no ' + letter)
    times += 1
if times == 10 and b != a:
    print('\nFalure =(\nThe right word was:', end = ' ')
    print(*a)
