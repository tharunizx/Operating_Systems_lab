def optimal_page_replacement(pages, capacity):
    frame = []
    page_faults = 0
    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < capacity:
                frame.append(pages[i])
            else:
                furthest_index = -1
                page_to_replace = -1
                for f in frame:
                    try:
                        index = pages[i+1:].index(f)
                    except ValueError:
                        index = float('inf')
                    if index > furthest_index:
                        furthest_index = index
                        page_to_replace = f
                frame.remove(page_to_replace)
                frame.append(pages[i])
            page_faults += 1
        print_frame = [str(page) if page != -1 else "-1" for page in frame]
        print(" ".join(print_frame) + " " * (capacity - len(frame)) + "-1" * (capacity - len(frame)))
    print(f"Number of page faults: {page_faults}")
pages = list(map(int,input("Enter page values: ").split()))
capacity = 3

optimal_page_replacement(pages, capacity)
