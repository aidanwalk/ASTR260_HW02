def semiEmpMassFormula(A, Z):
    '''Semi-Empirical Mass Formula: Computes binding energy B
        for an atomic nucleus with atomic number Z and mass number A'''
    bindingEnergy = volumeTerm(A)-surfaceTerm(A)-coulombTerm(A,Z)-asymmetryTerm(A,Z)+pairingTerm(A,Z)
    return bindingEnergy

def is_even(number):
    '''Determines if a number is even or odd'''
    if number%2==1: #number is odd
        return False
    else:
        return True
    
def find_a5(A,Z):
    '''Determines value of a5 depending on even-ness of A and Z'''
    if A == False:
        return 0
    elif A==True and Z==True:
        return 12.0
        
def volumeTerm(A):
    '''Computes the volume term value based on a1, A'''
    a1=15.8 #in MeV
    value = a1*A
    return value 

def surfaceTerm(A):
    '''Computes the surface term value based on a2, A'''
    a2=18.3 #in MeV
    value = a2* A**(2/3)
    return value 

def coulombTerm(A,Z):
    '''Computes the coulomb term value based on a3, A, Z'''
    a3=0.714 #in MeV
    value = a3*(Z**2/A**(1/3))
    return value 

def asymmetryTerm(A,Z):
    '''Computes the asymmetery term value based on a4, A, Z'''
    a4=23.2 #in MeV
    value = a4*((A - 2*Z)**2/A)
    return value 

def pairingTerm(A,Z):
    '''Computes the pairing term value based on A, Z'''
    a5 = find_a5(is_even(A), is_even(Z))
    value = a5/A**(1/2)
    return value     

if __name__ == "__main__":
    Z=28
    maxBindingEnergyPerNucleon = -10000 
    for s in range(1,4):
        A = Z*s
        bindingEnergyPerNucleon = semiEmpMassFormula(A, Z)/A
        if maxBindingEnergyPerNucleon < bindingEnergyPerNucleon:
            maxBindingEnergyPerNucleon = bindingEnergyPerNucleon
            stableA = A
        
    print("The most stable nucleus is mass number: ", stableA)
    print("With a binding energy per nucleon of: ", maxBindingEnergyPerNucleon)


