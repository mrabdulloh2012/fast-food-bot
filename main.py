from aiogram import Dispatcher, Bot , filters, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from aiogram.fsm.state import State , StatesGroup
from aiogram.fsm.context import FSMContext

bot = Bot(token="7342485991:AAEweGntW-iUl070n2lMY1OAAfvj3-SO95M")
dp = Dispatcher(bot = bot)

class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()


contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
])


















keyboards_start = [
    [KeyboardButton(text="menu"),KeyboardButton(text="siz haqida ma'lumot")]
]

start_button = ReplyKeyboardMarkup(keyboard=keyboards_start, resize_keyboard=True)


# keyboards_menu = [
#     [KeyboardButton(text="lavash"),KeyboardButton(text="burger"),KeyboardButton(text="drinks")],
#     [KeyboardButton(text='kartoshka')]
# ]

# menu_button = ReplyKeyboardMarkup(keyboard=keyboards_menu,resize_keyboard=True)


keyboards_lavash = [
    [KeyboardButton(text="goshli lavash"),KeyboardButton(text="pishloqli lavash"),KeyboardButton(text="tovuqli lavash")],
    [KeyboardButton(text="ortga")]
]

lavash_button = ReplyKeyboardMarkup(keyboard=keyboards_lavash,resize_keyboard=True)


keyboards_burger = [
    [KeyboardButton(text="standart burger"),KeyboardButton(text="hamburger"),KeyboardButton(text="chizburger")],
    [KeyboardButton(text="ortga")]
]

burger_button = ReplyKeyboardMarkup(keyboard=keyboards_burger,resize_keyboard=True)


keyboards_drinks = [
    [KeyboardButton(text="cola"),KeyboardButton(text="royal"),KeyboardButton(text="fanta")],
    [KeyboardButton(text="ortga")]
]

drinks_button = ReplyKeyboardMarkup(keyboard=keyboards_drinks,resize_keyboard=True)


keyboards_yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="sotib olish",callback_data="sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
])


keyboards_kartoshka = [
    [KeyboardButton(text='kartoshka fri'),KeyboardButton(text='qishloq kartoshkasi')],
    [KeyboardButton(text='ortga')]
]
    
kartoshka_button = ReplyKeyboardMarkup(keyboard=keyboards_kartoshka,resize_keyboard=True)





keyboards_menu_korzinka = [
    [KeyboardButton(text="lavash"),KeyboardButton(text="burger"),KeyboardButton(text="drinks")],
    [KeyboardButton(text='kartoshka')],
    [KeyboardButton(text='korzinka')]
]

menu_korzinka_button = ReplyKeyboardMarkup(keyboard=keyboards_menu_korzinka,resize_keyboard=True)
















    
keyboards_yes_no_goshli_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="goshli lavash sotib olish",callback_data="goshli lavash sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_pishloqli_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="pishloqli lavash sotib olish",callback_data="pishloqli lavash sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_tovuqli_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="tovuqli lavash sotib olish",callback_data="tovuqli lavash sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 









keyboards_yes_no_standart_burger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="standart burger sotib olish",callback_data="standart burger sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_hamburger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="hamburger sotib olish",callback_data="hamburger sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_chizburger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="chizburger sotib olish",callback_data="chizburger sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 











keyboards_yes_no_cola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="cola sotib olish",callback_data="cola sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_royal = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="royal sotib olish",callback_data="royal sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 

keyboards_yes_no_fanta = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="fanta sotib olish",callback_data="fanta sotib olish"),InlineKeyboardButton(text="imkor qilish",callback_data="imkor qilish")]
    
]) 
    
keyboards_sell_products = [
    [KeyboardButton(text='ha sotib olaman'),KeyboardButton(text="yoq sotib olmayman")]
]   
    
sell_products_button = ReplyKeyboardMarkup(keyboard=keyboards_sell_products,resize_keyboard=True)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    

@dp.message(filters.Command("start"))
async def start_function(message: types.Message, state: FSMContext):
    # await message.answer(f"Assalomu alaykum {message.from_user.full_name}", reply_markup=start_button)
    await state.set_state(Registration.first_name)
    await message.answer('xush kelibsiz\n ismingizni kiriting')
    
@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name = message.text)
    await state.set_state(Registration.last_name)
    await message.answer('yaxshi end familiyani kiriting: ')
   
   
@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name = message.text)
    await state.set_state(Registration.number)
    await message.answer('yaxshi end nomer kiriting: ', reply_markup=contact_button)
    

   
@dp.message(F.text == "siz haqida ma'lumot")
async def about_function(message: types.Message):
    await message.answer(f'full name: {message.from_user.full_name}\nuser name: {message.from_user.username}\nID: {message.from_user.id}')
    
@dp.message(F.text == "menu")
async def menu_function(message: types.Message):
    await message.answer("menu",reply_markup=menu_korzinka_button)   




   
@dp.message(F.text == "lavash")
async def lavash_function(message: types.Message):
    await message.answer("lavash", reply_markup=lavash_button)     
    
@dp.message(F.text == "goshli lavash")
async def lavash_oddiy_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4fikHKsb7lpQ8_BJVuUfwHp021iI7vLruxA&s",caption='goshli lavash',reply_markup=keyboards_yes_no_goshli_lavash)         
    
@dp.message(F.text == "pishloqli lavash")
async def lavash_pishloq_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROweC0I1Y3A70ccFprzK00dTllOeEXnWL79g&s",caption='pishloqli lavash',reply_markup=keyboards_yes_no_pishloqli_lavash)                   
    
@dp.message(F.text == "tovuqli lavash")
async def lavash_tovuqli_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUKVp7dSWxB9r6buzP62A5I7SZlhKyQiDkWA&s",caption='tovuqli lavash',reply_markup=keyboards_yes_no_tovuqli_lavash)         
    
    
    
    
@dp.message(F.text == "burger")
async def burger_function(message: types.Message):
    await message.answer("burger", reply_markup=burger_button)     
    
@dp.message(F.text == "standart burger")
async def burger_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPz-LNhaGDVkpfS7dB3OQhALi5ZsvWoxrpBg&s",caption='burger',reply_markup=keyboards_yes_no_standart_burger)     
    
@dp.message(F.text == "hamburger")
async def burger_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQElpavZnBQwnBjLid9VidYUzse-VnPuL-Wrg&s",caption='hamburger',reply_markup=keyboards_yes_no_hamburger)     
    
@dp.message(F.text == "chizburger")
async def burger_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXIkusJx-NqQm7iOQCWvHiRNQoqHmGnr6mzQ&s",caption='chizburger',reply_markup=keyboards_yes_no_chizburger)         
      





@dp.message(F.text == "drinks")
async def drinks_function(message: types.Message):
    await message.answer("drinks", reply_markup=drinks_button)  
    
    
@dp.message(F.text == "cola")
async def drinks_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRztIcocs1A7XkPBdYDOMNV3hCd0J5u10YFVA&s",caption="cola",reply_markup=keyboards_yes_no_cola)      

    
@dp.message(F.text == "royal")
async def drinks_function(message: types.Message):
    await message.answer_photo(photo="https://basket-10.wbcontent.net/vol1582/part158222/158222549/images/big/1.webp",caption="royal",reply_markup=keyboards_yes_no_royal)  
    
    
@dp.message(F.text == "fanta")
async def drinks_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1B213iqx-bk2oi1sQamZIJKmT-_V1nqokSA&s",caption="fanta",reply_markup=keyboards_yes_no_fanta)
        
     
      
     
  
  
@dp.message(F.text == 'kartoshka')
async def kartoshka_function(message: types.Message):
    await message.answer('kartoshka',reply_markup=kartoshka_button)  
    
@dp.message(F.text == 'kartoshka fri')
async def kartoshka_fri_kichik_function(message: types.Message):
    await message.answer_photo(photo="https://img.razrisyika.ru/kart/23/89218-kartoshka-fri-31.jpg",caption='kartoshka fri',reply_markup=keyboards_yes_no)  
    
@dp.message(F.text == 'qishloq kartoshkasi')
async def kartoshka_fri_kichik_function(message: types.Message):
    await message.answer_photo(photo="https://vostorg.buzz/uploads/posts/2023-01/1674525192_31-vostorg-buzz-p-sous-k-kartofelyu-aidakho-54.jpg",caption='qishloq kartoshkasi',reply_markup=keyboards_yes_no)  
    


# products = {int(0):{'goshli lavash':30000},0:{'pishloqli lavash':30000},0:{'tovuqli lavash':30000},0:{'standart burger':26000},0:{'hamburger':28000},0:{'chizburger':25000},0:{'cola':12000},0:{'royal':7000},0:{'fanta':14000}}
  
products_number = []
products_key = []
# products_value = {}
  
  
  
  
@dp.callback_query(F.data == 'goshli lavash sotib olish')
async def goshli_lavash_sotib_olish_function(callback: types.CallbackQuery):
    products_key.append('goshli lavash')
    # products_value.add("30000")
    # for key,value in products[0].items():
    #     for key,value in value.items():
             
    #         if key == 'goshli lavash':
    #             key += int(1)
    #         else:
    #             continue
       
    await callback.message.answer('siz goshli lavash sotib oldis',reply_markup=menu_korzinka_button) 
    
@dp.callback_query(F.data == "pishloqli lavash sotib olish")
async def send_random_value(callback: types.CallbackQuery):  
    products_key.append('pishloqli lavash')  
    await callback.message.answer('siz pishloqli lavash sotib oldiz',reply_markup=menu_korzinka_button)
    
@dp.callback_query(F.data == 'tovuqli lavash sotib olish')
async def tovuqli_lavash_sotib_olish_function(callback: types.CallbackQuery):  
    products_key.append('tovuqli lavash')
    await callback.message.answer('siz tovuqli lavash sotib oldis',reply_markup=menu_korzinka_button) 
  

         
  
  

  
  
# @dp.callback_query(F.data == 'standart burger sotib olish')
# async def standart_burger_sotib_olish_function(callback: types.CallbackQuery):
#     products.update({'standart burger':26000})    
#     await callback.message.answer('siz standart burger sotib oldis',reply_markup=menu_korzinka_button) 
    
# @dp.callback_query(F.data == "hamburger sotib olish")
# async def send_random_value(callback: types.CallbackQuery):  
#     products.update({'hamburger':28000})   
#     await callback.message.answer('siz hamburger sotib oldiz',reply_markup=menu_korzinka_button)
    
# @dp.callback_query(F.data == 'chizburger sotib olish')
# async def tovuqli_lavash_sotib_olish_function(callback: types.CallbackQuery):  
#     products.update({'chizburger':25000})  
#     await callback.message.answer('siz chizburger sotib oldis',reply_markup=menu_korzinka_button)   

  
  
  
  
  
  
  
# @dp.callback_query(F.data == 'cola sotib olish')
# async def goshli_lavash_sotib_olish_function(callback: types.CallbackQuery):
#     products.update({'cola':12000})    
#     await callback.message.answer('siz cola sotib oldis',reply_markup=menu_korzinka_button) 
    
# @dp.callback_query(F.data == "royal sotib olish")
# async def send_random_value(callback: types.CallbackQuery):  
#     products.update({'royal':30000})   
#     await callback.message.answer('siz royal sotib oldiz',reply_markup=menu_korzinka_button)
    
# @dp.callback_query(F.data == 'fanta sotib olish')
# async def tovuqli_lavash_sotib_olish_function(callback: types.CallbackQuery):  
#     products.update({'fanta':30000})  
#     await callback.message.answer('siz fanta sotib oldis',reply_markup=menu_korzinka_button) 
  
  
# all_products = ['goshli lavash','pishloqli lavash','tovuqli lavash','standart burger','hamburger','chizburger','cola','royal','fanta']
# a = []
# for i in all_products:
#     if i in products_key:
#         for i in products_key:
#             a += 1
#     else:
#         continue 
#     products_number.append(len(a))

            
          
  
  
  
  
  
  
  
  
  
  
  
 
 
  
  
  

        
  
  
  
  
  
  
  
  
  
  
@dp.message(F.text == 'korzinka')
async def korzinka_function(message: types.Message):
    all_products = ['goshli lavash','pishloqli lavash','tovuqli lavash','standart burger','hamburger','chizburger','cola','royal','fanta']
    for i in all_products:
        a = 0
        if i in products_key:
            for i in products_key:
             a += 1
        else:
            continue
        products_number.append(a)
        await message.answer(f'{products_number}ta {str(products_key[i])}')
    # for i in products_number:
        # products_number[i],products_key[i]
    
    # for key,value in products.items():
    #     for key,value in value.items():
    #         if int(key) > 0:
    #             await message.answer(f'{key}ta {value.key} -{value.value}')
    #         else:
    #             continue
#     # if products[1] and products[2] in products:
#     #     for i in products_key:
#     #         if i.count() > 1:
#     #             products.append(i)
#     #         else:
#     #             continue
#     #     await message.answer(str(products))
#     # else:
#     #     await message.answer(str(products))
# #     if products == {}:
# #         await message.answer('siz hali hech narsa sotib omadis',reply_markup=menu_korzinka_button)
# #     else:
# #         result = "\n".join([f"{key} - {value}" for key, value in products.items()])
# #         await message.answer(f'{result} \n sotib olasizmi?',reply_markup=sell_products_button)   
    
# # @dp.message(F.text == 'ha sotib olaman')
# # async def yes_function(message: types.Message):
# #     products.clear()
# #     await message.answer('yoqimli ishtaha',reply_markup=menu_korzinka_button)   
    
# # @dp.message(F.text == 'yoq sotib olmayman')
# # async def no_function(message: types.Message):
# #     products.clear()
# #     await message.answer('boshqattan zakas qiling',reply_markup=menu_korzinka_button)   
  


    
        
@dp.callback_query(F.data == "imkor qilish")
async def imkor_qilish(callback: types.CallbackQuery):
    await callback.message.answer('imkor qilish',reply_markup=menu_korzinka_button)     
      
     
     
     
      
@dp.message(F.text == "ortga")
async def back_function(message: types.Message):
    await message.answer('menu',reply_markup=menu_korzinka_button) 
      
        
async def main():
    await dp.start_polling(bot)
    
    
    
if __name__== '__main__':
    asyncio.run(main())