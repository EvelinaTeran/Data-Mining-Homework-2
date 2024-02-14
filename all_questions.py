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
    
    p_c0_parent = 5/10 #Probability of class 0 (No lung cancer) in the parent node
    p_c1_parent = 5/10 #Probability of lass 1 (Lung cancer) in the parent node
    
    # Calculate entropy for the parent node
    entropy_parent = u.calculate_entropy(p_c0_parent, p_c1_parent)
    
    entropy_smoking = -5/10 * (1/5 * u.log2(1/5) + 4/5 * u.log2(4/5)) - 5/10 * (4/5 * u.log2(4/5) + 1/5 * u.log2(1/5))
    info_gain_smoking = entropy_parent - entropy_smoking

    
    entropy_cough = -7/10 * (4/7 * u.log2(4/7) + 3/7 * u.log2(3/7)) - 3/10 * (1/3 * u.log2(1/3) + 2/3 * u.log2(2/3))
    info_gain_cough = entropy_parent - entropy_cough
   
        
    entropy_radon = -2/10 * ( 2/2 * u.log2(2/2)) - 8/10 * (5/8 * u.log2(5/8) + 3/8 * u.log2(3/8))    
    info_gain_radon = entropy_parent - entropy_radon
       
    
    entropy_weight_loss = -5/10 * (2/5 * u.log2(2/5) + 3/5 * u.log2(3/5)) - 5/10 * (3/5 * u.log2(3/5) + 2/5 * u.log2(2/5))
    info_gain_weight_loss = entropy_parent - entropy_weight_loss

    

    
    level1["smoking"] = 1.
    level1["smoking_info_gain"] = info_gain_smoking

    level1["cough"] = -1.
    level1["cough_info_gain"] = -1.

    level1["radon"] = -1.
    level1["radon_info_gain"] = -1.

    level1["weight_loss"] = -1.
    level1["weight_loss_info_gain"] = -1.
    
    
    radon_left_gain = -4/5 * (3/4 * u.log2(3/4) + 1/4 * u.log2(1/4)) - 1/4 * (1 * u.log2(1) + 0 )
    
    
    cough_left_gain = -4/5 * (4/4 * u.log2(4/4) + 0) - 1/4 * (1 * u.log2(1) + 0 )
    
    
    weight_left_gain = -3/5 * (2/3 * u.log2(2/3) + 1/3 * u.log2(1/3)) - 2/5 * (1 * u.log2(1) + 0 )
    

    level2_left["smoking"] = -1.
    level2_left["smoking_info_gain"] = -1.
    level2_right["smoking"] = -1.
    level2_right["smoking_info_gain"] = -1.

    level2_left["radon"] = 1.
    level2_left["radon_info_gain"] = radon_left_gain

    level2_left["cough"] = -1.
    level2_left["cough_info_gain"] = -1.

    level2_left["weight_loss"] = -1.
    level2_left["weight_loss_info_gain"] = -1.

    
    cough_right_gain = -2/5 * (1/2 * u.log2(1/2) + 1/2 * u.log2(1/2)) - 3/5 * (1 * u.log2(1) + 0 )
   
    
    weight_right_gain = -3/5 * (1/3 * u.log2(1/3) + 2/3 * u.log2(2/3)) - 2/5 * (1 * u.log2(1) + 0 )
    
    
    level2_right["radon"] = -1.
    level2_right["radon_info_gain"] = -1.

    level2_right["cough"] = -1.
    level2_right["cough_info_gain"] = -1.

    level2_right["weight_loss"] = 1.
    level2_right["weight_loss_info_gain"] = weight_right_gain
    
    
    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    def construct_tree():
        tree = u.BinaryTree("Smoking Tobacco")
        A = tree.insert_left("Radon Exposure")
        B = tree.insert_right("Weight Loss")
        A.insert_left("Lung Cancer")
        A.insert_right("No Lung Cancer")
        B.insert_left("Lung Cancer")
        B.insert_right("No Lung Cancer")
        
        training_error = 5/10
        return tree, training_error

    # Fill up `construct_tree``
    tree, training_error = construct_tree()
      # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 5/10

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    prob_A = .3*.3 + .4*.8
    prob_B = .2*.2 + .6*.7
    prob_C = .3*.3 + .2*.2
    
    entropy_entire = -(prob_A*u.log2(prob_A) + prob_B*u.log2(prob_B) + prob_C*u.log2(prob_C))
    
    # Answers are floats
    answer["(a) entropy_entire_data"] = entropy_entire
    
    # x <= .2
    probA_R1 = 0
    probB_R1 = (.2*.2 + .6*.2) / (.2)
    probC_R1 = (.2*.2) / .2
    
    entropy_R1 = -.2 *(probB_R1*u.log2(probB_R1) + probC_R1*u.log2(probC_R1))
    
    probA_R2 = (.4*.8 + .3*.3) / .8
    probB_R2 = (.6*.5) / .8
    probC_R2 = (.3*.3) / .8
    
    entropy_R2 = -.8* (probA_R2*u.log2(probA_R2) + probB_R2*u.log2(probB_R2) + probC_R2*u.log2(probC_R2))
    
    entropy_x_leq_2 = entropy_R1 + entropy_R2
    
    info_gain_x_leq_2 = entropy_entire - entropy_x_leq_2
    
    # x <= .7
    probA_R1 = .4*.5/.7
    probB_R1 = (.2*.2 + .6*.7)/.7
    probC_R1 = .2*.2/.7
    
    entropy_R1 = -.7*(probA_R1*u.log2(probA_R1) + probB_R1*u.log2(probB_R1) + probC_R1*u.log2(probA_R1))
    
    probA_R2 = (.4*.3 + .3*.3) / .3
    probB_R2 = 0
    probC_R2 = .3*.3/.3
    
    entropy_R2 = -.3*(probA_R2*u.log2(probA_R2) + 0 + probC_R2*u.log2(probA_R2))
    
    entropy_x_leq_7 = entropy_R1 + entropy_R2
    
    info_gain_x_leq_7 = entropy_entire - entropy_x_leq_7
    
    # y <= .6
    probA_R1 = .8*.4/.4
    probB_R1 = .2*.2/.4
    probC_R1 = .2*.2/.4
    
    entropy_R1 = -.4*(probA_R1*u.log2(probA_R1) + probB_R1*u.log2(probB_R1) + probC_R1*u.log2(probA_R1))
    
    probA_R2 = .3*.3/.6
    probB_R2 = .7*.6/.6
    probC_R2 = .3*.3/.6
    
    entropy_R2 = -.6*(probA_R2*u.log2(probA_R2) + 0 + probC_R2*u.log2(probA_R2))
    
    entropy_y_leq_6 = entropy_R1 + entropy_R2
    
    info_gain_y_leg_6 = entropy_entire - entropy_y_leq_6
    
    # Infogain
    answer["(b) x <= 0.2"] = info_gain_x_leq_2
    answer["(b) x <= 0.7"] = info_gain_x_leq_7
    answer["(b) y <= 0.6"] = info_gain_y_leg_6

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y <= .6")
    A = tree.insert_left(" x <= .7")
    B = tree.insert_right("x <= .2")
    A.insert_left("B")
    C = A.insert_right("y <= .3")
    C.insert_left("A")
    C.insert_right("C")
    B.insert_right("A")
    D = B.insert_left("y <= .8")
    D.insert_left("C")
    D.insert_right("B")
    
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
    answer["a, level 1"] = "y <= .4"
    answer["a, level 2, right"] ="x <= .5"
    answer["a, level 2, left"] = "A"
    answer["a, level 3, left"] = "B"
    answer["a, level 3, right"] = "A"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    
    expected_error = .2*.3 
    answer["b, expected error"] = expected_error

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("y <= .4")
    tree.insert_left("A")
    A = tree.insert_right("x <= .5")
    A.insert_left("B")
    A.insert_right("A")
    
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    id_entropy_before_split = -((10/20)*u.log2(10/20) + (10/20)*u.log2(10/20))
    id_entropy_after_split = 0
    id_info_gain = id_entropy_before_split - id_entropy_after_split
    
    handedness_entropy_before_split = -((10/20)*u.log2(10/20) + (10/20)*u.log2(10/20))
    handedness_entropy_left = -((9/10)*u.log2(9/10) + (1/10)*u.log2(1/10))
    handedness_entropy_right = -((1/10)*u.log2(1/10) + (9/10)*u.log2(9/10))
    handedness_entropy_after_split = (10/20)*handedness_entropy_left + (10/20)*handedness_entropy_right
    handedness_info_gain = handedness_entropy_before_split - handedness_entropy_after_split
    
    answer["a, info gain, ID"] = id_info_gain
    answer["b, info gain, Handedness"] = handedness_info_gain

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    
    id_split_info = -((10/20)*u.log2(10/20) + (10/20)*u.log2(10/20))
    id_gain_ratio = id_info_gain / id_split_info
    
    handedness_split_info = -((10/20)*u.log2(10/20) + (10/20)*u.log2(10/20))
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

