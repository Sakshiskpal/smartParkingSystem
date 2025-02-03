# import tkinter as tk
# import cv2
# import pickle
# import cvzone
# import numpy as np
# from PIL import Image, ImageTk
# from tkinter import *
# import tkinter as tk


# class OpenCVTkinterApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("OpenCV with Tkinter")

#         self.header = tk.Label(self.root, text='Smart Parking', bg='lightgrey', height=2, width=250,
#                                font=('Microsoft Yahei UI Light', 23, 'bold'), fg='grey')
#         self.header.pack()

#         self.canvas = tk.Canvas(self.root, width=990, height=660, bg='white')
#         self.canvas.pack()

#         self.cap = cv2.VideoCapture('carPark.mp4')

#         with open('CarParkPos', 'rb') as f:
#             self.posList = pickle.load(f)

#         self.width, self.height = 107, 48

#         self.process_video()

#     def process_video(self):
#         success, img = self.cap.read()
#         print(f"Read frame: {success}")
#         if not success:
#             return

#         imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
#         imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25,
#                                              16)
#         imgMedian = cv2.medianBlur(imgThreshold, 5)
#         kernel = np.ones((3, 3), np.uint8)
#         imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
#         self.check_space_location(imgDilate, img)

#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         img = cv2.resize(img, (990, 660))

#         # Convert the NumPy array to a PIL Image
#         pil_image = Image.fromarray(img)
        
#         # Convert the PIL Image to a PhotoImage object
#         self.photo = ImageTk.PhotoImage(image=pil_image)
        
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

#         self.root.after(10, self.process_video)

#     def check_space_location(self, imgPro, img):
#         spaceCounter = 0

#         for pos in self.posList:
#             x, y = pos
#             imgCrop = imgPro[y:y + self.height, x:x + self.width]
#             count = cv2.countNonZero(imgCrop)
#             cvzone.putTextRect(img, str(count), (x, y + self.height - 10), scale=1.5, thickness=2, offset=0)
#             if count < 900:
#                 color = (0, 255, 0)
#                 thickness = 5
#                 spaceCounter += 1
#             else:
#                 color = (0, 0, 255)
#                 thickness = 3
#             cv2.rectangle(img, pos, (pos[0] + self.width, pos[1] + self.height), color, thickness)
#         cvzone.putTextRect(img, str(count), (x, y + self.height - 3), scale=1,
#                            thickness=2, offset=0, colorR=color)

#         cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(self.posList)}', (100, 50), scale=3,
#                            thickness=5, offset=20, colorR=(0,200,0))



# def open_availability_page():
#     root = tk.Tk()
#     app = OpenCVTkinterApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     open_availability_page()
import tkinter as tk
import cv2
import pickle
import cvzone
import numpy as np
from PIL import Image, ImageTk

class OpenCVTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenCV with Tkinter")

        self.header = tk.Label(self.root, text='Smart Parking', bg='lightgrey', height=2, width=250,
                               font=('Microsoft Yahei UI Light', 23, 'bold'), fg='grey')
        self.header.pack()

        self.canvas = tk.Canvas(self.root, width=990, height=660, bg='white')
        self.canvas.pack()

        self.cap = cv2.VideoCapture('carPark.mp4')

        with open('CarParkPos', 'rb') as f:
            self.posList = pickle.load(f)

        self.width, self.height = 107, 48
        
        self.process_video()

    def process_video(self):
        success, img = self.cap.read()
        print(f"Read frame: {success}")
        if not success:
            return

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25,
                                             16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
        self.check_space_location(imgDilate, img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (990, 660))

        pil_image = Image.fromarray(img)
        self.photo = ImageTk.PhotoImage(image=pil_image)
        
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.root.after(10, self.process_video)

    def check_space_location(self, imgPro, img):
        spaceCounter = 0
        
        for pos in self.posList:
            x, y = pos
            imgCrop = imgPro[y:y + self.height, x:x + self.width]
            count = cv2.countNonZero(imgCrop)
            cvzone.putTextRect(img, str(count), (x, y + self.height - 10), scale=1.5, thickness=2, offset=0)
            if count < 900:
                color = (0, 255, 0)
                thickness = 5
                spaceCounter += 1
            else:
                color = (0, 0, 255)
                thickness = 3
            cv2.rectangle(img, pos, (pos[0] + self.width, pos[1] + self.height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + self.height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(self.posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))
        

def open_availability_page():
    root = tk.Tk()
    app = OpenCVTkinterApp(root)
    root.mainloop()

if __name__ == "__main__":
    open_availability_page()
