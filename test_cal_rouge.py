from cal_rouge import test_rouge, rouge_results_to_str

if __name__ == "__main__":
    c = ["1 2 3 4", "1 2 3 4", "1 2 3 4", "1 2 3 4"]
    r = ["4 3 2 1", "4 3 2 1", "4 2 3 1", "4 2 3 1"]
    p = 2
    results = test_rouge(c, r, p)
    print(rouge_results_to_str(results))
