def get_num_of_characters(inputStr):
    count = 0
    for i in range(0,len(inputStr)):
        count+=1
    return count
def output_without_whitespace(inputStr):
    inputStr = inputStr.replace(' ', '')
    return inputStr
    
if __name__ == '__main__':
    inputStr = input('Enter a sentence or phrase: ')
    print()
    print('You entered:', inputStr)
    print()
    print('Number of characters:', get_num_of_characters(inputStr))
    print('String with no whitespace:', output_without_whitespace(inputStr))
