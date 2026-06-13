from fractions import Fraction 
import sys

# input your values below. (e.g. 3a + 5b = 5, so we have [3, 5, 5])
a = [2, 2, 3]
b = [2, 6, 2]

b_ot = [1,1,1]

if a[0] == 0:
    try:
        b_ot = [a1 / a[1] for a1 in a]
    except ZeroDivisionError as e:
        print('Invalid linear equation:', e)
        sys.exit()
    a = b
if b[0] == 0:
    try:
        b_ot = [b1 / b[1] for b1 in b]
    except ZeroDivisionError as e:
        print('Invalid linear equation:', e)
        sys.exit()
    
def first():
    if b_ot[0] == 0:
        coef_1 = a[1] / b_ot[1]
        b_1 = [b * coef_1 for b in b_ot]
        b_1 = [b_1 - a for a, b_1 in zip(a, b_1)]
        try:
            b_ans = [b / b_1[0] for b in b_1]
        except ZeroDivisionError as e:
            print('Invalid linear equation:', e)
            sys.exit()
        return b_ans
    else:
        coef_1 = a[0] / b[0]
        b_1 = [b * coef_1 for b in b]
        b_1 = [b_1 - a for a, b_1 in zip(a, b_1)]
        try:
            b_ans = [b / b_1[1] for b in b_1]
        except ZeroDivisionError as e:
            print('Invalid linear equation:', e)
            print('Another possible reasons is that two lines provided are parallel or they are dependent to each other.')
            sys.exit()
        return b_ans

def second():
    b_ans = first()
    if b_ans[1] == 0:
        pass
    else:
        coef_2 = a[1] / b_ans[1]
        b_fa = [b_ans * coef_2 for b_ans in b_ans]
        a_1 = [a - b_fa for a, b_fa in zip(a, b_fa)]
        a_ans = [a / a_1[0] for a in a_1]
        return a_ans

def answer(list_num):
    return [str(Fraction(num).limit_denominator()) for num in list_num]

def fred(ya, yo):
    print(answer(ya))
    print(answer(yo))
    print(f"a = {Fraction(ya[2]).limit_denominator()}\nb = {Fraction(yo[2]).limit_denominator()}")

ax = second()
bx = first()

if b_ot[0] == 0:
    fred(bx, b_ot)
else:
    fred(ax, bx)
