# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

check = True

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not(x or y or z) != (not x) and (not y) and (not z):
                print('Не верно')
                check = False
                break
            
if check: print("Выражение верно")