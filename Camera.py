import face_recognition
import numpy as np
import cv2 as cv2
import pandas as pd
import os
import streamlit as st
from datetime import date
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Attendance System",page_icon=":pencil:",layout="wide")
nav=st.sidebar.radio("Attendance System",["Home","Register by Capturing image","Register by uploading image","Mark Attendance","View Attendance Sheet"])

with open('Attendance.csv', 'r+') as f:
         myDataList = f.readlines()

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
def markAttendance(name):
    data = pd.read_csv("Attendance.csv")
    if date.today() not in data.columns:
        data[str(date.today())] = "A"
        data.to_csv('Attendance.csv', index=False)
    for i in data.index:
        # print("Name:",name)
        if (data['name'][i] == str.upper(name) and data[str(date.today())][i] != 'p'):
            data.at[i, str(date.today())] = 'p'
            data.to_csv('Attendance.csv', index=False)
            # print(data[str(date.today())][i])
    st.success("Attendance Marked")

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # st.write("Test",img)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

if nav=="Home":
    st.subheader("Welcome")
    backg = Image.open("HomePage.jpg")
    st.image(backg, width=1000)

if nav == "Register by Capturing image":
    st.title('Registration portal')
    MAX_FRAMES = 1
    name=st.text_input("Enter your name:", "")
    st.markdown(f"Welcome {name}")
    check=st.checkbox("Register")
    if check:
        run = st.button("Capture image")
        if True:
            capture = cv2.VideoCapture(0)
            img_display = st.empty()

            while True:
                ret, img = capture.read()
                # print("ans:",ret)
                if run:
                    Y=str.upper(name)
                    cv2.imwrite('Training_images\\{}.jpg'.format(Y), img)
                    df=pd.read_csv("Attendance.csv")
                    totc=len(df.columns)

                    row={'name':[Y]}
                    for i in df.columns:
                        if(i!="name"):
                           row[i] = ["-"]
                    df2 = pd.DataFrame(row)
                    df = pd.concat([df,df2],ignore_index=True,axis=0)
                    df.to_csv('Attendance.csv', index=False)
                    # img_display.image(img, channels='BGR')
                    break
                img_display.image(img, channels='BGR')
            capture.release()
            st.markdown("Registration complete")
            lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_01bh9ld2.json")
            st_lottie(lottie_coding,height=300,key="Registered")
if nav=="Register by uploading image":
    def load_image(image_file):
        img = Image.open(image_file)
        return img

    st.subheader("Image")
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        # To See details
        file_details = {"filename": image_file.name, "filetype": image_file.type,
                        "filesize": image_file.size}
        # st.write(file_details)
        x=image_file.name.split('.')
        Y=str.upper(x[0])
        df=pd.read_csv("Attendance.csv")
        row = {'name': [Y]}
        for i in df.columns:
            if (i != "name"):
                row[i] = ["-"]
        df2 = pd.DataFrame(row)
        df = pd.concat([df, df2], ignore_index=True, axis=0)
        df.to_csv('Attendance.csv', index=False)
        # img_display.image(img, channels='BGR')

        st.write("YOUR IMAGE IS INSERTED")

        # To View Uploaded Image
        st.image(load_image(image_file), width=250)

        with open(os.path.join("Training_images", image_file.name), "wb") as f:
            f.write(image_file.getbuffer())
        st.success("Saved File")

if nav == "Mark Attendance":
    st.title("Mark Your Attendance")
    st.markdown("Press mark Button to mark your attendance")
    run = st.button('Mark')
    FRAME_WINDOW = st.image([])
    path = 'Training_images'
    images = []

    personName = []
    myList = os.listdir(path)
    # print(myList)
    camera = cv2.VideoCapture(0)
    for cu_img in myList:
        current_img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_img)
        print(images)
        personName.append(os.path.splitext(cu_img)[0])
        print(personName)
        encodeListKnown = faceEncodings(images)
    print("All Encodings Completed!!!")

    flag=0
    while run:
        ret, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personName[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (107, 184, 250), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (107, 184, 250), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                if flag==0:
                    markAttendance(name)
                    flag=1
        #         break
        # if flag==1:
        #     break
            # else:
            #     st.write('Stopped')
        # mark = st.checkbox("Register")
        # if mark:
        #     break

        FRAME_WINDOW.image(frame)




if nav == "View Attendance Sheet":
    df=pd.read_csv("Attendance.csv")
    st.dataframe(df)
    st.markdown(" ")
    backg = Image.open("viewAtten.jpg")
    st.image(backg, width=600)

