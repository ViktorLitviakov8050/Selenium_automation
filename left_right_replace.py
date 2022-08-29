# def left_join(phrases: tuple) -> str:
#     join_phrases = ",".join(phrases)
#     result = join_phrases.replace("right", "left")
#     return result
#
# def left_join2(phrases: tuple) -> str:
#     return ",".join(phrases).replace("right", "left")
#
# def left_join3(phrases: tuple) -> str:
#     return ",".join([phrase.replace("right", "left") for phrase in phrases])
#
# print("Example:")
# print(left_join(("left", "right", "left", "stop")))
# print("Example2:")
# print(left_join2(("left", "right", "left", "stop")))
#
# print("Example3:")
# print(left_join2(("left", "right", "left", "stop")))
# #
# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

#****************************************

# def first_word(text: str) -> str:
#     text = text.replace('.', ' ').replace(',', ' ')
#     text_split = text.split()
#     print(text_split[0])
#
# first_word("asdf,asdf ,asdf .sdf asdf.")
# #
# print("Example:")
# print(first_word("Hello world"))
#
# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
# assert first_word("greetings, friends") == "greetings"
# assert first_word("... and so on ...") == "and"
# assert first_word("hi") == "hi"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


#******************************************
from datetime import date, timedelta
def days_diff(a, b):
    f = date(*t) # 31 december 2014
    s = date(*o) # 1 january 2011
    day_diff = f - s
    return abs(day_diff)

if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))