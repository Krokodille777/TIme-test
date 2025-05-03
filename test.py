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
    "9 + 10": 19,
    "12 x 3": 36,
    "15 - 7": 8,
    "24 / 6": 4,
    "15 + 72": 87,
    "8 x 9": 72,
    "100 - 25": 75,
    "-17 + 5": -12,
    "50 / 5": 10,
    "cos(90)": 0,
    "164 : 4": 41,
    "19 x 5": 95,
    "8 + 7": 15,
    "sqrt(225)": 15,
    "4^3": 64,
    "log(1000)": 3,
    "ln(e)": 1,
    "2.5 + 3.5": 6,
    "3.14 x 2": 6.28,
    "5.5 - 2.5": 3,
    "round(2.7)": 3,
    "floor(3.9)": 3,
    "ceil(2.1)": 3,
    "abs(-5)": 5,
    "abs(-3.5)": 3.5,
    "max(1, 2, 3)": 3,
    "min(1, 2, 3)": 1,
    "2^4 + 3^2": 25,
    "sqrt(16) + sqrt(9)": 7,
    "6!": 720,
    "2020 - 1990": 30,
    "1000 / 4": 250,
    "sqrt(100) + 5": 15,
    "log(10) + log(100)": 3,
    "72 / 8": 9,
    "sqrt(144)": 12,
    "sqrt(729)": 27,
    "round(16.1)": 16,
    "round(16.5)": 17,
    "25 + 27": 52,
    "50 - 25": 25,
    "10 x 10": 100,
    "20 / 4": 5,
    "2x + 3 = 11": "x = 4",
    "3x - 5 = 7": "x = 4",
    "3x(2 + 4) = 108": "x = 6",
    "2x + 3y = 12, y = 2": "x = 3",
    "x^2 + 4x + 4 = 0": "x = -2",
    "27 giga + 5 tera (1 giga = 1024 mega, 1 tera = 1024 giga). Gigas?": "5.027",
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
    print(f"Average time per question: {total_time/5:.2f} seconds".format(total_time / 5))



if __name__ == "__main__":
    main()
