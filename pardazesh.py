import re

def Processing_sentence(sentence):
    return sentence.split()


def find_max(ls):
    _max_ = max(ls)
    for i in range(len(ls)):
        if ls[i] == _max_:
            return i

def check_command():
    user_exit = True
    while user_exit:
        entry = input('Please Enter Command').replace('"', '')
        if '-r' in entry:
            # print(1)
            if len(re.findall('(-r|-nr) [A-Z:a-z_]*.(png|jpg|jpeg|gif) edit (grayscale|negative|blackandwhite|contour|edgeenhance|emboss|findedges|blur|smooth)* [a-z]*', entry)) != 0:
                # print(2)
                user_exit = False
        else:
            if '/' in (entry.split()[1]).split('.')[0] or (
                    '_' in (entry.split()[1]).split('.')[0] or '-' in (entry.split()[1]).split('.')[0] or '(' in (entry.split()[1]).split('.')[0] or ')' in (entry.split()[1]).split('.')[0]):
                if len(re.findall('-nr [^,;]+.(png|jpg|jpeg|gif) edit (grayscale|negative|blackandwhite|contour|edgeenhance|emboss|findedges|blur|smooth)* [a-z]*',
                                  entry)) != 0:
                    user_exit = False
    return user_exit, Processing_sentence(entry)

def recommender(word, options):
    p = []
    word = word.strip()
    for option in options:
        t = 0
        for letter in option.strip():
            if letter in word:
                t += 1
        p.append(t / len(option))

    return options[find_max(p)]


#def Check_command(command):
    #image_address =

#print(recommender('negabla', ['grayscale', 'negative', 'blackandwhite']))
#print(find_max([1.0, 1.625, 0.46153846153846156]))