import ast
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title('文化資產保存')
st.header('事例:南港闕家古厝德成居(from[維基百科](https://zh.wikipedia.org/zh-tw/%E5%8D%97%E6%B8%AF%E9%97%95%E5%AE%B6%E5%8F%A4%E5%8E%9D%E5%BE%B7%E6%88%90%E5%B1%85))')
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/%E5%8D%97%E6%B8%AF%E9%97%95%E5%AE%B6%E5%8F%A4%E5%8E%9D%E6%AD%A3%E5%BB%B3.jpg/1280px-%E5%8D%97%E6%B8%AF%E9%97%95%E5%AE%B6%E5%8F%A4%E5%8E%9D%E6%AD%A3%E5%BB%B3.jpg')
st.write('1995年間，陸續有建商談合建，但闕家意見不一致告吹，之後由基泰建設陸續收購持份，逐步蠶食，買賣範圍甚至擴大到德成居周邊土地。')
st.write('2017年5月22日，文資審議當日，在地議員闕枚莎連同闕家十多名所有權人到場陳情。陳情人闕陳娜妮指出，其中一筆地號的土地面積，市價約五億，劃為歷史建築後，市價則降至五千萬，損失高達四億多。委員認為德成居見證早期家族移民墾殖史，紅磚建材和工法少見，兼具文史和工藝價值。但陳情人認為此屋已樓梯與連通道坍塌，想拆除作開發。最終代理主席、委員黃英霓最終裁示採取「全區保存」登錄歷史建築，對所有權人辦理容積移轉等事宜較有利，也建議臺北市文化局及臺北市都發局後續朝三個原則辦理，讓所有權人財產損失最小化、維護建築安全。都發局表示，祖厝基地後方的保護區、防災空間以及人行道系統皆需保存，按現場基地情況，撇除歷史建物部分土地，大樓興建可蓋到七、八層，但後續仍要畫模擬圖，細部了解容積移轉的價值。')
st.write('基泰建設為加速開發，求仍住在此闕家人家繳付租金，甚至提出分割共有物之訴。之後，所有權人聯合告臺北市文化局侵害私有財產，2017年進行訴訟，古厝則日漸塌壞。直到2019年8月12日，文化資產審議委員會再次將此屋以「南港闕家古厝德成居」之名登錄歷史建築。2022年3月10日法拍時，筆錄記載建物包含左廂房、中間正廳、右廂房老舊，漏水、樓梯已坍塌。據2023年4月24日新聞報導及比對網上法拍屋資訊顯示，基泰建設已透過法拍程序取得此古厝與多筆地號之產權。')

st.header('困境')
st.write('法律只保護已登記的古蹟，但登錄古蹟又會導致價值下降，同時登記步驟繁複，非常麻煩，令古蹟所有權人陷入兩難。')

st.header('台灣文化資產失火、破壞列表(from[全能古蹟燒毀王](https://shaohui.simpleinfo.cc/more/))')
st.write('這個Google my map 來源於:https://www.google.com/maps/d/embed?mid=11yl4gOQPCqLQGVoHlwjy6zcOK70&hl=en_US&ll=23.574257149931483%2C120.73631799999997&z=8')
st.markdown("""<iframe src="https://www.google.com/maps/d/embed?mid=11yl4gOQPCqLQGVoHlwjy6zcOK70&hl=en_US&ehbc=2E312F" width="640" height="480"></iframe>"""
            , unsafe_allow_html=True)
