import numpy as np
import pandas as pd
import jinja2

do_q = True
question_number = 10
file_name = "Testing4"

um = "um"
i = "i"
in_ = "in"
ma = "ma"
mag = "mag"
na = "na"
nag = "nag"
an = "an"
hin = "hin"
ni = "ni"
ini = "ini"

tense_array = []
vowels = ["a","e","i","o","u"]
vowel_check = []

# Some Tagalog verbs have conjugation rules that have no standard. A bank 
# has been made to correctly conjugate all those tagalog rarities/oddities. 
# IN VERBS
hin_verb_bank = ["sisi","sesanti","sabi", "bura"]
ni_verb_bank = ["linis","yakup","nakaw"]
# I VERBS
ini_verb_bank = ["luto", "hain", "labas", "bigay", "hatid", "lista", "hulog", "lubog", "unat"]

# tense_array, 2d Array, will be appended to
# root_verb, string
# variations, list[strings], (um, ma, mag, in, i verb types)
def add_tense_words(tense_array, root_verb, variations, meanings):
    for (l, verb_type) in enumerate(variations):
        if verb_type == um:
            tense_array.append(np.hstack([root_verb, um, meanings[l], make_um_verb(root_verb)]))
        if verb_type == in_:
            tense_array.append(np.hstack([root_verb, in_, meanings[l], make_in_verb(root_verb)]))
        if verb_type == ma:
            tense_array.append(np.hstack([root_verb, ma, meanings[l], make_ma_verb(root_verb)]))
        if verb_type == mag:
            tense_array.append(np.hstack([root_verb, mag, meanings[l], make_mag_verb(root_verb)]))
        if verb_type == i:
            tense_array.append(np.hstack([root_verb, i, meanings[l], make_i_verb(root_verb)]))

# MAKES DIFFERENT TYPES OF TAGALOG VERBS
def make_um_verb(root_verb):
    for (j,vowel) in enumerate(vowels):
        if root_verb.find(vowels[j]) == 0:
            return [um+root_verb, um+root_verb, um+vowel+root_verb, vowel+root_verb]
    list_verb = list(root_verb)
    return [list_verb[0] + um + "".join(list_verb[1:]), list_verb[0] + um + "".join(list_verb[1:]), list_verb[0] + um + list_verb[1] + root_verb, "".join(list_verb[0:2]) + root_verb]

# TODO: Convert O's to U's in the right circumstances
def make_in_verb(root_verb):
    for (j,vowel) in enumerate(vowels):
        if root_verb.find(vowel) == 0:
            # Check for banked verbs
            for (k,banked_verb) in enumerate(hin_verb_bank):
                if root_verb == banked_verb:
                    return [root_verb + hin, in_ + root_verb, in_ + list_verb[0] + root_verb, list_verb[0] + root_verb + hin]
            list_verb = list(root_verb)
            # Check for the O -> U verbs
            
            if list_verb[-2] == "o":
                root_verb_u = "".join(list_verb[0:-2]) + "u" + list_verb[-1]
                return [root_verb_u + in_, in_ + root_verb, in_ + list_verb[0] + root_verb, list_verb[0] + root_verb_u + in_]
            elif list_verb[-1] == "o":
                root_verb_u = "".join(list_verb[0:-1]) + "u"
                return [root_verb_u + in_, in_ + root_verb, in_ + list_verb[0] + root_verb, list_verb[0] + root_verb_u + in_]
            return [root_verb + in_, in_ + root_verb, in_ + list_verb[0] + root_verb, list_verb[0] + root_verb + in_]
        
    list_verb = list(root_verb)
    # Check for banked verb
    for (k,banked_verb) in enumerate(hin_verb_bank):
        if root_verb == banked_verb:
            return [root_verb + hin, list_verb[0] + in_ + "".join(list_verb[1:]), list_verb[0] + in_ + list_verb[1] + root_verb, "".join(list_verb[0:2]) + root_verb + hin]
    for (k,banked_verb) in enumerate(ni_verb_bank):
        if root_verb == banked_verb:
            return [root_verb + in_, ni + root_verb, ni + "".join(list_verb[0:2]) + root_verb, "".join(list_verb[0:2]) + root_verb + in_]
    # Check for the O -> U verbs
    if list_verb[-2] == "o":
        return ["".join(list_verb[0:-2]) + "u" + list_verb[-1] + in_,  list_verb[0] + in_ + "".join(list_verb[1:]), list_verb[0] + in_ + list_verb[1] + root_verb, "".join(list_verb[0:2]) + "".join(list_verb[0:-2]) + "u" + list_verb[-1] + in_]
    elif list_verb[-1] == "o":
        return ["".join(list_verb[0:-1]) + "u" + in_,  list_verb[0] + in_ + "".join(list_verb[1:]), list_verb[0] + in_ + list_verb[1] + root_verb, "".join(list_verb[0:2]) + "".join(list_verb[0:-1]) + "u" + in_]
    return [root_verb + in_, list_verb[0] + in_ + "".join(list_verb[1:]), list_verb[0] + in_ + list_verb[1] + root_verb, "".join(list_verb[0:2]) + root_verb + in_]

def make_ma_verb(root_verb):
    list_verb = list(root_verb)
    return [ma + root_verb, na + root_verb, na + "".join(list_verb[0:2]) + root_verb, ma + "".join(list_verb[0:2]) + root_verb]

def make_mag_verb(root_verb):
    list_verb = list(root_verb)
    return [mag + root_verb, nag + root_verb, nag + "".join(list_verb[0:2]) + root_verb, mag + "".join(list_verb[0:2]) + root_verb]

def make_i_verb(root_verb):
    list_verb = list(root_verb)
    # for (j,root) in enumerate(ini_verb_bank):
    #     if root_verb == root:
    #         # Check for the O -> U verbs
    #         if list_verb[-2] == "o":
    #             return ["".join(list_verb[0:-2]) + "u" + list_verb[-1] + in_,  list_verb[0] + in_ + "".join(list_verb[1:]), list_verb[0] + in_ + list_verb[1] + root_verb, "".join(list_verb[0:2]) + "".join(list_verb[0:-2]) + "u" + list_verb[-1] + in_]
    #         elif list_verb[-1] == "o":
    #             return ["".join(list_verb[0:-1]) + "u" + in_,  list_verb[0] + in_ + "".join(list_verb[1:]), list_verb[0] + in_ + list_verb[1] + root_verb, "".join(list_verb[0:2]) + "".join(list_verb[0:-1]) + "u" + in_]
    #         else:
    #             return [i + root_verb, i + list_verb[0] + in_ + "".join(list_verb[1:]), i + list_verb[0] + in_ + list_verb[1] + root_verb, i + "".join(list_verb[0:2]) + root_verb]
    for (j,vowel) in enumerate(vowels):
        if root_verb.find(vowel) == 0:
            return [i + root_verb, ini + root_verb, ini + list_verb[0] + root_verb, i + list_verb[0] + root_verb]
    
    return [i + root_verb, i + list_verb[0] + in_ + "".join(list_verb[1:]), i + list_verb[0] + in_ + list_verb[1] + root_verb, i + "".join(list_verb[0:2]) + root_verb]

# TESTING
# print(make_um_verb("kain"))
# print(make_um_verb("inom"))
# print(make_in_verb("kain"))
# print(make_in_verb("init"))
# print(make_in_verb("linis"))
# print(make_in_verb("sabi"))
# print(make_mag_verb("lakad"))
# print(make_ma_verb("ligo"))
# print(make_in_verb("ayos"))
# print(make_in_verb("sundo"))
# print(make_in_verb("ako"))
# print(make_i_verb("kulong"))
# print(make_i_verb("unat"))
# print(make_in_verb("inom"))

if do_q == True:
    tag_df = pd.read_csv("Tagalog.csv")

    for x in range(0,len(tag_df)):
        add_tense_words(tense_array,tag_df["Verb"][x],[tag_df["Type 1"][x], tag_df["Type 2"][x], tag_df["Type 3"][x]],[tag_df["English 1"][x], tag_df["English 2"][x], tag_df["English 3"][x]])

    tenses = ["Root","Verb Type", "Meaning", "Infinitive", "Past", "Present", "Future"]
    tense_frame = pd.DataFrame(np.array(tense_array), columns=tenses)
    print(tense_frame)

    # Generate 5 Questions
    question_list = []

    for x in range(0,question_number):
        print("QUESTION {}".format(x+1))
        question = np.random.randint(0, len(tense_frame))
        print("What does " + tense_frame["Root"][question] + " mean? Type: " + tense_frame["Verb Type"][question])
        answer1 = input()
        print("Answer: " + tense_frame["Meaning"][question] + "\n")
        question_tense = np.random.randint(0,4)
        print("What is the " + tenses[3+question_tense] + " tense of " + tense_frame["Root"][question])
        answer2 = input()
        print("\n")
        print("Use " + tense_frame.iloc[question, 3+question_tense] + " in a sentence.")
        answer3 = input()
        print("\n")
        question_list.append(np.hstack([tense_frame["Root"][question], tense_frame["Verb Type"][question], tense_frame["Meaning"][question], answer1, tense_frame.iloc[question, 3+question_tense], answer2, answer3]))

    question_columns = ["Root Verb", "Verb Type", "Meaning", "Attempted Meaning", "Tense", "Attempted Tense", "Attempted Sentence"]
    # print(question_list)
    question_frame = pd.DataFrame(np.array(question_list), columns=question_columns)
    print(question_frame)
    print("\n\n\n")
    # print(question_frame.to_latex(index=False,
    #                   formatters={"name": str.upper},
    #                   float_format="{:.1f}".format,
    # ))
    question_frame.to_csv(file_name + ".csv")

    
    







