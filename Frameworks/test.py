from distutils import text_file
from tokenize import Number
from telebot import types
import telebot
import re
from Frameworks.test_variable import *

class TelegramBot():
   
    def __init__(self, config) -> None:
        #threading.Thread.__init__(self)
        self.config = config
        self.bot = telebot.TeleBot(self.config['TELEGRAM']['token'])

    def run(self) -> None:
        #переход старт
        
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message) -> None:
          __send_message_with_inlinekeyboard(message, start_message, start_button)
          global data_dict
          global data_dict_test2
          global max_ball
          max_ball.update({message.chat.id: 0})
          data_dict.update({message.chat.id: [0,0,0,0,0,0]})
          data_dict_test2.update({message.chat.id: [0,0,0,0,0,0]})
          global test2_number
          test2_number.update({message.chat.id: [0]})
          global test1_number
          test1_number.update({message.chat.id: [0]})
          print("Пользователь: "+ str(message.chat.id))
             
        @self.bot.message_handler (regexp=cancel_btn )
        def general_menu_res(message) -> None:
          __send_message_with_inlinekeyboard(message, what_test, test1_button, test2_button) 
          global data_dict
          global data_dict_test2
          global max_ball
          max_ball.update({message.chat.id: 0})
          data_dict.update ({message.chat.id: [0,0,0,0,0,0]})
          data_dict_test2.update ({message.chat.id: [0,0,0,0,0,0]})
          global test2_number
          test2_number.update({message.chat.id: [0]})
          global test1_number
          test1_number.update({message.chat.id: [0]})

        
        
        #Если нажата кнопка Поехали вывести выбор текста
        @self.bot.callback_query_handler(func=lambda call: call.data in buttons_for_general_menu)
        def general_menu(call) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(cancel_button)
            self.bot.send_message(call.message.chat.id,
                                  good,
                                 allow_sending_without_reply=False,
                                  reply_markup = markup,
                                  parse_mode='html')
                              
            __send_message_with_inlinekeyboard(call.message, what_test, test1_button, test2_button)  
            global data_dict
            global data_dict_test2
            global test2_number
            global max_ball
            max_ball.update({call.message.chat.id: 0})
            data_dict.update ({call.message.chat.id: [0,0,0,0,0,0]})
            data_dict_test2.update ({call.message.chat.id: [0,0,0,0,0,0]})
            test2_number.update({call.message.chat.id: [0]})
            global test1_number
            test1_number.update({call.message.chat.id: [0]})

        def generl_menu(message, s_call) -> None:
            if message.text == cancel_btn:
                general_menu_res(s_call)
                return
                
        # обработка первого теста
        @self.bot.callback_query_handler(func=lambda call: call.data == test1_btn) #Первый вопрос
        def urachem_menu(call) -> None:
            global test1_number
            global data_dict
            global max_ball
            print("Первый тест пользователя: "+str(call.message.chat.id))
            max_ball.update({call.message.chat.id: 0})
            data_dict.update({call.message.chat.id: [0,0,0,0,0,0]})
            global test1_number
            test1_number.update({call.message.chat.id: [0]})
            number=test1_number[call.message.chat.id][0] 
            __image(call, number+1)
            __send_message_with_inlinekeyboard(call.message, str(number+1)+': '+list_prof_test1[number][0] +' или '+list_prof_test1[number][1], 
                                              types.InlineKeyboardButton(list_prof_test1[number][0] ,callback_data=list_prof_test1[number][0] ) ,
                                              types.InlineKeyboardButton(list_prof_test1[number][1],callback_data=list_prof_test1[number][1]) )
            test1_number[call.message.chat.id][0]=test1_number[call.message.chat.id][0] + 1   

        @self.bot.callback_query_handler(func=lambda call: call.data in [list_prof_test1[test1_number[call.message.chat.id][0]-1][0],list_prof_test1[test1_number[call.message.chat.id][0]-1][1]]) #Первый вопрос
        def urachem_menu(call) -> None:
            global test1_number
            number=test1_number[call.message.chat.id][0] 
            if number<30:
              __rezult_test(call,list_rezult_test1,data_dict) 
              __image(call, number+1)
              __send_message_with_inlinekeyboard(call.message, str(number+1)+': '+list_prof_test1[number][0] +' или '+list_prof_test1[number][1] , 
                                               types.InlineKeyboardButton(list_prof_test1[number][0] ,callback_data=list_prof_test1[number][0] ) ,
                                              types.InlineKeyboardButton(list_prof_test1[number][1],callback_data=list_prof_test1[number][1]) )
              test1_number[call.message.chat.id][0]=test1_number[call.message.chat.id][0] + 1 

            if number==30: 
              __rezult_test(call,list_rezult_test1,data_dict) 
              __send_message_with_inlinekeyboard(call.message, end_questions, 
                                               close_test_button_test1)

        
        @self.bot.callback_query_handler(func=lambda call: call.data ==close_test_bth) #10вопрос
        def urachem_menu(call) -> None:
            __rezult_test_print_1(call,data_dict)
            print ("Итог первого теста"+str(call.message.chat.id),': ',str(data_dict[call.message.chat.id][0]), 
                str(data_dict[call.message.chat.id][1]), str(data_dict[call.message.chat.id][2]),
                 str(data_dict[call.message.chat.id][3]),str(data_dict[call.message.chat.id][4]),str(data_dict[call.message.chat.id][5]) ) 

        @self.bot.callback_query_handler(func=lambda call: call.data == end_btn)
        def urachem_menu(call) -> None:
            self.bot.send_message(call.message.chat.id,
                                 end_message,
                                 allow_sending_without_reply=False,
                                 parse_mode='html')

        @self.bot.callback_query_handler(func=lambda call: call.data == repeat_test_btn)
        def urachem_menu(call) -> None:
          __send_message_with_inlinekeyboard(call.message, what_test, test1_button, test2_button) 
          global data_dict
          global data_dict_test2
          global max_ball
          max_ball.update({call.message.chat.id: 0})
          data_dict.update ({call.message.chat.id: [0,0,0,0,0,0]})
          data_dict_test2.update ({call.message.chat.id: [0,0,0,0,0,0]})
          global test2_number
          test2_number.update({call.message.chat.id: [0]})
          global test1_number
          test1_number.update({call.message.chat.id: [0]})


                                 
        # обработка второго теста
        @self.bot.callback_query_handler(func=lambda call: call.data == test2_btn) #Первый вопрос
        def urachem_menu(call) -> None:
            global test2_number
            global data_dict_test2
            print("Второй тест пользователя: "+str(call.message.chat.id))
            data_dict_test2.update({call.message.chat.id: [0,0,0,0,0,0]})
            test2_number.update({call.message.chat.id: [0]})
            number=test2_number[call.message.chat.id][0] 
            __send_message_with_inlinekeyboard(call.message, str(number+1)+': ' +list_prof_test2[number][0] +' или '+list_prof_test2[number][1] , 
                                               types.InlineKeyboardButton(list_prof_button[number][0],callback_data=list_prof_button[number][0]) ,
                                               types.InlineKeyboardButton(list_prof_button[number][1],callback_data=list_prof_button[number][1]) )
            test2_number[call.message.chat.id][0]=test2_number[call.message.chat.id][0] + 1
            
        @self.bot.callback_query_handler(func=lambda call: call.data in [list_prof_button[test2_number[call.message.chat.id][0]-1][0],list_prof_button[test2_number[call.message.chat.id][0]-1][1]]) #Первый вопрос
        def urachem_menu(call) -> None:
            global test2_number
            number=test2_number[call.message.chat.id][0] 
            if number<42:
              __rezult_test(call,list_rezult_test2,data_dict_test2) 
              __send_message_with_inlinekeyboard(call.message, str(number+1)+': '+list_prof_test2[number][0] +' или '+list_prof_test2[number][1] , 
                                               types.InlineKeyboardButton(list_prof_button[number][0],callback_data=list_prof_button[number][0]) ,
                                               types.InlineKeyboardButton(list_prof_button[number][1],callback_data=list_prof_button[number][1]) )
              test2_number[call.message.chat.id][0]=test2_number[call.message.chat.id][0] + 1

            if number==42: 
              __rezult_test(call,list_rezult_test2,data_dict_test2) 
              __send_message_with_inlinekeyboard(call.message, end_questions, 
                                               close_test_button_test2) 

        @self.bot.callback_query_handler(func=lambda call: call.data == close_test_bth_test2) #результаты второго теста
        def urachem_menu(call) -> None:
              __rezult_test_print_2(call,data_dict_test2)
              print ("Итог второго теста "+str(call.message.chat.id),': ',str(data_dict_test2[call.message.chat.id][0]), 
                str(data_dict_test2[call.message.chat.id][1]), str(data_dict_test2[call.message.chat.id][2]),
                str( data_dict_test2[call.message.chat.id][3]),str(data_dict_test2[call.message.chat.id][4]),str(data_dict_test2[call.message.chat.id][5]))  
        

        
        # функции 
        def  __send_message_with_inlinekeyboard(message, message_text, *buttons) -> None:
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(*buttons)      
            self.bot.send_message(message.chat.id,
                                message_text,
                                allow_sending_without_reply=False,
                                reply_markup=keyboard,
                                parse_mode='html')
                                
        def __image (call,number)->None: #Отображение картинок 
            image = open(ImagePath+str(number) +'a.jpg', 'rb')      
            self.bot.send_photo(call.message.chat.id, image)
            image = open(ImagePath+str(number)+'b.jpg', 'rb')      
            self.bot.send_photo(call.message.chat.id, image)
            
        def __rezult_test_print_1 (call,data_dict) -> None:  #печать результатов тестов
            max_ball[call.message.chat.id]=max ([data_dict[call.message.chat.id][0],data_dict[call.message.chat.id][1],data_dict[call.message.chat.id][2],
                         data_dict[call.message.chat.id][3],data_dict[call.message.chat.id][4],data_dict[call.message.chat.id][5]])
            print("Максимальный балл пользователя "+str(call.message.chat.id)+ ': '+str(max_ball[call.message.chat.id]))
            __rezult_test_level(call,max_ball)
            if __rezult_test_level(call,max_ball)!= ball_0_2:
              # self.bot.send_message(call.message.chat.id,
              #                           __rezult_test_text_type(call,max_ball[call.message.chat.id],data_dict)[0][0],
              #                           parse_mode='html')
              __send_message_with_inlinekeyboard(call.message, __rezult_test_text_type(call,max_ball[call.message.chat.id],data_dict)[0][1], 
                                                  types.InlineKeyboardButton(repeat_test_btn,callback_data=repeat_test_btn),
                                                   types.InlineKeyboardButton(end_btn,callback_data=end_btn)
                                                  ) 
            max_ball.update({call.message.chat.id: 0})

        def __rezult_test_print_2 (call,data_dict) -> None:  #печать результатов тестов
            max_ball[call.message.chat.id]=max ([data_dict[call.message.chat.id][0],data_dict[call.message.chat.id][1],data_dict[call.message.chat.id][2],
                         data_dict[call.message.chat.id][3],data_dict[call.message.chat.id][4],data_dict[call.message.chat.id][5]])
            print("Максимальный балл пользователя "+str(call.message.chat.id)+ ': '+str(max_ball[call.message.chat.id]))
            __rezult_test_level(call,max_ball) 
            if __rezult_test_level(call,max_ball)!= ball_0_2:
              # self.bot.send_message(call.message.chat.id,
              #                           __rezult_test_text_type(call,max_ball[call.message.chat.id],data_dict)[0][0],
              #                           parse_mode='html')
              __send_message_with_inlinekeyboard(call.message, __rezult_test_level(call,max_ball)) 
              __send_message_with_inlinekeyboard(call.message, __rezult_test_text_type(call,max_ball[call.message.chat.id],data_dict)[0][0], 
                                                  types.InlineKeyboardButton(repeat_test_btn,callback_data=repeat_test_btn),
                                                   types.InlineKeyboardButton(end_btn,callback_data=end_btn)
                                                  ) 
            max_ball.update({call.message.chat.id: 0})  

        def __rezult_test (call,list_rezult,data_dict_test) -> None:#обработка результатов теста
          global data_dict_test2
          global data_dict
          print(call.message.chat.id, call.data)
          if call.data in list_rezult[0]: #one_list_test2: 
            data_dict_test[call.message.chat.id][0] = data_dict_test[call.message.chat.id][0] + 1
          if call.data in list_rezult[1]:
            data_dict_test[call.message.chat.id][1] = data_dict_test[call.message.chat.id][1]+ 1
          if call.data in list_rezult[2]:
            data_dict_test[call.message.chat.id][2] = data_dict_test[call.message.chat.id][2]+ 1
          if call.data in list_rezult[3]: 
            data_dict_test[call.message.chat.id][3] = data_dict_test[call.message.chat.id][3]+ 1
          if call.data in list_rezult[4]:
            data_dict_test[call.message.chat.id][4] = data_dict_test[call.message.chat.id][4]+ 1
          if call.data in list_rezult[5]:
            data_dict_test[call.message.chat.id][5] = data_dict_test[call.message.chat.id][5]+ 1
          print (call.message.chat.id,':',data_dict_test[call.message.chat.id][0], 
                data_dict_test[call.message.chat.id][1], data_dict_test[call.message.chat.id][2],
                 data_dict_test[call.message.chat.id][3],data_dict_test[call.message.chat.id][4],data_dict_test[call.message.chat.id][5])  

        def __rezult_test_level(call, data)-> None: #определение уровня полученных баллов
          global max_ball
          if (data[call.message.chat.id] >=8 and data[call.message.chat.id] <=15): rezult= ball_8_10
          if (data[call.message.chat.id] >=5 and data[call.message.chat.id] <=7): rezult= ball_5_7
          if (data[call.message.chat.id] >=2 and data[call.message.chat.id] <=4): rezult= ball_2_4
          if (data[call.message.chat.id] >=0 and data[call.message.chat.id] <=2): rezult= ball_0_2
          return (rezult)
        
        def __rezult_test_text_type (call, data,data_dict_test)-> None:#определение текста результатов
          global data_dict
          global data_dict_test2
          if data==data_dict_test[call.message.chat.id][0]:
             rezult_type= one,
          if data==data_dict_test[call.message.chat.id][1]:
             rezult_type= two,
          if data==data_dict_test[call.message.chat.id][2]:
             rezult_type= three,
          if data==data_dict_test[call.message.chat.id][3]:
             rezult_type= four,
          if data==data_dict_test[call.message.chat.id][4]:
             rezult_type= five,
          if data==data_dict_test[call.message.chat.id][5]:
             rezult_type= six,
          return (rezult_type)
        
        self.bot.infinity_polling()

        
     


