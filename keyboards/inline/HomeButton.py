from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.data import StartData, AndijonData, BuxoroData, FargonaData, JizzaxData, \
    NamanganData, NavoiyData, QashqadaryoData, QoraqalpoqData, SamarqandData, SirdaryoData, \
    SurxondaryoData, toshkentshData, toshkentvilData, XorazmData

from keyboards.inline.data import AndijonHovliData, BuxoroHovliData, FargonaHovliData, JizzaxHovliData, \
    NamanganHovliData, NavoiyHovliData, QashqaHovliData, QoraqalpoqHovliData, SamarqandHovliData, \
    SirdaryoHovliData, SurxonHovliData, ToshketnShHovliData, ToshkentVilHovliData, XorazmHovliData

from keyboards.inline.data import AndijonKvartiraData, BuxoroKvartiraData, FargonaKvartiraData, \
    JizzaxKvartiraData, NamanganKvartiraData, NavoiyKvartiraData, QashqaKvartiraData, \
    QoraqalpoqKvartiraData, SamarqandKvartiraData, SirdaryoKvartiraData, SurxonKvartiraData, \
    ToshketnShKvartiraData, ToshkentVilKvartiraData, XorazmKvartiraData

from keyboards.inline.data import AndijonYerData, BuxoroYerData, FargonaYerData, \
    JizzaxYerData, NamanganYerData, NavoiyYerData, QashqaYerData, \
    QoraqalpoqYerData, SamarqandYerData, SirdaryoYerData, SurxonYerData, \
    ToshketnShYerData, ToshkentVilYerData, XorazmYerData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData
from keyboards.inline.data import DocumentHaveData, DocumentNotData



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
                                          [InlineKeyboardButton(text="Квартира", callback_data=ToshketnShKvartiraData(word="toshshkv").pack()),
                                           InlineKeyboardButton(text="Ховли Участка", callback_data=ToshketnShHovliData(word="toshshhovli").pack())],
                                          [InlineKeyboardButton(text="Қуруқ Ер", callback_data=ToshketnShYerData(word="toshshyer").pack())],
                                          [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                      ])

toshkentVilHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text="Квартира", callback_data=ToshkentVilKvartiraData(word="toshvilkv").pack()),
                                            InlineKeyboardButton(text="Ховли Участка", callback_data=ToshkentVilHovliData(word="toshvilhovli").pack())],
                                           [InlineKeyboardButton(text="Қуруқ Ер", callback_data=ToshkentVilYerData(word="toshvilyer").pack())],
                                           [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                       ])

andijonHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="Квартира", callback_data=AndijonKvartiraData(word="andijonkv").pack()),
                                        InlineKeyboardButton(text="Ховли Участка", callback_data=AndijonHovliData(word="andijonhovli").pack())],
                                       [InlineKeyboardButton(text="Қуруқ Ер", callback_data=AndijonYerData(word="andijonyer").pack())],
                                       [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                   ])

namanganHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Квартира", callback_data=NamanganKvartiraData(word="namangankv").pack()),
                                         InlineKeyboardButton(text="Ховли Участка", callback_data=NamanganHovliData(word="namanganhovli").pack())],
                                        [InlineKeyboardButton(text="Қуруқ Ер", callback_data=NamanganYerData(word="namanganyer").pack())],
                                        [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                    ])

fargonaHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="Квартира", callback_data=FargonaKvartiraData(word="fargonakv").pack()),
                                        InlineKeyboardButton(text="Ховли Участка", callback_data=FargonaHovliData(word="fargonahovli").pack())],
                                       [InlineKeyboardButton(text="Қуруқ Ер", callback_data=FargonaYerData(word="fargonayer").pack())],
                                       [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                   ])

samarqandHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text="Квартира", callback_data=SamarqandKvartiraData(word="samarqandkv").pack()),
                                          InlineKeyboardButton(text="Ховли Участка", callback_data=SamarqandHovliData(word="samarqandhovli").pack())],
                                         [InlineKeyboardButton(text="Қуруқ Ер", callback_data=SamarqandYerData(word="samarqandyer").pack())],
                                         [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                     ])

buxoroHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=BuxoroKvartiraData(word="buxorokv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=BuxoroHovliData(word="buxorohovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=BuxoroYerData(word="buxoroyer").pack())],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])

sirdaryoHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Квартира", callback_data=SirdaryoKvartiraData(word="sirdaryokv").pack()),
                                         InlineKeyboardButton(text="Ховли Участка", callback_data=SirdaryoHovliData(word="sirdaryohovli").pack())],
                                        [InlineKeyboardButton(text="Қуруқ Ер", callback_data=SirdaryoYerData(word="sirdaryoyer").pack())],
                                        [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                    ])

qashqadaryoHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text="Квартира", callback_data=QashqaKvartiraData(word="qashqakv").pack()),
                                            InlineKeyboardButton(text="Ховли Участка", callback_data=QashqaHovliData(word="qashqadaryohovli").pack())],
                                           [InlineKeyboardButton(text="Қуруқ Ер", callback_data=QashqaYerData(word="qashqayer").pack())],
                                           [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                       ])

surxonHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=SurxonKvartiraData(word="surxonkv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=SurxonHovliData(word="surxonhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=SurxonYerData(word="surxonyer").pack())],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])

navoiyHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=NavoiyKvartiraData(word="navoiykv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=NavoiyHovliData(word="navoiyhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=NavoiyYerData(word="navoiyyer").pack())],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])

jizzaxHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=JizzaxKvartiraData(word="jizzaxkv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=JizzaxHovliData(word="jizzaxhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=JizzaxYerData(word="jizzaxyer").pack())],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])

xorazmHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=XorazmKvartiraData(word="xorazmkv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=XorazmHovliData(word="xorazmhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=XorazmYerData(word="xorazmyer").pack())],
                                      [InlineKeyboardButton(text="⬅️ Ортга", callback_data="hometypeortgabutton")]
                                  ])

qoraqalpoqHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Квартира", callback_data=QoraqalpoqKvartiraData(word="qoraqalpoqkv").pack()),
                                           InlineKeyboardButton(text="Ховли Участка", callback_data=QoraqalpoqHovliData(word="qoraqalpoqhovli").pack())],
                                          [InlineKeyboardButton(text="Қуруқ Ер", callback_data=QoraqalpoqYerData(word="qoraqalpoqyer").pack())],
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
                                          [InlineKeyboardButton(text="Бор,  қонуний", callback_data=DocumentHaveData(word="dokumentbor").pack())],
                                          [InlineKeyboardButton(text="Тайёр эмас", callback_data=DocumentNotData(word="dokumentyoq").pack())]
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
