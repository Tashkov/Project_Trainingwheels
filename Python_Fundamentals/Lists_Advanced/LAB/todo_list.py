line = input()
notes = [0] * 20

while line != "End":
    todo_note = line.split("-")
    importance = int(todo_note[0])
    task = todo_note[1]
    notes.insert(importance, task)
    line = input()
result = []
for element in notes:
    if element != 0:
        result.append(element)
print(result)