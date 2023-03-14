# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Add label
my_label = HTMLLabel(root, html="""
	<ul>
		<li><a href='https://www.geeksforgeeks.org/python-programming-language/'>Python</a></li>
		<li><a href='https://www.geeksforgeeks.org/c-plus-plus/'>C++</a></li>
		<li><a href='https://www.geeksforgeeks.org/java/'>Java</a></li>
	</ul>
	""")

# Adjust label
my_label.pack(pady=20, padx=20)

# Add label
my_label1 = HTMLLabel(root, html="""
        <h1>GEEKSFORGEEKS</h1>
        <h2>GEEKSFORGEEKS</h2>
        <h3>GEEKSFORGEEKS</h3>
        <h4>GEEKSFORGEEKS</h4>
        <h5>GEEKSFORGEEKS</h5>
        <h6>GEEKSFORGEEKS</h6>
    """)
 
# Adjust label
my_label1.pack(pady=20, padx=20)
# Execute Tkinter
root.mainloop()
