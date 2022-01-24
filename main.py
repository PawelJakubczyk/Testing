

def poem_cuter(line_to_cut: int) -> str:
    text_to_cut = open('Library_Mock/poem.txt', 'r')
    verse_list = []
    for verse in text_to_cut:
        verse_list.append(verse.rstrip('\n'))
    return verse_list[line_to_cut-1]


poem_cuter(2)



