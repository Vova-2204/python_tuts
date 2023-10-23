inputPrompt = "Enter todo: "
tasksList = []

while True:
  todo = input(inputPrompt)
  if(todo == "exit"):
    break
  tasksList.append(todo)
  print(tasksList)
  print("Next")