inp = input("Введите трёхзначное число: ")
if int(inp).isdigit() and len(str(inp)) == 2:
  print(str(inp[0] + inp[2] + inp[1]))
