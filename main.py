from tkinter import *

window = Tk()
window.minsize(width=800, height=600)
# window.maxsize(width=800, height=1000)

def check_words():
    # Total Words
    global word_c
    print(sentence_entry.get().split(' '))
    word_c = len(sentence_entry.get().split(' '))
    # Correct Words
    global correct_words
    correct_words = []
    is_it_equal_function = lambda x: x in sentence.split(' ')
    correct_words = list(map(is_it_equal_function, sentence_entry.get().split(' ')))

seconds = 60
def start_countdown():
    countdown(seconds)
def countdown(count):
    global seconds
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
        seconds_label = Label(window, text=count)
        seconds_label.grid(row=3, column=0)
    else:
        print('End')
        check_words()
        result_label = Label(window, text=f'Words per minute: {word_c}\nOf which correct: {correct_words.count(True)}')
        result_label.grid(row=4, column=0)

# Label
sentence = "Best friends are like old tomatoes and shoelaces the overpass went under the highway and into a secret world the beauty of the African sunset disguised\n the danger lurking nearby he found rain fascinating yet unpleasant the complicated school homework left the parents trying to help their kids quite\n confused the llama couldn't resist trying the lemonade I'm confused: when people ask me what's up, and I point, they groan weather is not trivial - \nit's especially important when you're standing in it when transplanting seedlings, candied teapots will make the task easier it's difficult to understand the \nlengths he'd go to remain short"
sentence_label = Label(window, text=sentence)
sentence_label.grid(row=0, column=0)

# Entry
sentence_entry = Entry(window, width=120)
sentence_entry.grid(row=1, column=0)

# Button
timer_btn = Button(window, text='START', bd='2', command=start_countdown)
timer_btn.grid(row=2, column=0)

window.mainloop()