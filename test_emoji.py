
import re


def Preprocess(string):
    replace_list = {
        #Quy các icon về 7 loại emoj:

           '🙂':'Thích thú', '😀':'Thích thú' ,	'😄':'Thích thú',	'😆':'Thích thú'	,
    '😅':'Thích thú',	'😂':'Thích thú',	'😊':'Thích thú'	,'😌':'Thích thú'	,'😉':'Thích thú'	,'😏':'Thích thú'	,
    '😍':'Thích thú',	'🙃':'Thích thú',	'😺':'Thích thú','🎃':'Thích thú'	,'💩':'Thích thú',	'😎':'Thích thú',	'😋':'Thích thú',	'😜':'Thích thú',
    '😝':'Thích thú',	'😛':'Thích thú',	'😈':'Thích thú',	'😇':'Thích thú',
    '😸':'Thích thú',	'😹':'Thích thú',	'😼':'Thích thú',	'🌜':'Thích thú',	'🌛':'Thích thú',	'🌚':'Thích thú',	'🌝':'Thích thú'	,'🌞':'Thích thú',
    '🙁':'Buồn bã',	'☹':'Buồn bã',
    '😞':'Buồn bã'	,'😖':'Buồn bã',	'😔':'Buồn bã'	,'😓':'Buồn bã',	'😢':'Buồn bã',	'😢':'Buồn bã'	,'😭':'Buồn bã',	'😟':'Buồn bã'	,'🙎':'Buồn bã'	,'😿':'Buồn bã',
    '😰':'Sợ hãi',	'😱':'Sợ hãi',	'🙀':'Sợ hãi'	,'😧':'Sợ hãi',	'😨':'Sợ hãi',
    '👍':'Tin tưởng'	,'👌':'Tin tưởng',	'✌':'Tin tưởng'	,'🙌':'Tin tưởng',	'💯':'Tin tưởng'	,'🙋':'Tin tưởng',	'✋':'Tin tưởng',
    '✅':'Tin tưởng'	,'✔':'Tin tưởng'	,'👍':'Tin tưởng'	,'👌':'Tin tưởng',	'👏':'Tin tưởng',	'💪':'Tin tưởng',
    '🙏':'hy vọng',	'☀':'hy vọng',	'👉':'hy vọng'	,'🏃':'hy vọng',	'☝':'hy vọng',
    '🙄':'Ngạc nhiên'	,'💥':'Ngạc nhiên',	'😲':'Ngạc nhiên'	,'😳':'Ngạc nhiên',}
    for k, v in replace_list.items():
        string = string.replace(k, v)
#   Remove các ký tự kéo dài: vd: đẹppppppp
    string = re.sub(r'([A-Z])\1+', lambda m: m.group(1).upper(), string, flags=re.IGNORECASE)
#     viết thường
    string = string.lower()
#     link
    string = re.sub('<.*?>', '', string).strip()
    string = re.sub('(\s)+', r'\1', string)
#     xóa ký tự đặt biệt
    string = re.sub(r"[-()\\\"#/@;:<>{}`+=~|.!?,%/]", "",string)
    string = re.sub('\n', ' ',string)
    string = re.sub('--', '',string)
    string = re.sub('  ', ' ',string)
    string = re.sub('   ', ' ',string)
    string = re.sub('    ', ' ',string)
#     xóa số
    string = re.sub(r"\d+", "number", string)
#     xóa
    string = re.sub("added.*photo", "", string)
    string = re.sub("added.*photos", "", string)
    string = re.sub("is.*post", "", string)
    string = re.sub("Photos.*post", "", string)
    string = re.sub("from.*post", "", string)
    string = re.sub("shared.*group", "", string)
    string = re.sub("shared.*post", "", string)
    string = re.sub("shared.*video", "", string)
    string = re.sub("is.*motivated", "", string)
    string = re.sub("is.*with", "", string)

        # xử lý emoj
   
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    string = emoji_pattern.sub(r'', string)

    string = string.replace(u'"', u' ')
    string = string.replace(u'️', u'')
    string = string.replace('🏻','')

    return string
        
samples = [
    "Món này ngon quá 😍",
    "Trời ơi 😂😂😂",
    "Hơi buồn 😢",
    "Ok luôn 👍",
    "Không ngờ luôn 😲"
]

# for s in samples:
#     print("Input :", s)
#     print("Output:", Preprocess(s))
#     print()

import re

def test_code(string):

    emoji_pattern = re.compile("[" 
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)

    string = emoji_pattern.sub(r'', string)

    replace_list = {
        '🙂':'Thích thú',
        '😀':'Thích thú',
        '😂':'Thích thú',
        '😢':'Buồn bã',
        '👍':'Tin tưởng',
        '🙏':'Hy vọng',
        '😲':'Ngạc nhiên'
    }

    for k, v in replace_list.items():
        string = string.replace(k, v)

    return string

for s in samples:
    print("Input :", s)
    print("Output:", Preprocess(s))
    print()