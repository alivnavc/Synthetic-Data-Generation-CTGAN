# import streamlit as st
# import pandas as pd
# from sdv.single_table import CTGANSynthesizer
# from sdv.metadata import SingleTableMetadata

# def main():
#   st.title("Data Synthesizer")

#   # File upload
#   uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
#   if uploaded_file is not None:
#     try:
#       df = pd.read_csv(uploaded_file)
#       st.write("Uploaded Data:")
#       st.dataframe(df)

#       # Handle missing values (optional)
#       # df = df.dropna()  # Example for removing rows with missing values

#       # Metadata definition
#       metadata = SingleTableMetadata()
#       metadata.add_column('delivery_date', sdtype='datetime')
#       metadata.add_column('external_log_provider', sdtype='categorical')
#       metadata.add_column('order_id', sdtype='id')
#       metadata.add_column('plant_id', sdtype='categorical')
#       metadata.add_column('price', sdtype='numerical')
#       metadata.add_column('product_id', sdtype='categorical')
#       metadata.add_column('purchase_order_date', sdtype='datetime')
#       metadata.add_column('quantity', sdtype='numerical')
#       metadata.add_column('requisition_date', sdtype='datetime')
#       metadata.add_column('ship_from', sdtype='categorical')
#       metadata.add_column('ship_to', sdtype='categorical')
#       metadata.add_column('status', sdtype='categorical')
#       metadata.add_column('transportation_mode', sdtype='categorical')
#       metadata.add_column('vendor_id', sdtype='id')
#       metadata.add_column('zio_from', sdtype='categorical') 
#       metadata.add_column('zip_to', sdtype='categorical')
#       metadata.set_primary_key('order_id')

#       # Train the CTGAN model
#       model = CTGANSynthesizer(metadata)
#       model.fit(df)

#       # Generate synthetic data
#       num_rows = st.number_input("Number of synthetic rows to generate", min_value=1, value=50)
#       if st.button("Generate Synthetic Data"):
#         new_data = model.sample(num_rows)
#         st.write("Synthetic Data:")
#         st.dataframe(new_data)
#     except Exception as e:
#       st.error(f"An error occurred: {e}")

# if __name__ == "__main__":
#   main()
import streamlit as st
import pandas as pd
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata

def main():
    st.title("Data Synthesizer")

    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Uploaded Data:")
            st.dataframe(df)

            # Display column names and their data types
            columns = df.columns.tolist()
            data_types = ["categorical","datetime", "id", "numerical"]
            metadata = SingleTableMetadata()

            # Create dropdowns for each column to select its data type
            column_data_types = {}
            for column in columns:
                column_data_types[column] = st.selectbox(f"Select data type for column: {column}", data_types, key=column)

            # Set primary key
            primary_key = st.selectbox("Select the primary key column", columns)

            # Number of synthetic rows to generate
            num_rows = st.number_input("Number of synthetic rows to generate", min_value=1, value=50)

            # Submit button
            if st.button("Submit"):
                # Add columns to metadata
                for column, dtype in column_data_types.items():
                    metadata.add_column(column, sdtype=dtype)
                metadata.set_primary_key(primary_key)

                # Train the CTGAN model
                model = CTGANSynthesizer(metadata)
                model.fit(df)

                # Generate synthetic data
                new_data = model.sample(num_rows)
                st.write("Synthetic Data:")
                st.dataframe(new_data)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
