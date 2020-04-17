with open("kolejna_praca/plikdo1.py","a") as example:
    example.write("\nBeunos dias hombre")
    example.close()

with open("kolejna_praca/plikdo1.py","r") as example:
    for cos in example:
        print(cos, end="")
    example.close()