"""
    ** basic code to create a dropdown, will need  one for both input and output **

     widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        ### use a loop to add items from list:
        i = len(inputs)
        for _ in range(i):
            widget.addItems(inputs[i]) 

        # sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect( self.index_changed)

        #There is an alternate signal to send the text.
        widget.currentTextChanged.connect( self.text_changed )

        self.setCentralWidget(widget)
    """


        """
    I/O functions

    #function to pull the audio inputs, need to add to list and then send to QComboBox object
    #def audio_i:
        i = 0
        inputs = []
        #if matches := re.search((r"^(\d*):\s IN, name: (+*),.*$"), [find way to get list]):
            #*matches.group(0) is an audio input*
            inputs[i] = (f"{group.(0)} - {group.(1)}")
            i += 1
        #else:
            #"select input"

    #function to pull the audio outputs, need to add to list and then send to QComboBox object
    #def audio_o:
        i = 0
        outputs = []
        if matches := re.search((r"^(\d*):\s OUT, name: (+*),.*$"), [find way to get list]):
            #*matches.group(0) is an audio input*
            outputs[i] = (f"{group.(0)} - {group.(1)}")
            i += 1
        #else:
            #"select output"
    """


"""
slot - responds when something happens
ex. def Button_clicked():
    print("button clicked")

app = QApplication()
button = QPushButton("press me")

#wire  a slot to a signal using syntax below:
button.clicked.connect(button_clicked)

button.show()
app.exec()

*** QDials
    -  only outputs ints
    - will need to divide by 100.0 to get floats to pass to effects components 
"""