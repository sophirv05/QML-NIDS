# Hybrid quantum machine learning for network intrusion detection: a hardware application

Core concept: Process classical data and encode using QuASK's quantum kernel method; train and evlauate on SVM to classify intrusion detection points as benign or anomalous. 

**Usage:**
Set up virtual environment and install dependencies from requirements.txt with pip install -r requirements.txt.

Preprocess data if necessary & convert to numpy arrays (PREPROCESSING.py). 

Locate QuASK package and replace core/kernel.py with the provided updated_kernel.py. Perform same for core_implementation/qiskit_kernel.py with updated_qiskit_kernel.py.

Run in NIDS-QKERNEL.ipynb (supports simulator and hardware testing)
