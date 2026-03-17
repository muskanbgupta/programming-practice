import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Product Launch Predictor",
    layout="wide"
)
st.title("PRODUCT LAUNCH POPULARITY MODEL")
st.info("**created by MUSKAN BANSRAJ GUPTA**",width=300)
Intro,Config,Analysis=st.tabs(["**Introduction**","**Configure**","**Analysis**"])
if "page" not in st.session_state:
        st.session_state.page=1
def pageone():
     st.session_state.page=1
def how_to_use():
        st.session_state.page=2
def popularity_model(p0,k,r,alpha,days):
        P = [p0]
        for t in range(days):
            Pt = P[-1]
            next_P = Pt + r*Pt*(1 - Pt/k) + alpha*Pt
            P.append(next_P)
        return P
def chart():
        st.warning(f"Let's Observe Product: {name}",width=300)
        fig, ax = plt.subplots()
        ax.plot(st.session_state.popularity)
        ax.set_xlabel("Days")
        ax.set_ylabel("Popularity")
        ax.set_title("Product Popularity Growth")
        st.pyplot(fig)
        st.divider()
        early=(int(st.session_state.popularity[-1]*0.15))
        hype=st.session_state.popularity[-1]/k*100
        buyer=(int(st.session_state.popularity[-1]*0.60))
        passive=(int(st.session_state.popularity[-1]*0.25))
        st.subheader(f"Hype Score: {round(hype,2)}% 📈")

        st.progress(hype/100)

        if hype > 80:
            st.success("🚀 Product is likely to go VIRAL!")
        elif hype > 50:
            st.info("📈 Product may become popular.")
        else:
            st.warning("⚠ Product growth may be slow.")

        st.subheader(f"Earlyer Adopters: {early}") 
        if early > 100:
            st.success("People are Loving the Product!💓")
        elif hype > 50:
            st.info("People May like the Product!😊")
        else:
            st.warning("⚠ Product are not Liking the Product.")

        st.subheader(f"Buyers: {buyer}")
        if buyer > k*0.3:
         st.success("🛒 Strong purchase activity! Many users are buying the product.")
        elif buyer > k*0.2:
            st.info("📊 Moderate buying interest from users.")
        else:
            st.warning("⚠ Buying activity is currently low.")
        
        st.subheader(f"Passive User: {passive}")
        if passive > 200:
            st.warning("👀 Many users are only observing the product but not buying yet.")
        elif passive > 100:
            st.info("Some users are interested but waiting before purchasing.")
        else:
            st.success("👍 Most users are actively adopting the product!")

        st.divider()
        st.subheader("Pie Chart Analysis")
        fig1,ax1=plt.subplots()
        ax1.pie([early,buyer,passive],labels=["EARLYER ADOPTERS","BUYERS","PASSIVE"],autopct="%1.1f%%")
        st.pyplot(fig1)
        st.subheader("Above Diagram Shows")
        with st.container(border=True):
            st.write("**_Orange color_** :- \n- Indicates Number of Buyers")
            st.write("**_Blue color_** :- \n- Indicates Number of Earlyer Adopters")
            st.write("**_Green color_** :- \n- Indicates Number of Passive Users")

with Intro:
      if st.session_state.page==1:
        
        st.header("Description of the Model")
        with st.container(border=True):
            st.write("""Product Launch Popularity Model is a simulation
                    tool that predicts how popular a newly launched gadget may become 
                    over time. \n- The model combines logistic growth and network effects 
                    to simulate how early adopters, buyers, and passive users influence
                    product adoption.\n- By adjusting parameters such as market size, 
                    marketing strength, and hype level, users can explore how different
                    factors affect the popularity of a product launch.""")
        st.header("Objective of Model")
        with st.container(border=True):
            st.write("""The objective of this model is to simulate how a newly launched 
                    gadget gains popularity over time. The model analyzes the influence 
                    of early adopters, social network effects, and market size to predict
                    product adoption and hype levels.""")
        st.header("**Model Components**")
        with st.expander("Click to View"):
            st.write("""\n- Early Adopters\n- Buyers\n- Passive\n- Users Network Influence
                    \n- Hype Level""")
        st.divider()
        st.write("**HOW TO USE THIS MODEL?**")
        st.button("**Help**",on_click=how_to_use)
        st.divider()
   
with Config:
        name=st.text_input("**_Enter Product Name_**") 
        p0=st.number_input("**_Initial User_**",value=100)
        k=st.number_input("**_Market Size of Product_** (Popularity of Product)",value=1000)
        r=st.number_input("**_Earlyer Adopter of Product_**  (Growth rate)",value=0.02)
        alpha=st.number_input("**_Network effect strength_**  (Users Influence other people to buy the Product.)",value=0.05)
        days=st.number_input("**_Simulation days_**  (Number of days the model runs)",value=31)
        k=int(k)
        r=float(r)
        alpha=float(alpha)
        days=int(days)
        if st.button("**Run Simulation**"):
            st.session_state.popularity=popularity_model(p0,k,r,alpha,days)
        if "popularity" in st.session_state:
            chart()     
with Analysis:
    st.header("Project: Product Launch Popularity Model")
    st.subheader("Objective ")
    st.caption("This model simulates real-world product growth by combining natural adoption limits (logistic growth) with user influence (network effects).")
    st.markdown("""\n- Model hype of new gadget online
                     \n- Combine: Logistic Growth + Network Effects \n-  Components: 
                     Early adopters, Buyers, Passive \n-  Include: Hype prediction""")
    st.header("Sources Used to Build this Frontend Project")
    with st.container(border=True):
         st.write("""
This frontend project was developed using Streamlit, which I chose because of its simplicity, 
ease of use, and ability to quickly transform ideas into interactive web applications.

While there are many frameworks available for frontend development such as React, Angular, 
and plain HTML/CSS/JavaScript, I preferred Streamlit because it allows rapid development 
with minimal code and is especially beginner-friendly.

Key reasons for choosing Streamlit:
- Simple and clean syntax
- No need for extensive frontend knowledge (HTML/CSS/JS)
- Fast development and prototyping
- Easy integration with Python logic and data analysis
- Built-in UI components like sliders, buttons, and charts

This project demonstrates how powerful and efficient Streamlit can be for building 
data-driven and interactive frontend applications.
""")
    st.divider()
    st.header("Formula Used(Logistic Growth + Network Effects)")
    with st.expander("Click to View"):
        st.subheader("_Pt + r*Pt*(1 - Pt/k) + alpha*Pt_")
        st.info("Meaning of Short froms \n- Pt --> current Users \n- r --> Growth rate \n- k --> Carrying Capacity \n- Alpha --> Network effect strength ")
    st.header("""Categorized users into:\n- Early Adopters → First users driven by innovation\n- Buyers → Majority users influenced by growth
              \n- Passive Users → Observers with low interaction""")
    st.header("Designed a Hype Prediction System based on:\n- Interest level\n- Marketing strength\n- Trend factor")
    st.header("Implemented logic to classify product performance:\n- High growth → Viral\n- Medium growth → Growing\n- Low growth → Slow adoption")
    st.header("""Built an interactive frontend using Streamlit to:\n- Input parameters (interest, marketing, etc.)\n- Visualize growth and hype
                \n- Display predictions in real-time""")
    
if st.session_state.page==2:
        st.subheader("**GO TO CONFIGURE**")
        st.markdown("""\n 1️. Enter Product Details\n
        Type the name of the gadget or product you want to simulate.
        \n2️. Set the Market Size\n
        Choose the total number of potential users who might buy the product.
    \n 3️. Adjust Early Adopters\n
        Select the percentage of people who buy the product immediately after launch.
        \n4️. Set Network Effect Strength\n
        This controls how much existing users influence new users to buy the product.
        \n5️. Choose Marketing Strength / Hype Level\n
        Higher marketing or hype increases product popularity faster.
        \n6️. Select Simulation Days\n
        Choose how many days you want the model to simulate product growth.
        \n7️. Run the Simulation\n
        The model will generate results based on the selected inputs.
        \n8️. View the Results\n
        The app will display:
        📈 Popularity growth chart
        🔥 Hype score
        👥 User distribution (early adopters, buyers, passive users)
        📊 Prediction of product success""")
        st.button("**BACK**",on_click=pageone)
            
        
    