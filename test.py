import time
import random

test_dict = {
    "2 + 4": 6,
    "7 x 6": 42,
    "16 - 9": 7,
    "33 / 3": 11,
    "5 + 8": 13,
    "18 x 5 ": 90,
    "20 - 4": 16,
    "32 / 8": 4,
    "16^2": 256,
    "sqrt(49)": 7,
    "3^5": 243,
    "log(100)": 2,
    "sin(30)": 0.5,
    "1^10000": 1,
    "tan(45)": 1,
    "70 / 2": 35,
}


def random_test_question():
    question = random.choice(list(test_dict.keys()))
    answer = test_dict[question]
    return question, answer


def time_per_question():
    question, answer = random_test_question()
    print(f"Question: {question}")

    
    start_time = time.time()
    user_answer = input("Your answer: ")
    end_time = time.time()
    time_limit = 5  # seconds
    if end_time - start_time > time_limit:
        print("Time's up!")
        question, answer = random_test_question()
        return time_limit, 0
    
    elapsed_time = end_time - start_time
    score = 0
    
    if user_answer == str(answer):
        print("Correct!")
        score = 1
    else:
        print(f"Incorrect. The correct answer is {answer}.")
    
    print(f"Time taken: {elapsed_time:.2f} seconds")
    return elapsed_time, score



def main():
    total_score = 0
    total_time = 0
    
    for i in range(5):
        print(f"Question {i + 1}:")
        time_taken, question_score = time_per_question()
        total_score += question_score
        total_time += time_taken
        print("-" * 20)
        
        time.sleep(1) 
    
    print("Test completed!")
    print(f"Your score is: {total_score}/5")
    print(f"Your total time is: {total_time:.2f} seconds")
    print(f"Average time per question: {total_time/5:.2f} seconds".format(total_time / 5))



if __name__ == "__main__":
    main()
