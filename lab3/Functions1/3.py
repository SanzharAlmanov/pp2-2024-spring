def farm(heads, legs):
    rab = (legs - (2 * heads))//2
    chick = heads - rab
    print("chicken =", chick, "rabbits =", rab)
farm(35, 94)