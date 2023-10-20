
import telebot
from telebot import types
from telegram import *
import telebot
import pytesseract
from keras.models import load_model
from tensorflow.keras import layers
from tensorflow.keras import models
from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from dotenv import load_dotenv
from os import environ as env

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


dataset_train = "17flowers/train"
dataset_test = "17flowers/test"
img_data_generator = ImageDataGenerator(

    rotation_range=10,
    width_shift_range=0.3,
    height_shift_range=0.3,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True,
    vertical_flip=False,
    rescale=1./255,           #normalization - divide each pixels into 255
    validation_split=0.2,
)
train_dataset = img_data_generator.flow_from_directory(
    dataset_train,
    shuffle=True,
    #save_to_dir="/content/drive/MyDrive/aug" ,
    subset="training",
    target_size=(224,224)
)
model = load_model("weights.keras")


@bot.message_handler(commands=['start']) #decorator
def send_welcome(message):

  bot.send_message(message.chat.id , "🌼 Hi Dear " + message.from_user.first_name +"🌼"+ "\nWelcome to Flower Recognition bot ")
  FL_recognizer(message)


counter = 0
@bot.message_handler()
def FL_recognizer(message):
    global counter
    if counter == 0 :
      initial_message = bot.send_message(message.chat.id, "Upload a Flower image 🔄 ... " + "\nAnd wait for it's Name " )
      bot.register_next_step_handler(initial_message , flower_recognizer)
      counter += 1
    elif counter != 0 :
      initial_message = bot.send_message(message.chat.id, "Do you still want to continue ?😃 \nSo Upload another image 🔄🌸🌻 ... " )
      bot.register_next_step_handler(initial_message , flower_recognizer)
def flower_recognizer(message):
	  # Get file id
    file_id = message.photo[-1].file_id
    # Get file path
    file_path = bot.get_file(file_id).file_path
    # Download file
    downloaded_file = bot.download_file(file_path)
    # Save file
    try:
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception as e:
        bot.reply_to(message, "Error saving file.")
        return

    # Open image
    try:
        image = Image.open("image.jpg")
    except Exception as e:
        bot.reply_to(message, "Error opening file.")
        return

    # Get text from image
    #bot.send_photo(chat_id=message.chat.id, photo=image)
    # file = context.bot.get_file(update.message.document.file_id)


    image = load_img("image.jpg" , target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    output = model.predict(image)
    predicted_class = np.argmax(output)
    print(predicted_class)
    mylist = list(train_dataset.class_indices)
    print("predicted label : " , mylist[np.argmax(output)])
    bot.send_message(message.chat.id,  mylist[np.argmax(output)])
    FL_recognizer(message)



bot.infinity_polling()