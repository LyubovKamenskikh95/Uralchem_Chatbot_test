from telebot import types

ImagePath ='Files/'

start_message = '''
Привет! 👋🏻
Команда <b>Уралхим и Уралкалий</b> разработала для тебя этот тест, взяв за основу методику Голланда. 
В этом тесте нет «правильных» и «неправильных» ответов. Любой выбранный тобой ответ свидетельствует о тех или иных предпочтениях и то, что для одной профессии неприемлемо, для другой может очень даже пригодиться. 
Очень важно найти себя в той профессии, специальности, должности, которая вдохновляет, развивает, мотивирует и воодушевляет!
И так, поехали.
'''

end_message = '''
Теперь тебе будет проще определиться с выбором будущей профессии. 
Успехов, развития и реализации твоего умственного и творческого потенциала. 
Не забывай просматривать наши <a href="https://www.uralchem.ru/career/"> Вакансии Уралхим </a> , <a href="https://www.uralkali.com/ru/career/"> Вакансии Уралкалий </a>,  у нас есть интересные программы и предложения для студентов.
'''
data_dict = dict()
data_dict_test2= dict()
test2_number=dict()
test1_number=dict()
max_ball=dict()


what_test = '''
Выбери тест:
'''
good = '''
Отлично!
'''
start_btn = 'Поехали🚀'
cancel_btn = 'Главное меню'
test1_btn='Определись с профессией за 5 минут'
test2_btn='Профессиональный тип личности '
close_test_bth='Узнать результаты'
close_test_bth_test2='Узнать результаты теста'
end_questions ='Вопросы закончились!'

different_test_btn= "Выбрать другой тест"
repeat_test_btn= "Повторить/изменить тест"
end_btn= "Закончить тестирование"


ball_8_10 ='Ярко выраженный тип 🔴'
ball_5_7 ='Средне выраженный тип 🟢'
ball_2_4 ='Слабо выраженный тип 🟡'
ball_0_2 ='Результаты некорректные 😔, повтори, пожалуйста, попытку'

#кнопки внизу
cancel_button = types.KeyboardButton(cancel_btn) #Кнопка Главное меню
buttons_for_general_menu = [start_btn, cancel_btn]
start_button = types.InlineKeyboardButton(start_btn, callback_data=start_btn)


test1_button = types.InlineKeyboardButton(test1_btn, callback_data=test1_btn)#Кнопка Тест1
test2_button = types.InlineKeyboardButton(test2_btn, callback_data=test2_btn)#Кнопка Тест1
close_test_button_test1 = types.InlineKeyboardButton(close_test_bth, callback_data=close_test_bth)
close_test_button_test2 = types.InlineKeyboardButton(close_test_bth_test2, callback_data=close_test_bth_test2)
list_prof_test1=[
["Электромеханик","Физиотерапевт"]  ,
["IT- специалист", "Такелажник"  ],
["Оператор связи",  "Кинооператор"],
["Водитель", "Продавец"],
["Инженер-проектировщик", "Менеджер по продажам"],
["Диспетчер", "Дизайнер компьютерных программ "],
["Ветеринар", "Эколог"],
["Химик", "Фермер"],
["Лаборант химического анализа", "Дрессировщик"],
["Агроном", "Фельдшер"],
["Селекционер", "Аппаратчик"],
["Микробиолог ", "Ландшафтный дизайнер"],
["Слесарь-ремонтник","Воспитатель"],
["Преподаватель","Предприниматель"],
["Администратор ", "Режиссер театра и кино "],
["Официант", "Врач "],
["Психолог", "Торговый представитель"],
["Страховой агент ", "Хореограф"],
["Ювелир-гравер", "Журналист"],
["Искусствовед", "Продюсер "],
["Редактор", "Музыкант "],
["Дизайнер интерьера", "Экскурсовод "],
["Арт-директор ", "Музейный работник "],
["Музейный работник ", "Актер театра и кино   "],
["Верстальщик", "Гид-переводчик"],
["Лингвист", "Антикризисный управляющий   "],
["Корректор", "Художественный редактор  "],
["Наборщик текстов ", "Юрисконсульт "],
["Программист ", "Брокер "],
["Бухгалтер", "Литературный переводчик"]]

#Вопросы теста
test1_questions_text_1a = "Электромеханик"
test1_questions_text_1b = "Физиотерапевт"
test1_questions_text_2a = "IT- специалист"
test1_questions_text_2b = "Такелажник"
test1_questions_text_3a = "Оператор связи"
test1_questions_text_3b = "Кинооператор"
test1_questions_text_4a = "Водитель"
test1_questions_text_4b = "Продавец"
test1_questions_text_5a = "Инженер-проектировщик"
test1_questions_text_5b = "Менеджер по продажам"
test1_questions_text_6a = "Диспетчер"
test1_questions_text_6b = "Дизайнер компьютерных программ "
test1_questions_text_7a = "Ветеринар"
test1_questions_text_7b = "Эколог"
test1_questions_text_8a = "Химик"
test1_questions_text_8b = "Фермер"
test1_questions_text_9a = "Лаборант химического анализа"
test1_questions_text_9b = "Дрессировщик"
test1_questions_text_10a = "Агроном"
test1_questions_text_10b = "Фельдшер"
test1_questions_text_11a = "Селекционер"
test1_questions_text_11b = "Аппаратчик"
test1_questions_text_12a = "Микробиолог "
test1_questions_text_12b = "Ландшафтный дизайнер"
test1_questions_text_13a = "Слесарь-ремонтник"
test1_questions_text_13b = "Воспитатель"
test1_questions_text_14a = "Преподаватель"
test1_questions_text_14b = "Предприниматель"
test1_questions_text_15a = "Администратор "
test1_questions_text_15b = "Режиссер театра и кино "
test1_questions_text_16a = "Официант"
test1_questions_text_16b = "Врач "
test1_questions_text_17a = "Психолог"
test1_questions_text_17b = "Торговый представитель"
test1_questions_text_18a = "Страховой агент "
test1_questions_text_18b = "Хореограф"
test1_questions_text_19a = "Ювелир-гравер"
test1_questions_text_19b = "Журналист"
test1_questions_text_20a = "Искусствовед"
test1_questions_text_20b = "Продюсер "
test1_questions_text_21a = "Редактор"
test1_questions_text_21b = "Музыкант "
test1_questions_text_22a = "Дизайнер интерьера"
test1_questions_text_22b = "Экскурсовод "
test1_questions_text_23a = "Композитор"
test1_questions_text_23b = "Арт-директор "
test1_questions_text_24a = "Музейный работник "
test1_questions_text_24b = "Актер театра и кино   "
test1_questions_text_25a = "Верстальщик"
test1_questions_text_25b = "Гид-переводчик"
test1_questions_text_26a = "Лингвист"
test1_questions_text_26b = "Антикризисный управляющий   "
test1_questions_text_27a = "Корректор"
test1_questions_text_27b = "Художественный редактор  "
test1_questions_text_28a = "Наборщик текстов "
test1_questions_text_28b = "Юрисконсульт "
test1_questions_text_29a = "Программист "
test1_questions_text_29b = "Брокер "
test1_questions_text_30a = "Бухгалтер"
test1_questions_text_30b = "Литературный переводчик "





# Кнопки теста 1
test1_questions_text_1a_button = types.InlineKeyboardButton(test1_questions_text_1a,callback_data= test1_questions_text_1a)#Кнопка Тест1
test1_questions_text_1b_button = types.InlineKeyboardButton(test1_questions_text_1b,callback_data= test1_questions_text_1b)#Кнопка Тест1
test1_questions_text_2a_button = types.InlineKeyboardButton(test1_questions_text_2a,callback_data= test1_questions_text_2a)#Кнопка Тест1
test1_questions_text_2b_button = types.InlineKeyboardButton(test1_questions_text_2b,callback_data= test1_questions_text_2b)#Кнопка Тест1
test1_questions_text_3a_button = types.InlineKeyboardButton(test1_questions_text_3a,callback_data= test1_questions_text_3a)#Кнопка Тест1
test1_questions_text_3b_button = types.InlineKeyboardButton(test1_questions_text_3b,callback_data= test1_questions_text_3b)#Кнопка Тест1
test1_questions_text_3a_button = types.InlineKeyboardButton(test1_questions_text_3a,callback_data= test1_questions_text_3a)#Кнопка Тест1
test1_questions_text_3b_button = types.InlineKeyboardButton(test1_questions_text_3b,callback_data= test1_questions_text_3b)#Кнопка Тест1
test1_questions_text_4a_button = types.InlineKeyboardButton(test1_questions_text_4a,callback_data= test1_questions_text_4a)#Кнопка Тест1
test1_questions_text_4b_button = types.InlineKeyboardButton(test1_questions_text_4b,callback_data= test1_questions_text_4b)#Кнопка Тест1
test1_questions_text_5a_button = types.InlineKeyboardButton(test1_questions_text_5a,callback_data= test1_questions_text_5a)#Кнопка Тест1
test1_questions_text_5b_button = types.InlineKeyboardButton(test1_questions_text_5b,callback_data= test1_questions_text_5b)#Кнопка Тест1
test1_questions_text_6a_button = types.InlineKeyboardButton(test1_questions_text_6a,callback_data= test1_questions_text_6a)#Кнопка Тест1
test1_questions_text_6b_button = types.InlineKeyboardButton(test1_questions_text_6b,callback_data= test1_questions_text_6b)#Кнопка Тест1
test1_questions_text_7a_button = types.InlineKeyboardButton(test1_questions_text_7a,callback_data= test1_questions_text_7a)#Кнопка Тест1
test1_questions_text_7b_button = types.InlineKeyboardButton(test1_questions_text_7b,callback_data= test1_questions_text_7b)#Кнопка Тест1
test1_questions_text_8a_button = types.InlineKeyboardButton(test1_questions_text_8a,callback_data= test1_questions_text_8a)#Кнопка Тест1
test1_questions_text_8b_button = types.InlineKeyboardButton(test1_questions_text_8b,callback_data= test1_questions_text_8b)#Кнопка Тест1
test1_questions_text_9a_button = types.InlineKeyboardButton(test1_questions_text_9a,callback_data= test1_questions_text_9a)#Кнопка Тест1
test1_questions_text_9b_button = types.InlineKeyboardButton(test1_questions_text_9b,callback_data= test1_questions_text_9b)#Кнопка Тест1
test1_questions_text_10a_button = types.InlineKeyboardButton(test1_questions_text_10a,callback_data= test1_questions_text_10a)#Кнопка Тест1
test1_questions_text_10b_button = types.InlineKeyboardButton(test1_questions_text_10b,callback_data= test1_questions_text_10b)#Кнопка Тест1
test1_questions_text_11a_button = types.InlineKeyboardButton(test1_questions_text_11a,callback_data= test1_questions_text_11a)#Кнопка Тест1
test1_questions_text_11b_button = types.InlineKeyboardButton(test1_questions_text_11b,callback_data= test1_questions_text_11b)#Кнопка Тест1
test1_questions_text_12a_button = types.InlineKeyboardButton(test1_questions_text_12a,callback_data= test1_questions_text_12a)#Кнопка Тест1
test1_questions_text_12b_button = types.InlineKeyboardButton(test1_questions_text_12b,callback_data= test1_questions_text_12b)#Кнопка Тест1
test1_questions_text_13a_button = types.InlineKeyboardButton(test1_questions_text_13a,callback_data= test1_questions_text_13a)#Кнопка Тест1
test1_questions_text_13b_button = types.InlineKeyboardButton(test1_questions_text_13b,callback_data= test1_questions_text_13b)#Кнопка Тест1
test1_questions_text_14a_button = types.InlineKeyboardButton(test1_questions_text_14a,callback_data= test1_questions_text_14a)#Кнопка Тест1
test1_questions_text_14b_button = types.InlineKeyboardButton(test1_questions_text_14b,callback_data= test1_questions_text_14b)#Кнопка Тест1
test1_questions_text_15a_button = types.InlineKeyboardButton(test1_questions_text_15a,callback_data= test1_questions_text_15a)#Кнопка Тест1
test1_questions_text_15b_button = types.InlineKeyboardButton(test1_questions_text_15b,callback_data= test1_questions_text_15b)#Кнопка Тест1
test1_questions_text_16a_button = types.InlineKeyboardButton(test1_questions_text_16a,callback_data= test1_questions_text_16a)#Кнопка Тест1
test1_questions_text_16b_button = types.InlineKeyboardButton(test1_questions_text_16b,callback_data= test1_questions_text_16b)#Кнопка Тест1
test1_questions_text_17a_button = types.InlineKeyboardButton(test1_questions_text_17a,callback_data= test1_questions_text_17a)#Кнопка Тест1
test1_questions_text_17b_button = types.InlineKeyboardButton(test1_questions_text_17b,callback_data= test1_questions_text_17b)#Кнопка Тест1
test1_questions_text_18a_button = types.InlineKeyboardButton(test1_questions_text_18a,callback_data= test1_questions_text_18a)#Кнопка Тест1
test1_questions_text_18b_button = types.InlineKeyboardButton(test1_questions_text_18b,callback_data= test1_questions_text_18b)#Кнопка Тест1
test1_questions_text_19a_button = types.InlineKeyboardButton(test1_questions_text_19a,callback_data= test1_questions_text_19a)#Кнопка Тест1
test1_questions_text_19b_button = types.InlineKeyboardButton(test1_questions_text_19b,callback_data= test1_questions_text_19b)#Кнопка Тест1
test1_questions_text_20a_button = types.InlineKeyboardButton(test1_questions_text_20a,callback_data= test1_questions_text_20a)#Кнопка Тест1
test1_questions_text_20b_button = types.InlineKeyboardButton(test1_questions_text_20b,callback_data= test1_questions_text_20b)#Кнопка Тест1
test1_questions_text_21a_button = types.InlineKeyboardButton(test1_questions_text_21a,callback_data= test1_questions_text_21a)#Кнопка Тест1
test1_questions_text_21b_button = types.InlineKeyboardButton(test1_questions_text_21b,callback_data= test1_questions_text_21b)#Кнопка Тест1
test1_questions_text_22a_button = types.InlineKeyboardButton(test1_questions_text_22a,callback_data= test1_questions_text_22a)#Кнопка Тест1
test1_questions_text_22b_button = types.InlineKeyboardButton(test1_questions_text_22b,callback_data= test1_questions_text_22b)#Кнопка Тест1
test1_questions_text_23a_button = types.InlineKeyboardButton(test1_questions_text_23a,callback_data= test1_questions_text_23a)#Кнопка Тест1
test1_questions_text_23b_button = types.InlineKeyboardButton(test1_questions_text_23b,callback_data= test1_questions_text_23b)#Кнопка Тест1
test1_questions_text_24a_button = types.InlineKeyboardButton(test1_questions_text_24a,callback_data= test1_questions_text_24a)#Кнопка Тест1
test1_questions_text_24b_button = types.InlineKeyboardButton(test1_questions_text_24b,callback_data= test1_questions_text_24b)#Кнопка Тест1
test1_questions_text_25a_button = types.InlineKeyboardButton(test1_questions_text_25a,callback_data= test1_questions_text_25a)#Кнопка Тест1
test1_questions_text_25b_button = types.InlineKeyboardButton(test1_questions_text_25b,callback_data= test1_questions_text_25b)#Кнопка Тест1
test1_questions_text_26a_button = types.InlineKeyboardButton(test1_questions_text_26a,callback_data= test1_questions_text_26a)#Кнопка Тест1
test1_questions_text_26b_button = types.InlineKeyboardButton(test1_questions_text_26b,callback_data= test1_questions_text_26b)#Кнопка Тест1
test1_questions_text_27a_button = types.InlineKeyboardButton(test1_questions_text_27a,callback_data= test1_questions_text_27a)#Кнопка Тест1
test1_questions_text_27b_button = types.InlineKeyboardButton(test1_questions_text_27b,callback_data= test1_questions_text_27b)#Кнопка Тест1
test1_questions_text_28a_button = types.InlineKeyboardButton(test1_questions_text_28a,callback_data= test1_questions_text_28a)#Кнопка Тест1
test1_questions_text_28b_button = types.InlineKeyboardButton(test1_questions_text_28b,callback_data= test1_questions_text_28b)#Кнопка Тест1
test1_questions_text_29a_button = types.InlineKeyboardButton(test1_questions_text_29a,callback_data= test1_questions_text_29a)#Кнопка Тест1
test1_questions_text_29b_button = types.InlineKeyboardButton(test1_questions_text_29b,callback_data= test1_questions_text_29b)#Кнопка Тест1
test1_questions_text_30a_button = types.InlineKeyboardButton(test1_questions_text_30a,callback_data= test1_questions_text_30a)#Кнопка Тест1
test1_questions_text_30b_button = types.InlineKeyboardButton(test1_questions_text_30b,callback_data= test1_questions_text_30b)#Кнопка Тест1



# Списки данных для определения результатов первого теста

one_list= [test1_questions_text_1a ,test1_questions_text_2b , test1_questions_text_3b , test1_questions_text_4a,test1_questions_text_7a,
test1_questions_text_9a,test1_questions_text_11b,test1_questions_text_13a,test1_questions_text_19a,test1_questions_text_28a]
two_list= [test1_questions_text_5a ,test1_questions_text_7b , test1_questions_text_8a , test1_questions_text_10a,test1_questions_text_11a,test1_questions_text_12a,test1_questions_text_24a, test1_questions_text_26a,test1_questions_text_29a, test1_questions_text_30b]
three_list= [test1_questions_text_1b ,test1_questions_text_4b , test1_questions_text_10b, test1_questions_text_13b, test1_questions_text_14a, test1_questions_text_16b ,test1_questions_text_17a, test1_questions_text_19b, test1_questions_text_22b, test1_questions_text_25b]
four_list= [test1_questions_text_2a ,test1_questions_text_3a , test1_questions_text_6a, test1_questions_text_15a , test1_questions_text_21a , test1_questions_text_28b, test1_questions_text_30a  , test1_questions_text_22a , test1_questions_text_25a , test1_questions_text_27a  ]
five_list= [test1_questions_text_5b ,test1_questions_text_8b, test1_questions_text_14b , test1_questions_text_16a , test1_questions_text_17b , test1_questions_text_18a , test1_questions_text_20b, test1_questions_text_23b, test1_questions_text_26b, test1_questions_text_29b  ]
six_list= [test1_questions_text_6b ,test1_questions_text_9b, test1_questions_text_12b , test1_questions_text_15b, test1_questions_text_18b, test1_questions_text_20a , test1_questions_text_21b, test1_questions_text_23a, test1_questions_text_24b, test1_questions_text_27b    ]

# Результаты первого теста
one_type= '''
<b> Реалистический тип (Р)</b>
Люди, относящиеся к этому типу, предпочитают выполнять работу, требующую силы, ловкости, подвижности, хорошей координации движений, навыков практической работы. Результаты труда профессионалов этого типа ощутимы и реальны – их руками создан весь окружающий нас предметный мир. Люди реалистического типа охотнее делают, чем говорят, они настойчивы и уверены в себе, в работе предпочитают четкие и конкретные указания. Придерживаются традиционных ценностей, поэтому критически относятся к новым идеям. 
'''
one_type_profess='''
<i>Профессии:</i> ученый, физик, химик, инженер, программист, маркшейдер, геолог, геодезист, метролог, инженер по автоматизации, инженер-проектировщик, инженер-строитель, механика, энергетика, электромеханика, IT-специалисты и т.д. 
'''
two_type= '''
<b> Интеллектуальный (И) </b>
Людей, относящихся к этому типу, отличают аналитические способности, рационализм, независимость и оригинальность мышления, умение точно формулировать и излагать свои мысли, решать логические задачи, генерировать новые идеи. Они часто выбирают научную и исследовательскую работу. Им нужна свобода для творчества. Работа способна увлечь их настолько, что стирается грань между рабочим временем и досугом. Мир идей для них может быть важнее, чем общение с людьми. Материальное благополучие для них обычно не на первом месте.  
'''
two_type_profess='''
<i>Профессии:</i> ученый, физик, химик, инженер, программист, маркшейдер, геолог, геодезист, метролог, инженер по автоматизации, инженер-проектировщик, инженер-строитель, механика, энергетика, электромеханика, IT-специалисты и т.д. 
 
'''
three_type= '''
<b> Социальный (С)</b>
Люди, относящиеся к этому типу, предпочитают профессиональную деятельность, связанную с обучением, воспитанием, лечением, консультированием, обслуживанием. Люди этого типа гуманны, чувствительны, активны, ориентированы на социальные нормы, способны понять эмоциональное состояние другого человека. Для них характерно хорошее речевое развитие, живая мимика, интерес к людям, готовность прийти на помощь. Материальное благополучие для них обычно не на первом месте. 

'''
three_type_profess='''
<i>Профессии:</i> учитель, продавец, врач, психолог, диспетчер, менеджер по персоналу, социальный работник, специалист по подбору персонала, специалист по организации обучения, специалист по связям с общественностью, журналист и т.д. 
'''
four_type= '''
<b> Офисный (О)</b>
Люди этого типа обычно проявляют склонность к работе, связанной с обработкой и систематизацией информации, предоставленной в виде условных знаков, цифр, формул, текстов (ведение документации, установление количественных соотношений между числами и условными знаками). Они отличаются аккуратностью, пунктуальностью, практичностью, ориентированы на социальные нормы, предпочитают четко регламентированную работу. Материальное благополучие для них более значимо, чем для других типов. Склонны к работе, не связанной с широкими контактами и принятием ответственных решений. 
'''
four_type_profess='''
<i>Профессии:</i> экономист, бухгалтер, нотариус, библиотекарь, секретарь, IT-специалисты, специалист по кадровому делопроизводству и т.д.
'''
five_type= '''
<b> Предпринимательский (П) </b>
Люди этого типа находчивы, практичны, быстро ориентируются в сложной обстановке, склонны к самостоятельному принятию решений, социально активны, готовы рисковать, ищут острые ощущения. Любят и умеют общаться. Имеют высокий уровень притязаний. Избегают занятий, требующих усидчивости, большой и длительной концентрации внимания. Для них значимо материальное благополучие. Предпочитают деятельность, требующую энергии, организаторских способностей, связанную с руководством, управлением и влиянием на людей. 
 
'''
five_type_profess='''
<i>Профессии:</i> директор, брокер, риелтор, предприниматель, адвокат, менеджер по продажам, маркетолог, специалист по закупкам и т.д.
'''
six_type= '''
<b> Артистический (А) </b>
Люди этого типа оригинальны, независимы в принятии решений, редко ориентируются на социальные нормы и одобрение, обладают необычным взглядом на жизнь, гибкостью мышления, эмоциональной чувствительностью. Отношения с людьми строят, опираясь на свои ощущения, эмоции, воображение, интуицию. Они не выносят жесткой регламентации, предпочитая свободный график работы. Часто выбирают профессии, связанные с литературой, театром, кино, музыкой, изобразительным искусством. 
'''
six_type_profess='''
<i>Профессии:</i> актер, музыкант, художник, фотограф, дизайнер, журналист, специалист по работе с молодежью, специалист по рекламе и т.д.
'''

list_prof_test2= [["инженер-технолог", "инженер-конструктор"],
["электрорадиотехник" , "врач-терапевт"],
[ "оператор станков с числовым  программным управлением", "кодировщик (обработка информации)"],
[ "фотограф" , "коммерсант "],
[ "спасатель МЧС" , "дизайнер"],
[ "политолог "," психиатр "],
["ученый химик ","бухгалтер "],
["философ ","частный предприниматель "],
[ "лингвист ","модельер "],
[ "инспектор службы занятости населения "," статист "],
[ "социальный педагог ", "биржевой маклер "],
[ "тренер" , "искусствовед" ],
[ "нотариус "," менеджер "],
[ "перфораторщик" , "художник "],
[ "лидер политической партии, общего движения ", "писатель "],
[ "закройщик" , "метеоролог" ],
[ "водитель ","работник пресс-службы "],
[ "чертежник" ,"риелтор"],
[ "специалист по ремонту компьютеров и оргтехники ", "секретарь-референт"],
[ "микробиолог" , "психолог "],
["видеооператор" , "режиссер "],
[ "экономист" , "провизор "],
["зоолог" , "главный инженер "],
[ "программист ", "архитектор "],
[ "работник инспекции по делам несовершеннолетних"  , "коммивояжер (сетевой маркетинг)"],
[ "преподаватель ", "биржевой маклер "],
[ "воспитатель" , "декоратор "],
[ "реставратор" , "зав. отделом предприятия "],
["корректор" , "литератор и кинокритик "],
[ "фермер ", "визажист "],
[ "парикмахер" ,"социолог "],
[ "экспедитор" ,"редактор "],
["ветеринар ","директор (финансовый) "],
[ "автомеханик" ," стилист "],
[ "археолог" , "эксперт "],
[ "библиограф" , "корреспондент "],
[ "эколог "," актер "],
[ "логопед" , "контролер "],
[ "адвокат" ,"директор (глава АО) "],
[ "кассир ", "продюсер "],
[ "поэт, писатель ","продавец "],
[ "криминалист (баллистик) ", "композитор"]]

list_prof_button = [["инженер-технолог", "инженер-конструктор"],
["электрорадиотехник" , "врач-терапевт"],
[ "оператор станков с ЧПУ", "кодировщик "],
[ "фотограф" , "коммерсант "],
[ "спасатель МЧС" , "дизайнер"],
[ "политолог "," психиатр "],
["ученый химик ","бухгалтер "],
["философ ","частный предприниматель "],
[ "лингвист ","модельер "],
[ "инспектор "," статист "],
[ "социальный педагог ", "биржевой маклер "],
[ "тренер" , "искусствовед" ],
[ "нотариус"," менеджер"],
[ "перфораторщик" , "художник "],
[ "лидер политической партии ", "писатель"],
[ "закройщик" , "метеоролог" ],
[ "водитель ","работник пресс-службы "],
[ "чертежник" ,"риелтор"],
[ "специалист по ремонту", "секретарь-референт"],
[ "микробиолог" , "психолог "],
["видеооператор" , "режиссер "],
[ "экономист" , "провизор "],
["зоолог" , "главный инженер "],
[ "программист ", "архитектор "],
[ "работник инспекции "  , "коммивояжер "],
[ "преподаватель ", "биржевой маклер "],
[ "воспитатель" , "декоратор "],
[ "реставратор" , "зав. отделом предприятия "],
["корректор" , "литератор и кинокритик "],
[ "фермер ", "визажист"],
[ "парикмахер" ,"социолог"],
[ "экспедитор" ,"редактор"],
["ветеринар ","директор "],
[ "автомеханик" ," стилист "],
[ "археолог" , "эксперт "],
[ "библиограф" , "корреспондент"],
[ "эколог "," актер"],
[ "логопед" , "контролер"],
[ "адвокат" ,"директор (глава АО)"],
[ "кассир ", "продюсер"],
[ "поэт, писатель ","продавец "],
[ "криминалист ", "композитор"]]




one_list_test2= [list_prof_button[0][0],list_prof_button[1][0],list_prof_button[2][0],list_prof_button[3][0],
list_prof_button[4][0],list_prof_button[16][0],list_prof_button[16][0],list_prof_button[18][0],list_prof_button[20][0],
list_prof_button[27][1],list_prof_button[30][0],list_prof_button[31][0],list_prof_button[32][0],list_prof_button[33][0]]

two_list_test2= [list_prof_button[0][1],list_prof_button[5][0],list_prof_button[6][0],list_prof_button[7][0],
list_prof_button[8][0],list_prof_button[15][1],list_prof_button[19][0],list_prof_button[21][0],list_prof_button[22][0],
list_prof_button[23][0],list_prof_button[30][1],list_prof_button[34][0],list_prof_button[35][0],list_prof_button[36][0]]

three_list_test2= [list_prof_button[1][1],list_prof_button[5][1],list_prof_button[9][0],list_prof_button[10][0],
list_prof_button[11][0],list_prof_button[16][1],list_prof_button[18][1],list_prof_button[24][0],list_prof_button[25][0],
list_prof_button[26][0],list_prof_button[35][1],list_prof_button[37][0],list_prof_button[38][0],list_prof_button[40][1]]

four_list_test2= [list_prof_button[2][1],list_prof_button[6][1], list_prof_button[9][1], list_prof_button[12][0], 
list_prof_button[13][0], list_prof_button[17][0], list_prof_button[18][1],list_prof_button[21][1], list_prof_button[28][0], 
list_prof_button[31][1], list_prof_button[34][1], list_prof_button[37][1], list_prof_button[39][0], list_prof_button[41][0] ]

five_list_test2= [list_prof_button[3][1], list_prof_button[7][1], list_prof_button[10][1],list_prof_button[12][1],
 list_prof_button[14][0], list_prof_button[17][1], list_prof_button[22][1], list_prof_button[24][1],list_prof_button[25][1], 
 list_prof_button[27][1],list_prof_button[29][0], list_prof_button[32][1], list_prof_button[38][1],  list_prof_button[39][1]    ]

six_list_test2= [list_prof_button[4][1], list_prof_button[8][1],list_prof_button[11][1], list_prof_button[13][1], 
list_prof_button[14][1], list_prof_button[20][1], list_prof_button[23][1], list_prof_button[26][1], list_prof_button[28][1], 
list_prof_button[29][1],list_prof_button[33][1],list_prof_button[36][1], list_prof_button[40][0], list_prof_button[41][1],      ]


list_rezult_test1=[one_list,two_list,three_list,four_list,five_list,six_list]
list_rezult_test2=[one_list_test2, two_list_test2,three_list_test2,four_list_test2,five_list_test2,six_list_test2]

one=[one_type,one_type_profess]
two=[one_type,two_type_profess]
three=[three_type,three_type_profess]
four=[four_type,four_type_profess]
five=[five_type,five_type_profess]
six=[six_type,six_type_profess]