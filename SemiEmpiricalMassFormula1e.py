import numpy as np

def semiEmpMassFormula(A, Z):
    '''Semi-Empirical Mass Formula: Computes binding energy B
        for an atomic nucleus with atomic number Z and mass number A'''
    bindingEnergy = volumeTerm(A)-surfaceTerm(A)-coulombTerm(A,Z)-asymmetryTerm(A,Z)+pairingTerm(A,Z)
    return bindingEnergy

def is_even(number):
    '''Determines if a number is even or odd'''
    if number%2==0: #number is even
        return True
    else:
        return False

def find_a5(A,Z):
    '''Determines value of a5 depending on even-ness of A and Z'''
    if A == False:
        return 0
    elif A==True and Z==True:
        return 12.0
    elif A==True and Z==False:
        return -12.0   

def volumeTerm(A):
    '''Computes the volume term value based on a1, A
    returns the value of the term'''
    a1=15.8 #in MeV
    value = a1*A
    return value 

def surfaceTerm(A):
    '''Computes the surface term value based on a2, A
    returns the value of the term'''
    a2=18.3 #in MeV
    value = a2* A**(2/3)
    return value 

def coulombTerm(A,Z):
    '''Computes the coulomb term value based on a3, A, Z
    returns the value of the term'''
    a3=0.714 #in MeV
    value = a3*(Z**2/A**(1/3))
    return value 

def asymmetryTerm(A,Z):
    '''Computes the asymmetery term value based on a4, A, Z
    returns the value of the term'''
    a4=23.2 #in MeV
    value = a4*((A - 2*Z)**2/A)
    return value 

def pairingTerm(A,Z):
    '''Computes the pairing term value based on A, Z
    returns the value of the term'''
    a5 = find_a5(is_even(A), is_even(Z))
    value = a5/A**(1/2)
    return value   

def findMaxZ(experimentalData):
    '''Finds the last atomic mass number in an array'''
    maxZ = len(experimentalData)
    return maxZ

if __name__ == "__main__":
    '''
    '''
    experimentalData = np.loadtxt('nuclear_data.txt', dtype=int, usecols=(0,1))
    maxZ = findMaxZ(experimentalData)
    
    data = np.zeros((maxZ, 3), float) #initialize data array to print to with zeros
    
    for step in range(0,(maxZ)):
        Z = experimentalData[step,0].item() #initialize Z
        A = experimentalData[step, 1].item()
        
        bindingEnergyPerNucleon = semiEmpMassFormula(A, Z)/A
            
        data[(step), 0] = Z #append Z to data
        data[(step), 1] = A #append A to data array
        data[(step), 2] = bindingEnergyPerNucleon
        
    np.savetxt('aidansNuclearData.txt', data, delimiter=' ', header='Z,A,Energy/Nucleon')
    