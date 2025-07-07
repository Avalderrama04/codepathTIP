"""
Write a function nanana_batman() that accepts an integer x and 
prints the string "nanana batman!" where "na" is repeated x times.
Do not use the * operator

"""

def nanana_batman(x):
    """
    U- Understand 
        I - Inputs 
            x: int - the number of times we want to append "na" to "batman!"
        O - outputs
            None (shout print instead of return a value)
        C - constrains/considerations 
            - Cannot use the * to multiply the "na" prefix
            - when input is 0, be sure to not include the space
        E - Examples/ edge cases
            Examples:
                - nanana_batman(6) -> "nanananana batman!"
                - nanana_batman(0) -> "batman!"
                - nanana_batman(-3) -> None
            Edge cases:
                - Negative numbers ? ->
                - Zero ? -> "batman!"
    P- Plan
        1) Using a loop, append to a string, then return the string
            Steps:
                1. Define the empty string result
                2. Use a loop to concatenate "na" to the result string x times
                3. Append "batman!" to the result
                4. Print the result
        2) Using a list, append "na" to the list x times, then use ''.join() to merge the list, then append "batman!"

    I - imp

    
    """
    if x == 0:
        print("batman!")
        return 
    
    if x < 0:
        return None


    result = ""

    for _ in range(x): # 0 (inclusive) to x (exclusive)
        result += "na"
    result += " batman!"

    print(result)

nanana_batman(6)