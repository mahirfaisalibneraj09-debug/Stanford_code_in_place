import random

def main():
    print("Khansole Academy")
    correct=0
    while correct!=3:
        x =random.randint(10, 100) 
        y =random.randint(10, 100)
        print(f"What is {x} + {y}?")
        ans=int(input("Your answer: "))
        if ans==x+y:
            print("Correct!")
            correct+=1
            print(f"You've gotten {correct} correct in a row. ")
        else:
            print("Incorrect.")
            print(f"The expected answer is {x+y}")

    
    
    
if __name__ == '__main__':
    main()