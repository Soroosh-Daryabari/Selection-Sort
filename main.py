def selection_sort(List):
    for i in range(len(List)):
        lowest_value_index = i
        for j in range(i + 1, len(List)):
            if List[j] < List[lowest_value_index]:
                lowest_value_index = j
        List[i], List[lowest_value_index] = List[lowest_value_index], List[i]
    return List


if __name__ == "__main__":
    list_to_sort = [8, 7, 95, 10, 4, 3, 5, 22, 66, 98, 45, 47, 12, 23, 12, 444, 555859, 879774]
    sorted_list = selection_sort(list_to_sort)
    print(sorted_list)
