



student_tuples = [
        ['john', 'A', 15,1],
        ['jane', 'B', 12,8],
        ['dave', 'B', 10,4],
]

result = sorted(student_tuples, key=lambda a: a[3]) 

print(result)
