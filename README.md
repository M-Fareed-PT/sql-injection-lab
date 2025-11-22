# sql-injection-lab
# 💉 SQL Injection Lab  
A deliberately vulnerable SQL injection lab environment designed for learning, practicing, and demonstrating SQL injection attacks and defenses.

This project simulates a basic web application + backend database with intentional SQL injection flaws.

---

## 🎯 Objectives
- Understand how SQL injection works  
- Practice exploiting different SQL injection types  
- Learn how to extract data using injection  
- Explore authentication bypass via SQLi  
- Test UNION-based, error-based, and boolean-based attacks  
- Learn how to fix insecure queries

---

## 🚀 Features
✔ Vulnerable login form  
✔ Search/functionality with injectable queries  
✔ Multiple SQL injection points  
✔ Sample database with users & secrets  
✔ Attack + defense examples  
✔ Can be used with tools like sqlmap  

---

## 🧠 Skills Demonstrated
- Web app hacking basics  
- SQL injection exploitation  
- Database enumeration via SQLi  
- Secure coding & parameterization  
- Input validation & sanitization concepts  
- Offensive + defensive mindset  

---

## 📁 Project Structure
```text
sql-injection-lab/
│── db_init.sql              # Creates vulnerable DB schema & data
│── insecure_queries.sql     # Contains intentionally insecure queries
│── README.md
└── (optional web part)
    ├── index.php            # Login / search page (vulnerable)
    ├── config.php           # DB connection settings
    └── other vulnerable endpoints
