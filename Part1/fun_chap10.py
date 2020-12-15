#the text in ''' ...''' is called text annotation

def count_words(file_name):
    '''calculate the number of words that exist in a file'''
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        ##msg = "Sorry, the file " + file_name + " does not exsit."
        ##print(msg)
        pass
    else:
        words = contents.split()
        print("The file " + file_name + " has " + str(len(words)) + " words")