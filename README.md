# Programming Repository - Q2 2026

This repository contains the practical assignments and classwork corresponding to the second trimester of the Data Engineering and Cybersecurity academic program.

## Exercises

### 🔹 CW07: Check Digit Calculator (Dígito Verificador)

**Description:**
A Python-based application developed to calculate and validate check digits (dígitos verificadores). This project focuses on implementing data integrity principles by ensuring that input sequences match their corresponding validation codes, mimicking standard real-world cybersecurity and data entry verification protocols.

The project has been structured strictly according to the professor's architectural requirements, isolating the script inside its dedicated directory.

**Key Features:**
* **Data Validation:** Implements algorithms to compute verification digits for data compliance.
* **Standardized Structure:** Organizes source code neatly within the `CW07` directory.
* **Clean Code:** Written following Python's best practices for readability and maintenance.

**Execution Instructions:**
To run this program locally, ensure you have Python installed, navigate to the project root, and execute the following command in your terminal:

python Classwork7/CW07.py


### 🔹 CW08: Numerical Integration

**Description:**
This project implements mathematical numerical integration techniques using Python. It includes a structured algorithm capable of executing calculations through multiple integration methods, ensuring accurate approximation and logic design before the coding phase.

Following the strict architectural guidelines of the course, this assignment integrates comprehensive pseudocode documentation and visual logic flows alongside the production code.

**Key Features:**
* **Academic Pseudocode (PPP.txt):** Includes a detailed planning file structured in plain English, utilizing standard assignment arrows (<-) and comment hashes (#) without relying on Python syntax.
* **Logic Architecture (Flowchart.png):** Features a full algorithmic flowchart mapping the exact iteration flow for each method and the decision tree for the selection modes.
* **Segmented Source Code (numerical_integration.py):** A fully operational Python program organized strictly into standard architectural boundaries: # INPUT, # PROCESS, and # OUTPUT.

**Execution Instructions:**
To run the integration script locally, execute the following command in your terminal:

python Classwork8/CW08.py

### 🔹 CW09: Spanish Verb Conjugator

**Description:**
An automated application designed to process and execute Spanish verb conjugations utilizing Python. The system targets linguistic logic structures by mapping verb endings (`-ar`, `-er`, `-ir`) and processing them through iterative loops and decision-making matrices for different grammatical tenses and modes.

This project fulfills the full development cycle required by the course, incorporating architectural planning documentation and structured logic flowcharts prior to deployment.

**Key Features:**
* **Linguistic Pseudocode (`PPP.txt`):** Structured entirely in plain English using strict formatting rules (`←` for assignments and `#` for comments) to isolate algorithmic processes from syntax dependencies.
* **Algorithmic Flow (`Flowchart.png`):** A comprehensive diagram tracking the core selection mechanics for the conjugator modes and the internal loop paths for each conjugation method.
* **Architectural Source Code (`spanish_verb_conjugator.py`):** A functional Python script clearly partitioned into data entry, algorithmic computation, and result rendering using standard labels: `# INPUT`, `# PROCESS`, and `# OUTPUT`.

**Execution Instructions:**
To run the verb conjugator program locally, execute the following command in your terminal:

Classwork-09-Spanish-Verb-Conjugator/CW09.py

### 🔹 CW10: School Management System

**Description:**
A comprehensive Python application developed to simulate a foundational School Management System. This project integrates core data engineering principles by handling basic database operations, structuring student records, managing institutional metrics, and utilizing iterative validation loops to ensure information accuracy.

The project encompasses the complete logical pipeline required by the course, maintaining full alignment between architectural pseudocode planning, structural flowcharts, and the production script.

**Key Features:**
* **Academic Pseudocode (`PPP.txt`):** Formatted strictly in plain English utilizing standard assignment arrows (`←`) and comment hashes (`#`) to decouple algorithmic logic from language-specific syntax.
* **System Architecture (`Flowchart.png`):** A thorough logic diagram mapping out the decision trees for system modes and the precise iteration flows for administrative data routines.
* **Segmented Source Code (`school_management_system.py`):** An operational script neatly partitioned and labeled within standard architectural boundaries: `# INPUT`, `# PROCESS`, and `# OUTPUT`.

**Execution Instructions:**
To run the school management system locally, execute the following command in your terminal:

python Classwork-10-School-Management-System/school_management_system.py

### 🔹 Classwork 11: Mandelbrot Set Generator
**Description:**
A mathematical computational script developed in Python to generate data for the iconic Mandelbrot Set fractal. This project reads dynamic grid dimensions and coordinate boundaries from an external configuration file, applies complex number transformations within an escape-time algorithm, and exports the structural iteration matrix into a standardized CSV file for future data visualization.

The script models standard pipeline workflows: parsing configuration environments, executing intense nested loops for spatial mapping, and streaming tabular data efficiently.

**Key Features:**
* **Dynamic Configuration (`config.txt`):** Parses environmental parameters at runtime, allowing seamless modification of canvas dimensions (`ancho`, `alto`), maximum thresholds, and complex plane limits.
* **Mathematical Complex Mapping:** Translates 2D matrix indices (rows and columns) into equivalent real and imaginary numbers on the complex plane ($z = z^2 + c$).
* **Data Stream Engineering (`clase.csv`):** Systematically writes organized rows, columns, and iteration escape values to disk using standard comma-separated styling.

**Execution Instructions:**
To run the Mandelbrot computation script locally, ensure a valid `config.txt` file is present in the directory and execute:

### 🔹 Classwork 12: Mandelbrot Fractal Image Renderer

**Description:**
A data processing and visualization script that converts tabular numerical data into a high-resolution visual representation of the Mandelbrot Set fractal. This project parses spatial layout definitions from an external configuration file, ingests raw coordinate iteration streams from a CSV file, translates escape-time counts into dynamic HSV color values, and utilizes the Python Imaging Library (`PIL`/Pillow) to render and save the final fractal geometry into a production-ready PNG image.

The application implements standard data visualization architectures: transforming textual data matrices into multidimensional coordinate arrays, managing custom color models, and exporting optimized graphic media.

**Key Features:**
* **Tabular Data Ingestion:** Optimally reads structural coordinates and execution weights from disk (`clase.csv`), stripping header boundaries and streaming matrix data into memory arrays.
* **HSV Color Space Mapping:** Computes pixel brightness dynamically by normalising iterative escape factors against maximum thresholds ($iteraciones / max\_iter$), ensuring crisp contrast for bounded sets.
* **Image Synthesis Pipelines (`mandelbrot.clase.png`):** Maps logical rows and columns directly onto discrete coordinate matrices (`putpixel`), handle hue-saturation-value formatting, and converts assets to universal RGB bitstreams prior to saving.

**Execution Instructions:**
To run the Mandelbrot rendering script locally, ensure the processed `clase.csv` and a valid `config.txt` are located in your working workspace, and execute:
python Classwork-12-Mandelbrot-Renderer/mandelbrot_renderer.py


### 🔹 Classwork 13: Error Handling (CW07 to CW09 Refactoring)

**Description:**
A comprehensive code refactoring project focused on implementing robust error handling architecture across previous software assignments (`CW07`, `CW08`, and `CW09`). This assignment structures persistent input validation loops and exceptions matrices to secure applications against malformed data streams, invalid data types, mathematical anomalies, and runtime anomalies without risking systemic program collapse.

The suite aligns structural execution with standard reliability engineering principles, utilizing specialized try-except blocks to catch boundary constraints before processing pipeline segments.

**Key Features:**
* **Robust Check Digit Calculator (`CW07`):** Integrates nested validation blocks ensuring input sequences match rigorous standard alphanumeric boundaries, handling dynamic `ValueError` structures during character casting.
* **Fault-Tolerant Numerical Integration (`CW08`):** Restructures analytical logic sequences to capture integration boundaries, preventing script crashes triggered by math domain boundaries like `ZeroDivisionError`, `SyntaxError` within `eval()`, or illegal inputs.
* **Immune Spanish Verb Conjugator (`CW09`):** Hardens linguistic lookup arrays via conditional guards, managing custom string criteria and handling `KeyError` anomalies gracefully during linguistic dictionary lookups.

**Execution Instructions:**
To execute any of the refactored, error-immune scripts locally, navigate into the workspace folder and run the targeted script from your terminal:

To run the Refactored Check Digit Calculator
python Classwork-13-Error-Handling/check_digit_calculator.py

To run the Refactored Numerical Integration
python Classwork-13-Error-Handling/numerical_integration.py

To run the Refactored Spanish Verb Conjugator
python Classwork-13-Error-Handling/spanish_verb_conjugator.py

**AI Use Declaration:**
No AI tools were used during the algorithmic development, logic design, or version control setup of this specific assignment. All code, pseudocode, and flowcharts were created entirely by the author following course guidelines.
