import mysql.connector
import streamlit as st

#Establish a connection to Mysql server
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vasanthi@78",
    database="crud_new1"
)
mycursor=mydb.cursor()
print("Connection Established")

#Create streamlit App
def main():
    st.title("CRUD Operations with MYSQL")
    #Display Options for CRUD Operations
    option=st.sidebar.selectbox("# Select an Opeation",["Create","Read","Update","Delete"])
    #perform selected CRUD operation
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Name")
        email=st.text_input("Enter Email")
        if st.button("Create"):
            sql="insert into users(name,email) values(%s,%s)"
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully")

    elif option=="Read":
        st.subheader("Read Records")
        mycursor.execute("select * from users")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)
    elif option=="Update":
        st.subheader("Update a Record")
        id=st.text_input("Enter ID")
        name=st.text_input("Enter the new name")
        email=st.text_input("Enter the new email")
        if st.button("update"):
            sql="Update users set name=%s,email=%s where id=%s"
            val=(name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")

    elif option=="Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter Id",min_value=1)
        if st.button("Delete"):
            sql="delete from users where id=%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Delete Record Successfully!!!")






if __name__=="__main__":
    main()