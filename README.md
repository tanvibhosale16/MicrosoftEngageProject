 # Face Recognition Attendance System #

  ***Recognize The faces And Take Automatic Attendance***
  
We seek to provide a valuable attendance service for both teachers and students.
With a face recognition attendance system, the entire environment is automated. You won't just take the attendance but also automatically record the attendance of the students or teachers.

**Tech Used :**

**Build With** -  Python 3.9

**Modules Used** - All The Modules are of Latest Versions.

      OpenCV Contrib  Python 4.5.5.64
      face_recognition
      numpy
      pandas
      plotty
      csv
      cv2
      os
      requests
      cmake
      dlib
      PIL
      datetime
      streamlit
      streamlit_lottie
      
  **Software Used -**
      
        Pycharm 2022.1.1
        VS CODE(Desktop C & C++ environment required)

**Create environment :**
(Requirements: Open the complete folder of project in the pycharm,the folder should contain Training_images folder,Attendance.csv,venv folder ,Camera.py,config.toml file,HomePage.jpg,viewAtten.jpg) 

![Reqirements](https://user-images.githubusercontent.com/89827357/170851784-feef7355-a7c9-4bbc-8375-020d72a14394.png)

Save config.toml file in .streamlit folder 

![Screenshot (14)](https://user-images.githubusercontent.com/89827357/170852106-033c3c55-a354-467d-b180-20d6449615f7.png)

Go to the terminal in pycharm(at bottom of pycharm) and select the command prompt option and run the following command to run the .py file.

**Streamlit run Camera.py**

![Screenshot (17)](https://user-images.githubusercontent.com/89827357/170852111-802089f7-124f-4f9a-8e16-04841412d37e.png)

![Screenshot (21)](https://user-images.githubusercontent.com/89827357/170852234-25d2abee-5ef9-4e23-9efc-0cf5e27ceec5.png)

**Features:**

    Upload images 
    Train Faces
    Capture Faces
    Recognize Faces & Mark Attendance
    Automatic update of attendance in csv file


**Contents:**

    Home page:Introduction of the Project
       If you are new student then you have to register first which is done by adding his/her image  to Traning_images and  appending his/her name to the csv file
       For that two options are provided :
         i)Register by Uploading image
         ii)Register by capturing image
     Mark Attendance:To mark the Attendance by Recognizing the face
     View Attendance Sheet:To view the attendance sheet




**Limitations:**

While Capturing the image using Register by capturing image feature,the face must be detected properly.If blur image or image with extra light on face or in background is captured then it will be problematic while encoding the images.

**Solution:**

Go for Register by Uploading image feature for registration if there is no proper lightning.

**Demo Video Link:**
  https://drive.google.com/drive/folders/1zudySQaiHQQBAAJpz_ktoF6oyFnhScuW

