This prac is a learning activity. Unlike some of the other pracs in the course, I haven’t given you set questions to
do. Instead, I have told you to make use of online resources and challenges that match your own level of understanding of programming. This prac has several important purposes: firstly, it helps me get an idea for the range
of programming levels in the class so I can adjust the course accordingly. Secondly, it teaches you to make use of
online resources to help teach yourself anything that you need to know. Thirdly, it helps you practice evaluating
online resources so you can use them more effectively.

Part 1 involves doing an online python tutorial and answering a set of questions about it. Part 2 involves doing 3
challenges and answering 5 questions about each. Part 3 is a written reflection on the activity.
Submit your answers as a pdf that answers all 5 questions for the tutorial for part 1, all 5 questions for each
challenge for part 2 and includes your written reflection for part 3. You may use any word processor you like (such
as google docs, libre office, or microsoft word) but you must convert your answer sheet to a pdf and submit it
using iKamva. At the top of your answer document you should clearly indicate your name and student number.
Your answer sheet should be named like this: <student_number>_prac1.pdf. So if your student number is 1234567,
your assignment answers should be named 1234567_prac1.pdf. Make sure your code is formatted correctly in your
answer sheet. Failure to correctly follow instructions will result in a loss of marks. There is a video on iKamva to
help you format your reports correctly.

This prac will count for marks. However, there are no right answers. All you have to do is attempt a tutorial
and a few challenges and report back honestly about how it went. For each part, you will receive full marks if you
answer every question and attempted the number of tutorials or challenges asked for, partial marks if you only
completed some of the tutorials or challenges asked for and no marks if you did not answer the question.
Enjoy the prac and remember you are welcome to ask for clarification or help on whatsapp or by email!

Part 1: Python Tutorial (15 marks)
3 marks per question
Choose one tutorial from https://www.learnpython.org/ that is on a topic you’re not familiar with yet. If
you have not yet used functions in python, you MUST choose the “functions” tutorial. If you’re already quite
comfortable with programming, choose a more advanced tutorial such as pandas, classes or modules.
Complete the tutorial and answer the following questions:
1. Title of tutorial
2. Roughly how long did the tutorial take
3. Do you feel you understand the concept?
4. Were you able to complete the exercise at the end?
5. Copy paste your code used to answer the exercise at the end (whether it was correct or not)
You should spend roughly 1 hour on this task. If while working you’re finding it’s taking you a very short or long
amount of time, select a different tutorial that matches your experience. This is important practice in self-learning.
Computational Physics
Solution:
#Part 1:Python Tutorial
# Create a list of weights in kg.
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2046

# Print out np_weight_lbs
print(np_weight_lbs)

Part 2: Challenges (15 marks)

1 mark per question, 5 marks per challenge
Create a free account on this website: https://edabit.com/. Select python and whatever difficulty level you
choose. Pick three challenges to complete that you judge will be difficult for you to do but you think you can
handle.
Unfortunately Edabit only lets you submit a maximum of five challenges for them to check. You can still
do as many challenges as you like and check them yourselves (for instance using the online platform https:
//trinket.io/python) but you’ll only be able to check you are correct using edabit for five challenges for the free
version. For this practical, it doesn’t matter whether you successfully complete the challenge, it only matters that
make a good attempt.
For each challenge answer the following questions:
1. Challenge title and difficulty level (as specified by the website)
2. Copy-paste the challenge instruction text
3. Copy-paste the code for your solution
4. Roughly how long did it take you to finish this challenge?
5. How difficult was it?
You should spend 1-2 hours on this task. If you’re finding it’s taking you too long or you’re getting through
exercises too quickly, change your difficulty level or select a different challenge. This is another lesson in how to
find the appropriate level of resource for your experience level.

Solution:
#Part 2:Challenges
def longest_alternating_substring(s):
    """
    Function to find the longest substring with alternating odd/even or even/odd digits.
    
    Args:
    s (str): A string of digits.

    Returns:
    str: The longest substring with alternating odd and even digits.
    """
    
    def is_odd(digit):
        """
        Helper function to check if a digit is odd.
        
        Args:
        digit (str): A single character representing a digit.

        Returns:
        bool: True if the digit is odd, False otherwise.
        """
        return int(digit) % 2 != 0
    
    def is_even(digit):
        """
        Helper function to check if a digit is even.
        
        Args:
        digit (str): A single character representing a digit.

        Returns:
        bool: True if the digit is even, False otherwise.
        """
        return int(digit) % 2 == 0

    # Initialize variables to keep track of the maximum length substring
    max_length = 0
    max_substring = ""
    start = 0  # Start index of the current alternating substring

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        # Check if the current digit alternates in parity with the previous digit
        if (is_odd(s[i]) and is_even(s[i - 1])) or (is_even(s[i]) and is_odd(s[i - 1])):
            # Continue the current alternating substring
            current_length = i - start + 1
        else:
            # End of the current alternating substring
            current_length = i - start
            # Check if the length of the current substring is greater than the max found so far
            if current_length > max_length:
                max_length = current_length
                max_substring = s[start:i]
            # Reset the start index for the next potential alternating substring
            start = i

    # After the loop, check the last substring from the last start index to the end of the string
    current_length = len(s) - start
    if current_length > max_length:
        max_length = current_length
        max_substring = s[start:]

    return max_substring

print(longest_alternating_substring("225424272163254474441338664823"))
print(longest_alternating_substring("594127169973391692147228678476")) 
print(longest_alternating_substring("721449827599186159274227324466")) 

Part 3: Reflection (15 marks)

15 marks for detailed and insightful reflection,
10 marks for a reflection of adequate length but insufficient detail,
5 marks if it is less than 100 words
Write a reflection of 100 words minimum about what you have learned from the tutorial and challenges. Also
discuss what you have learned about making use of online resources to improve your programming ability. Reflect
on your experience of choosing your own challenge level and tutorials and discuss how this type of independence
may be relevant in your career after university.

Solution:
Throughout the tutorial and challenges, I learned the importance of systematically
approaching problem-solving in programming. By breaking down a problem into manageable
steps and utilizing specific algorithms, I was able to write efficient and effective code. The
process highlighted the significance of understanding fundamental concepts and applying
them to real-world scenarios.
Using online resources proved invaluable; they offered diverse perspectives and solutions
that expanded my problem-solving toolkit. For example, exploring forums and
documentation deepened my understanding of various programming techniques and best
practices.
Choosing my own challenges and tutorials fostered a sense of independence and
self-directed learning. This autonomy is crucial for a career in programming, where
continuous self-improvement and adaptability are key. It encourages proactive
problem-solving and helps develop a personalized approach to learning, which will be
essential for tackling complex projects and staying current with technological advancements
in my future career.
