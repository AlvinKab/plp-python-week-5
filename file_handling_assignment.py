try:
    text_file = open("my_file.txt", "a+")
    text_file.write("\nMore lines!!!\n")
    text_file.write("Line 10\n")
    text_file.write("Line 11\n")
    text_file.write("Line 12")
    text_file.seek(0)
    file_content = text_file.read()
    print(file_content)
except:
    print("An error occurred")
finally:
    print("Session terminated")