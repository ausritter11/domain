import streamlit as st
from streamlit_app import contacts, linkedin_search, website_finder

st.title("Search Utility")

st.header("Contact Search")
contact_query = st.text_input("Enter contact name", key="contact")
if st.button("Search Contacts"):
    try:
        results = contacts.search_contacts(contact_query)
        st.write(results)
    except Exception as e:
        st.error(str(e))

st.header("LinkedIn Lookup")
linkedin_name = st.text_input("Enter LinkedIn profile name", key="linkedin")
if st.button("Lookup"):
    try:
        profile_info = linkedin_search.lookup_profile(linkedin_name)
        st.write(profile_info)
    except Exception as e:
        st.error(str(e))

st.header("Website Finder")
company_name = st.text_input("Enter company name", key="website")
if st.button("Find Website"):
    try:
        website_url = website_finder.find_website(company_name)
        st.write(website_url)
    except Exception as e:
        st.error(str(e))
