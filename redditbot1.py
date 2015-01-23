from Tkinter import * # Tkinter allows us to create a GUI for our python script
from PIL import ImageTk, Image
import pprint # pprint allows us to unpack dictionaries -- a list of terms and their definitions
import praw

user_agent = ("simple python practice script for searching posts by /u/King-Neptune")
r = praw.Reddit(user_agent = user_agent)
v_fixed = [] # an empty list which will be filled with submissions that match a user inputted criteria

class Application(Frame):
	def __init__(self, master):
		# initializes the Frame
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.instruction = Label(self, text = "Please select a term to search: ")
		self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		self.keyword = Entry(self)		
		self.keyword.grid(row = 1, column = 1, sticky = W)
		self.instruction2 = Label(self, text = "Please select a subreddit to search: ")
		self.instruction2.grid(row = 2, column = 0, columnspan = 2, sticky = W)
		self.credit = Label(self, text = "This bot is a test implementation of the PRAW wrapper for the Reddit API")
		self.credit.grid(row = 20, column = 0, columnspan = 2, sticky = W)
		self.subreddit = Entry(self)		
		self.subreddit.grid(row = 3, column = 1, sticky = W)

		self.submit_button = Button(self, text = "Submit", command = self.results)
		self.submit_button.grid(row = 4, column = 0, sticky = W)

		self.text = Text(self, width = 35, height = 20, wrap = WORD)
		self.text.grid(row = 5, column = 1, columnspan = 2, sticky = W)





	def results(self):
		directory = self.subreddit.get()  # uses the get function to retrieve information from the create_widgets object instance
		keyword = self.keyword.get()
		subreddit = r.get_subreddit(directory)
		
		for submission in subreddit.get_hot(limit = 50):
			title = submission.title
			if keyword in title.lower():
				self.text.delete(0.0, END) #PROBLEM: text box is cleared but v_fixed remains and gets reprinted
				v_fixed.append(title)
				cleanResults = pprint.pformat(v_fixed, indent = 1) # returns the results of the v_fixed dictionary in a more readable format
				self.text.insert(0.0, cleanResults) #inserts the readable results of v_fixed into the results text box in the GUI

		if subreddit.get_hot(limit = 50) > 50:
			v_fixed[:] = []

		if keyword not in title.lower():
			self.text.delete(0.0, END)
			self.text.insert(0.0, "Nothing was found.")





root = Tk()
img = ImageTk.PhotoImage(Image.open("redditlogo.png"))
panel = Label(root, image = img).grid(row = 0, column = 0)
root.title("Reddit Submission Finder")
root.geometry("400x600")
app = Application(root)
root.mainloop()
