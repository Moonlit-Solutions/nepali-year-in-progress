import datetime as dt
import nepali_datetime

mapping = {
    "0":"०",
    "1":"१",
    "2":"२",
    "3":"३",
    "4":"४",
    "5":"५",
    "6":"६",
    "7":"७",
    "8":"८",
    "9":"९"
}

date_dict = {1: '░░░░░░░░░░░░░░░░░░░░░░░░░ ०%',
 5: '░░░░░░░░░░░░░░░░░░░░░░░░░ १%',
 9: '█░░░░░░░░░░░░░░░░░░░░░░░░ २%',
 12: '█░░░░░░░░░░░░░░░░░░░░░░░░ ३%',
 16: '█░░░░░░░░░░░░░░░░░░░░░░░░ ४%',
 20: '█░░░░░░░░░░░░░░░░░░░░░░░░ ५%',
 23: '██░░░░░░░░░░░░░░░░░░░░░░░ ६%',
 27: '██░░░░░░░░░░░░░░░░░░░░░░░ ७%',
 31: '██░░░░░░░░░░░░░░░░░░░░░░░ ८%',
 34: '██░░░░░░░░░░░░░░░░░░░░░░░ ९%',
 38: '███░░░░░░░░░░░░░░░░░░░░░░ १०%',
 41: '███░░░░░░░░░░░░░░░░░░░░░░ ११%',
 45: '███░░░░░░░░░░░░░░░░░░░░░░ १२%',
 49: '███░░░░░░░░░░░░░░░░░░░░░░ १३%',
 52: '████░░░░░░░░░░░░░░░░░░░░░ १४%',
 56: '████░░░░░░░░░░░░░░░░░░░░░ १५%',
 60: '████░░░░░░░░░░░░░░░░░░░░░ १६%',
 63: '████░░░░░░░░░░░░░░░░░░░░░ १७%',
 67: '█████░░░░░░░░░░░░░░░░░░░░ १८%',
 71: '█████░░░░░░░░░░░░░░░░░░░░ १९%',
 74: '█████░░░░░░░░░░░░░░░░░░░░ २०%',
 78: '█████░░░░░░░░░░░░░░░░░░░░ २१%',
 82: '██████░░░░░░░░░░░░░░░░░░░ २२%',
 85: '██████░░░░░░░░░░░░░░░░░░░ २३%',
 89: '██████░░░░░░░░░░░░░░░░░░░ २४%',
 93: '██████░░░░░░░░░░░░░░░░░░░ २५%',
 96: '███████░░░░░░░░░░░░░░░░░░ २६%',
 100: '███████░░░░░░░░░░░░░░░░░░ २७%',
 104: '███████░░░░░░░░░░░░░░░░░░ २८%',
 107: '███████░░░░░░░░░░░░░░░░░░ २९%',
 111: '████████░░░░░░░░░░░░░░░░░ ३०%',
 114: '████████░░░░░░░░░░░░░░░░░ ३१%',
 118: '████████░░░░░░░░░░░░░░░░░ ३२%',
 122: '████████░░░░░░░░░░░░░░░░░ ३३%',
 125: '█████████░░░░░░░░░░░░░░░░ ३४%',
 129: '█████████░░░░░░░░░░░░░░░░ ३५%',
 133: '█████████░░░░░░░░░░░░░░░░ ३६%',
 136: '█████████░░░░░░░░░░░░░░░░ ३७%',
 140: '██████████░░░░░░░░░░░░░░░ ३८%',
 144: '██████████░░░░░░░░░░░░░░░ ३९%',
 147: '██████████░░░░░░░░░░░░░░░ ४०%',
 151: '██████████░░░░░░░░░░░░░░░ ४१%',
 155: '███████████░░░░░░░░░░░░░░ ४२%',
 158: '███████████░░░░░░░░░░░░░░ ४३%',
 162: '███████████░░░░░░░░░░░░░░ ४४%',
 166: '███████████░░░░░░░░░░░░░░ ४५%',
 169: '████████████░░░░░░░░░░░░░ ४६%',
 173: '████████████░░░░░░░░░░░░░ ४७%',
 177: '████████████░░░░░░░░░░░░░ ४८%',
 180: '████████████░░░░░░░░░░░░░ ४९%',
 184: '█████████████░░░░░░░░░░░░ ५०%',
 187: '█████████████░░░░░░░░░░░░ ५१%',
 191: '█████████████░░░░░░░░░░░░ ५२%',
 195: '█████████████░░░░░░░░░░░░ ५३%',
 198: '██████████████░░░░░░░░░░░ ५४%',
 202: '██████████████░░░░░░░░░░░ ५५%',
 206: '██████████████░░░░░░░░░░░ ५६%',
 209: '██████████████░░░░░░░░░░░ ५७%',
 213: '███████████████░░░░░░░░░░ ५८%',
 217: '███████████████░░░░░░░░░░ ५९%',
 220: '███████████████░░░░░░░░░░ ६०%',
 224: '███████████████░░░░░░░░░░ ६१%',
 228: '████████████████░░░░░░░░░ ६२%',
 231: '████████████████░░░░░░░░░ ६३%',
 235: '████████████████░░░░░░░░░ ६४%',
 239: '████████████████░░░░░░░░░ ६५%',
 242: '█████████████████░░░░░░░░ ६६%',
 246: '█████████████████░░░░░░░░ ६७%',
 250: '█████████████████░░░░░░░░ ६८%',
 253: '█████████████████░░░░░░░░ ६९%',
 257: '██████████████████░░░░░░░ ७०%',
 260: '██████████████████░░░░░░░ ७१%',
 264: '██████████████████░░░░░░░ ७२%',
 268: '██████████████████░░░░░░░ ७३%',
 271: '███████████████████░░░░░░ ७४%',
 275: '███████████████████░░░░░░ ७५%',
 279: '███████████████████░░░░░░ ७६%',
 282: '███████████████████░░░░░░ ७७%',
 286: '████████████████████░░░░░ ७८%',
 290: '████████████████████░░░░░ ७९%',
 293: '████████████████████░░░░░ ८०%',
 297: '████████████████████░░░░░ ८१%',
 301: '█████████████████████░░░░ ८२%',
 304: '█████████████████████░░░░ ८३%',
 308: '█████████████████████░░░░ ८४%',
 312: '█████████████████████░░░░ ८५%',
 315: '██████████████████████░░░ ८६%',
 319: '██████████████████████░░░ ८७%',
 323: '██████████████████████░░░ ८८%',
 326: '██████████████████████░░░ ८९%',
 330: '███████████████████████░░ ९०%',
 333: '███████████████████████░░ ९१%',
 337: '███████████████████████░░ ९२%',
 341: '███████████████████████░░ ९३%',
 344: '████████████████████████░ ९४%',
 348: '████████████████████████░ ९५%',
 352: '████████████████████████░ ९६%',
 355: '████████████████████████░ ९७%',
 359: '█████████████████████████ ९८%',
 363: '█████████████████████████ ९९%',
 365: '█████████████████████████ १००%'}

def convert(val):
    val = str(val)
    return ''.join([mapping[char] for char in val])


def get_text():
    today = nepali_datetime.date.today()
    # today = nepali_datetime.date(2077, 12, 31)
    day_of_year = (today - nepali_datetime.date(today.year, 1, 1)).days 
    date_np = convert(today.day)+'-'+convert(today.month)+'-'+convert(today.year)
    if day_of_year in date_dict:
        return """
आज: {}
{}
        """.format(date_np, date_dict[day_of_year])
    return "" 