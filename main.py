def charCountFn(textArr):
    wordCount = {}
    for c in textArr:
        if not (ord(c) >= ord("a") ) and (ord(c) <= ord("z")): continue
        c = c.lower()
        wordCount[c] = wordCount.get(c,0) + 1
    return wordCount

with open("books/text.txt") as file:
    text = file.read()
    wordCount = len(text.split())
    textArr = [x.lower() for x in text]
    hash = charCountFn(textArr)
    ol = sorted(list(hash))

    print(f"""--- Begin report of books/frankenstein.txt ---\n{wordCount} words found in the document""")
    for c in ol:
        count = hash[c]
        print(f"The '{c}' character was found {count} times")
    
    print("""--- End report ---""")

