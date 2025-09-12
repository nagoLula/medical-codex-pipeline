# Medical Codex Pipeline

This repository contains a pipeline for processing and standardizing medical codex reference files.  
The purpose is to normalize different coding systems into a consistent format.

---

##  Repository Structure
medical-codex-pipeline/
├── input/ # Raw source files (ignored in git)
│ ├── snomed/
│ ├── icd10cm/
│ ├── icd10who/
│ ├── hcpcs/
│ ├── loinc/
│ ├── rxnorm/
│ └── NPI.csv
├── scripts/ # Processors for each codex
│ ├── snomed_processor.py
│ ├── icd10cm_processor.py
│ ├── icd10who_processor.py
│ ├── hcpcs_processor.py
│ ├── loinc_processor.py
│ ├── rxnorm_processor.py
│ └── npi_processor.py
├── output/
│ └── csv/ # Standardized outputs
├── utils/
│ └── common_functions.py # Shared helper functions
├── requirements.txt # Python dependencies
└── README.md # Documentation

Data Sources
ICD-10-CM (US):
icd10OrderFiles2025_0 (2)

HCPCS (US):
CMS Healthcare Common Procedure Coding System
HCPCS Data Files

NPI (US):
National Plan and Provider Enumeration System (NPPES)
NPI Registry Downloadable Files

Supported files
SNOMED CT (US edition)

ICD-10-CM (US)

ICD-10 (WHO)

HCPCS

LOINC

RxNorm

NPI

Setup instructions:
Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/medical-codex-pipeline.git
   cd medical-codex-pipeline

   python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt



