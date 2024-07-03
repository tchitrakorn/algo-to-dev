def largesum(numbers):
    # where numbers is a list of strings of each number
    if (len(numbers) == 0):
        return 0
    
    # create a placeholder for the sum at each digit's position across all numbers
    max_length = max(len(number) for number in numbers)
    sum_per_digit = [0] * max_length

    for number in numbers:
        # read the number from the back and treat the right-most digit as the first one (0th index in sum_per_digits)
        for i in range(len(number)-1, -1, -1):
            digit_index = len(number)-1 - i
            sum_per_digit[digit_index] += int(number[i])
    
    # now sum_per_digit is of order from left to right, left most is the smallest

    actual_sum = ""
    carry_over = 0
    # get the actual sum of every number by processing each digit one at a time
    for i in range(len(sum_per_digit)):
        sum_per_digit[i] += carry_over
        # remainder of each digit can be directly added to actual_sum
        remainder = str(sum_per_digit[i] % 10)
        actual_sum += remainder
        # each digit position may have carry over that must be rolled over to the next digit
        carry_over = sum_per_digit[i] // 10

    # now we need to consider the case that there is still carry-overs tha exceeds the number of digits.
    while carry_over > 0:
        remainder = str(carry_over % 10)
        actual_sum += remainder
        carry_over = carry_over // 10

    # actual_sum must be reversed as it is a conventional way for numeric values (reading from right-most to left-most)
    return int(actual_sum[::-1]) # calling int to get rid of leading zeroes
    


 

if __name__ == "__main__":

    file = open('input.txt', 'r')
    lines = file.readlines()
    numbers = [line.strip() for line in lines]

    fullsum = largesum(numbers)
    fullsumstr = str(fullsum)
    print("Full sum: " + fullsumstr)

    if(len(fullsumstr) >= 10):
        print("First 10 digits: " + fullsumstr[:10])

    else:
        print("First 10 digits: " + fullsumstr)
        