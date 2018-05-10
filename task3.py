"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

def rec_sum(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0] + rec_sum(lista[1:])




if __name__ == "__main__":
    niz = [1,3,4,2,5]
    print(rec_sum(niz))

