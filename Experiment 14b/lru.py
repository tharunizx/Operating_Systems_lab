def lru_page_replacement(pages, capacity):
    frame = []
    page_faults = 0
    lru = []  # To track the order of recent usage
    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < capacity:
                frame.append(pages[i])
            else:
                # Remove the least recently used page
                lru_page = lru.pop(0)
                frame.remove(lru_page)
                frame.append(pages[i])
            page_faults += 1
        else:
            # If the page is already in the frame, update its position in LRU list
            lru.remove(pages[i])

        # Add the current page to the most recent position in LRU list
        lru.append(pages[i])

        print_frame = [str(page) if page != -1 else "-1" for page in frame]
        print(" ".join(print_frame) + " " * (capacity - len(frame)) + "-1" * (capacity - len(frame)))

    print(f"Number of page faults: {page_faults}")

# Input
pages = list(map(int,input("Enter page values:").split()))
capacity = 3

lru_page_replacement(pages, capacity)
