🛒IKart – Modern Multi-Vendor E-Commerce Marketplace
IKart is a scalable, role-based multi-vendor e-commerce platform built using Python, Django, HTML5, and Tailwind CSS. It enables independent sellers to register, set up storefronts, and manage inventory, while offering buyers a unified catalog, search, and checkout experience.

🚀 Live Demo 
Live Demo (Vercel):https://ikart-marketplace-j3mx8zzj3-kuldeep-2f42.vercel.app/

✨ Features
🛍️ Customer Storefront
Dynamic Marketplace Catalog: Grid-based layout with responsive cards and active category filtering.
Global Search: Real-time multi-field search across product titles, descriptions, and store names.
Product Details: High-resolution product showcase with stock indicators and verified merchant bios.

🏪 Seller Hub (Vendor Portal)
Dedicated Onboarding: Custom registration flow with automated seller role assignment.
Storefront Bio & Status: Public store descriptions and verification badging
Inventory Management: Product uploads with image support, category selection, price, and stock controls.

🛡️ Admin Controls
Role-Based Access: Custom user model powered by Django's AbstractUser (is_vendor, is_customer).
Commission Management: Configurable commission percentage tracking per vendor store.

🛠️ Tech Stack
Backend: Python 3, Django (MTV Architecture, Custom User Models, ORM)
Frontend: HTML5, Tailwind CSS, FontAwesome Icons
Database: SQLite (Local Development) / PostgreSQL-compatible
Deployment: Vercel (Serverless Python WSGI Runtime)
