import Problem1

p = Problem1.Problem()

while True:
  user_input = input("레벨을 입력하세요.(1~100) ")
  
  if user_input == "exit":
    n = 123
    break
  elif user_input.isdecimal() and 1 <= int(user_input) <= 100:
    n = int(user_input)
    break
  else:
    print("오류 잘못된 입력입니다.")

while n <= 100:
  print(f"레벨 {n}")
  
  user_input = input(f"{p.get_problem(n)} ")
  
  if user_input == "exit":
    break
  elif user_input == "hint1":
    print(p.get_hint(n, False))
  elif user_input == "hint2":
    print(p.get_hint(n, True))
  elif p.check_password(n, user_input):
    print("비밀번호가 맞습니다.")
    
    n += 1
  else:
    print("비밀번호가 틀립니다.")

if n != 123:
  print("플레이 해주셔서 감사합니다.")