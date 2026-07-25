import random
import streamlit as st 
if 'num' not in st.session_state:
  st.session_state.num=0
if 'num1' not in st.session_state:
 st.session_state.num1=random.randint(1,20)
 st.session_state.num2=random.randint(1,20)
 st.session_state.sign=random.choice(['+','-','*','/'])
num1=st.session_state.num1
num2=st.session_state.num2
sign=st.session_state.sign
if sign=='+':
 sc=num1+num2
if sign=='-':
 sc=num1-num2
if sign=='*':
 sc=num1*num2
if sign=='/':
 sc=num1/num2
st.title("أهلا بك في لعبتي ")
st.write(num1,sign,num2)
number=st.number_input("ادخل النتيجه ")
if st.button("تاكيد الاجابه "):
 if number==sc:
  print("you are winner ")
  session_state.num=+1
 else:
  print("your answer is not true ") 
  num=0
if st.button(" السؤال التالي "):
 del st.session_state.num1 
 del st.session_state.num2
 del st.session_state.sign
 st.rerun()
st.write( st.session_state.num)
