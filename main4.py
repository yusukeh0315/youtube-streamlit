import streamlit
from PIL import Image
import time


streamlit.title('Streamlit Beginner')

streamlit.write('プログレスバーの表示')

'Start!!'

latest_iteration = streamlit.empty()
bar = streamlit.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.0001)

'Done!!!!'


left_column, right_column = streamlit.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')

expander1 = streamlit.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')

expander2 = streamlit.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')

expander3 = streamlit.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')

# selectbox
# option = streamlit.sidebar.selectbox(
option = streamlit.sidebar.selectbox(

    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

# text_input

#text = streamlit.sidebar.text_input('あなたの趣味を教えてください。')
text = streamlit.sidebar.text_input('あなたの趣味を教えてください。')

'あなたの趣味は、', text, 'です。'

# slider

#condition = streamlit.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
condition = streamlit.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
