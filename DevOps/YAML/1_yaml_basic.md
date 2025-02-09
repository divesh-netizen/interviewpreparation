
---

# **📌 Day 1: YAML Basics - Full Dive**
> 🎯 Goal: Understand YAML syntax, structure, and how it differs from JSON.  

## **🔹 1. What is YAML?**
YAML (**YAML Ain’t Markup Language**) is a **human-readable data format** often used for configuration files and data exchange between languages.  

💡 **Why YAML for DevOps & CI/CD?**  
✅ Easy to read & write  
✅ Used in CI/CD pipelines (GitHub Actions, Bitbucket Pipelines, GitLab CI, Azure DevOps)  
✅ Supports complex data structures (Lists, Dictionaries, etc.)  
✅ Used in **Kubernetes, Ansible, Terraform, Docker Compose, CloudFormation**  

---

## **🔹 2. YAML Syntax Basics**
Let's cover the **essential rules** of YAML.

### **🟢 2.1 Key-Value Pairs (Basic Structure)**
```yaml
name: John Doe
age: 30
city: New York
```
✔️ `name`, `age`, and `city` are **keys**  
✔️ `John Doe`, `30`, and `New York` are **values**  

---

### **🟢 2.2 Indentation (No Tabs Allowed!)**
✔️ **YAML is indentation-sensitive!**  
✔️ Use **spaces only (2 or 4 spaces recommended)**  
✔️ Do **NOT** use tabs  

```yaml
person:
  name: John Doe
  age: 30
  city: New York
```
🔹 **Correct**: Indentation with spaces  
❌ **Wrong**: Indentation with tabs  

---

### **🟢 2.3 Lists (Arrays)**
Lists in YAML use `-` (dash) notation:

```yaml
fruits:
  - Apple
  - Banana
  - Orange
```

🔹 Equivalent JSON:
```json
{
  "fruits": ["Apple", "Banana", "Orange"]
}
```

✔️ **Inline List (One-Liner Format)**
```yaml
fruits: [Apple, Banana, Orange]
```

---

### **🟢 2.4 Dictionaries (Nested Key-Value Pairs)**
Dictionaries (Objects) allow hierarchical data.

```yaml
person:
  name: John Doe
  details:
    age: 30
    city: New York
    skills:
      - DevOps
      - Python
      - AWS
```

🔹 Equivalent JSON:
```json
{
  "person": {
    "name": "John Doe",
    "details": {
      "age": 30,
      "city": "New York",
      "skills": ["DevOps", "Python", "AWS"]
    }
  }
}
```

✔️ **Inline Dictionary Format**
```yaml
person: {name: John Doe, age: 30, city: New York}
```

---

### **🟢 2.5 Multi-Line Strings**
If a string is long, we can break it into multiple lines.

✔️ **Preserve newlines (`|` - Literal Block Scalar)**
```yaml
bio: |
  John Doe is a DevOps engineer.
  He specializes in CI/CD and cloud infrastructure.
```

✔️ **Collapse newlines (`>` - Folded Block Scalar)**
```yaml
bio: >
  John Doe is a DevOps engineer.
  He specializes in CI/CD and cloud infrastructure.
```
🔹 **Difference:**  
`|` (pipe) → **Preserves line breaks**  
`>` (greater-than) → **Joins lines into one**  

---

### **🟢 2.6 Comments in YAML**
```yaml
# This is a comment
name: John Doe  # Inline comment
```
✔️ Comments start with `#`  
✔️ YAML **does not support block comments**  

---

## **🔹 3. YAML vs JSON**
| Feature         | YAML                          | JSON                          |
|---------------|----------------------------|----------------------------|
| **Readability**  | Human-friendly ✅  | Machine-friendly ❌ |
| **Syntax**  | Uses indentation | Uses brackets `{}` and `[]` |
| **File Size**  | Smaller (no brackets) | Bigger (with brackets) |
| **Data Types**  | Supports lists, dictionaries, strings | Same as YAML |
| **Multi-line**  | Supports multi-line (`|` and `>`) | Must use `\n` |

🔹 **Example Comparison**
✔️ YAML:
```yaml
person:
  name: "John Doe"
  age: 30
  languages:
    - Python
    - JavaScript
```
✔️ JSON:
```json
{
  "person": {
    "name": "John Doe",
    "age": 30,
    "languages": ["Python", "JavaScript"]
  }
}
```

---

## **🔹 4. Hands-on Practice**
### **🚀 Task 1: Write a YAML File**
✅ Create a YAML file named `config.yml`  
✅ Define the following:  
- **name**: Your Name  
- **age**: Your Age  
- **skills**: List of your skills  
- **experience**: Nested object (years, company, role)  

📌 **Example:**
```yaml
name: Alice Johnson
age: 28
skills:
  - DevOps
  - Kubernetes
  - Terraform
experience:
  years: 5
  company: TechCorp
  role: Senior DevOps Engineer
```
---

### **🚀 Task 2: Convert YAML to JSON**
Use Python to convert a YAML file to JSON.

📌 **Python Script (`convert_yaml_to_json.py`)**
```python
import yaml
import json

with open("config.yml", "r") as file:
    yaml_data = yaml.safe_load(file)

json_data = json.dumps(yaml_data, indent=2)
print(json_data)
```
Run it:
```sh
python convert_yaml_to_json.py
```
🎯 **Expected Output**
```json
{
  "name": "Alice Johnson",
  "age": 28,
  "skills": ["DevOps", "Kubernetes", "Terraform"],
  "experience": {
    "years": 5,
    "company": "TechCorp",
    "role": "Senior DevOps Engineer"
  }
}
```

---

### **🔹 5. Best Practices for YAML**
✅ **Use 2 spaces for indentation** (avoid tabs)  
✅ **Use `---` to separate multiple YAML documents in one file**  
✅ **Use anchors (`&`) and aliases (`*`) to avoid repetition**  
✅ **Use environment variables for sensitive values (CI/CD Secrets)**  

---

## **🔹 Summary**
✅ YAML is widely used in DevOps & CI/CD  
✅ YAML syntax is **indentation-based** and uses `-`, `:` for structure  
✅ YAML supports **lists, dictionaries, multi-line strings, and comments**  
✅ YAML is **more human-readable** than JSON  
✅ YAML is used in **GitHub Actions, Kubernetes, Docker Compose, Terraform**  

---
