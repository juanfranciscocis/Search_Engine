#Loading the data from the txt file
def data():

	f = open('huge_txt_example.txt', 'r')
	data = f.read()

	# data to lowercase
	data = data.lower()

	return data



# BOYER MOORE ALGORITHM
NO_OF_CHARS = 256

def badCharHeuristic(string, size):
	badChar = [-1]*NO_OF_CHARS

	for i in range(size):
		badChar[ord(string[i])] = i;

	return badChar

def boyer_moore_search(txt, pat):

	patternFound = []

	m = len(pat)
	n = len(txt)

	badChar = badCharHeuristic(pat, m)

	s = 0
	while(s <= n-m):
		j = m-1

		while j>=0 and pat[j] == txt[s+j]:
			j -= 1

		if j<0:
			#print("Pattern occur at shift = {}".format(s))
			patternFound.append(s)
			s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
		else:
			s += max(1, j-badChar[ord(txt[s+j])])


	return patternFound

# import all functions from the tkinter
import tkinter as tk
from tkinter.font import Font



# create a Pad class
class Pad(tk.Frame):

	# constructor to add buttons and text to the window
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.toolbar = tk.Frame(self, bg="#eee")
		self.toolbar.pack(side="top", fill="x")

		# create a label widget
		self.label = tk.Label(self.toolbar, text="Search:")
		self.label.pack(side="left")

		# create a text entry box
		self.search_txt = tk.Text(self.toolbar, height=1, width=30)
		self.search_txt.pack(side="left")

		#this will add Clear button in the window
		self.search_btn = tk.Button(self.toolbar, text="Search",
								command=self.highlight_text)
		self.search_btn.pack(side="left")







		# adding the text from the text file
		self.text = tk.Text(self)
		self.text.insert("end", data())
		self.text.focus()
		self.text.pack(fill="both", expand=True)

		#configuring a tag called start
		self.text.tag_configure("start", background="yellow", foreground="black")

	# method to highlight the selected text
	def highlight_text(self):

		# clear the previous highlighted text
		self.clear()

		# get the text from the text widget
		wordToSearch = self.search_txt.get("1.0", "end-1c")
		wordToSearchLen = len(wordToSearch)

		# search for the text in the text widget
		founded = boyer_moore_search(data(), str(wordToSearch))

		#show the occurrences of the word
		self.label = tk.Label(self.toolbar, text= str(len(founded)) + " ocurrences found")
		self.label.pack(side="right")

		# if found, highlight the text
		if founded:
			for i in founded:
				self.text.tag_add("start", "1.0 + {} chars".format(i), "1.0 + {} chars".format(i + wordToSearchLen))
		else:
			print("Pattern not found")

	# method to clear all contents from text widget.
	def clear(self):
		self.text.tag_remove("start", "1.0", 'end')

# function
def demo():

	# Create a GUI window
	root = tk.Tk()
	root.title("Text Founder")

	# place Pad object in the root window
	Pad(root).pack(expand=1, fill="both")

	# start the GUI
	root.mainloop()

# Driver code
if __name__ == "__main__":

	# function calling
	demo()







