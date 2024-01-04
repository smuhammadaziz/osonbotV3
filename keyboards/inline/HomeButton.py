from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.data import StartData, AndijonData, BuxoroData, FargonaData, JizzaxData, \
    NamanganData, NavoiyData, QashqadaryoData, QoraqalpoqData, SamarqandData, SirdaryoData, \
    SurxondaryoData, toshkentshData, toshkentvilData, XorazmData

from keyboards.inline.data import AndijonHovliData
from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData



allRegionsKvartira = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                          inline_keyboard=[
                                              [InlineKeyboardButton(text="Тошкент шаҳар", callback_data=toshkentshData(word="toshkent").pack()),
                                               InlineKeyboardButton(text="Тошкент вилояти",
                                                                    callback_data=toshkentvilData(word="toshkentvil").pack())],
                                              [InlineKeyboardButton(text="Андижон", callback_data=AndijonData(word="andijon").pack()),
                                               InlineKeyboardButton(text="Наманган", callback_data=NamanganData(word="namangan").pack())],
                                              [InlineKeyboardButton(text="Фарғона", callback_data=FargonaData(word="fargona").pack()),
                                               InlineKeyboardButton(text="Самарқанд", callback_data=SamarqandData(word="samarqand").pack())],
                                              [InlineKeyboardButton(text="Бухоро", callback_data=BuxoroData(word="buxoro").pack()),
                                               InlineKeyboardButton(text="Сирдарё", callback_data=SirdaryoData(word="sirdaryo").pack())],
                                              [InlineKeyboardButton(text="Қашқадарё", callback_data=QashqadaryoData(word="qashqa").pack()),
                                               InlineKeyboardButton(text="Сурхoндарё", callback_data=SurxondaryoData(word="surxon").pack())],
                                              [InlineKeyboardButton(text="Навоий", callback_data=NavoiyData(word="navoiy").pack()),
                                               InlineKeyboardButton(text="Жиззах", callback_data=JizzaxData(word="jizzax").pack())],
                                              [InlineKeyboardButton(text="Хоразм", callback_data=XorazmData(word="xorazm").pack()),
                                               InlineKeyboardButton(text="Қорақалпоғистон",
                                                                    callback_data=QoraqalpoqData(word="qora").pack())],
                                          ])

toshkentShHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Квартира", callback_data="toshshkv"),
                                           InlineKeyboardButton(text="Ховли Участка", callback_data="toshshhovli")],
                                          [InlineKeyboardButton(text="Қуруқ Ер", callback_data="toshshyer")],
                                          [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                      ])

toshkentVilHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text="Квартира", callback_data="toshvilkv"),
                                            InlineKeyboardButton(text="Ховли Участка", callback_data="toshvilhovli")],
                                           [InlineKeyboardButton(text="Қуруқ Ер", callback_data="toshvilyer")],
                                           [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                       ])

andijonHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="Квартира", callback_data="andijonkv"),
                                        InlineKeyboardButton(text="Ховли Участка", callback_data=AndijonHovliData(word="andijonhovli").pack())],
                                       [InlineKeyboardButton(text="Қуруқ Ер", callback_data="andijonyer")],
                                       [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                   ])

namanganHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Квартира", callback_data="namangankv"),
                                         InlineKeyboardButton(text="Ховли Участка", callback_data="namanganhovli")],
                                        [InlineKeyboardButton(text="Қуруқ Ер", callback_data="namanganyer")],
                                        [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                    ])

fargonaHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="Квартира", callback_data="fargonakv"),
                                        InlineKeyboardButton(text="Ховли Участка", callback_data="fargonahovli")],
                                       [InlineKeyboardButton(text="Қуруқ Ер", callback_data="fargonayer")],
                                       [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                   ])

samarqandHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text="Квартира", callback_data="samarqandkv"),
                                          InlineKeyboardButton(text="Ховли Участка", callback_data="samarqandhovli")],
                                         [InlineKeyboardButton(text="Қуруқ Ер", callback_data="samarqandyer")],
                                         [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                     ])

buxoroHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data="buxorokv"),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data="buxorohovli")],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data="buxoroyer")],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])

sirdaryoHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Квартира", callback_data="sirdaryokv"),
                                         InlineKeyboardButton(text="Ховли Участка", callback_data="sirdaryohovli")],
                                        [InlineKeyboardButton(text="Қуруқ Ер", callback_data="sirdaryoyer")],
                                        [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                    ])
qashqadaryoHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text="Квартира", callback_data="qashqadaryokv"),
                                            InlineKeyboardButton(text="Ховли Участка",
                                                                 callback_data="qashqadaryohovli")],
                                           [InlineKeyboardButton(text="Қуруқ Ер", callback_data="qashqadaryoyer")],
                                           [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                       ])
surxonHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data="surxonkv"),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data="surxonhovli")],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data="surxonyer")],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])
navoiyHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data="navoiykv"),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data="navoiyhovli")],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data="navoiyyer")],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])
jizzaxHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data="jizzaxkv"),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data="jizzaxhovli")],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data="jizzaxyer")],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])
xorazmHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data="xorazmkv"),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data="xorazmhovli")],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data="xorazmyer")],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])
qoraqalpoqHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Квартира", callback_data="qoraqalpoqkv"),
                                           InlineKeyboardButton(text="Ховли Участка", callback_data="qoraqalpoqhovli")],
                                          [InlineKeyboardButton(text="Қуруқ Ер", callback_data="qoraqalpoqyer")],
                                          [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                      ])

# =========================================================================================

borYoq = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text="✅ Бор", callback_data=BorData(word="bor").pack()),
                                   InlineKeyboardButton(text="❌ Йўқ", callback_data=YoqData(word="yoq").pack())]
                              ])

remontButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Евроремонт", callback_data=YevroremontData(word="yevroremont").pack())],
                                        [InlineKeyboardButton(text="Таъмирланган", callback_data=TamirlangantData(word="tamirlangan").pack())],
                                        [InlineKeyboardButton(text="Ўртача", callback_data=OrtachaData(word="ortacha").pack())],
                                        [InlineKeyboardButton(text=" Таъмирсиз", callback_data=TamirsizData(word="tamirsiz").pack())]
                                    ])

jihozlarButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Бор", callback_data=MavjudData(word="mavjud").pack())],
                                          [InlineKeyboardButton(text="Йўқ", callback_data=JihozlarsizData(word="jihozlarsiz").pack())]
                                      ])

valyutaButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text="$", callback_data=USDData(word="usd").pack())],
                                         [InlineKeyboardButton(text="сўм", callback_data=SUMData(word="sum").pack())]
                                     ])

documentButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Бор,  қонуний", callback_data="dokumentBor")],
                                          [InlineKeyboardButton(text="Тайёр эмас", callback_data="dokumentYoq")]
                                      ])

link_button = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="ЭЪЛОН БЕРИШ", url="https://t.me/OsonBozorBot")]
                                   ])

start_button = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="ЭЪЛОН БЕРИШ",
                                                              callback_data=StartData(word="start").pack())]
                                    ])
