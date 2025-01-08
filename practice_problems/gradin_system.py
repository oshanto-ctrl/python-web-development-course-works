"""
Grade System Using List Comprehension
Problem Statement:
You are given a list of scores, and you need to determine the corresponding grade for
each score based on the following grading system:
• A: 90 and above
• B: 80-89
• C: 70-79
• D: 60-69
• F: below 60
Using list comprehension, generate a new list where each score is replaced by its
corresponding grade.
Input Format: A list of integers, scores [], where each integer represents a score.
Output Format: A list of strings, where each string is the grade corresponding to the score
in the input list.
Example:
Input:
scores = [95, 67, 85, 78, 50, 91, 88, 72, 60]
Output:
 ['A', 'D', 'B', 'C', 'F', 'A', 'B', 'C', 'D']
Explanation:
• Score 95 → Grade A (because 95 ≥ 90)
• Score 67 → Grade D (because 60 ≤ 67 < 70)
• Score 85 → Grade B (because 80 ≤ 85 < 90)
• Score 78 → Grade C (because 70 ≤ 78 < 80)
• Score 50 → Grade F (because 50 < 60)
• Score 91 → Grade A (because 90 ≤ 91 < 100)
• Score 88 → Grade B (because 80 ≤ 88 < 90)
• Score 72 → Grade C (because 70 ≤ 72 < 80)
• Score 60 → Grade D (because 60 ≤ 60 < 70) 
"""
scores = [95, 67, 85, 78, 50, 91, 88, 72, 60]
# • A: 90 and above
# • B: 80-89
# • C: 70-79
# • D: 60-69
# • F: below 60
result_categories = ['A' if 90 <= score <= 100 else
                     'B' if 80 <= score <= 89 else
                     'C' if 70 <= score <= 79 else
                     'D' if 60 <= score <= 69 else
                     'F' if 0 <= score <= 59 else "Invallid Score"
                     for score in scores
                    ]

print(result_categories)