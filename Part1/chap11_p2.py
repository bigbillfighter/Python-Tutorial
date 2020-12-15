#test class
import unittest

class AnonymousSurvey():
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


##question = "What language did you first learn to speak?"
##my_survey = AnonymousSurvey(question)

##my_survey.show_question()
##print("Enter 'q' to quit.\n")
##while True:
    ##reponse = input("Language:")
    ##if reponse == 'q':
        ##break
    ##my_survey.store_response(reponse)

##print("\nThank you for your survey!")
##my_survey.show_results()

class TestAnonymousSurvey(unittest.TestCase):
    def test_single_responce(self):
        question = "Waht language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    def test_three_question(self):
        question = "What language can you speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['C', 'Java', 'Python', 'Pascal']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

class TestAnonynousAnother(unittest.TestCase):
    def setUp(self):
        '''
        Use setUp method, and the object and variables built here can be used in any other function in the class
        The program will run setUp method first and then run other test methods
        And don't forget to use self to set up the object or the variable
        '''
        question = "What language can you speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'French']

    def test_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()


