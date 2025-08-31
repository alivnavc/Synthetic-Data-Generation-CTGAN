#  Data Synthesizer using CTGAN & Streamlit

This project provides a **Streamlit web app** that allows users to upload a CSV file and generate **synthetic tabular data** using the **CTGAN (Conditional Tabular GAN)** model.

The app enables you to:

* Upload your dataset (`.csv`)
* Define **column data types** (categorical, datetime, numerical, ID)
* Select a **primary key**
* Train a **CTGAN model** on your dataset
* Generate synthetic data with the desired number of rows
* View the generated synthetic data directly in the app

---

## Features

* Interactive **Streamlit UI**
* Supports **custom metadata** definition
* Generates high-quality **synthetic tabular data**
* Helps with **data privacy** & **augmentation** use cases
* Easy to deploy (local or cloud)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/alivnavc/Synthetic-Data-Generation-CTGAN.git
cd Synthetic-Data-Generation-CTGAN
pip install -r requirements.txt
```

---

## 🛠 Requirements

`requirements.txt` should include:

```
streamlit
pandas
sdv
```

(You may also need `torch` depending on your environment, since CTGAN uses PyTorch.)

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Upload your CSV file
* Select **data types** for each column
* Choose the **primary key**
* Enter the number of synthetic rows to generate
* Click **Submit**
* View your synthetic dataset in the browser

---

## Demo

Example workflow:

1. Upload your dataset
2. Configure column types
3. Generate synthetic data


## References

* [SDV Documentation](https://sdv.dev/)
* [CTGAN Paper](https://arxiv.org/abs/1907.00503)
* [Streamlit](https://streamlit.io/)

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

