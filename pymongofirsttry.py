from pymongo import MongoClient

client = MongoClient('')

connect = client.testdb

collection = connect.datas

whattodo = input('Какое действие? Добавить\Удалить\Список\Найти: ')

if whattodo == 'Добавить':

	inputed_user_id = input('Айди пользователя: ')

	inputed_file_id = input('Айди файла: ')

	inputed_keyword = input('Ключ: ')

	collection_upd = collection.insert_one({'user_id':str(inputed_user_id), 'file_id': str(inputed_file_id), 'keyword': str(inputed_keyword)})

elif whattodo == 'Удалить':

	inputed_user_id = input('Айди пользователя: ')

	inputed_keyword = input('Введи ключ: ')

	collection_rem = collection.delete_one({'user_id':str(inputed_user_id), 'keyword': str(inputed_keyword)}) 

	print('Файл {keyword}\n Пользователя {user}\n удален'.format(inputed_keyword, inputed_user_id))

elif whattodo == 'Список':

	inputed_user_id = input('Введи user_id: ')

	for x in collection.find({'user_id': str(inputed_user_id)}):

		print(x)

elif whattodo == 'Найти':

	inputed_user_id = input('Введи user_id: ')

	inputed_file_id = input('Введи file_id: ')

	print(collection.find_one({'user_id':str(inputed_user_id),'file_id':str(inputed_file_id)}))