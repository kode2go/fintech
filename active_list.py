import streamlit as st
from streamlit_lottie import st_lottie
import json

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

def active_list():
    st.title("Active Listening Diagnostic")

    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.subheader("Instructions for Completing the Diagnostic:")
            st.markdown("""There are 15 questions listed below organized into 5 categories. Answer each question by entering an 'X' in one of the 5 boxes next to the question.  Please be careful to note how the scale should be applied for each question.  Sometimes the scale goes from 'Not at All' to 'Very Often' and sometimes the scale is reversed.  A summary score can be found at the bottom of the diagnostic tool.""")
    
        with col2:
            lottie2 = load_lottiefile("form.json")
            st_lottie(lottie2,key='place',height=300,width=300)
   
    with st.form("listening_diagnostic_form"):
        avoiding_interruption_scores = []
        st.header("Avoiding Interruption")
        avoiding_interruption_questions = [
            "I am mindful to let the other person finish talking before sharing my thoughts.",
            "I jump into conversations to present my views rather than wait and risk forgetting what I wanted to say.",
            "I stop the speaker and give my opinion when I disagree with something he or she has said."
        ]
        for idx, question in enumerate(avoiding_interruption_questions, start=1):
            st.subheader(f"Question {idx}")
            scale_options = ["Not at All", "Rarely", "Sometimes", "Often", "Very Often"]
            avoiding_interruption_scores.append(st.radio(question, scale_options,horizontal=True))

        postponing_evaluation_scores = []
        st.header("Postponing Evaluation")
        postponing_evaluation_questions = [
            "I keep an open mind about the speaker’s point of view until he / she has finished talking.",
            "I don’t evaluate what a person is saying until he or she has finished talking.",
            "While the speaker is talking, I quickly determine whether I like or dislike his or her ideas."
        ]
        for idx, question in enumerate(postponing_evaluation_questions, start=4):
            st.subheader(f"Question {idx}")
            scale_options = ["Not at All", "Rarely", "Sometimes", "Often", "Very Often"]
            postponing_evaluation_scores.append(st.radio(question, scale_options,horizontal=True))

        showing_interest_scores = []
        st.header("Showing Interest")
        showing_interest_questions = [
            "People can tell when I’m not concentrating on what they are saying.",
            "I nod my head and make other gestures to show I’m interested in the conversation.",
            "I say things like “I see” or “uh-huh” so people know that I’m really listening to them."
        ]
        for idx, question in enumerate(showing_interest_questions, start=4):
            st.subheader(f"Question {idx}")
            scale_options = ["Not at All", "Rarely", "Sometimes", "Often", "Very Often"]
            showing_interest_scores.append(st.radio(question, scale_options,horizontal=True))

        maintaining_interest_scores = []
        st.header("Maintaining Interest")
        maintaining_interest_questions = [
            "When someone takes a long time to present a simple idea, I let my mind wander to other things.",
            "I keep focused on what people are saying to me even when they don’t sound interesting.",
            "I pay close attention to what people are saying even when they are explaining something I already know."
        ]
        for idx, question in enumerate(maintaining_interest_questions, start=4):
            st.subheader(f"Question {idx}")
            scale_options = ["Not at All", "Rarely", "Sometimes", "Often", "Very Often"]
            maintaining_interest_scores.append(st.radio(question, scale_options,horizontal=True))

        organizing_information_scores = []
        st.header("Organizing Information")
        organizing_information_questions = [
            "While listening, I mentally sort out the speaker’s ideas in a way that makes sense to me.",
            "Rather than organizing the speaker’s ideas, I expect the person to summarize them for me.",
            "While listening, I concentrate on what is being said and regularly organize the information."
        ]
        for idx, question in enumerate(organizing_information_questions, start=4):
            st.subheader(f"Question {idx}")
            scale_options = ["Not at All", "Rarely", "Sometimes", "Often", "Very Often"]
            organizing_information_scores.append(st.radio(question, scale_options,horizontal=True))

        submitted = st.form_submit_button("Submit")

        if submitted:
            avoiding_interruption_total_score = sum([scale_options.index(score) + 1 for score in avoiding_interruption_scores])
            postponing_evaluation_total_score = sum([scale_options.index(score) + 1 for score in postponing_evaluation_scores])
            showing_interest_total_score = sum([scale_options.index(score) + 1 for score in showing_interest_scores])
            maintaining_interest_total_score = sum([scale_options.index(score) + 1 for score in maintaining_interest_scores])
            organizing_information_total_score = sum([scale_options.index(score) + 1 for score in organizing_information_scores])
            
            avoiding_interruption_percentage = (avoiding_interruption_total_score / 15) * 100
            postponing_evaluation_percentage = (postponing_evaluation_total_score / 15) * 100
            showing_interest_percentage = (showing_interest_total_score / 15) * 100
            maintaining_interest_percentage = (maintaining_interest_total_score / 15) * 100
            organizing_information_percentage = (organizing_information_total_score / 15) * 100
            
            # st.header("Summary")
            # st.write("Scores:")
            # st.write(f"Avoiding Interruption: {avoiding_interruption_total_score}/15 ({avoiding_interruption_percentage:.2f}%)")
            # st.write(f"Postponing Evaluation: {postponing_evaluation_total_score}/15 ({postponing_evaluation_percentage:.2f}%)")
            # st.write(f"Showing Interest: {showing_interest_total_score}/15 ({showing_interest_percentage:.2f}%)")
            # st.write(f"Maintaining Interest: {maintaining_interest_total_score}/15 ({maintaining_interest_percentage:.2f}%)")
            # st.write(f"Maintaining Interest: {organizing_information_total_score}/15 ({organizing_information_percentage:.2f}%)")
            # st.write("Maximum possible score: 15")

            st.header("Summary")
            summary_table = f"""
            | Aspect | Total Score | Percentage |
            | ------ | ----------- | ---------- |
            | Avoiding Interruption | {avoiding_interruption_total_score} | {avoiding_interruption_percentage:.2f}% |
            | Postponing Evaluation | {postponing_evaluation_total_score} | {postponing_evaluation_percentage:.2f}% |
            | Showing Interest | {showing_interest_total_score} | {showing_interest_percentage:.2f}% |
            | Maintaining Interest | {maintaining_interest_total_score} | {maintaining_interest_percentage:.2f}% |
            | Organizing Information | {organizing_information_total_score} | {organizing_information_percentage:.2f}% |
            | Maximum possible score | 15 | - |
            """
            st.markdown(summary_table)




