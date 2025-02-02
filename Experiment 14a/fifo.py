def fifo_page_replacement(pages, capacity):
    frame = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < capacity:
                frame.append(pages[i])
            else:
                frame.pop(0)
                frame.append(pages[i])
            page_faults += 1
        print_frame = [str(page) if page != -1 else "-1" for page in frame]
        print(" ".join(print_frame) + " " * (capacity - len(frame)) + "-1" * (capacity - len(frame)))

    print(f"Number of page faults: {page_faults}")

# Input
pages = list(map(int,input("Enter page values:").split()))
capacity = 3

fifo_page_replacement(pages, capacity)
