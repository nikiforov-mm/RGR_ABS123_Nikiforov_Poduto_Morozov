from PyQt5.QtCore import Qt, QSize
from copy import deepcopy
import gost as gt
import table as tb
import playfair as pf
import ceasar as cr
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QWidget, QVBoxLayout, QButtonGroup, QGridLayout, QPushButton, QCheckBox, QLabel, QRadioButton, QLineEdit, QPlainTextEdit
import sys

ciphers = ["Gronsfield", "Playfair", "Table shuffling", "Feistel", "Cipher4"]

def nop():
    pass

en_list = [cr.perfect_gronsfield_en, pf.playfair_no_loss_en, tb.table_shuffling_en, gt.feistel_en, nop]
de_list = [cr.perfect_gronsfield_de, pf.playfair_no_loss_de, tb.table_shuffling_de, gt.feistel_de, nop]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.op_list = en_list

        self.setWindowTitle("DeEncryptor")
        self.MainLayout = QGridLayout()
        CipherLayout = QVBoxLayout()
        ModeLayout = QGridLayout()
        FileLayout = QGridLayout()


        # RADIO GROUPS
        ModeGroup = QButtonGroup(self)
        CipherGroup = QButtonGroup(self)

        # ENCRYPT/DECRYPT
        ModeLabel = QLabel("Modes:")
        self.ExtendedMode = QCheckBox("EX")
        self.ExtendedMode.toggled.connect(self.change_ex_mode)
        self.mode1 = QRadioButton("Encrypt")
        self.mode1.setChecked(True)
        self.mode1.toggled.connect(lambda: self.change_de_en_mode(self.mode1))
        self.mode2 = QRadioButton("Decrypt")
        self.mode2.toggled.connect(lambda: self.change_de_en_mode(self.mode2))
        self.RadioMode = [self.mode1, self.mode2]

        # CIPHERS AND RADIOS
        cipher_label = QLabel("Ciphers:")

        self.cipher1 = QRadioButton(ciphers[0])
        self.cipher1.toggled.connect(lambda: self.change_curr_op(self.cipher1, 0))
        self.cipher1.setChecked(True)
        self.curr_op = self.op_list[0]

        self.cipher2 = QRadioButton(ciphers[1])
        self.cipher2.toggled.connect(lambda: self.change_curr_op(self.cipher2, 1))

        self.cipher3 = QRadioButton(ciphers[2])
        self.cipher3.toggled.connect(lambda: self.change_curr_op(self.cipher3, 2))

        self.cipher4 = QRadioButton(ciphers[3])
        self.cipher4.toggled.connect(lambda: self.change_curr_op(self.cipher4, 3))

        self.cipher5 = QRadioButton(ciphers[4])
        self.cipher5.toggled.connect(lambda: self.change_curr_op(self.cipher5, 4))

        self.RadioCipher = [self.cipher1, self.cipher2, self.cipher3, self.cipher4, self.cipher5]

        CipherLayout.addWidget(cipher_label)

        for mode in self.RadioMode:
            ModeGroup.addButton(mode)

        ModeLayout.addWidget(ModeLabel, *(0, 0))
        ModeLayout.addWidget(self.ExtendedMode, *(0, 1))
        ModeLayout.addWidget(self.mode1, *(1, 0))
        ModeLayout.addWidget(self.mode2, *(1, 1))

        for cipher in self.RadioCipher:
            CipherLayout.addWidget(cipher)
            CipherGroup.addButton(cipher)

        # INPUT HANDLERS
        InputLabel = QLabel("Input file")
        self.InputPath = QLineEdit()
        self.InputBrowse = QPushButton("...")
        self.InputBrowse.setFixedSize(20,20)

        KeyLabel = QLabel("Key file")
        self.KeyPath = QLineEdit()
        self.KeyPath.setEnabled(False)
        self.KeyBrowse = QPushButton("...")
        self.KeyBrowse.setFixedSize(20, 20)
        self.KeyBrowse.setEnabled(False)

        OutputLabel = QLabel("Output file")
        self.OutputPath = QLineEdit()
        self.OutputBrowse = QPushButton("...")
        self.OutputBrowse.setFixedSize(20,20)

        self.InputBrowse.clicked.connect(lambda: self.get_file_name(self.InputPath))
        self.KeyBrowse.clicked.connect(lambda: self.get_file_name(self.KeyPath))
        self.OutputBrowse.clicked.connect(lambda: self.get_file_name(self.OutputPath))


        FileLayout.addWidget(InputLabel, *(0, 0))
        FileLayout.addWidget(self.InputPath, *(0, 1))
        FileLayout.addWidget(self.InputBrowse, *(0, 2))

        FileLayout.addWidget(KeyLabel, *(1, 0))
        FileLayout.addWidget(self.KeyPath, *(1, 1))
        FileLayout.addWidget(self.KeyBrowse, *(1, 2))

        FileLayout.addWidget(OutputLabel, *(2, 0))
        FileLayout.addWidget(self.OutputPath, *(2, 1))
        FileLayout.addWidget(self.OutputBrowse, *(2, 2))

        self.MainLayout.addLayout(ModeLayout, *(0,0))
        self.MainLayout.addLayout(CipherLayout, *(1,0))
        self.MainLayout.addLayout(FileLayout, *(2,0))
        self.ManualLayout = QGridLayout()

        self.ManualInputLabel = QLabel("Manual Input:")
        self.ManualInput = QPlainTextEdit()
        self.ManualInpImport = QPushButton("Import")
        self.ManualInpImport.clicked.connect(lambda: self.import_button(self.ManualInput))

        self.ManualOutputLabel = QLabel("Manual Output:")
        self.ManualOutput = QPlainTextEdit()
        self.ManualOutImport = QPushButton("Import")
        self.ManualOutImport.clicked.connect(lambda: self.import_button(self.ManualOutput))

        self.ManualKeyLabel = QLabel("Manual Key:")
        self.ManualKey = QPlainTextEdit()
        self.ManualKeyImport = QPushButton("Import")
        self.ManualKeyImport.clicked.connect(lambda: self.import_button(self.ManualKey))

        #self.ManualLayout.addWidget(self.ManualInputLabel, 0, 0)
        #self.ManualLayout.addWidget(self.ManualInpImport, 0, 1)
        #self.ManualLayout.addWidget(self.ManualInput, 1, 0, 1, 2)

        #self.ManualLayout.addWidget(self.ManualOutputLabel, 0, 2)
        #self.ManualLayout.addWidget(self.ManualOutImport, 0, 3)
        #self.ManualLayout.addWidget(self.ManualOutput, 1, 2, 1, 2)
        #
        #self.ManualLayout.addWidget(self.ManualKeyLabel, 0, 4)
        #self.ManualLayout.addWidget(self.ManualKeyImport, 0, 5)
        #self.ManualLayout.addWidget(self.ManualKey, 1, 4, 1, 2)

        self.ManualWidgets = [self.ManualInputLabel, self.ManualInpImport, self.ManualInput,
                              self.ManualOutputLabel, self.ManualOutImport, self.ManualOutput,
                              self.ManualKeyLabel, self.ManualKeyImport, self.ManualKey]

        self.DoButton = QPushButton("Encrypt")
        self.DoButton.clicked.connect(self.crypt_button)
        self.MainLayout.addWidget(self.DoButton)


        widget = QWidget()
        widget.setLayout(self.MainLayout)
        self.setCentralWidget(widget)
        self.setMaximumSize(750, 350)

    def change_de_en_mode(self, radio):
        if radio.isChecked():
            self.DoButton.setText(radio.text())
            if "D" in radio.text():
                self.op_list = de_list
                if not self.ExtendedMode.isChecked():
                    self.KeyBrowse.setEnabled(True)
                    self.KeyPath.setEnabled(True)
            else:
                self.op_list = en_list
                self.KeyPath.setEnabled(False)
                self.KeyBrowse.setEnabled(False)
            for num, cipher in enumerate(self.RadioCipher):
                if cipher.isChecked():
                    self.curr_op = self.op_list[num]

    def disable_manual_widgets(self):
        while self.ManualLayout.count():
            item = self.ManualLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

    def enable_manual_widgets(self):
        col = 0
        app = self.ManualWidgets
        while col < 7:
            self.ManualLayout.addWidget(app[col], 0, col)
            self.ManualLayout.addWidget(app[col + 1], 0, col + 1)
            self.ManualLayout.addWidget(app[col + 2], 1, col, 1, 2)
            col += 3


    def ex_mode_widgets(self, flag):
        w_parent = []
        if flag:
            self.enable_manual_widgets()
            self.MainLayout.addLayout(self.ManualLayout, 0, 1, 4, 1)
        else:
            self.ManualLayout.setParent(None)
            self.disable_manual_widgets()

    def change_ex_mode(self):
        flag = self.ExtendedMode.isChecked()
        self.ex_mode_widgets(flag)
        self.InputPath.setEnabled(not flag)
        self.OutputPath.setEnabled(not flag)
        self.KeyPath.setEnabled(not flag)
        self.InputBrowse.setEnabled(not flag)
        self.OutputBrowse.setEnabled(not flag)
        self.KeyBrowse.setEnabled(not flag)

    def get_file_name(self, line):
        file_filter = "Text file (*.txt)"
        caption_str = ""
        for RM in self.RadioMode:
            if RM.isChecked():
                caption_str = RM.text()
        response, junk = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select file to {}.".format(caption_str),
            filter=file_filter,
            initialFilter=file_filter
        )
        line.setText(response)

    def change_curr_op(self, radio, num):
        if radio.isChecked():
            self.curr_op = self.op_list[num]

    def retrieve_from_input_file(self, path):
        self.retrieved_text = open(path, "r", encoding="utf-8").read()

    def import_button(self, line_edit):
        response, junk = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select file to import.",
            filter="Text file (*.txt)",
            initialFilter="Text file (*.txt)"
        )
        if not len(response):
            return 0
        imported_text = open(response, "r", encoding="utf-8").read()
        line_edit.setPlainText(imported_text)

    def crypt_button(self):
        if not self.ExtendedMode.isChecked():
            if self.mode1.isChecked():
                path = self.InputPath.text()
                self.retrieve_from_input_file(path)
                try:
                    encoded_text, private_key = self.curr_op(self.retrieved_text)
                except:
                    return 0
                outfile = open(self.OutputPath.text(), "w", encoding="utf-8")
                outfile.write(encoded_text)
                keyfile = open(self.OutputPath.text()[0:len(self.InputPath.text()) - 4] + "_key.txt", "w", encoding="utf-8")
                keyfile.write(private_key)
            else:
                path = self.InputPath.text()
                self.retrieve_from_input_file(path)
                key = open(self.KeyPath.text(), "r", encoding="utf-8").read()
                try:
                    decoded_text = self.curr_op(self.retrieved_text, key)
                except:
                    return 0
                outfile = open(self.OutputPath.text(), "w")
                outfile.write(decoded_text)
        else:
            self.retrieved_text = self.ManualInput.toPlainText()
            if self.mode1.isChecked():
                try:
                    encoded_text, private_key = self.curr_op(self.retrieved_text)
                except:
                    return 0
                self.ManualOutput.setPlainText(encoded_text)
                self.ManualKey.setPlainText(private_key)
            else:
                try:
                    key = self.ManualKey.toPlainText()
                    decoded_text = self.curr_op(self.retrieved_text, key)
                except:
                    return 0
                self.ManualOutput.setPlainText(decoded_text)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()