import random
import re

S, V, E = [list(map(str.lower, re.findall('[A-Z][a-z]*', x))) for x in ['BCDFGHJKLMNPRSTVWYZBlBrChClCrDrFlFrGhGlGnGrKnPhPlPrQuScShSkSlSmSnSpStThTrWhWrSchScrShmShrSquStrThr', 'AeAiAoAuEaEeEiEuIaIeIoOaOeOiOoOuUeUiAEIOU', 'BCDFGLMNPRSTXZBtChCkCtFtGhGnLbLdLfLkLlLmLnLpLtMbMnMpNkNgNtPhPtRbRcRdRfRgRkRlRmRnRpRtRvRzShSkSpSsStZzLchLshLthRchRshRstRthSchTch']]

def f(n, w=None):
    if w is None:
        w = random.choice(['', random.choice(S)])

    while n:
        e = random.choice(E)
        w += random.choice(V)[-(w[-1:] in V):] + random.choice([random.choice(S), e, e + random.choice([x for x in S if x[0]*2 != e])]) * (n > 1)
        n -= 1
    
    return (w + random.choice(['', e])).capitalize()

if __name__ == "__main__":
    print("With which letter/-s shall the name start?")
    print("No input is random.")
    start = input("> ")
    if start == "":
        start = None

    chosen = []
    while True:
        name = f(2, start) # random.choice(["", ""])
        inp = input(f"{name} [y|n|end]: ")
        if inp == "y":
            chosen.append(name)
        elif inp == "end":
            print("\n".join(chosen))
            filename = "chosen_names.txt"
            with open(filename) as file:
                file.writelines(chosen)
            print(f"Saved chosen namens in file {filename}")
            break

    input("Press any key to exit...")
