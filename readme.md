# Funduk-Script (`.fnd`)

> **The Esoteric, Politeness-Enforced & Case-Alternating Programming Language**

**Funduk-Script** is an experimental, transpiled esoteric programming language written in **Python 3.10**. It is designed to maximize syntactic frustration and mental discipline by enforcing absolute conversational etiquette, strict capitalization rhythms, and explicit ASCII-character construction.

---

## 🛠 System Requirements & Installation

* **Runtime:** Python 3.10 or higher
* **Dependencies:** Standard Library only (`sys`, `re`)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/Funduk34/funduk-lang.git
cd funduk-lang
```
2. Verify Python version:
```bash
python --version
# Expected output: Python 3.10.x
```

---

## 📐 Core Language Mechanics & Rules

Funduk-Script source files must use the `.fnd` extension. To successfully compile and execute a `.fnd` script, the source code must strictly comply with **three core constraints**:

### 1. Mandatory Politeness Protocol (MPP)
Funduk-Script requires absolute deference to the runtime engine. Every script **must** begin with a specific formal greeting on line 1 and end with a formal sign-off on the final line.

* **Line 1 (Opening Header):** `Здравствуйте глубокоуважаемый Фундук`
* **Last Line (Closing Footer):** `Спасибо за Орехи до Свидания`

> *Failure to include these exact phrases triggers an `UnpoliteNutError` and halts execution immediately.*

---

### 2. Sponging Case-Alternarchy Rule
To eliminate developer comfort, **every single word token** across the entire document must strictly alternate between starting with an uppercase letter and starting with a lowercase letter.

* **Token #1 (Odd):** Starts with **Uppercase** (e.g., `Здравствуйте`)
* **Token #2 (Even):** Starts with **lowercase** (e.g., `глубокоуважаемый`)
* **Token #3 (Odd):** Starts with **Uppercase** (e.g., `Фундук`)
* **Token #4 (Even):** Starts with **lowercase** (e.g., `фундучище`)

> *A single misplaced `Shift` key press triggers a `CaseAnarchyError` pointing directly to the offending token index.*

---

### 3. ASCII Synthesis Evaluation
String output is not defined through standard string literals. Instead, individual characters are dynamically constructed by evaluating weight-based nut operators in sequence:

Character Code = (count("фундучище") * 10) + count("фундучек") - count("гнилушка")

| Operator Token | Operation | Description |
| :--- | :--- | :--- |
| `фундучище` | +10 | Adds 10 to the target ASCII accumulator |
| `фундучек` | +1 | Adds 1 to the target ASCII accumulator |
| `гнилушка` | -1 | Subtracts 1 from the target ASCII accumulator |
| `выплюнуть фундук` | `print(chr(N))` | Evaluates accumulated sum, converts to character, and outputs it |

---

## 🔤 Syntax Mapping (Python 3.10 Engine)

Funduk-Script maps core Python control-flow structures to nut-themed equivalents during compilation:

| Funduk Keyword | Python Equivalent | Purpose |
| :--- | :--- | :--- |
| `фундук чини` | `def` | Function definition |
| `фундук хавен` | `while` | While loop |
| `фундук орех` | `if` | Conditional IF |
| `иначе орех` | `elif` | Conditional ELIF |
| `совсем гнилой` | `else` | Conditional ELSE |
| `приравнять` | `=` | Assignment operator |
| `жареный фундук` | `print()` | Standard console output |
| `вскопать` | `input()` | User input stream |
| `скорлупа` | `pass` | Null statement |
| `расколоть` | `break` | Loop termination |
| `орешек` | `:` | Block delimiter |
| `фундуковать` | `import` | Module import |

---

## 🚨 Runtime & Compile Exception Reference

* **`UnpoliteNutError`**: Thrown when the script omits the mandatory greeting or closing statement, or puts them on the wrong lines.
* **`CaseAnarchyError`**: Thrown when word token capitalization rhythm breaks sequence.

---

## 🚀 Usage & Code Example

To run a script using the main interpreter:

```bash
python compiler.py script.fnd
```

### Valid `script.fnd` Example
The following 3-line file produces the output `H` (ASCII code 72):

```text
Здравствуйте глубокоуважаемый Фундук
фундучище Фундучище фундучище Фундучище фундучище Фундучище фундучище Фундучек фундучек Выплюнуть фундук
Спасибо за Орехи до Свидания
```

### Token Rhythm Breakdown
1. `Здравствуйте` (Odd -> Upper)
2. `глубокоуважаемый` (Even -> Lower)
3. `Фундук` (Odd -> Upper)
4. `фундучище` (Even -> Lower)
5. `Фундучище` (Odd -> Upper)
6. `фундучище` (Even -> Lower)
...and so on.

---

## 📄 License
Distributed under the MIT License.