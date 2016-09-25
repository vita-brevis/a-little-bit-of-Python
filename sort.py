def insertion_sort(bom):
    for j in range(1, len(bom)):
        key = bom[j]
        i = j - 1
        while i >= 0 and key < bom[i]:
            bom[i+1] = bom[i]
            i -= 1
        bom[i+1] = key

    return bom

if __name__ == "__main__":
    bom = [10, 5, 2, 9, 4, 8, 9, 2, 1]
    print insertion_sort(bom)
