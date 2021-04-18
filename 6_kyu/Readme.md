_____multiples_of_3_or_5_____

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
    
    Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)
_____Build a pile of Cubes_____

    Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
    
    You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
    
    The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
    Examples:
    
    findNb(1071225) --> 45
    
    findNb(91716553919377) --> -1
