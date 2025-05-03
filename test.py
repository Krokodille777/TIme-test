import time
import random

test_dict ={
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
    score = 0
    start_time = time.time()
    question, answer = random_test_question()
    print(f"Question: {question}")
    user_answer = input("Your answer: ")
    end_time = time.time()
    elapsed_time = end_time - start_time
    if user_answer == str(answer):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {answer}.")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    return elapsed_time, score

for i in range(5):
    print(f"Question {i + 1}:")
    time_per_question()
    print("-" * 20)
    
    time.sleep(1)  # Adding a small delay between questions for better readability
print("Test completed!")


print ("Your score is: ")
print (score)
print ("Your time is: ")
print (elapsed_time)
