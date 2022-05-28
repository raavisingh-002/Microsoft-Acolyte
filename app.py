import streamlit as st
import json
from classfier import KNearestNeighbours
from operator import itemgetter
import base64
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('mss.jpg')

with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'names.json', 'r+', encoding='utf-8') as f:
    app_titles = json.load(f)

def knn(test_point, k):
    
    target = [0 for item in app_titles]
    
    model = KNearestNeighbours(data, target, test_point, k=k)
   
    model.fit()
    
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    
    table = list()
    for i in model.indices:
        
        table.append([app_titles[i][0], app_titles[i][2]])
    return table

if __name__ == '__main__':
    keyword = ['analytics',
 'animations',
 'appointments',
 'automate-content-processing',
 'automating-processes',
 'blank-canvas',
 'blogs',
 'bookings',
 'branding',
 'browsing',
 'business',
 'calendar',
 'charting',
 'cloud',
 'collaboration',
 'communications',
 'company',
 'connection',
 'content',
 'content-classification',
 'control',
 'conversation',
 'creative-writing',
 'custom-apps',
 'daily-planner',
 'data',
 'data-analysis',
 'data-grading',
 'dbms',
 'defence',
 'diagrams',
 'documentation',
 'dynamic-storage',
 'employee',
 'endpoint',
 'enterprise',
 'family safety',
 'files',
 'format',
 'freestyle-writin',
 'graphics',
 'identity',
 'kids mode',
 'large-group-discussion',
 'letters',
 'machine-learning-models',
 'mail',
 'management',
 'mobile',
 'online-meetings',
 'operating-systems',
 'organisation',
 'personal-task',
 'presentation',
 'productivity',
 'progress',
 'protection',
 'publish',
 'reminders',
 'report',
 'save-photos',
 'schedule-meetings',
 'scheduling-emails',
 'security',
 'services',
 'set-task',
 'small-group',
 'suite',
 'threat',
 'vba',
 'video',
 'video-calling',
 'virtual-machine',
 'web-clipper']
    apps_ms = [title[0] for title in app_titles]
    st.header('Microsoft-Acolyte') 
    apps = ['--Select--', 'App name based', 'Feature based']   
    app_options = st.selectbox('Choose from:', apps)
    
    if app_options == 'App name based':
        app_select = st.selectbox('Select APP:', ['--Select--'] + apps_ms)
        if app_select == '--Select--':
            st.write('Select an APP')
        else:
            n = st.number_input('Number of APPs:', min_value=1, max_value=5, step=1)
            apii = data[apps_ms.index(app_select)]
            test_point = apii
            table = knn(test_point, n)
            for i, link in table:
                st.markdown(f"[{i}]({link})")
    elif app_options == apps[2]:
        options = st.multiselect('Select Features:', keyword)
        if options:
            version_score = st.slider('score:', 1, 10, 8)
            n = st.number_input('Number of APPs:', min_value=1, max_value=5, step=1)
            test_point = [1 if i in options else 0 for i in keyword]
            test_point.append(version_score)
            table = knn(test_point, n)
            for i, link in table:
                st.markdown(f"[{i}]({link})")
        else:
                st.write("This is a simple Microsoft Apps Recommender application. "
                        "You can select the features and change the version score.")
    else:
        st.write('Select option')