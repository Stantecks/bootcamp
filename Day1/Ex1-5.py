def parens(dotpar):
    """Checks dot-parenthesis for valid number of open/close parens"""
    return dotpar.count('(') == dotpar.count(')')


def dotparen_to_bp(dotpar):
    # Declare variables
    openpar = []
    closepar = []
    mylist = []
    mytuple = ()
    # USE ENUMERATE!!!!!!!!
    for i in range(0, len(dotpar)):
        if dotpar[i] == '(':
            openpar += str(i)
        elif dotpar[i] == ')':
            closepar += str(i)
    i = 0
    count = len(openpar)
    while i < count:
        mytuple = (openpar.pop(0), closepar.pop())
        mylist.append(mytuple)
        i += 1
    return tuple(mylist)


def valid_parenbp(seq, a, wobble=True):
    if wobble is True:
        return seq[a[0]] + seq[a[1]] in ('GC', 'CG', 'AT', 'TA', 'GU', 'UG')
    else:
        return seq[a[0]] + seq[a[1]] in ('GC', 'CG', 'AT', 'TA')


def sterics(dotparen):
#   Need to calulate a difference between two coordinates
#    if '(..)' in dotparen:
#        return False

def rna_ss_validator(seq, sec_struc, wobble=True):
    if parens(sec_struc) == False:
        return False
    if sterics(sec_struc) == False:
        return False
    for i in range(0, len(dotparen_to_bp(sec_struc))):
        print(valid_parenbp(*dotparen_to_bp(sec_struc)[i]))
    return True

rna_ss_validator('GCAUCUAUGC', '(((....)))')
sterics('(((....)))')
