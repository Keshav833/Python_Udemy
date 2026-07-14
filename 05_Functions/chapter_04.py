def change( ):
    name = "Keshu" #local Scope
    print(f"Inside the function local scope: {name}")

name = "kishan" #global Scope
change()
print(f"Outside the function global  scope: {name}")