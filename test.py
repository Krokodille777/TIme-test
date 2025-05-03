import time
import random

test_dict = {
    "2 + 4": 6,
    "7 x 6": 42,
    "16 - 9": 7,
    "33 / 3": 11,
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
    
    elapsed_time = end_time - start_time
    score = 0
    
    if user_answer == str(answer):
        print("Correct!")
        score = 1
    else:
        print(f"Incorrect. The correct answer is {answer}.")
    
    print(f"Time taken: {elapsed_time:.2f} seconds")
    return elapsed_time, score


# Main code
def main():
    total_score = 0
    total_time = 0
    
    for i in range(5):
        print(f"Question {i + 1}:")
        time_taken, question_score = time_per_question()
        total_score += question_score
        total_time += time_taken
        print("-" * 20)
        
        time.sleep(1)  # Adding a small delay between questions for better readability
    
    print("Test completed!")
    print(f"Your score is: {total_score}/5")
    print(f"Your total time is: {total_time:.2f} seconds")
    print(f"Average time per question: {total_time/5:.2f} seconds".format(total_time / 5))


# Run the program
if __name__ == "__main__":
    main()
