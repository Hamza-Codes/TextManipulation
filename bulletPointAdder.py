# get text from clipboard, add a space and a * at the beginning of each line, and then paste this
# new text to the clipboard

# step - 1 Copy and Paste from the Clipboard. Paste text from clipboard, do something to it,
# paste this new text back to clipboad

import pyperclip
text = pyperclip.paste() # brings all the text from clipboard as one big string

# step - 2 Seperate the Lines of Text and Add the star

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*'+lines[i]
    
# step - 3 join the modified lines

text = '\n'.join(lines)
print(text)
pyperclip.copy(text)