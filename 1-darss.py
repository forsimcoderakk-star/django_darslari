from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# kerakli kutubxonalar chaqrilgan
API_TOKEN = '8429117299:AAH0HsrRTxdiv1sYRRw1fhs5_0c2qgEILpA'
# bot tokken ulanishi
class Malumotlar(StatesGroup):
    name = State()  
    yashash_manzil = State()
    age = State()
    tel = State() 

# foydalanuvchi bilan aniq sharoitda (yonalishda) malumotlarni olish

malumotlar_bazasi = MemoryStorage()

bot = Bot(token=API_TOKEN)
# StateGroup yordamida olingan malumotlarni saqlash uchun kerak
dp = Dispatcher(bot, storage=malumotlar_bazasi)

@dp.message_handler(commands='start', state="*")
async def cmd_start(message: types.Message):
    await Malumotlar.name.set()
    # shu joyga foydalanuvchida ism soralyabdi
    
    await message.reply("Ismni kiritng: ")

@dp.message_handler(state=Malumotlar.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    # statehga malumot saqlayabdi (qanday malumoy (name=message.text) ismini saqlayabdi)
    await Malumotlar.next()
    # stateni kegin malumotini olishga oadi
    await message.reply("Manzilingizni kiriting: ")

@dp.message_handler(state=Malumotlar.yashash_manzil)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(yashash_manzil=message.text)
    await Malumotlar.next()
    await message.reply("yoshingizni kiriting: ")

@dp.message_handler(state=Malumotlar.age)
async def tel_get(message:types.Message, state:FSMContext):
    await state.update_data(age=message.text)
    
    await Malumotlar.next()

    await message.reply("Telefon raqamingizni kiriting: ")
@dp.message_handler(state=Malumotlar.tel)
async def tel_raqam(message:types.Message,state:FSMContext):
    await state.update_data(tel=message.text)

    data = await state.get_data()
    print(data)
    name = data['name']
    age = data['age']
    tel = data['tel']
    y_manzil = data['yashash_manzil']
    await message.reply(f"Salom sizning malumotlaringiz\nIsmingiz:{name}\nYoshingiz: {age}\nTel raqamingiz: {tel}\nYashash manzilingiz: {y_manzil}")
    
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



# state yaratish 
# class State_nomi(StatesGroup):
#     # kerakli malumotlar
#     nomi = State()
# state malumotlarini saqlash
# nom = MemoryStorage() # malumotlarni saqlaysi

# await Form.name.set() foydalanuvchidan kerakli malumotni soraydi 
# await Form.next() foydalanuvhidan statedagi kegingi malumotni soraydi

# MemoryStorage ga malumotlarni yozish
# nom.update_data(message.text)

# MemoryStorage saqlangan malumotlarni olish
# nom.get_data() MemoryStorage dan barcha malumotlarni oladi
    
# await state.finish() MemoryStorage dan malumotlarni ochiradi 
# va foydalanuvchidan malumot sorashdan toxtaydi


