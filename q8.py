prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: prompt_b

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): prompt_b gives the AI a clear role ("data analyst"), setting the tone and expertize level of a response, and helps the AI understand the context and what is expected. This clarity can lead to more accurate and relevant responses.
# Your answer (Reason 2): prompt_b breaks down the task into clear, numbered steps, which makes it easier for the AI to follow exactly what to do and in what order, leading to a more structured and comprehensive response.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: prompt_a provides a real-world scenario, including the team involved (a marketing manager addressing a CEO), the background of the task and a clearer understanding of the deadline (prompt_b only highlighted a presentation on Friday, not specifically next Friday), which helps the AI understand the business setting and tone of the presentation.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer:The real-world context and clearer deadline from prompt_a can be borrowed to enhance prompt_b. This will provide the AI with a better understanding of the business setting and urgency of the task, which can help it generate a more tonally relevant executive summary as opposed to just following the steps.

prompt_improved = """
Role: You are a data analyst helping a retail marketing team.
Context: We have just completed a three-month campaign and need to present 
findings to our CEO next Friday.
Task: Analyse customer survey data from the campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Constraints: Keep the summary concise and free of technical jargon.
"""