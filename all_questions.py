# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 0.
    level1["smoking_info_gain"] = 0.

    level1["cough"] = 0.
    level1["cough_info_gain"] = 0.

    level1["radon"] = 0.
    level1["radon_info_gain"] = 0.

    level1["weight_loss"] = 0.0
    level1["weight_loss_info_gain"] = 0.

    level2_left["smoking"] = 0.
    level2_left["smoking_info_gain"] = 0.
    level2_right["smoking"] = 0.
    level2_right["smoking_info_gain"] = 0.

    level2_left["radon"] = 0.
    level2_left["radon_info_gain"] = 0.

    level2_left["cough"] = 0.
    level2_left["cough_info_gain"] = 0.

    level2_left["weight_loss"] = 0.
    level2_left["weight_loss_info_gain"] = 0.

    level2_right["radon"] = 0.
    level2_right["radon_info_gain"] = 0.

    level2_right["cough"] = 0.
    level2_right["cough_info_gain"] = 0.

    level2_right["weight_loss"] = 0.
    level2_right["weight_loss_info_gain"] = 0.

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # (a)
    p_c0 = 10/20 
    p_c1 = 10/20
    
    overall_gini = 1 - (p_c0**2 + p_c1**2)
    
    # (b) = 0.0
    
    # (c)
    m_p_c0 = 6/10
    m_p_c1 = 4/10
    
    f_p_c0 = 4/10
    f_p_c1 = 6/10
    
    male_gini = 1 - (m_p_c0**2 + m_p_c1**2)
    female_gini = 1 - (f_p_c0**2 + f_p_c1**2)
      
    gender_gini = ((10/20) * male_gini) + ((10/20) * female_gini)
    
    # (d)
    fam_p_c0 = 1/4 
    fam_p_c1 = 3/4
    
    sport_p_c0 = 8/8
    sport_p_c1 = 0/8
    
    lux_p_c0 = 1/7
    lux_p_c1 = 7/8
    
    gini_family = 1 - (fam_p_c0**2 + fam_p_c1**2)
    gini_sports = 1 - (sport_p_c0**2 + sport_p_c1**2)
    gini_luxury = 1 - (lux_p_c0**2 + lux_p_c1**2)    
    
    car_type_gini = ((4/20) * gini_family) + ((8/20) * gini_sports) + ((8/20) * gini_luxury)
    
    # (e)
    small_p_c0 = 3/5
    small_p_c1 = 2/5
    
    med_p_c0 = 3/7
    med_p_c1 = 4/7
    
    large_p_c0 = 2/4
    large_p_c1 = 2/4
    
    xl_p_c0 = 2/4
    xl_p_c1 = 2/4
    
    small_gini = 1 - (small_p_c0**2 + small_p_c1**2)
    med_gini = 1 - (med_p_c0**2 + med_p_c1**2)
    large_gini = 1 - (large_p_c0**2 + large_p_c1**2)
    xl_gini = 1 - (xl_p_c0**2 + xl_p_c1**2)
    
    
    shirt_type_gini = ((5/20)*small_gini) + ((7/20)*med_gini) + ((4/20)*large_gini) + ((4/20)*xl_gini)
    
    # float
    answer["(a) Gini, overall"] = overall_gini

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = gender_gini
    answer["(d) Gini, Car type"] = car_type_gini
    answer["(e) Gini, Shirt type"] = shirt_type_gini

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car Type has the lowest Gini index so splitting by this attribute will result in better separation of classes"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    # I am not sure on this one because technically this is ordinal as well
    answer["a"] = ['binary', 'qualitative', 'nominal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Binary because it is either AM or PM. Nominal because AM and PM don't have an order unless we know which came first (chicken or the egg problem). And qualitative because its a label."

    answer["b"] = ['continuous', 'quantitative', 'ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete', 'qualitative', 'ordinal']
    answer["c: explain"] = "I choose discrete because I assumed that people would be based brightness off of a set of options like (low, medium, high), however, it could also be continuous if they were using something like a sliding scale to judge the brightness."

    answer["d"] = ['continuous', 'quantitative', 'interval']
    answer["d: explain"] = ""

    answer["e"] = ['discrete', 'qualitative', 'ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continuous', 'quantitative', 'interval']
    answer["f: explain"] = ""

    answer["g"] = ['discrete', 'quantitative', 'ratio']
    answer["g: explain"] = ""

    answer["h"] = ['discrete', 'qualitative', 'nominal']
    answer["h: explain"] = ""

    answer["i"] = ['discrete', 'qualitative', 'ordinal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete', 'qualitative', 'ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continuous', 'quantitative', 'ratio']
    answer["k: explain"] = ""

    answer["l"] = ['continuous', 'quantitative', 'ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete', 'qualitative', 'nominal']
    answer["m: explain"] = ""

    return answer

# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Since the accuracy for Model 2 is on the testing set, I would prioritize its performance over the model run on the training set. Especially since we are interested in seeing how it performs on unseen data."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 1"
    explain["b explain"] = "When looking at the perfomance on the combined dataset, I would chose Model 1 because its higher accuracy shows that it has better generalization."

    explain["c similarity"] = ""
    explain["c similarity explain"] = "MDL and pessimistic error both penalize overly complex models to ensure better generalization and avoid overfitting."

    explain["c difference"] = ""
    explain["c difference explain"] = "A key difference is in the model selection process. MDL trys to find the simplest model that best explains the data by minimizing the combined length of the model and data descriptions. On the other hand, pessimistic error estimates a model's generalization error by considering complexity of the modela dn size of the training dataset. It does not explicitly minimize a description length."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    id_entropy_before_split = -((10/20)*log2(10/20) + (10/20)*log2(10/20))
    id_entropy_after_split = 0
    id_info_gain = id_entropy_before_split - id_entropy_after_split
    
    handedness_entropy_before_split = -((10/20)*log2(10/20) + (10/20)*log2(10/20))
    handedness_entropy_left = -((9/10)*log2(9/10) + (1/10)*log2(1/10))
    handedness_entropy_right = -((1/10)*log2(1/10) + (9/10)*log2(9/10))
    handedness_entropy_after_split = (10/20)*handedness_entropy_left + (10/20)*handedness_entropy_right
    handedness_info_gain = handedness_entropy_before_split - handedness_entropy_after_split
    
    answer["a, info gain, ID"] = id_info_gain
    answer["b, info gain, Handedness"] = handedness_info_gain

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    
    id_split_info = -((10/20)*log2(10/20) + (10/20)*log2(10/20))
    id_gain_ratio = id_info_gain / id_split_info
    
    handedness_split_info = -((10/20)*log2(10/20) + (10/20)*log2(10/20))
    handedness_gain_ratio = handedness_info_gain / handedness_split_info
    
    # answer is a float
    answer["d, gain ratio, ID"] = id_gain_ratio
    answer["e, gain ratio, Handedness"] = handedness_gain_ratio

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

