def main():
    
    plist = []
    
    inputInteger1 = int(input('Enter the starting integer: '))
    inputInteger2 = int(input('Enter the ending integer: '))
            
    if inputInteger1 <= 1 or inputInteger2 <= 1 or inputInteger2 < inputInteger1:
        print('Value Error')
    else:
        for i in range(inputInteger1, inputInteger2 + 1):
            countValue = 0
            for j in range(2, i):
                if i % j == 0:
                    countValue = countValue + 1
                    break
            if countValue == 0:
                plist.append(i)
    print(plist)
            
    
    
    return plist


if __name__ == '__main__':
    main()
