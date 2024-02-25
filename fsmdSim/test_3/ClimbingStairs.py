import sys


def loopCountStairs(n):
    finalStep = 0

    if n <= 2:
        finalStep = n
        return finalStep

    prev2 = 1
    prev1 = 2
    currentStairNumber = 2
    while True:
        if currentStairNumber >= n:
            break

        next = prev1 + prev2
        prev2 = prev1
        prev1 = next
        finalStep = next

        currentStairNumber += 1

    return finalStep

if __name__ == '__main__':
    if len(sys.argv[0]) < 1:
        raise Exception('Stairs number must be given as a parameter.')
    print(loopCountStairs(2))
