
---

# 🎟️ **Ticket Booking Management System**

An interactive, fully containerized **Django web application** to manage ticket bookings for events and shows. From browsing events to real-time seat selection and a custom admin dashboard — this project is built with a focus on **usability, scalability, and clean code practices**.

✨ **Built with Class-Based Views (CBVs)** and hand-coded forms — no Django shortcuts. Just pure logic.

---

## 👨‍💻 **Developer Info**
- **Name:** Prabhat Kale  
- **Roll No:** 44

---

## 🌟 **Why This Project?**

Most ticket booking systems rely heavily on Django’s default features. But not this one. This system is:

- ✅ **Fully Custom-Built** — No Django Admin, no built-in forms  
- ✅ **DevOps-Ready** — Integrated with Docker & Jenkins  
- ✅ **Student-Friendly** — Easy to set up, explore, and expand  
- ✅ **Realistic UI** — Seats, booking history, and show management — all built to simulate real-world platforms  

---

## 📌 **Table of Contents**
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [DevOps Integration](#-devops-integration)
- [Screenshots](#-screenshots)
- [Setup Instructions](#️-setup-instructions)
- [Project Structure](#-project-structure)
- [Developer Info](#-contact--developer-info)
- [Contributing](#-contributing--feedback)

---

## 🚀 **Features**

### 👤 **User Panel**
- 🔐 **Authentication** – Register, login, logout securely  
- 📅 **Browse Events** – Upcoming shows, details & availability  
- 🪑 **Select Seats** – Dynamic, clickable seat selection interface  
- 📖 **Booking History** – Personalized list of all your past bookings  

### 🛠️ **Admin Panel (Custom-Built)**
- ➕ **Add/Edit/Delete Shows**  
- 📋 **View & Manage all user bookings**  
- 💡 **Modern UI** – Replaces Django's default admin interface  

### 💡 **Extra Goodies**
- 💻 **Clean, modular code structure**  
- 🧩 **Easy to integrate with payment gateways**  
- 🖱️ **Responsive & intuitive frontend**  

---

## 🛠️ **Tech Stack**

| **Layer**     | **Tech Used**                   |
|---------------|---------------------------------|
| **Frontend**  | HTML5, CSS3, JavaScript         |
| **Backend**   | Django (Python 3.x)             |
| **Database**  | PostgreSQL (via Docker)         |
| **DevOps**    | Docker, Docker Compose, Jenkins |
| **Others**    | Git, REST, CBVs                 |

---

## 🐳 **DevOps Integration**

### 🚢 **Dockerized App**
- Instant containerized deployment with `Dockerfile` and `docker-compose.yml`  
- All dependencies packed and ready for any environment  

### 🛠️ **CI/CD with Jenkins**
- `Jenkinsfile` handles build/test/deploy automatically  
- Scalable for future cloud deployment  

---

## 🖼️ **Screenshots**

🖼️ Screenshots
![Screenshot 2025-04-25 222152](https://github.com/user-attachments/assets/e1c3f0e8-195b-474c-842d-7bc279a110df)

![Screenshot 2025-04-25 222220](https://github.com/user-attachments/assets/dfaba58e-4acd-4bbb-a198-b88328a096ee)

![Screenshot 2025-04-25 222239](https://github.com/user-attachments/assets/7a637e4f-3f24-495d-b7b7-0bf0346c1f15)

![Screenshot 2025-04-25 222250](https://github.com/user-attachments/assets/d20a9460-78ed-475d-bf63-c0cd3606cfa7)

![Screenshot 2025-04-25 222354](https://github.com/user-attachments/assets/d9dbbfc8-1ee2-4fe1-b7b2-8ec454c08cb2)

| | |
|:--:|:--:|
| ![Booking History](https://github.com/user-attachments/assets/e1c3f0e8-195b-474c-842d-7bc279a110df) | ![Admin Dashboard](https://github.com/user-attachments/assets/dfaba58e-4acd-4bbb-a198-b88328a096ee) |
| ![Seat Selection](https://github.com/user-attachments/assets/7a637e4f-3f24-495d-b7b7-0bf0346c1f15) | ![Events List](https://github.com/user-attachments/assets/d20a9460-78ed-475d-bf63-c0cd3606cfa7) |
| ![Home Page](https://github.com/user-attachments/assets/d9dbbfc8-1ee2-4fe1-b7b2-8ec454c08cb2) | |

---

## ▶️ **Setup Instructions**

```bash
# 1. Clone the Repository
git clone https://github.com/kaleprabhat24/ticket_booking.git
cd booking-ticket-app

# 2. Build & Run using Docker
docker-compose up --build

# 3. Access the Web App
http://localhost:8090/
```

---

## 📁 **Project Structure**

```bash
BOOKING-TICKET-APP/
├── ticket_booking/             # Django project settings
│   ├── settings.py, urls.py
├── core/                       # Main application logic
│   ├── models.py, views.py, templates/
├── static/                     # CSS, JS, images
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── manage.py
└── screenshots/                # UI previews
```

---

## 📬 **Contact & Developer Info**
- 👨‍💻 **Developer:** Prabhat Kale  
- 🎓 **Roll No:** 44  

---

## 🙌 **Contributing & Feedback**

Have an idea? Found a bug?  
Feel free to **fork**, **star ⭐**, or **raise an issue**!  
Your feedback is invaluable.

---

🔥 *This project is a perfect base for building movie, concert, or even sports ticketing platforms. Clean code, modular design, and scalable setup make it developer-friendly and fun to expand!*

---
