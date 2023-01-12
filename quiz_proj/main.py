# class User:
#     def __init__(self, userId, userName):
#         self.id = userId
#         self.userName = userName
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user1 = User(1,"Joey")
# user2 = User(2, "Jack")
# user1.follow(user2)
# print(user1.id, user1.userName, user1.followers, user1.following)

from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_1 = Quiz(question_bank)
quiz_1.run_questions()
quiz_1.get_results()