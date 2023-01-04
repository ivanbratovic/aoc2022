import numpy as np

test = False

def read_input():
    global test
    filename = "inputs/day08-input.txt"
    if test:
        filename = "inputs/day08-test.txt"
    with open(filename, "r") as file:
        return np.array(list(map(lambda x: list(map(int, x.strip())), file.readlines())))



def get_visible_trees_onesided(trees):
    visible_trees = np.zeros_like(trees)
    scores_trees = np.ones_like(trees)
    for i, row in enumerate(trees):
        tallest = max(row)
        edge = row[0]
        visible_trees[i][0] = 1
        last_seen = [0] * 10
        for j, tree in enumerate(row):
            if tree > edge and tree < tallest:
                visible_trees[i][j] = 1
                edge = tree
            scores_trees[i][j] = abs(j - max(last_seen[tree:])) 
            last_seen[tree] = j
            if tree == tallest:
                visible_trees[i][j] = 1
    return visible_trees, scores_trees

def get_visible_trees(trees):
    return get_visible_trees_onesided(trees)[0] \
        |  np.rot90(get_visible_trees_onesided(np.rot90(trees, 1))[0], 3) \
        |  np.rot90(get_visible_trees_onesided(np.rot90(trees, 2))[0], 2) \
        |  np.rot90(get_visible_trees_onesided(np.rot90(trees, 3))[0], 1),\
            get_visible_trees_onesided(trees)[1] \
        *  np.rot90(get_visible_trees_onesided(np.rot90(trees, 1))[1], 3) \
        *  np.rot90(get_visible_trees_onesided(np.rot90(trees, 2))[1], 2) \
        *  np.rot90(get_visible_trees_onesided(np.rot90(trees, 3))[1], 1)

def main():
    trees = read_input()
    visible, scores = get_visible_trees(trees)
    print(sum(sum(visible)))
    print(np.max(scores))

if __name__ == "__main__":
    main()