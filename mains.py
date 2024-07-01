import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import sys
import subprocess

# Get the current working directory
cwd = os.getcwd()
# Load the dataset
df_12th = pd.read_csv(os.path.join(cwd,"stud_training.csv"))

# Define the features and target for 10th and 12th class
features_12th = ['Drawing', 'Teaching', 'Coding', 'Electricity Components', 'Mechanic Parts', 'Computer Parts', 
                 'Architecture', 'Botany', 'Zoology', 'Physics', 'Accounting', 'Economics', 'Sociology',
                 'Psycology', 'History', 'Science', 'Chemistry', 'Mathematics', 'Biology',
                 'Designing', 'Literature','Solving Puzzles', 'Engeeniering', 'Pharmisist','Bussiness',]
target_12th = 'Courses'

# Split the data into training and testing sets
X_train_12th, X_test_12th, y_train_12th, y_test_12th = train_test_split(df_12th[features_12th], df_12th[target_12th], test_size=0.2, random_state=42)

# Train the KNN models

knn_12th = KNeighborsClassifier(n_neighbors=5)
knn_12th.fit(X_train_12th, y_train_12th)


# PyQt GUI implementation
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(440, 200, 900, 500)

        layout = QVBoxLayout()
        self.setStyleSheet("background-color: #FFF5BA;")  # Set background color to light yellow

        title_label = QLabel("<html><body><p style='font-size:35pt; font-weight:bold;'>Career Prediction Using KNN Algorithm</p>")
        title_label.setAlignment(Qt.AlignCenter)  # Align the label text to the center
        layout.addWidget(title_label)

        layout.addSpacing(50)

        education_label = QLabel("<html><body><p style='font-size:16pt; font-weight:bold;'>Select the Education Level</p>")
        education_label.setAlignment(Qt.AlignCenter)  # Align the label text to the center
        layout.addWidget(education_label)

        class10th_button = QPushButton("10th Class")
        class10th_button.clicked.connect(self.show_class10th_window)
        class10th_button.setStyleSheet("QPushButton { background-color: #FFA07A; margin: 95px; padding: 30px; font-size: 20px; border-radius: 20px; }")

        class12th_button = QPushButton("12th Class")
        class12th_button.clicked.connect(self.show_class12th_window)
        class12th_button.setStyleSheet("QPushButton { background-color: #FFA07A; margin: 95px; padding: 30px; font-size: 20px; border-radius: 20px; }")

        layout.addWidget(class10th_button)
        layout.addWidget(class12th_button)

        self.setLayout(layout)

    def show_class10th_window(self):
        # Get the path to the Python interpreter
        python = sys.executable

        # Get the current working directory
        current_dir = os.getcwd()

        # Construct the full path to class10.py
        class10_path = os.path.join(current_dir, "class10.py")

        # Run the class10.py file
        subprocess.Popen([python, class10_path])

    def show_class12th_window(self):
        self.class12th_window = Class12thWindow()
        self.class12th_window.show()

class Class10thWindow(QWidget):
    def __init__(self):
        pass
        
class Class12thWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("12th Class")
        self.setGeometry(440, 200, 900, 500)  # Adjust the size here

        layout = QVBoxLayout()
        self.setStyleSheet("background-color: #FFF5BA;")  # Set background color for the window

        self.interest_combos = []

        for i in range(5):
            interest_label = QLabel(f"<b>Interest {i + 1}:</b>")
            interest_combo = QComboBox()
            interest_combo.addItems(["Select"] + features_12th)
            interest_combo.currentIndexChanged.connect(self.update_combos)  # Connect to the update function

            layout.addWidget(interest_label)
            layout.addWidget(interest_combo)

            # Style the labels and combo boxes
            interest_label.setStyleSheet("QLabel { background-color: #FFF5BA; padding: 10px; margin-bottom: 5px; }")
            interest_combo.setStyleSheet("QComboBox { margin-bottom: 10px; }")

            self.interest_combos.append(interest_combo)

        predict_button = QPushButton("Predict")
        predict_button.clicked.connect(self.make_prediction)
        predict_button.setStyleSheet("QPushButton { background-color: #FFA07A; margin: 49px; padding: 10px; font-size: 14px; }")

        self.prediction_label = QLabel("<b>Prediction will appear here</b>")
        self.prediction_label.setStyleSheet("QLabel { margin-top: 20px; }")

        # Add back button
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.close)
        back_button.setStyleSheet("QPushButton { background-color: #FFA07A; margin: 49px; padding: 10px; font-size: 14px; border-radius: 30px; }")

        layout.addWidget(predict_button)
        layout.addWidget(self.prediction_label)
        layout.addWidget(back_button)  # Add back button to layout

        self.setLayout(layout)

    def update_combos(self):
        selected_interests = [combo.currentText() for combo in self.interest_combos if combo.currentText() != "Select"]

        for combo in self.interest_combos:
            current_selection = combo.currentText()
            combo.blockSignals(True)  # Block signals to prevent infinite loop
            combo.clear()
            combo.addItem("Select")
            for interest in features_12th:
                if interest not in selected_interests or interest == current_selection:
                    combo.addItem(interest)
            combo.setCurrentText(current_selection)
            combo.blockSignals(False)  # Unblock signals

    def make_prediction(self):
        # Check if all combo boxes have a valid selection
        if any(combo.currentText() == "Select" for combo in self.interest_combos):
            self.prediction_label.setText("<font color='red'><b>Please select values for all interests.</b></font>")
            return

        selected_interests = [combo.currentText() for combo in self.interest_combos if combo.currentText() != "Select"]
        input_vector = [1 if interest in selected_interests else 0 for interest in features_12th]

        # Make prediction using the trained model for 12th class
        prediction = knn_12th.predict([input_vector])[0]

        # Display the prediction
        self.prediction_label.setText(f"<font color='blue'><b>Prediction for 12th class: {prediction}</b></font>")

        #Testing and Accuracy
        knn_accuracy_12th = accuracy_score(y_test_12th, knn_12th.predict(X_test_12th))
        print(f"KNN accuracy: {knn_accuracy_12th}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())