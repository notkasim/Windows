#Creates file
def write_file (file_name):
    with open(file_name, "w") as text_file:
        text_file.write("""Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In vitae turpis massa sed elementum tempus egestas sed. Accumsan in nisl nisi scelerisque eu ultrices. Nunc sed velit dignissim sodales ut eu sem integer vitae. Nisl rhoncus mattis rhoncus urna neque viverra justo nec ultrices. Ultrices eros in cursus turpis massa tincidunt dui. Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac. Nulla facilisi morbi tempus iaculis urna id volutpat lacus. Viverra nibh cras pulvinar mattis nunc sed. Ultricies mi quis hendrerit dolor magna eget. Nibh mauris cursus mattis molestie a iaculis at erat pellentesque. Dui sapien eget mi proin sed libero enim sed faucibus. Sit amet est placerat in egestas.

Libero enim sed faucibus turpis in. In est ante in nibh mauris cursus mattis molestie a. Ac tortor dignissim convallis aenean. Consectetur adipiscing elit pellentesque habitant. Habitant morbi tristique senectus et. Erat nam at lectus urna duis convallis convallis tellus. Elementum pulvinar etiam non quam lacus suspendisse faucibus. Dolor magna eget est lorem ipsum dolor sit amet consectetur. Euismod nisi porta lorem mollis aliquam. Rutrum quisque non tellus orci ac. Elit pellentesque habitant morbi tristique senectus et netus et. Metus dictum at tempor commodo ullamcorper a. Tincidunt augue interdum velit euismod in pellentesque. Tortor pretium viverra suspendisse potenti nullam ac. Dui sapien eget mi proin. Sed faucibus turpis in eu mi bibendum. Auctor elit sed vulputate mi. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Sed cras ornare arcu dui vivamus arcu felis.

Venenatis tellus in metus vulputate eu scelerisque. Elementum sagittis vitae et leo. Arcu bibendum at varius vel pharetra vel turpis nunc eget. Elementum eu facilisis sed odio. Tellus mauris a diam maecenas sed enim ut sem. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Vitae et leo duis ut diam quam nulla porttitor. Auctor eu augue ut lectus arcu bibendum at varius vel. Libero justo laoreet sit amet cursus sit amet dictum sit. Lorem sed risus ultricies tristique. Viverra accumsan in nisl nisi. Nulla posuere sollicitudin aliquam ultrices sagittis. Feugiat nibh sed pulvinar proin gravida hendrerit. Blandit libero volutpat sed cras ornare. Tristique senectus et netus et malesuada fames ac. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper. At urna condimentum mattis pellentesque id nibh tortor id. Elit sed vulputate mi sit amet mauris commodo quis imperdiet. Sed blandit libero volutpat sed cras ornare arcu dui vivamus. Ultrices sagittis orci a scelerisque purus semper eget duis at.

Nisl rhoncus mattis rhoncus urna neque viverra. Cursus eget nunc scelerisque viverra mauris in. Pretium quam vulputate dignissim suspendisse. Et ultrices neque ornare aenean. Volutpat est velit egestas dui id ornare arcu odio ut. Morbi tristique senectus et netus et malesuada fames ac. Purus sit amet luctus venenatis. Urna molestie at elementum eu facilisis sed odio morbi quis. Integer enim neque volutpat ac tincidunt vitae semper. Turpis egestas pretium aenean pharetra magna ac. Imperdiet sed euismod nisi porta lorem mollis aliquam ut. Vulputate enim nulla aliquet porttitor lacus luctus. Mattis enim ut tellus elementum sagittis. Lacinia quis vel eros donec. In est ante in nibh mauris cursus.

Facilisi nullam vehicula ipsum a. Neque egestas congue quisque egestas diam in arcu cursus euismod. Enim tortor at auctor urna. Nibh sed pulvinar proin gravida hendrerit. Posuere sollicitudin aliquam ultrices sagittis orci a. Malesuada bibendum arcu vitae elementum curabitur vitae. Maecenas sed enim ut sem viverra. In iaculis nunc sed augue. Facilisis sed odio morbi quis commodo odio aenean. Diam phasellus vestibulum lorem sed risus. Habitant morbi tristique senectus et netus et malesuada fames ac. Ornare lectus sit amet est. Eget aliquet nibh praesent tristique magna. Sed cras ornare arcu dui vivamus arcu felis. Et ligula ullamcorper malesuada proin libero nunc consequat interdum. Sem nulla pharetra diam sit amet nisl. Egestas erat imperdiet sed euismod nisi. Non enim praesent elementum facilisis. Tortor at auctor urna nunc id cursus. Vel fringilla est ullamcorper eget nulla facilisi etiam.
""")
absolute_path = input("Enter the absolute path to the file: ")
write_file(absolute_path)


#Counts words
def count_things (file):

    with open (file, "r") as text_file:
        file_content = text_file.read()
        word_count = len(file_content.split())
        sentence_count = file_content.count(".")
        paragraphs_count = len(file_content.split("\n\n"))
    print(f"This text contains {word_count} words.")
    print(f"This text contains {sentence_count} sentences.")
    print(f"This text contains {paragraphs_count} paragraphs.")

    lowercase = file_content.lower()
    dict_count = {}

    for character in lowercase:
        if character.isalpha():
            dict_count[character] = dict_count.get(character,0) + 1

    number_count = 0
    for letter, amount in dict_count.items():
        if amount > number_count:
            number_count = amount
            the_choosen_leter = letter
    print(f"The letter '{the_choosen_leter}' appears {number_count} in the text.")

path = absolute_path
count_things(path)