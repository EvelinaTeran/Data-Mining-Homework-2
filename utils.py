import math
import pickle


def log2(x):
    return math.log(x, 2)

def save_dict(filenm, dct):
    with open(filenm, "wb") as file:
        pickle.dump(dct, file)


# Loading from a pickle file
def load_dict(filenm, dct):
    with open(filenm, "rb") as file:
        loaded_data = pickle.load(file)
        return loaded_data
    raise "load_dict:: Error loading data"


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
            return self.left
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node
            return new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
            return self.right
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node
            return new_node

    def __repr__(self):
        return f"BinaryTree({self.value})"

    def __str__(self, level=0):
        ret = "\t" * level + repr(self) + "\n"
        if self.left is not None:
            ret += self.left.__str__(level + 1)
        if self.right is not None:
            ret += self.right.__str__(level + 1)
        return ret

    def print_tree(self):
        print(self.__str__())

# Function to compute entropy (Evelina made)     
def entropy(class_labels):
    class_counts = {}
    for label in class_labels:
        if label not in class_counts:
            class_counts[label] = 0
        class_counts[label] += 1
    entropy_val = 0
    total_samples = len(class_labels)
    for count in class_counts.values():
        probability = count / total_samples
        entropy_val -= probability * log2(probability)
    return entropy_val


# Function to calculate information gain
def information_gain(data, atrribute_index, target_index):
    total_entropy = entropy([row[target_index] for row in data])
    attribute_values = set([row[attribute_index] for row in data])
    attribute_entropy = 0
    total_samples = len(data)
    for value in atrribute_values:
        subset = [row for row in data if row[attribute_index] == value]
        subset_entropy = entropy([row[target_index] for row in subset]) * len(subset) / total_samples
        attribute_entropy += subset_entropy
    return total_entropy - attribute_entropy

# Example on how to create a binary tree
# A has two children: B and C
# B has two children: D and E
# C has two children: F and G
# Construct the binary tree:
def construct_binary_tree():
    root = BinaryTree("A")
    root.insert_left("B")
    root.insert_right("C")
    root.left.insert_left("D")
    root.left.insert_right("E")
    root.right.insert_left("F")
    root.right.insert_right("G")
    return root

def calculate_entropy(p_c0, p_c1):
    if p_c0 == 0 or p_c1 == 0:
        return 0
    return - (p_c0 * math.log2(p_c0) + p_c1 * math.log2(p_c1))

def calculate_information_gain(p_c0_parent, p_c1_parent, p_c0_left, p_c1_left, p_c0_right, p_c1_right):
    entropy_parent = calculate_entropy(p_c0_parent, p_c1_parent)
    weight_left = p_c0_left + p_c1_left
    weight_right = p_c0_right + p_c1_right
    entropy_left = calculate_entropy(p_c0_left, p_c1_left)
    entropy_right = calculate_entropy(p_c0_right, p_c1_right)
    information_gain = entropy_parent - ((weight_left * entropy_left + weight_right * entropy_right) / (weight_left + weight_right))
    return information_gain
