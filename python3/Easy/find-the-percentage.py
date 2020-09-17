# solution of the find the percentage challenge 

if __name__=='__main__':
    n = int(input()) 
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() 
        score = list(map(float, line))
        student_marks[name] = score
    query_name = input()    
    avg = 0 
    for key in student_marks.keys():
        keyy = str(key)
        if query_name == student_marks[keyy]:
            some = student_marks[keyy]
    print(sum/len(some))          
