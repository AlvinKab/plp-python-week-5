text_file = open("my_file.txt", "w+")
text_file.write("line 1\n")
text_file.write("2\n")
text_file.write("line 3\n")
text_file.write("line 4\n")
text_file.write("Five\nLine 6")
text_file.seek(0)
file_content = text_file.read()
print(file_content)