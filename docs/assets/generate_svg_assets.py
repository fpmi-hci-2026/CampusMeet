#!/usr/bin/env python3
"""
Generate professional SVG assets for CampusMeet Lab 2:
- 5 Low-fidelity Wireframes (Desktop Catalog, Desktop Details, Mobile Ticket, Mobile Scanner, Desktop Dashboard)
- 6 High-fidelity UI Mockups in color (Desktop Catalog, Desktop Details, Desktop Dashboard, Mobile Catalog, Mobile Ticket, Mobile Scanner)
"""

import os

os.makedirs("docs/assets/wireframes", exist_ok=True)
os.makedirs("docs/assets/mockups", exist_ok=True)

# -------------------------------------------------------------
# 1. WIREFRAMES
# -------------------------------------------------------------

def generate_wireframe_desktop_catalog():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" width="1440" height="900" font-family="'Inter', -apple-system, sans-serif">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.5"/>
    </pattern>
  </defs>
  <!-- Background -->
  <rect width="1440" height="900" fill="#f8fafc"/>
  <rect width="1440" height="900" fill="url(#grid)" opacity="0.6"/>

  <!-- Top Navigation Bar -->
  <rect x="0" y="0" width="1440" height="70" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="60" y="18" width="160" height="34" rx="6" fill="#0f172a"/>
  <text x="140" y="40" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">CampusMeet</text>

  <!-- Nav links -->
  <text x="270" y="41" fill="#0f172a" font-size="14" font-weight="600">Афиша</text>
  <line x1="270" y1="48" x2="320" y2="48" stroke="#0f172a" stroke-width="2"/>
  <text x="350" y="41" fill="#64748b" font-size="14">Хакатоны</text>
  <text x="450" y="41" fill="#64748b" font-size="14">Биржа команд</text>
  <text x="580" y="41" fill="#64748b" font-size="14">Календарь</text>
  <text x="680" y="41" fill="#64748b" font-size="14">О платформе</text>

  <!-- Search Bar -->
  <rect x="800" y="16" width="340" height="38" rx="8" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="820" y="40" fill="#64748b" font-size="13">🔍 Поиск событий, спикеров, тегов...</text>

  <!-- Right CTA -->
  <rect x="1160" y="16" width="150" height="38" rx="8" fill="#3b82f6"/>
  <text x="1235" y="40" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">+ Создать митап</text>
  <circle cx="1350" cy="35" r="18" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="1350" y="40" fill="#475569" font-size="12" font-weight="bold" text-anchor="middle">АК</text>

  <!-- Breadcrumbs & Title Row -->
  <g transform="translate(60, 95)">
    <text x="0" y="15" fill="#64748b" font-size="12">Главная &gt; События &gt; Каталог</text>
    <text x="0" y="50" fill="#0f172a" font-size="28" font-weight="800">[WIREFRAME] Каталог IT-мероприятий и митапов</text>
    <text x="0" y="75" fill="#64748b" font-size="14">12-колоночная модульная сетка Bootstrap 1440px | Логическая разметка элементов низкой точности</text>
  </g>

  <!-- Left Sidebar (Filters) -->
  <g transform="translate(60, 195)">
    <rect width="280" height="660" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="24" y="36" fill="#0f172a" font-size="16" font-weight="bold">Фильтрация (Фасеты)</text>

    <!-- Filter Block 1: Date -->
    <text x="24" y="70" fill="#334155" font-size="13" font-weight="600">ДАТА ПРОВЕДЕНИЯ</text>
    <rect x="24" y="85" width="232" height="32" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="36" y="106" fill="#64748b" font-size="12">📅 Выберите даты</text>

    <rect x="24" y="125" width="110" height="28" rx="4" fill="#e2e8f0"/>
    <text x="79" y="143" fill="#1e293b" font-size="11" text-anchor="middle">Сегодня (2)</text>
    <rect x="146" y="125" width="110" height="28" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="201" y="143" fill="#64748b" font-size="11" text-anchor="middle">На неделе (7)</text>

    <!-- Filter Block 2: Format -->
    <text x="24" y="185" fill="#334155" font-size="13" font-weight="600">ФОРМАТ СОБЫТИЯ</text>
    <rect x="24" y="200" width="16" height="16" rx="3" fill="#3b82f6"/>
    <text x="50" y="213" fill="#1e293b" font-size="13">Офлайн-митап (14)</text>

    <rect x="24" y="228" width="16" height="16" rx="3" fill="#ffffff" stroke="#94a3b8"/>
    <text x="50" y="241" fill="#1e293b" font-size="13">Хакатон (4)</text>

    <rect x="24" y="256" width="16" height="16" rx="3" fill="#ffffff" stroke="#94a3b8"/>
    <text x="50" y="269" fill="#1e293b" font-size="13">Воркшоп / Лекция (6)</text>

    <!-- Filter Block 3: Categories -->
    <text x="24" y="315" fill="#334155" font-size="13" font-weight="600">НАПРАВЛЕНИЕ / СТЕК</text>
    <rect x="24" y="330" width="16" height="16" rx="3" fill="#3b82f6"/>
    <text x="50" y="343" fill="#1e293b" font-size="13">Artificial Intelligence / ML</text>

    <rect x="24" y="358" width="16" height="16" rx="3" fill="#3b82f6"/>
    <text x="50" y="371" fill="#1e293b" font-size="13">Web Development / TS</text>

    <rect x="24" y="386" width="16" height="16" rx="3" fill="#ffffff" stroke="#94a3b8"/>
    <text x="50" y="399" fill="#1e293b" font-size="13">Distributed Systems &amp; Go</text>

    <rect x="24" y="414" width="16" height="16" rx="3" fill="#ffffff" stroke="#94a3b8"/>
    <text x="50" y="427" fill="#1e293b" font-size="13">UI/UX &amp; HCI Design</text>

    <!-- Filter Block 4: Availability -->
    <text x="24" y="475" fill="#334155" font-size="13" font-weight="600">ДОСТУПНОСТЬ МЕСТ</text>
    <rect x="24" y="490" width="16" height="16" rx="3" fill="#3b82f6"/>
    <text x="50" y="503" fill="#1e293b" font-size="13">Есть свободные места</text>
    <rect x="24" y="518" width="16" height="16" rx="3" fill="#ffffff" stroke="#94a3b8"/>
    <text x="50" y="531" fill="#1e293b" font-size="13">Лист ожидания (Waitlist)</text>

    <!-- Filter Block 5: Location -->
    <text x="24" y="580" fill="#334155" font-size="13" font-weight="600">ЛОКАЦИЯ</text>
    <rect x="24" y="595" width="232" height="32" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="36" y="616" fill="#64748b" font-size="12">🏛 Все корпуса БГУ</text>
  </g>

  <!-- Right Content Area (Grid of Events) -->
  <g transform="translate(365, 195)">
    <!-- Controls Bar -->
    <rect width="1015" height="46" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="20" y="28" fill="#64748b" font-size="13">Найдено: <tspan fill="#0f172a" font-weight="bold">18 мероприятий</tspan></text>

    <!-- Active Tags -->
    <rect x="200" y="10" width="130" height="26" rx="13" fill="#e2e8f0"/>
    <text x="265" y="27" fill="#334155" font-size="11" text-anchor="middle">AI / ML ✕</text>
    <rect x="340" y="10" width="120" height="26" rx="13" fill="#e2e8f0"/>
    <text x="400" y="27" fill="#334155" font-size="11" text-anchor="middle">Офлайн ✕</text>

    <!-- Sort Dropdown -->
    <rect x="800" y="8" width="195" height="30" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="815" y="28" fill="#334155" font-size="12">Сортировка: Ближайшие ▼</text>

    <!-- Event Cards Grid (2 rows x 3 cols) -->
    <!-- Card 1 -->
    <g transform="translate(0, 65)">
      <rect width="325" height="375" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <rect x="1" y="1" width="323" height="150" rx="9" fill="#e2e8f0" stroke="#94a3b8" stroke-dasharray="4,4"/>
      <text x="162" y="80" fill="#64748b" font-size="14" text-anchor="middle">[Изображение / Баннер ивента]</text>
      <rect x="15" y="15" width="80" height="24" rx="4" fill="#0f172a"/>
      <text x="55" y="31" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">МИТАП</text>

      <text x="15" y="180" fill="#3b82f6" font-size="12" font-weight="600">15 октября 2026 • 17:00</text>
      <text x="15" y="208" fill="#0f172a" font-size="16" font-weight="bold">CampusMeet: AI &amp; Web</text>
      <text x="15" y="232" fill="#64748b" font-size="12">🏛 Главный корпус БГУ, Ауд. 512</text>
      <text x="15" y="254" fill="#64748b" font-size="12">👤 Спикеры: В. Громов (Lead Arch), Д. Мельниченко</text>

      <!-- Progress bar -->
      <rect x="15" y="280" width="295" height="8" rx="4" fill="#e2e8f0"/>
      <rect x="15" y="280" width="260" height="8" rx="4" fill="#22c55e"/>
      <text x="15" y="306" fill="#64748b" font-size="11">Занято: 88 / 100 мест (Осталось 12)</text>

      <!-- CTA -->
      <rect x="15" y="325" width="295" height="36" rx="6" fill="#0f172a"/>
      <text x="162" y="347" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">Зарегистрироваться (Free)</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(345, 65)">
      <rect width="325" height="375" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <rect x="1" y="1" width="323" height="150" rx="9" fill="#e2e8f0" stroke="#94a3b8" stroke-dasharray="4,4"/>
      <text x="162" y="80" fill="#64748b" font-size="14" text-anchor="middle">[Изображение / Баннер ивента]</text>
      <rect x="15" y="15" width="90" height="24" rx="4" fill="#f59e0b"/>
      <text x="60" y="31" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">ХАКАТОН</text>

      <text x="15" y="180" fill="#3b82f6" font-size="12" font-weight="600">24-25 октября 2026 • 10:00</text>
      <text x="15" y="208" fill="#0f172a" font-size="16" font-weight="bold">FPMI Hack 2026 (24h)</text>
      <text x="15" y="232" fill="#64748b" font-size="12">🏛 ФПМИ БГУ, 5 этаж коворкинг</text>
      <text x="15" y="254" fill="#64748b" font-size="12">👥 Команды по 3-5 чел • Призовой фонд</text>

      <rect x="15" y="280" width="295" height="8" rx="4" fill="#e2e8f0"/>
      <rect x="15" y="280" width="295" height="8" rx="4" fill="#ef4444"/>
      <text x="15" y="306" fill="#ef4444" font-size="11" font-weight="600">Лимит исчерпан: Лист ожидания (+14)</text>

      <rect x="15" y="325" width="295" height="36" rx="6" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="162" y="347" fill="#475569" font-size="13" font-weight="600" text-anchor="middle">В лист ожидания</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(690, 65)">
      <rect width="325" height="375" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <rect x="1" y="1" width="323" height="150" rx="9" fill="#e2e8f0" stroke="#94a3b8" stroke-dasharray="4,4"/>
      <text x="162" y="80" fill="#64748b" font-size="14" text-anchor="middle">[Изображение / Баннер ивента]</text>
      <rect x="15" y="15" width="95" height="24" rx="4" fill="#8b5cf6"/>
      <text x="62" y="31" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">ВОРКШОП</text>

      <text x="15" y="180" fill="#3b82f6" font-size="12" font-weight="600">29 октября 2026 • 18:30</text>
      <text x="15" y="208" fill="#0f172a" font-size="16" font-weight="bold">System Design &amp; Highload</text>
      <text x="15" y="232" fill="#64748b" font-size="12">🏛 Корпус ФФСН, Ауд. 302</text>
      <text x="15" y="254" fill="#64748b" font-size="12">👤 Практический разбор микросервисов</text>

      <rect x="15" y="280" width="295" height="8" rx="4" fill="#e2e8f0"/>
      <rect x="15" y="280" width="130" height="8" rx="4" fill="#22c55e"/>
      <text x="15" y="306" fill="#64748b" font-size="11">Занято: 35 / 80 мест (Свободно 45)</text>

      <rect x="15" y="325" width="295" height="36" rx="6" fill="#0f172a"/>
      <text x="162" y="347" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">Зарегистрироваться (Free)</text>
    </g>

    <!-- Pagination -->
    <g transform="translate(350, 480)">
      <rect x="0" y="0" width="36" height="36" rx="6" fill="#0f172a"/>
      <text x="18" y="23" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">1</text>
      <rect x="46" y="0" width="36" height="36" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
      <text x="64" y="23" fill="#475569" font-size="14" text-anchor="middle">2</text>
      <rect x="92" y="0" width="36" height="36" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
      <text x="110" y="23" fill="#475569" font-size="14" text-anchor="middle">3</text>
      <text x="150" y="23" fill="#64748b" font-size="14">... Следующая →</text>
    </g>
  </g>
</svg>'''
    with open("docs/assets/wireframes/wireframe_desktop_catalog.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_wireframe_desktop_event_details():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 1000" width="1440" height="1000" font-family="'Inter', -apple-system, sans-serif">
  <!-- Background -->
  <rect width="1440" height="1000" fill="#f8fafc"/>

  <!-- Top Navigation Bar -->
  <rect x="0" y="0" width="1440" height="70" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="60" y="18" width="160" height="34" rx="6" fill="#0f172a"/>
  <text x="140" y="40" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">CampusMeet</text>
  <text x="270" y="41" fill="#0f172a" font-size="14" font-weight="600">Афиша</text>
  <text x="350" y="41" fill="#64748b" font-size="14">Хакатоны</text>
  <text x="450" y="41" fill="#64748b" font-size="14">Биржа команд</text>
  <circle cx="1350" cy="35" r="18" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="1350" y="40" fill="#475569" font-size="12" font-weight="bold" text-anchor="middle">АК</text>

  <!-- Hero Banner Area -->
  <g transform="translate(60, 90)">
    <text x="0" y="15" fill="#64748b" font-size="12">Главная &gt; События &gt; CampusMeet: AI &amp; Modern Web 2026</text>
    <rect x="0" y="30" width="1320" height="260" rx="12" fill="#e2e8f0" stroke="#94a3b8" stroke-dasharray="6,6"/>
    <text x="660" y="130" fill="#64748b" font-size="18" text-anchor="middle">[Широкоформатный баннер митапа: 1320 x 260 px]</text>
    
    <rect x="30" y="170" width="80" height="26" rx="4" fill="#0f172a"/>
    <text x="70" y="187" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">МИТАП</text>
    <text x="30" y="230" fill="#0f172a" font-size="28" font-weight="800">CampusMeet #4: Архитектура распределенных систем и GenAI</text>
  </g>

  <!-- Main Grid: Two columns -->
  <g transform="translate(60, 380)">
    <!-- Left Column (Content & Schedule) -->
    <g transform="translate(0, 0)">
      <rect width="860" height="580" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      
      <!-- Tabs inside event page -->
      <line x1="0" y1="50" x2="860" y2="50" stroke="#cbd5e1"/>
      <text x="30" y="32" fill="#0f172a" font-size="15" font-weight="bold">О мероприятии</text>
      <line x1="30" y1="49" x2="140" y2="49" stroke="#0f172a" stroke-width="3"/>
      <text x="180" y="32" fill="#64748b" font-size="15">Программа докладов</text>
      <text x="360" y="32" fill="#64748b" font-size="15">Спикеры (3)</text>
      <text x="480" y="32" fill="#64748b" font-size="15">Площадка &amp; Карта</text>
      <text x="640" y="32" fill="#64748b" font-size="15">FAQ и правила</text>

      <!-- Content text placeholders -->
      <g transform="translate(30, 75)">
        <text x="0" y="20" fill="#0f172a" font-size="18" font-weight="bold">Описание митапа</text>
        <rect x="0" y="35" width="800" height="12" rx="3" fill="#e2e8f0"/>
        <rect x="0" y="55" width="760" height="12" rx="3" fill="#e2e8f0"/>
        <rect x="0" y="75" width="710" height="12" rx="3" fill="#e2e8f0"/>

        <!-- Interactive Schedule Preview -->
        <text x="0" y="125" fill="#0f172a" font-size="18" font-weight="bold">Таймлайн программы (Tracks)</text>
        
        <!-- Slot 1 -->
        <rect x="0" y="145" width="800" height="70" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
        <text x="20" y="175" fill="#3b82f6" font-size="14" font-weight="bold">17:00 - 17:15</text>
        <text x="150" y="175" fill="#0f172a" font-size="15" font-weight="bold">Открытие митапа и вступительное слово</text>
        <text x="150" y="195" fill="#64748b" font-size="12">Максим Романов (Председатель IT-клуба ФПМИ)</text>

        <!-- Slot 2 -->
        <rect x="0" y="225" width="800" height="85" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
        <text x="20" y="255" fill="#3b82f6" font-size="14" font-weight="bold">17:15 - 18:00</text>
        <text x="150" y="255" fill="#0f172a" font-size="15" font-weight="bold">Highload в реальном мире: Event-Driven сервисы на Go</text>
        <text x="150" y="275" fill="#64748b" font-size="12">Виктор Громов (Senior Backend Architect) • 40 мин + Q&amp;A</text>
        <rect x="710" y="245" width="70" height="26" rx="4" fill="#e2e8f0"/>
        <text x="745" y="262" fill="#334155" font-size="11" text-anchor="middle">★ В мою</text>

        <!-- Slot 3: Break -->
        <rect x="0" y="320" width="800" height="50" rx="8" fill="#ecfdf5" stroke="#a7f3d0"/>
        <text x="20" y="350" fill="#059669" font-size="14" font-weight="bold">18:00 - 18:30</text>
        <text x="150" y="350" fill="#065f46" font-size="14" font-weight="600">Кофе-брейк, пицца и нетворкинг у стендов</text>

        <!-- Slot 4 -->
        <rect x="0" y="380" width="800" height="85" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
        <text x="20" y="410" fill="#3b82f6" font-size="14" font-weight="bold">18:30 - 19:20</text>
        <text x="150" y="410" fill="#0f172a" font-size="15" font-weight="bold">Автономные LLM-агенты в продакшене</text>
        <text x="150" y="430" fill="#64748b" font-size="12">Александр Белов (AI Research Lead) • Презентация кейсов</text>
      </g>
    </g>

    <!-- Right Column (Sticky Registration & Venue Card) -->
    <g transform="translate(890, 0)">
      <rect width="430" height="580" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <g transform="translate(30, 30)">
        <text x="0" y="20" fill="#0f172a" font-size="20" font-weight="800">Регистрация на событие</text>
        <text x="0" y="45" fill="#64748b" font-size="13">Бесплатный электронный билет с QR-кодом</text>

        <!-- Progress bar -->
        <rect x="0" y="65" width="370" height="10" rx="5" fill="#e2e8f0"/>
        <rect x="0" y="65" width="325" height="10" rx="5" fill="#22c55e"/>
        <text x="0" y="95" fill="#1e293b" font-size="12" font-weight="600">88 из 100 мест занято (88%)</text>
        <text x="370" y="95" fill="#059669" font-size="12" font-weight="bold" text-anchor="end">Осталось 12 мест</text>

        <!-- Main Action CTA -->
        <rect x="0" y="115" width="370" height="48" rx="8" fill="#0f172a"/>
        <text x="185" y="145" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">Зарегистрироваться (Free)</text>
        <text x="185" y="180" fill="#64748b" font-size="11" text-anchor="middle">⚡ Билет сразу доступен в офлайн-режиме смартфона</text>

        <line x1="0" y1="205" x2="370" y2="205" stroke="#e2e8f0"/>

        <!-- Details block -->
        <text x="0" y="235" fill="#0f172a" font-size="15" font-weight="bold">Дата и время</text>
        <text x="0" y="258" fill="#334155" font-size="13">Четверг, 15 октября 2026</text>
        <text x="0" y="278" fill="#64748b" font-size="12">17:00 – 20:30 (Сбор гостей с 16:30)</text>

        <text x="0" y="315" fill="#0f172a" font-size="15" font-weight="bold">Локация</text>
        <text x="0" y="338" fill="#334155" font-size="13">Минск, пр-т Независимости 4</text>
        <text x="0" y="358" fill="#64748b" font-size="12">Главный корпус БГУ, Аудитория 512 (5 этаж)</text>

        <!-- OpenStreetMap Widget wireframe -->
        <rect x="0" y="380" width="370" height="120" rx="8" fill="#e2e8f0" stroke="#cbd5e1" stroke-dasharray="4,4"/>
        <text x="185" y="445" fill="#64748b" font-size="13" text-anchor="middle">📍 [Интеграция OpenStreetMap / Координаты: 53.8938, 27.5471]</text>

        <text x="0" y="525" fill="#3b82f6" font-size="12">⤓ Добавить в Google Calendar / Apple iCal</text>
      </g>
    </g>
  </g>
</svg>'''
    with open("docs/assets/wireframes/wireframe_desktop_event_details.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_wireframe_mobile_ticket():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 375 812" width="375" height="812" font-family="'Inter', -apple-system, sans-serif">
  <!-- Phone Frame background -->
  <rect width="375" height="812" rx="40" fill="#f8fafc" stroke="#cbd5e1" stroke-width="4"/>
  <!-- Dynamic Island / Speaker notch -->
  <rect x="125" y="12" width="125" height="28" rx="14" fill="#0f172a"/>

  <!-- Mobile Header -->
  <g transform="translate(20, 55)">
    <text x="0" y="20" fill="#0f172a" font-size="18">←</text>
    <text x="167" y="20" fill="#0f172a" font-size="16" font-weight="bold" text-anchor="middle">[WIREFRAME] Мой билет</text>
    <text x="335" y="20" fill="#0f172a" font-size="16" text-anchor="end">↗</text>
  </g>

  <!-- Offline Status Badge -->
  <g transform="translate(20, 95)">
    <rect width="335" height="34" rx="8" fill="#ecfdf5" stroke="#a7f3d0"/>
    <circle cx="20" cy="17" r="4" fill="#059669"/>
    <text x="34" y="22" fill="#065f46" font-size="11" font-weight="600">OFFLINE-READY: Билет сохранен в памяти телефона</text>
  </g>

  <!-- Ticket Card Container -->
  <g transform="translate(20, 145)">
    <rect width="335" height="520" rx="16" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    
    <!-- Header of card -->
    <rect x="0" y="0" width="335" height="90" rx="16" fill="#0f172a"/>
    <text x="20" y="32" fill="#38bdf8" font-size="11" font-weight="bold">CAMPUSMEET IT-EVENT</text>
    <text x="20" y="58" fill="#ffffff" font-size="16" font-weight="bold">AI &amp; Modern Web Meetup</text>
    <text x="20" y="78" fill="#94a3b8" font-size="12">15 октября 2026 • 17:00 • Ауд. 512</text>

    <!-- Participant metadata -->
    <g transform="translate(20, 110)">
      <text x="0" y="15" fill="#64748b" font-size="11">УЧАСТНИК</text>
      <text x="0" y="35" fill="#0f172a" font-size="15" font-weight="bold">Артём Ковалёв</text>

      <text x="200" y="15" fill="#64748b" font-size="11">РОЛЬ / МЕСТО</text>
      <text x="200" y="35" fill="#0f172a" font-size="15" font-weight="bold">Слушатель • #88</text>
    </g>

    <!-- Dashed separator with punch notches -->
    <line x1="15" y1="175" x2="320" y2="175" stroke="#cbd5e1" stroke-dasharray="6,6" stroke-width="2"/>
    <circle cx="0" cy="175" r="12" fill="#f8fafc"/>
    <circle cx="335" cy="175" r="12" fill="#f8fafc"/>

    <!-- QR Code Section -->
    <g transform="translate(67, 205)">
      <rect width="200" height="200" rx="12" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>
      <!-- QR corner locators -->
      <rect x="20" y="20" width="40" height="40" fill="#0f172a"/>
      <rect x="28" y="28" width="24" height="24" fill="#ffffff"/>
      <rect x="34" y="34" width="12" height="12" fill="#0f172a"/>

      <rect x="140" y="20" width="40" height="40" fill="#0f172a"/>
      <rect x="148" y="28" width="24" height="24" fill="#ffffff"/>
      <rect x="154" y="34" width="12" height="12" fill="#0f172a"/>

      <rect x="20" y="140" width="40" height="40" fill="#0f172a"/>
      <rect x="28" y="148" width="24" height="24" fill="#ffffff"/>
      <rect x="34" y="154" width="12" height="12" fill="#0f172a"/>

      <!-- Matrix simulation -->
      <rect x="75" y="30" width="15" height="15" fill="#0f172a"/>
      <rect x="100" y="45" width="20" height="15" fill="#0f172a"/>
      <rect x="85" y="80" width="30" height="30" fill="#0f172a"/>
      <rect x="130" y="100" width="20" height="25" fill="#0f172a"/>
      <rect x="40" y="90" width="25" height="25" fill="#0f172a"/>
      <rect x="90" y="140" width="35" height="20" fill="#0f172a"/>
      <rect x="145" y="145" width="25" height="25" fill="#0f172a"/>

      <text x="100" y="110" fill="#3b82f6" font-size="11" font-weight="bold" text-anchor="middle">HMAC PASS</text>
    </g>

    <!-- Rolling Security Info -->
    <text x="167" y="430" fill="#64748b" font-size="11" text-anchor="middle">Токен обновлен • Валиден еще 42с</text>
    <text x="167" y="448" fill="#059669" font-size="11" font-weight="600" text-anchor="middle">☼ Яркость экрана установлена на 100%</text>

    <!-- Wallet Button -->
    <rect x="30" y="465" width="275" height="40" rx="8" fill="#000000"/>
    <text x="167" y="490" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle">Add to Apple Wallet</text>
  </g>

  <!-- Bottom Navigation Bar -->
  <g transform="translate(0, 735)">
    <rect width="375" height="77" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <text x="45" y="35" fill="#64748b" font-size="11" text-anchor="middle">Афиша</text>
    <text x="135" y="35" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">● Билеты</text>
    <text x="235" y="35" fill="#64748b" font-size="11" text-anchor="middle">Команды</text>
    <text x="330" y="35" fill="#64748b" font-size="11" text-anchor="middle">Профиль</text>
  </g>
</svg>'''
    with open("docs/assets/wireframes/wireframe_mobile_ticket.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_wireframe_mobile_scanner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 375 812" width="375" height="812" font-family="'Inter', -apple-system, sans-serif">
  <!-- Phone Frame background -->
  <rect width="375" height="812" rx="40" fill="#0f172a" stroke="#334155" stroke-width="4"/>
  <rect x="125" y="12" width="125" height="28" rx="14" fill="#000000"/>

  <!-- Camera Viewfinder simulation (Dark gray) -->
  <rect x="10" y="50" width="355" height="710" rx="20" fill="#1e293b"/>

  <!-- Top Scanner Header -->
  <g transform="translate(20, 65)">
    <rect width="335" height="50" rx="10" fill="#0f172a" opacity="0.8"/>
    <text x="20" y="24" fill="#ffffff" font-size="13" font-weight="bold">Входная зона: Главный корпус</text>
    <text x="20" y="42" fill="#38bdf8" font-size="11">Волонтер: Дарья М. • Режим: Offline</text>
    <text x="315" y="33" fill="#22c55e" font-size="16" font-weight="bold" text-anchor="end">88/100</text>
  </g>

  <!-- Central Reticle (Aiming Target) -->
  <g transform="translate(57, 180)">
    <!-- Scanning box -->
    <rect width="260" height="260" rx="16" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="8,8"/>
    
    <!-- Target corner brackets -->
    <path d="M 0 30 L 0 0 L 30 0" fill="none" stroke="#22c55e" stroke-width="5"/>
    <path d="M 230 0 L 260 0 L 260 30" fill="none" stroke="#22c55e" stroke-width="5"/>
    <path d="M 0 230 L 0 260 L 30 260" fill="none" stroke="#22c55e" stroke-width="5"/>
    <path d="M 230 260 L 260 260 L 260 230" fill="none" stroke="#22c55e" stroke-width="5"/>

    <!-- Green Laser line -->
    <line x1="10" y1="130" x2="250" y2="130" stroke="#22c55e" stroke-width="3"/>
    <text x="130" y="120" fill="#22c55e" font-size="11" font-weight="bold" text-anchor="middle">СКАНИРОВАНИЕ &lt; 500 МС</text>
  </g>

  <!-- Recognition Result Card (Feedback HUD) -->
  <g transform="translate(20, 480)">
    <rect width="335" height="130" rx="12" fill="#064e3b" stroke="#22c55e" stroke-width="2"/>
    <circle cx="40" cy="40" r="20" fill="#22c55e"/>
    <text x="40" y="47" fill="#ffffff" font-size="20" font-weight="bold" text-anchor="middle">✓</text>
    
    <text x="75" y="35" fill="#a7f3d0" font-size="12" font-weight="bold">ВХОД РАЗРЕШЕН</text>
    <text x="75" y="58" fill="#ffffff" font-size="18" font-weight="800">Артём Ковалёв</text>
    <text x="75" y="78" fill="#cbd5e1" font-size="12">ФПМИ БГУ, 3 курс • Билет #8841-A</text>
    
    <rect x="20" y="95" width="295" height="24" rx="4" fill="#047857"/>
    <text x="167" y="111" fill="#ffffff" font-size="11" text-anchor="middle">Отсканировано в 16:48:12 • Тактильный виброотклик: OK</text>
  </g>

  <!-- Manual Lookup for Cracked Screens -->
  <g transform="translate(20, 630)">
    <rect width="335" height="44" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="20" y="27" fill="#94a3b8" font-size="12">⌨ Поиск по фамилии при разбитом экране...</text>
  </g>

  <!-- Flashlight / Audio Toggles -->
  <g transform="translate(20, 690)">
    <rect x="0" y="0" width="160" height="36" rx="8" fill="#334155"/>
    <text x="80" y="23" fill="#ffffff" font-size="12" text-anchor="middle">💡 Фонарик [ВКЛ]</text>

    <rect x="175" y="0" width="160" height="36" rx="8" fill="#334155"/>
    <text x="255" y="23" fill="#ffffff" font-size="12" text-anchor="middle">🔔 Звук / Вибро [ВКЛ]</text>
  </g>
</svg>'''
    with open("docs/assets/wireframes/wireframe_mobile_scanner.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_wireframe_desktop_dashboard():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" width="1440" height="900" font-family="'Inter', -apple-system, sans-serif">
  <!-- Background -->
  <rect width="1440" height="900" fill="#f8fafc"/>

  <!-- Left Sidebar Navigation -->
  <rect x="0" y="0" width="260" height="900" fill="#0f172a"/>
  <!-- Brand -->
  <rect x="25" y="24" width="140" height="32" rx="6" fill="#38bdf8"/>
  <text x="95" y="46" fill="#0f172a" font-size="15" font-weight="800" text-anchor="middle">CampusMeet</text>
  <text x="25" y="80" fill="#94a3b8" font-size="11">КАБИНЕТ ОРГАНИЗАТОРА</text>

  <!-- Nav Items -->
  <g transform="translate(15, 110)">
    <rect x="0" y="0" width="230" height="40" rx="8" fill="#1e293b"/>
    <text x="20" y="25" fill="#38bdf8" font-size="13" font-weight="bold">📊 Дашборд события</text>

    <text x="20" y="70" fill="#cbd5e1" font-size="13">📅 Конструктор расписания</text>
    <text x="20" y="110" fill="#cbd5e1" font-size="13">👥 Участники и чекины</text>
    <text x="20" y="150" fill="#cbd5e1" font-size="13">🎤 Заявки спикеров (CFP)</text>
    <text x="20" y="190" fill="#cbd5e1" font-size="13">📱 Сканеры и волонтеры</text>
    <text x="20" y="230" fill="#cbd5e1" font-size="13">🚨 Экстренный Push</text>
    <text x="20" y="270" fill="#cbd5e1" font-size="13">📄 Выгрузка отчетов (CSV)</text>
    <text x="20" y="310" fill="#cbd5e1" font-size="13">⚙️ Настройки квот</text>
  </g>

  <!-- Top App Bar -->
  <rect x="260" y="0" width="1180" height="70" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <g transform="translate(290, 20)">
    <text x="0" y="20" fill="#64748b" font-size="12">Текущее событие:</text>
    <text x="0" y="40" fill="#0f172a" font-size="16" font-weight="bold">CampusMeet: AI &amp; Modern Web 2026</text>
    <rect x="330" y="22" width="140" height="24" rx="12" fill="#ecfdf5"/>
    <text x="400" y="38" fill="#059669" font-size="11" font-weight="bold" text-anchor="middle">🟢 ЧЕКИН АКТИВЕН</text>
    
    <!-- Fast Emergency Alert Button -->
    <rect x="780" y="6" width="200" height="38" rx="8" fill="#ef4444"/>
    <text x="880" y="30" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">🚨 Экстренный Push (1 клик)</text>
    
    <circle cx="1080" cy="25" r="18" fill="#e2e8f0"/>
    <text x="1080" y="30" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">МР</text>
  </g>

  <!-- Workspace Container -->
  <g transform="translate(290, 95)">
    <!-- Title -->
    <text x="0" y="25" fill="#0f172a" font-size="24" font-weight="800">[WIREFRAME] Мониторинг проходов и квот зала в реальном времени</text>
    
    <!-- 4 KPI Cards -->
    <g transform="translate(0, 45)">
      <!-- KPI 1 -->
      <rect x="0" y="0" width="265" height="95" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="20" y="28" fill="#64748b" font-size="12">ВСЕГО РЕГИСТРАЦИЙ</text>
      <text x="20" y="62" fill="#0f172a" font-size="26" font-weight="800">100 / 100</text>
      <text x="20" y="82" fill="#059669" font-size="11">✓ Hard Cap заполнен на 100%</text>

      <!-- KPI 2 -->
      <rect x="285" y="0" width="265" height="95" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="20" y="28" fill="#64748b" font-size="12">ПРОШЛИ ЧЕКИН НА ВХОДЕ</text>
      <text x="20" y="62" fill="#22c55e" font-size="26" font-weight="800">88 чел. (88%)</text>
      <text x="20" y="82" fill="#64748b" font-size="11">Осталось подойти: 12 чел.</text>

      <!-- KPI 3 -->
      <rect x="570" y="0" width="265" height="95" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="20" y="28" fill="#64748b" font-size="12">ЛИСТ ОЖИДАНИЯ (WAITLIST)</text>
      <text x="20" y="62" fill="#f59e0b" font-size="26" font-weight="800">14 чел.</text>
      <text x="20" y="82" fill="#d97706" font-size="11">Авто-перевод при неявке</text>

      <!-- KPI 4 -->
      <rect x="855" y="0" width="265" height="95" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="20" y="28" fill="#64748b" font-size="12">СРЕДНЯЯ СКОРОСТЬ ВХОДА</text>
      <text x="20" y="62" fill="#3b82f6" font-size="26" font-weight="800">1.1 сек / чел</text>
      <text x="20" y="82" fill="#059669" font-size="11">2 активных сканера волонтеров</text>
    </g>

    <!-- Main Table & Live Stream -->
    <g transform="translate(0, 165)">
      <rect width="1120" height="580" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      
      <!-- Table Header Bar -->
      <text x="25" y="36" fill="#0f172a" font-size="16" font-weight="bold">Поток верификации участников (Live Check-In Feed)</text>
      <rect x="800" y="16" width="150" height="32" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="875" y="37" fill="#475569" font-size="12" text-anchor="middle">🔍 Поиск по ФИО</text>
      <rect x="965" y="16" width="130" height="32" rx="6" fill="#0f172a"/>
      <text x="1030" y="37" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Экспорт CSV</text>

      <line x1="0" y1="65" x2="1120" y2="65" stroke="#cbd5e1"/>

      <!-- Table Headings -->
      <text x="30" y="90" fill="#64748b" font-size="12" font-weight="bold">ВРЕМЯ</text>
      <text x="140" y="90" fill="#64748b" font-size="12" font-weight="bold">ФИО УЧАСТНИКА</text>
      <text x="360" y="90" fill="#64748b" font-size="12" font-weight="bold">КУРС / ГРУППА</text>
      <text x="540" y="90" fill="#64748b" font-size="12" font-weight="bold">ТИП БИЛЕТА</text>
      <text x="720" y="90" fill="#64748b" font-size="12" font-weight="bold">ВОЛОНТЕР / ТОЧКА</text>
      <text x="940" y="90" fill="#64748b" font-size="12" font-weight="bold">СТАТУС</text>

      <!-- Row 1 -->
      <line x1="0" y1="105" x2="1120" y2="105" stroke="#f1f5f9"/>
      <text x="30" y="130" fill="#334155" font-size="13">16:48:12</text>
      <text x="140" y="130" fill="#0f172a" font-size="13" font-weight="bold">Ковалёв Артём Игоревич</text>
      <text x="360" y="130" fill="#475569" font-size="13">ФПМИ БГУ, 3 курс</text>
      <text x="540" y="130" fill="#475569" font-size="13">Слушатель (#88)</text>
      <text x="720" y="130" fill="#475569" font-size="13">Дарья М. (Сканер №1)</text>
      <rect x="940" y="115" width="100" height="24" rx="4" fill="#ecfdf5"/>
      <text x="990" y="131" fill="#059669" font-size="11" font-weight="bold" text-anchor="middle">✓ Подтвержден</text>

      <!-- Row 2 -->
      <line x1="0" y1="150" x2="1120" y2="150" stroke="#f1f5f9"/>
      <text x="30" y="175" fill="#334155" font-size="13">16:47:58</text>
      <text x="140" y="175" fill="#0f172a" font-size="13" font-weight="bold">Савицкий Кирилл Павлович</text>
      <text x="360" y="175" fill="#475569" font-size="13">ФПМИ БГУ, 4 курс</text>
      <text x="540" y="175" fill="#475569" font-size="13">Капитан хакатона</text>
      <text x="720" y="175" fill="#475569" font-size="13">Иван К. (Сканер №2)</text>
      <rect x="940" y="160" width="100" height="24" rx="4" fill="#ecfdf5"/>
      <text x="990" y="176" fill="#059669" font-size="11" font-weight="bold" text-anchor="middle">✓ Подтвержден</text>

      <!-- Row 3: Duplicate Warning -->
      <line x1="0" y1="195" x2="1120" y2="195" stroke="#f1f5f9"/>
      <text x="30" y="220" fill="#ef4444" font-size="13">16:46:40</text>
      <text x="140" y="220" fill="#ef4444" font-size="13" font-weight="bold">Костылев Влад (Повторный QR)</text>
      <text x="360" y="220" fill="#475569" font-size="13">Сторонний гость</text>
      <text x="540" y="220" fill="#475569" font-size="13">Скриншот (#42)</text>
      <text x="720" y="220" fill="#475569" font-size="13">Дарья М. (Сканер №1)</text>
      <rect x="940" y="205" width="120" height="24" rx="4" fill="#fef2f2"/>
      <text x="1000" y="221" fill="#dc2626" font-size="11" font-weight="bold" text-anchor="middle">⚠ Дубликат (16:34)</text>

      <!-- Row 4 -->
      <line x1="0" y1="240" x2="1120" y2="240" stroke="#f1f5f9"/>
      <text x="30" y="265" fill="#334155" font-size="13">16:45:10</text>
      <text x="140" y="265" fill="#0f172a" font-size="13" font-weight="bold">Громов Виктор Михайлович</text>
      <text x="360" y="265" fill="#475569" font-size="13">Приглашенный докладчик</text>
      <text x="540" y="265" fill="#475569" font-size="13">Спикер (VIP pass)</text>
      <text x="720" y="265" fill="#475569" font-size="13">Максим Р. (Организатор)</text>
      <rect x="940" y="250" width="100" height="24" rx="4" fill="#ecfdf5"/>
      <text x="990" y="266" fill="#059669" font-size="11" font-weight="bold" text-anchor="middle">✓ Подтвержден</text>
    </g>
  </g>
</svg>'''
    with open("docs/assets/wireframes/wireframe_desktop_dashboard.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 2. HIGH-FIDELITY COLOR MOCKUPS
# -------------------------------------------------------------

def generate_mockup_desktop_catalog():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="1440" height="960" font-family="'Inter', -apple-system, sans-serif">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="glowHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0.2"/>
    </linearGradient>
  </defs>

  <!-- Deep Slate Background -->
  <rect width="1440" height="960" fill="url(#bgGrad)"/>

  <!-- Top Glassmorphic Navigation -->
  <rect width="1440" height="72" fill="#0f172acc" stroke="#334155" stroke-width="1"/>
  
  <!-- Logo -->
  <g transform="translate(60, 20)">
    <rect width="36" height="36" rx="8" fill="url(#accentGrad)"/>
    <text x="18" y="24" fill="#0f172a" font-size="18" font-weight="900" text-anchor="middle">⚡</text>
    <text x="46" y="25" fill="#ffffff" font-size="18" font-weight="800">Campus<tspan fill="#38bdf8">Meet</tspan></text>
  </g>

  <!-- Navigation items -->
  <g transform="translate(240, 36)">
    <text x="0" y="0" fill="#38bdf8" font-size="14" font-weight="700">Афиша</text>
    <line x1="0" y1="8" x2="45" y2="8" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="80" y="0" fill="#94a3b8" font-size="14" font-weight="500">Хакатоны</text>
    <text x="185" y="0" fill="#94a3b8" font-size="14" font-weight="500">Биржа команд</text>
    <text x="320" y="0" fill="#94a3b8" font-size="14" font-weight="500">Календарь</text>
    <text x="430" y="0" fill="#94a3b8" font-size="14" font-weight="500">О проекте</text>
  </g>

  <!-- Search Bar with Suggestions -->
  <g transform="translate(730, 16)">
    <rect width="340" height="40" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="20" y="25" fill="#64748b" font-size="13">🔍 Поиск событий, спикеров, Go, AI...</text>
    <rect x="290" y="10" width="36" height="20" rx="4" fill="#334155"/>
    <text x="308" y="24" fill="#94a3b8" font-size="11" text-anchor="middle">⌘K</text>
  </g>

  <!-- Action CTA -->
  <g transform="translate(1090, 16)">
    <rect width="160" height="40" rx="8" fill="url(#accentGrad)"/>
    <text x="80" y="25" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">+ Создать ивент</text>

    <!-- User Profile Avatar -->
    <circle cx="200" cy="20" r="18" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="200" y="25" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">АК</text>
  </g>

  <!-- Hero Header Ribbon -->
  <g transform="translate(60, 95)">
    <rect width="1320" height="85" rx="12" fill="url(#glowHeader)" stroke="#38bdf844" stroke-width="1"/>
    <text x="25" y="32" fill="#38bdf8" font-size="12" font-weight="700" letter-spacing="1">ЭКОСИСТЕМА СТУДЕНЧЕСКИХ МИТАПОВ И ХАКАТОНОВ</text>
    <text x="25" y="62" fill="#ffffff" font-size="24" font-weight="800">Афиша предстоящих IT-мероприятий г. Минска</text>
    
    <!-- Stat pills on right -->
    <rect x="980" y="24" width="140" height="36" rx="18" fill="#0f172a88" stroke="#334155"/>
    <text x="1050" y="47" fill="#f8fafc" font-size="12" text-anchor="middle">🎉 18 активных событий</text>

    <rect x="1135" y="24" width="160" height="36" rx="18" fill="#0f172a88" stroke="#334155"/>
    <text x="1215" y="47" fill="#22c55e" font-size="12" text-anchor="middle">⚡ Zero-Latency чекин</text>
  </g>

  <!-- Sidebar Filters -->
  <g transform="translate(60, 205)">
    <rect width="280" height="715" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1"/>
    <g transform="translate(24, 25)">
      <text x="0" y="0" fill="#ffffff" font-size="16" font-weight="700">Фильтры афиши</text>
      
      <!-- Date Filter -->
      <text x="0" y="38" fill="#94a3b8" font-size="11" font-weight="700" letter-spacing="0.5">ВРЕМЯ ПРОВЕДЕНИЯ</text>
      <rect x="0" y="48" width="112" height="32" rx="6" fill="#38bdf822" stroke="#38bdf8"/>
      <text x="56" y="69" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">Ближайшие</text>

      <rect x="120" y="48" width="112" height="32" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="176" y="69" fill="#94a3b8" font-size="12" text-anchor="middle">На неделе</text>

      <!-- Format Filter -->
      <text x="0" y="115" fill="#94a3b8" font-size="11" font-weight="700" letter-spacing="0.5">ТИП МЕРОПРИЯТИЯ</text>
      
      <rect x="0" y="128" width="16" height="16" rx="4" fill="#38bdf8"/>
      <text x="8" y="140" fill="#0f172a" font-size="11" text-anchor="middle">✓</text>
      <text x="28" y="141" fill="#f8fafc" font-size="13">Офлайн-митапы (14)</text>

      <rect x="0" y="156" width="16" height="16" rx="4" fill="#1e293b" stroke="#475569"/>
      <text x="28" y="169" fill="#94a3b8" font-size="13">Хакатоны (4)</text>

      <rect x="0" y="184" width="16" height="16" rx="4" fill="#1e293b" stroke="#475569"/>
      <text x="28" y="197" fill="#94a3b8" font-size="13">Воркшопы и лекции (6)</text>

      <!-- Tech stack -->
      <text x="0" y="240" fill="#94a3b8" font-size="11" font-weight="700" letter-spacing="0.5">НАПРАВЛЕНИЯ &amp; ТЕХНОЛОГИИ</text>
      
      <rect x="0" y="253" width="16" height="16" rx="4" fill="#38bdf8"/>
      <text x="8" y="265" fill="#0f172a" font-size="11" text-anchor="middle">✓</text>
      <text x="28" y="266" fill="#f8fafc" font-size="13">Artificial Intelligence / ML</text>

      <rect x="0" y="281" width="16" height="16" rx="4" fill="#38bdf8"/>
      <text x="8" y="293" fill="#0f172a" font-size="11" text-anchor="middle">✓</text>
      <text x="28" y="294" fill="#f8fafc" font-size="13">Web / Frontend / React</text>

      <rect x="0" y="309" width="16" height="16" rx="4" fill="#1e293b" stroke="#475569"/>
      <text x="28" y="322" fill="#94a3b8" font-size="13">Backend / Highload / Go</text>

      <rect x="0" y="337" width="16" height="16" rx="4" fill="#1e293b" stroke="#475569"/>
      <text x="28" y="350" fill="#94a3b8" font-size="13">Mobile &amp; Cross-Platform</text>

      <!-- University / Venue -->
      <text x="0" y="395" fill="#94a3b8" font-size="11" font-weight="700" letter-spacing="0.5">УНИВЕРСИТЕТ И ЛОКАЦИЯ</text>
      <rect x="0" y="408" width="232" height="34" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="14" y="430" fill="#f8fafc" font-size="12">🏛 Главный корпус БГУ</text>

      <!-- Toggle Free spots -->
      <text x="0" y="480" fill="#94a3b8" font-size="11" font-weight="700" letter-spacing="0.5">ДОСТУПНОСТЬ</text>
      <rect x="0" y="492" width="40" height="22" rx="11" fill="#22c55e"/>
      <circle cx="29" cy="503" r="8" fill="#ffffff"/>
      <text x="50" y="508" fill="#f8fafc" font-size="13">Только со свободными местами</text>

      <!-- Reset CTA -->
      <rect x="0" y="620" width="232" height="36" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="116" y="643" fill="#94a3b8" font-size="12" text-anchor="middle">Сбросить все фильтры</text>
    </g>
  </g>

  <!-- Right Content: Event Grid -->
  <g transform="translate(365, 205)">
    <!-- Active filters bar -->
    <rect width="1015" height="44" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="20" y="27" fill="#94a3b8" font-size="13">Показано <tspan fill="#ffffff" font-weight="700">18 митапов</tspan> по запросу</text>
    
    <rect x="220" y="9" width="130" height="26" rx="13" fill="#38bdf822" stroke="#38bdf8"/>
    <text x="285" y="26" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">AI &amp; ML ✕</text>

    <rect x="360" y="9" width="130" height="26" rx="13" fill="#38bdf822" stroke="#38bdf8"/>
    <text x="425" y="26" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Офлайн БГУ ✕</text>

    <!-- Sort dropdown -->
    <rect x="800" y="7" width="195" height="30" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="815" y="27" fill="#cbd5e1" font-size="12">Сортировка: Ближайшие ▼</text>

    <!-- Event Cards (Row 1) -->
    <!-- Card 1 (CampusMeet #4) -->
    <g transform="translate(0, 65)">
      <rect width="325" height="400" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
      <!-- Event Image banner with gradient -->
      <rect width="325" height="150" rx="12" fill="#1e3a8a"/>
      <circle cx="280" cy="50" r="40" fill="#38bdf8" opacity="0.3"/>
      <text x="25" y="45" fill="#38bdf8" font-size="11" font-weight="800" letter-spacing="1">БГУ • ФПМИ</text>
      <text x="25" y="75" fill="#ffffff" font-size="18" font-weight="800">CampusMeet #4: GenAI</text>
      <text x="25" y="95" fill="#93c5fd" font-size="13">Распределенные архитектуры</text>

      <rect x="20" y="115" width="75" height="22" rx="4" fill="#0f172acc"/>
      <text x="57" y="130" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">МИТАП</text>

      <rect x="105" y="115" width="85" height="22" rx="4" fill="#059669cc"/>
      <text x="147" y="130" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">БЕСПЛАТНО</text>

      <!-- Card details -->
      <g transform="translate(20, 175)">
        <text x="0" y="0" fill="#38bdf8" font-size="12" font-weight="600">15 октября 2026 • 17:00</text>
        <text x="0" y="24" fill="#ffffff" font-size="16" font-weight="700">CampusMeet: AI &amp; Web</text>
        <text x="0" y="48" fill="#94a3b8" font-size="12">🏛 Главный корпус БГУ, Ауд. 512</text>
        <text x="0" y="70" fill="#cbd5e1" font-size="12">🎤 В. Громов (Lead Arch), Д. Мельников</text>

        <!-- Progress quota -->
        <rect x="0" y="95" width="285" height="6" rx="3" fill="#334155"/>
        <rect x="0" y="95" width="250" height="6" rx="3" fill="#22c55e"/>
        <text x="0" y="118" fill="#94a3b8" font-size="11">Занято мест: 88 / 100</text>
        <text x="285" y="118" fill="#22c55e" font-size="11" font-weight="bold" text-anchor="end">Осталось 12</text>

        <!-- CTA Button -->
        <rect x="0" y="145" width="285" height="40" rx="8" fill="url(#accentGrad)"/>
        <text x="142" y="170" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">Зарегистрироваться (Free)</text>
      </g>
    </g>

    <!-- Card 2 (FPMI Hack 2026) -->
    <g transform="translate(345, 65)">
      <rect width="325" height="400" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
      <rect width="325" height="150" rx="12" fill="#78350f"/>
      <circle cx="280" cy="50" r="40" fill="#f59e0b" opacity="0.3"/>
      <text x="25" y="45" fill="#fcd34d" font-size="11" font-weight="800" letter-spacing="1">ХАКАТОН • 24 ЧАСА</text>
      <text x="25" y="75" fill="#ffffff" font-size="18" font-weight="800">FPMI Hack 2026</text>
      <text x="25" y="95" fill="#fde68a" font-size="13">Призовой фонд 5000 BYN</text>

      <rect x="20" y="115" width="85" height="22" rx="4" fill="#0f172acc"/>
      <text x="62" y="130" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">ХАКАТОН</text>

      <rect x="115" y="115" width="95" height="22" rx="4" fill="#dc2626cc"/>
      <text x="162" y="130" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">WAITLIST (+14)</text>

      <g transform="translate(20, 175)">
        <text x="0" y="0" fill="#f59e0b" font-size="12" font-weight="600">24–25 октября 2026 • 10:00</text>
        <text x="0" y="24" fill="#ffffff" font-size="16" font-weight="700">FPMI Hackathon: Web &amp; AI</text>
        <text x="0" y="48" fill="#94a3b8" font-size="12">🏛 ФПМИ БГУ, 5 этаж коворкинг</text>
        <text x="0" y="70" fill="#cbd5e1" font-size="12">👥 Команды 3–5 чел • Нужен дизайнер</text>

        <rect x="0" y="95" width="285" height="6" rx="3" fill="#334155"/>
        <rect x="0" y="95" width="285" height="6" rx="3" fill="#ef4444"/>
        <text x="0" y="118" fill="#ef4444" font-size="11" font-weight="bold">Лимит 100 мест исчерпан</text>
        <text x="285" y="118" fill="#f59e0b" font-size="11" text-anchor="end">В очереди 14 чел.</text>

        <rect x="0" y="145" width="285" height="40" rx="8" fill="#1e293b" stroke="#f59e0b"/>
        <text x="142" y="170" fill="#fcd34d" font-size="13" font-weight="700" text-anchor="middle">Встать в лист ожидания</text>
      </g>
    </g>

    <!-- Card 3 (Highload Workshop) -->
    <g transform="translate(690, 65)">
      <rect width="325" height="400" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
      <rect width="325" height="150" rx="12" fill="#312e81"/>
      <circle cx="280" cy="50" r="40" fill="#818cf8" opacity="0.3"/>
      <text x="25" y="45" fill="#a5b4fc" font-size="11" font-weight="800" letter-spacing="1">ВОРКШОП • ПРАКТИКА</text>
      <text x="25" y="75" fill="#ffffff" font-size="18" font-weight="800">System Design &amp; Highload</text>
      <text x="25" y="95" fill="#c7d2fe" font-size="13">Архитектура отказоустойчивости</text>

      <rect x="20" y="115" width="90" height="22" rx="4" fill="#0f172acc"/>
      <text x="65" y="130" fill="#818cf8" font-size="10" font-weight="bold" text-anchor="middle">ВОРКШОП</text>

      <rect x="120" y="115" width="85" height="22" rx="4" fill="#059669cc"/>
      <text x="162" y="130" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">БЕСПЛАТНО</text>

      <g transform="translate(20, 175)">
        <text x="0" y="0" fill="#818cf8" font-size="12" font-weight="600">29 октября 2026 • 18:30</text>
        <text x="0" y="24" fill="#ffffff" font-size="16" font-weight="700">System Design на практике</text>
        <text x="0" y="48" fill="#94a3b8" font-size="12">🏛 ФФСН БГУ, Ауд. 302</text>
        <text x="0" y="70" fill="#cbd5e1" font-size="12">🎤 Практический разбор микросервисов</text>

        <rect x="0" y="95" width="285" height="6" rx="3" fill="#334155"/>
        <rect x="0" y="95" width="125" height="6" rx="3" fill="#22c55e"/>
        <text x="0" y="118" fill="#94a3b8" font-size="11">Занято мест: 35 / 80</text>
        <text x="285" y="118" fill="#22c55e" font-size="11" font-weight="bold" text-anchor="end">Свободно 45 мест</text>

        <rect x="0" y="145" width="285" height="40" rx="8" fill="url(#accentGrad)"/>
        <text x="142" y="170" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">Зарегистрироваться (Free)</text>
      </g>
    </g>

    <!-- Pagination -->
    <g transform="translate(350, 500)">
      <rect x="0" y="0" width="38" height="38" rx="8" fill="url(#accentGrad)"/>
      <text x="19" y="24" fill="#0f172a" font-size="14" font-weight="800" text-anchor="middle">1</text>
      
      <rect x="50" y="0" width="38" height="38" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="69" y="24" fill="#cbd5e1" font-size="14" text-anchor="middle">2</text>

      <rect x="100" y="0" width="38" height="38" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="119" y="24" fill="#cbd5e1" font-size="14" text-anchor="middle">3</text>

      <text x="160" y="24" fill="#94a3b8" font-size="14">Следующая →</text>
    </g>
  </g>
</svg>'''
    with open("docs/assets/mockups/mockup_desktop_catalog.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_mockup_desktop_event_details():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 1100" width="1440" height="1100" font-family="'Inter', -apple-system, sans-serif">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="accentGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="heroGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1440" height="1100" fill="url(#bgGrad2)"/>

  <!-- Top Glassmorphic Navigation -->
  <rect width="1440" height="72" fill="#0f172acc" stroke="#334155" stroke-width="1"/>
  <g transform="translate(60, 20)">
    <rect width="36" height="36" rx="8" fill="url(#accentGrad2)"/>
    <text x="18" y="24" fill="#0f172a" font-size="18" font-weight="900" text-anchor="middle">⚡</text>
    <text x="46" y="25" fill="#ffffff" font-size="18" font-weight="800">Campus<tspan fill="#38bdf8">Meet</tspan></text>
  </g>
  <g transform="translate(240, 36)">
    <text x="0" y="0" fill="#38bdf8" font-size="14" font-weight="700">Афиша</text>
    <text x="80" y="0" fill="#94a3b8" font-size="14" font-weight="500">Хакатоны</text>
    <text x="185" y="0" fill="#94a3b8" font-size="14" font-weight="500">Биржа команд</text>
  </g>
  <circle cx="1380" cy="36" r="18" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="1380" y="41" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">АК</text>

  <!-- Breadcrumbs & Hero Banner -->
  <g transform="translate(60, 95)">
    <text x="0" y="15" fill="#64748b" font-size="13">Главная &gt; Афиша &gt; CampusMeet #4: Распределенные системы и GenAI</text>

    <!-- Hero Card Container -->
    <rect x="0" y="30" width="1320" height="250" rx="16" fill="url(#heroGrad)" stroke="#38bdf844" stroke-width="1.5"/>
    
    <!-- Hero Badges -->
    <rect x="40" y="60" width="75" height="24" rx="4" fill="#38bdf8"/>
    <text x="77" y="76" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">МИТАП</text>

    <rect x="125" y="60" width="90" height="24" rx="4" fill="#22c55e"/>
    <text x="170" y="76" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">БЕСПЛАТНО</text>

    <rect x="225" y="60" width="140" height="24" rx="4" fill="#0f172a88" stroke="#38bdf8"/>
    <text x="295" y="76" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">ОСТАЛОСЬ 12 МЕСТ</text>

    <!-- Main Title -->
    <text x="40" y="125" fill="#ffffff" font-size="32" font-weight="800">CampusMeet #4: Архитектура распределенных систем и GenAI</text>
    
    <!-- Meta details bar -->
    <text x="40" y="165" fill="#93c5fd" font-size="15">📅 15 октября 2026 • 17:00 – 20:30 (Сбор гостей в 16:30)</text>
    <text x="40" y="195" fill="#cbd5e1" font-size="15">🏛 Главный корпус БГУ, Ленинский пр-т / Независимости 4, Ауд. 512 (5 этаж)</text>
    <text x="40" y="225" fill="#94a3b8" font-size="13">Организатор: Студенческий IT-клуб ФПМИ БГУ • Модератор: Максим Романов</text>
  </g>

  <!-- Two-column Body -->
  <g transform="translate(60, 395)">
    <!-- Left Column: Tabs, Schedule, Speakers (860px) -->
    <g transform="translate(0, 0)">
      <rect width="860" height="660" rx="12" fill="url(#cardGrad2)" stroke="#334155" stroke-width="1.5"/>
      
      <!-- Sub-tabs Navigation -->
      <line x1="0" y1="52" x2="860" y2="52" stroke="#334155"/>
      <text x="35" y="34" fill="#38bdf8" font-size="15" font-weight="700">Программа докладов</text>
      <line x1="35" y1="50" x2="200" y2="50" stroke="#38bdf8" stroke-width="3"/>

      <text x="240" y="34" fill="#94a3b8" font-size="15" font-weight="500">Спикеры (3)</text>
      <text x="360" y="34" fill="#94a3b8" font-size="15" font-weight="500">О митапе</text>
      <text x="470" y="34" fill="#94a3b8" font-size="15" font-weight="500">Схема прохода</text>
      <text x="620" y="34" fill="#94a3b8" font-size="15" font-weight="500">Вопросы и ответы (FAQ)</text>

      <!-- Interactive Schedule Timeline -->
      <g transform="translate(35, 80)">
        <!-- Slot 1 -->
        <rect width="790" height="85" rx="10" fill="#1e293b" stroke="#334155"/>
        <rect x="0" y="0" width="6" height="85" rx="3" fill="#38bdf8"/>
        <text x="25" y="32" fill="#38bdf8" font-size="14" font-weight="700">17:00 – 17:15</text>
        <text x="160" y="32" fill="#ffffff" font-size="16" font-weight="700">Открытие митапа и представление спикеров</text>
        <text x="160" y="55" fill="#94a3b8" font-size="13">Максим Романов (Председатель IT-клуба ФПМИ)</text>
        <rect x="680" y="24" width="90" height="30" rx="6" fill="#334155"/>
        <text x="725" y="44" fill="#cbd5e1" font-size="12" text-anchor="middle">В программе</text>

        <!-- Slot 2 (Keynote) -->
        <g transform="translate(0, 100)">
          <rect width="790" height="110" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
          <rect x="0" y="0" width="6" height="110" rx="3" fill="#22c55e"/>
          <text x="25" y="32" fill="#22c55e" font-size="14" font-weight="700">17:15 – 18:00</text>
          <text x="160" y="32" fill="#ffffff" font-size="16" font-weight="700">Highload &amp; Distributed Systems: Практика построения на Go</text>
          <text x="160" y="55" fill="#cbd5e1" font-size="13">Виктор Громов (Senior Backend Architect, 8+ лет в финтехе)</text>
          <text x="160" y="80" fill="#94a3b8" font-size="12">Разбор реальных кейсов масштабирования, шардирования и обработки 100k RPS.</text>
          
          <rect x="660" y="24" width="110" height="32" rx="6" fill="#22c55e22" stroke="#22c55e"/>
          <text x="715" y="45" fill="#22c55e" font-size="12" font-weight="bold" text-anchor="middle">★ Мой трек</text>
        </g>

        <!-- Slot 3 (Networking & Pizza) -->
        <g transform="translate(0, 225)">
          <rect width="790" height="70" rx="10" fill="#064e3b33" stroke="#059669"/>
          <text x="25" y="40" fill="#34d399" font-size="14" font-weight="700">18:00 – 18:30</text>
          <text x="160" y="40" fill="#ffffff" font-size="15" font-weight="600">🍕 Кофе-брейк, горячая пицца и нетворкинг у стендов IT-компаний</text>
        </g>

        <!-- Slot 4 (GenAI) -->
        <g transform="translate(0, 310)">
          <rect width="790" height="110" rx="10" fill="#1e293b" stroke="#334155"/>
          <rect x="0" y="0" width="6" height="110" rx="3" fill="#818cf8"/>
          <text x="25" y="32" fill="#818cf8" font-size="14" font-weight="700">18:30 – 19:20</text>
          <text x="160" y="32" fill="#ffffff" font-size="16" font-weight="700">Автономные мультиагентные системы на базе LLM в продакшене</text>
          <text x="160" y="55" fill="#cbd5e1" font-size="13">Александр Белов (AI Research Lead) • Демо реального пайплайна</text>
          <text x="160" y="80" fill="#94a3b8" font-size="12">Как заставить агентов оркестрировать сложные задачи без галлюцинаций.</text>
          
          <rect x="660" y="24" width="110" height="32" rx="6" fill="#334155"/>
          <text x="715" y="45" fill="#cbd5e1" font-size="12" text-anchor="middle">+ Добавить</text>
        </g>

        <!-- Slot 5 (Q&A Panel) -->
        <g transform="translate(0, 435)">
          <rect width="790" height="85" rx="10" fill="#1e293b" stroke="#334155"/>
          <rect x="0" y="0" width="6" height="85" rx="3" fill="#f59e0b"/>
          <text x="25" y="32" fill="#f59e0b" font-size="14" font-weight="700">19:20 – 20:15</text>
          <text x="160" y="32" fill="#ffffff" font-size="16" font-weight="700">Открытая панельная дискуссия и вопросы из зала</text>
          <text x="160" y="55" fill="#94a3b8" font-size="13">Все спикеры на сцене • Розыгрыш подарков и мерча от партнеров</text>
        </g>
      </g>
    </g>

    <!-- Right Sticky Column: Registration & Map (430px) -->
    <g transform="translate(890, 0)">
      <rect width="430" height="660" rx="12" fill="url(#cardGrad2)" stroke="#334155" stroke-width="1.5"/>
      <g transform="translate(30, 30)">
        <text x="0" y="20" fill="#ffffff" font-size="20" font-weight="800">Бронирование билета</text>
        <text x="0" y="45" fill="#94a3b8" font-size="13">Вход свободный по электронному билету</text>

        <!-- Hard Cap Capacity -->
        <rect x="0" y="65" width="370" height="8" rx="4" fill="#334155"/>
        <rect x="0" y="65" width="325" height="8" rx="4" fill="#22c55e"/>
        <text x="0" y="95" fill="#cbd5e1" font-size="12">Занято мест: 88 из 100 (88%)</text>
        <text x="370" y="95" fill="#22c55e" font-size="12" font-weight="bold" text-anchor="end">Осталось 12 мест</text>

        <!-- CTA Register -->
        <rect x="0" y="115" width="370" height="50" rx="10" fill="url(#accentGrad2)"/>
        <text x="185" y="146" fill="#0f172a" font-size="16" font-weight="800" text-anchor="middle">Зарегистрироваться в 1 клик</text>
        <text x="185" y="185" fill="#94a3b8" font-size="11" text-anchor="middle">⚡ Билет сразу сохранится в смартфон для офлайн-прохода</text>

        <line x1="0" y1="210" x2="370" y2="210" stroke="#334155"/>

        <!-- Details -->
        <text x="0" y="240" fill="#38bdf8" font-size="11" font-weight="bold" letter-spacing="1">МЕСТО ПРОВЕДЕНИЯ</text>
        <text x="0" y="265" fill="#ffffff" font-size="15" font-weight="700">Главный корпус БГУ, Ауд. 512</text>
        <text x="0" y="288" fill="#cbd5e1" font-size="13">г. Минск, пр-т Независимости 4 (метро Площадь Ленина)</text>

        <!-- OpenStreetMap Vector Mockup -->
        <g transform="translate(0, 310)">
          <rect width="370" height="170" rx="10" fill="#1e293b" stroke="#475569"/>
          <!-- Map streets vector simulation -->
          <path d="M 0 50 L 370 70" stroke="#475569" stroke-width="8"/>
          <path d="M 120 0 L 140 170" stroke="#475569" stroke-width="6"/>
          <path d="M 260 0 L 240 170" stroke="#475569" stroke-width="6"/>
          <rect x="150" y="60" width="80" height="50" rx="4" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="190" y="90" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Главный БГУ</text>
          
          <!-- Map Pin -->
          <circle cx="190" cy="55" r="14" fill="#ef4444"/>
          <circle cx="190" cy="55" r="5" fill="#ffffff"/>
          
          <rect x="10" y="130" width="350" height="30" rx="6" fill="#0f172acc"/>
          <text x="185" y="150" fill="#94a3b8" font-size="11" text-anchor="middle">OpenStreetMap Nominatim: 53.8938° N, 27.5471° E</text>
        </g>

        <!-- Calendar Buttons -->
        <g transform="translate(0, 510)">
          <rect width="180" height="38" rx="8" fill="#1e293b" stroke="#334155"/>
          <text x="90" y="24" fill="#cbd5e1" font-size="12" text-anchor="middle">📅 Google Calendar</text>

          <rect x="190" y="0" width="180" height="38" rx="8" fill="#1e293b" stroke="#334155"/>
          <text x="280" y="24" fill="#cbd5e1" font-size="12" text-anchor="middle">🍏 Apple iCal</text>
        </g>
      </g>
    </g>
  </g>
</svg>'''
    with open("docs/assets/mockups/mockup_desktop_event_details.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_mockup_desktop_dashboard():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="1440" height="960" font-family="'Inter', -apple-system, sans-serif">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="cardGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="accentGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1440" height="960" fill="url(#bgGrad3)"/>

  <!-- Left Sidebar Navigation -->
  <rect x="0" y="0" width="260" height="960" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  
  <!-- Logo -->
  <g transform="translate(25, 24)">
    <rect width="32" height="32" rx="8" fill="url(#accentGrad3)"/>
    <text x="16" y="22" fill="#0f172a" font-size="16" font-weight="900" text-anchor="middle">⚡</text>
    <text x="42" y="23" fill="#ffffff" font-size="17" font-weight="800">Campus<tspan fill="#38bdf8">Meet</tspan></text>
  </g>
  <text x="25" y="82" fill="#94a3b8" font-size="11" font-weight="700" letter-spacing="0.5">ОРГАНИЗАТОР: МАКСИМ Р.</text>

  <!-- Menu items -->
  <g transform="translate(15, 110)">
    <rect x="0" y="0" width="230" height="42" rx="8" fill="#38bdf822" stroke="#38bdf8"/>
    <text x="20" y="26" fill="#38bdf8" font-size="13" font-weight="700">📊 Дашборд события</text>

    <text x="20" y="75" fill="#cbd5e1" font-size="13">📅 Конструктор таймлайна</text>
    <text x="20" y="120" fill="#cbd5e1" font-size="13">👥 База гостей и чекины (88)</text>
    <text x="20" y="165" fill="#cbd5e1" font-size="13">🎤 Заявки спикеров CFP (4)</text>
    <text x="20" y="210" fill="#cbd5e1" font-size="13">📱 Сканеры волонтеров (2)</text>
    
    <rect x="10" y="245" width="210" height="40" rx="8" fill="#ef444422" stroke="#ef4444"/>
    <text x="25" y="270" fill="#f87171" font-size="13" font-weight="700">🚨 Экстренный Push</text>

    <text x="20" y="325" fill="#cbd5e1" font-size="13">📄 Экспорт отчетов (CSV/PDF)</text>
    <text x="20" y="370" fill="#cbd5e1" font-size="13">⚙️ Лимиты и квоты мест</text>
  </g>

  <!-- Top App Bar -->
  <rect x="260" y="0" width="1180" height="72" fill="#0f172acc" stroke="#334155" stroke-width="1"/>
  <g transform="translate(290, 20)">
    <text x="0" y="16" fill="#94a3b8" font-size="12">Управление активным событием:</text>
    <text x="0" y="38" fill="#ffffff" font-size="17" font-weight="800">CampusMeet #4: Распределенные системы и GenAI</text>
    
    <rect x="420" y="18" width="150" height="26" rx="13" fill="#064e3b" stroke="#22c55e"/>
    <circle cx="433" cy="31" r="5" fill="#22c55e"/>
    <text x="490" y="35" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">ЧЕКИН АКТИВЕН</text>

    <!-- Emergency Button -->
    <rect x="800" y="6" width="220" height="40" rx="8" fill="#ef4444"/>
    <text x="910" y="31" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">🚨 Экстренное оповещение</text>

    <circle cx="1100" cy="26" r="18" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="1100" y="31" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">МР</text>
  </g>

  <!-- Dashboard Workspace -->
  <g transform="translate(290, 95)">
    <!-- 4 KPI Cards -->
    <g transform="translate(0, 10)">
      <!-- KPI 1 -->
      <rect x="0" y="0" width="265" height="105" rx="12" fill="url(#cardGrad3)" stroke="#334155" stroke-width="1.5"/>
      <text x="20" y="30" fill="#94a3b8" font-size="11" font-weight="700">РЕГИСТРАЦИИ (HARD CAP)</text>
      <text x="20" y="68" fill="#ffffff" font-size="28" font-weight="800">100 / 100</text>
      <rect x="20" y="82" width="225" height="6" rx="3" fill="#334155"/>
      <rect x="20" y="82" width="225" height="6" rx="3" fill="#38bdf8"/>

      <!-- KPI 2 -->
      <rect x="285" y="0" width="265" height="105" rx="12" fill="url(#cardGrad3)" stroke="#22c55e" stroke-width="1.5"/>
      <text x="20" y="30" fill="#a7f3d0" font-size="11" font-weight="700">ПРОШЛИ ВХОД (ЧЕКИН)</text>
      <text x="20" y="68" fill="#22c55e" font-size="28" font-weight="800">88 чел. (88%)</text>
      <text x="20" y="90" fill="#94a3b8" font-size="11">Осталось подойти: 12 гостей</text>

      <!-- KPI 3 -->
      <rect x="570" y="0" width="265" height="105" rx="12" fill="url(#cardGrad3)" stroke="#334155" stroke-width="1.5"/>
      <text x="20" y="30" fill="#fcd34d" font-size="11" font-weight="700">ЛИСТ ОЖИДАНИЯ (WAITLIST)</text>
      <text x="20" y="68" fill="#f59e0b" font-size="28" font-weight="800">14 чел.</text>
      <text x="20" y="90" fill="#94a3b8" font-size="11">Авто-перевод при неявке: ВКЛ</text>

      <!-- KPI 4 -->
      <rect x="855" y="0" width="265" height="105" rx="12" fill="url(#cardGrad3)" stroke="#334155" stroke-width="1.5"/>
      <text x="20" y="30" fill="#94a3b8" font-size="11" font-weight="700">ТЕМП СКАНИРОВАНИЯ</text>
      <text x="20" y="68" fill="#38bdf8" font-size="28" font-weight="800">1.1 сек / гость</text>
      <text x="20" y="90" fill="#22c55e" font-size="11">✓ Очереди у дверей нет (0 мин)</text>
    </g>

    <!-- Real-time Live Log & Quick Actions -->
    <g transform="translate(0, 140)">
      <rect width="1120" height="700" rx="12" fill="url(#cardGrad3)" stroke="#334155" stroke-width="1.5"/>
      
      <!-- Table Header Bar -->
      <text x="25" y="36" fill="#ffffff" font-size="17" font-weight="800">Журнал верификации на входе в реальном времени (Live Audit Log)</text>
      <rect x="760" y="16" width="180" height="34" rx="6" fill="#0f172a" stroke="#334155"/>
      <text x="780" y="38" fill="#94a3b8" font-size="12">🔍 Поиск по фамилии...</text>
      <rect x="960" y="16" width="135" height="34" rx="6" fill="url(#accentGrad3)"/>
      <text x="1027" y="38" fill="#0f172a" font-size="12" font-weight="700" text-anchor="middle">Экспорт в CSV</text>

      <line x1="0" y1="65" x2="1120" y2="65" stroke="#334155"/>

      <!-- Table Column Titles -->
      <text x="30" y="92" fill="#94a3b8" font-size="12" font-weight="700">ВРЕМЯ</text>
      <text x="130" y="92" fill="#94a3b8" font-size="12" font-weight="700">ФИО УЧАСТНИКА</text>
      <text x="360" y="92" fill="#94a3b8" font-size="12" font-weight="700">ФАКУЛЬТЕТ / КУРС</text>
      <text x="540" y="92" fill="#94a3b8" font-size="12" font-weight="700">РОЛЬ</text>
      <text x="700" y="92" fill="#94a3b8" font-size="12" font-weight="700">СКАНИРОВАЛ</text>
      <text x="920" y="92" fill="#94a3b8" font-size="12" font-weight="700">СТАТУС ВХОДА</text>

      <!-- Row 1: Artem Kovalev -->
      <line x1="0" y1="110" x2="1120" y2="110" stroke="#1e293b"/>
      <text x="30" y="136" fill="#38bdf8" font-size="13" font-weight="600">16:48:12</text>
      <text x="130" y="136" fill="#ffffff" font-size="14" font-weight="700">Ковалёв Артём Игоревич</text>
      <text x="360" y="136" fill="#cbd5e1" font-size="13">ФПМИ БГУ, 3 курс</text>
      <text x="540" y="136" fill="#cbd5e1" font-size="13">Слушатель (#88)</text>
      <text x="700" y="136" fill="#94a3b8" font-size="13">Дарья М. (Сканер 1)</text>
      <rect x="920" y="120" width="120" height="26" rx="6" fill="#064e3b" stroke="#22c55e"/>
      <text x="980" y="137" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">✓ Подтвержден</text>

      <!-- Row 2: Kirill Savitsky -->
      <line x1="0" y1="160" x2="1120" y2="160" stroke="#1e293b"/>
      <text x="30" y="186" fill="#38bdf8" font-size="13" font-weight="600">16:47:58</text>
      <text x="130" y="186" fill="#ffffff" font-size="14" font-weight="700">Савицкий Кирилл Павлович</text>
      <text x="360" y="186" fill="#cbd5e1" font-size="13">ФПМИ БГУ, 4 курс</text>
      <text x="540" y="186" fill="#cbd5e1" font-size="13">Капитан хакатона</text>
      <text x="700" y="186" fill="#94a3b8" font-size="13">Иван К. (Сканер 2)</text>
      <rect x="920" y="170" width="120" height="26" rx="6" fill="#064e3b" stroke="#22c55e"/>
      <text x="980" y="187" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">✓ Подтвержден</text>

      <!-- Row 3: Vlad Kostylev (Fraud Alert) -->
      <line x1="0" y1="210" x2="1120" y2="210" stroke="#1e293b"/>
      <text x="30" y="236" fill="#ef4444" font-size="13" font-weight="600">16:46:40</text>
      <text x="130" y="236" fill="#f87171" font-size="14" font-weight="700">Костылев Влад (Повторный вход)</text>
      <text x="360" y="236" fill="#cbd5e1" font-size="13">Гость</text>
      <text x="540" y="236" fill="#ef4444" font-size="13">Скриншот (#42)</text>
      <text x="700" y="236" fill="#94a3b8" font-size="13">Дарья М. (Сканер 1)</text>
      <rect x="920" y="220" width="135" height="26" rx="6" fill="#7f1d1d" stroke="#ef4444"/>
      <text x="987" y="237" fill="#fecaca" font-size="11" font-weight="bold" text-anchor="middle">⚠ Дубликат QR (16:34)</text>

      <!-- Row 4: Viktor Gromov -->
      <line x1="0" y1="260" x2="1120" y2="260" stroke="#1e293b"/>
      <text x="30" y="286" fill="#38bdf8" font-size="13" font-weight="600">16:45:10</text>
      <text x="130" y="286" fill="#ffffff" font-size="14" font-weight="700">Громов Виктор Михайлович</text>
      <text x="360" y="286" fill="#cbd5e1" font-size="13">Senior Backend Architect</text>
      <text x="540" y="286" fill="#38bdf8" font-size="13" font-weight="bold">Спикер (VIP pass)</text>
      <text x="700" y="286" fill="#94a3b8" font-size="13">Максим Р. (Организатор)</text>
      <rect x="920" y="270" width="120" height="26" rx="6" fill="#064e3b" stroke="#22c55e"/>
      <text x="980" y="287" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">✓ Подтвержден</text>
    </g>
  </g>
</svg>'''
    with open("docs/assets/mockups/mockup_desktop_dashboard.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_mockup_mobile_catalog():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 375 812" width="375" height="812" font-family="'Inter', -apple-system, sans-serif">
  <defs>
    <linearGradient id="mBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="mCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="mAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <!-- Mobile phone shell -->
  <rect width="375" height="812" rx="42" fill="url(#mBg)" stroke="#334155" stroke-width="4"/>
  <rect x="125" y="12" width="125" height="28" rx="14" fill="#000000"/>

  <!-- Mobile Header -->
  <g transform="translate(20, 55)">
    <rect width="30" height="30" rx="8" fill="url(#mAccent)"/>
    <text x="15" y="20" fill="#0f172a" font-size="15" font-weight="900" text-anchor="middle">⚡</text>
    <text x="38" y="21" fill="#ffffff" font-size="17" font-weight="800">Campus<tspan fill="#38bdf8">Meet</tspan></text>
    <circle cx="320" cy="15" r="15" fill="#1e293b" stroke="#334155"/>
    <text x="320" y="19" fill="#94a3b8" font-size="12" text-anchor="middle">🔔</text>
  </g>

  <!-- Search Input with pill -->
  <g transform="translate(20, 100)">
    <rect width="335" height="42" rx="10" fill="#1e293b" stroke="#334155"/>
    <text x="18" y="26" fill="#94a3b8" font-size="13">🔍 Поиск митапов, хакатонов...</text>
  </g>

  <!-- Category Pills carousel -->
  <g transform="translate(20, 155)">
    <rect x="0" y="0" width="60" height="30" rx="15" fill="url(#mAccent)"/>
    <text x="30" y="19" fill="#0f172a" font-size="12" font-weight="700" text-anchor="middle">Все</text>

    <rect x="68" y="0" width="85" height="30" rx="15" fill="#1e293b" stroke="#334155"/>
    <text x="110" y="19" fill="#cbd5e1" font-size="12" text-anchor="middle">AI &amp; ML</text>

    <rect x="160" y="0" width="95" height="30" rx="15" fill="#1e293b" stroke="#334155"/>
    <text x="207" y="19" fill="#cbd5e1" font-size="12" text-anchor="middle">Хакатоны</text>

    <rect x="262" y="0" width="73" height="30" rx="15" fill="#1e293b" stroke="#334155"/>
    <text x="298" y="19" fill="#cbd5e1" font-size="12" text-anchor="middle">Web</text>
  </g>

  <!-- Event Cards list -->
  <g transform="translate(20, 205)">
    <!-- Event Card 1 -->
    <rect width="335" height="235" rx="14" fill="url(#mCard)" stroke="#334155" stroke-width="1.5"/>
    <rect width="335" height="75" rx="14" fill="#1e3a8a"/>
    <rect x="15" y="12" width="70" height="20" rx="4" fill="#0f172acc"/>
    <text x="50" y="26" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">МИТАП</text>
    <text x="15" y="55" fill="#ffffff" font-size="16" font-weight="800">CampusMeet #4: GenAI &amp; Web</text>

    <text x="15" y="98" fill="#38bdf8" font-size="12" font-weight="600">15 октября • 17:00 • Ауд. 512 БГУ</text>
    <text x="15" y="118" fill="#cbd5e1" font-size="12">Спикер: В. Громов (Lead Arch)</text>

    <!-- Quota bar -->
    <rect x="15" y="135" width="305" height="6" rx="3" fill="#334155"/>
    <rect x="15" y="135" width="268" height="6" rx="3" fill="#22c55e"/>
    <text x="15" y="156" fill="#94a3b8" font-size="10">88/100 мест занято</text>
    <text x="320" y="156" fill="#22c55e" font-size="10" font-weight="bold" text-anchor="end">Осталось 12</text>

    <rect x="15" y="175" width="305" height="42" rx="8" fill="url(#mAccent)"/>
    <text x="167" y="201" fill="#0f172a" font-size="13" font-weight="800" text-anchor="middle">Зарегистрироваться в 1 тап</text>

    <!-- Event Card 2 -->
    <g transform="translate(0, 255)">
      <rect width="335" height="235" rx="14" fill="url(#mCard)" stroke="#334155" stroke-width="1.5"/>
      <rect width="335" height="75" rx="14" fill="#78350f"/>
      <rect x="15" y="12" width="80" height="20" rx="4" fill="#0f172acc"/>
      <text x="55" y="26" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">ХАКАТОН</text>
      <text x="15" y="55" fill="#ffffff" font-size="16" font-weight="800">FPMI Hack 2026 (24h)</text>

      <text x="15" y="98" fill="#f59e0b" font-size="12" font-weight="600">24–25 октября • 10:00 • Коворкинг</text>
      <text x="15" y="118" fill="#cbd5e1" font-size="12">Команды по 3-5 чел • Призовой фонд</text>

      <rect x="15" y="135" width="305" height="6" rx="3" fill="#334155"/>
      <rect x="15" y="135" width="305" height="6" rx="3" fill="#ef4444"/>
      <text x="15" y="156" fill="#ef4444" font-size="10" font-weight="bold">Лимит мест исчерпан</text>
      <text x="320" y="156" fill="#f59e0b" font-size="10" text-anchor="end">Лист ожидания (+14)</text>

      <rect x="15" y="175" width="305" height="42" rx="8" fill="#1e293b" stroke="#f59e0b"/>
      <text x="167" y="201" fill="#fcd34d" font-size="13" font-weight="700" text-anchor="middle">В лист ожидания</text>
    </g>
  </g>

  <!-- Bottom Navigation Bar (4 tabs) -->
  <g transform="translate(0, 735)">
    <rect width="375" height="77" fill="#0f172acc" stroke="#334155" stroke-width="1"/>
    
    <text x="48" y="28" fill="#38bdf8" font-size="18" text-anchor="middle">📅</text>
    <text x="48" y="44" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Афиша</text>

    <text x="142" y="28" fill="#94a3b8" font-size="18" text-anchor="middle">🎟️</text>
    <text x="142" y="44" fill="#94a3b8" font-size="10" text-anchor="middle">Билеты</text>

    <text x="236" y="28" fill="#94a3b8" font-size="18" text-anchor="middle">👥</text>
    <text x="236" y="44" fill="#94a3b8" font-size="10" text-anchor="middle">Команды</text>

    <text x="328" y="28" fill="#94a3b8" font-size="18" text-anchor="middle">👤</text>
    <text x="328" y="44" fill="#94a3b8" font-size="10" text-anchor="middle">Профиль</text>
  </g>
</svg>'''
    with open("docs/assets/mockups/mockup_mobile_catalog.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_mockup_mobile_ticket():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 375 812" width="375" height="812" font-family="'Inter', -apple-system, sans-serif">
  <defs>
    <linearGradient id="tBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="tCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="tHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <!-- Phone Shell -->
  <rect width="375" height="812" rx="42" fill="url(#tBg)" stroke="#334155" stroke-width="4"/>
  <rect x="125" y="12" width="125" height="28" rx="14" fill="#000000"/>

  <!-- Header -->
  <g transform="translate(20, 55)">
    <text x="0" y="20" fill="#ffffff" font-size="18">←</text>
    <text x="167" y="20" fill="#ffffff" font-size="16" font-weight="800" text-anchor="middle">Мой электронный билет</text>
    <text x="335" y="20" fill="#38bdf8" font-size="16" text-anchor="end">↗</text>
  </g>

  <!-- Offline Status Capsule -->
  <g transform="translate(20, 95)">
    <rect width="335" height="32" rx="8" fill="#064e3b" stroke="#22c55e" stroke-width="1"/>
    <circle cx="20" cy="16" r="4" fill="#22c55e"/>
    <text x="32" y="20" fill="#a7f3d0" font-size="11" font-weight="700">OFFLINE-READY • Билет сохранен в памяти телефона</text>
  </g>

  <!-- Ticket Body -->
  <g transform="translate(20, 140)">
    <rect width="335" height="530" rx="16" fill="url(#tCard)" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Header ribbon of ticket -->
    <rect width="335" height="90" rx="16" fill="url(#tHeader)"/>
    <text x="20" y="30" fill="#38bdf8" font-size="11" font-weight="800" letter-spacing="1">БГУ ФПМИ • IT-МИТАП</text>
    <text x="20" y="55" fill="#ffffff" font-size="17" font-weight="800">CampusMeet: AI &amp; Web 2026</text>
    <text x="20" y="75" fill="#e0f2fe" font-size="12">15 октября 2026 • 17:00 • Ауд. 512 (5 этаж)</text>

    <!-- Guest metadata -->
    <g transform="translate(20, 115)">
      <text x="0" y="0" fill="#94a3b8" font-size="10" font-weight="700">ГОСТЬ / СЛУШАТЕЛЬ</text>
      <text x="0" y="22" fill="#ffffff" font-size="15" font-weight="800">Артём Ковалёв</text>
      <text x="0" y="38" fill="#38bdf8" font-size="11">ФПМИ БГУ, 3 курс</text>

      <text x="210" y="0" fill="#94a3b8" font-size="10" font-weight="700">МЕСТО / КВОТА</text>
      <text x="210" y="22" fill="#22c55e" font-size="15" font-weight="800">#88 / 100</text>
      <text x="210" y="38" fill="#94a3b8" font-size="11">Подтверждено</text>
    </g>

    <!-- Ticket tear punch -->
    <line x1="15" y1="180" x2="320" y2="180" stroke="#334155" stroke-dasharray="6,6" stroke-width="2"/>
    <circle cx="0" cy="180" r="12" fill="#0b1120"/>
    <circle cx="335" cy="180" r="12" fill="#0b1120"/>

    <!-- Dynamic Contrast QR Code Box -->
    <g transform="translate(62, 205)">
      <!-- Pure white box for optical reading -->
      <rect width="210" height="210" rx="14" fill="#ffffff"/>
      
      <!-- QR Locators -->
      <rect x="20" y="20" width="45" height="45" fill="#0f172a"/>
      <rect x="28" y="28" width="29" height="29" fill="#ffffff"/>
      <rect x="34" y="34" width="17" height="17" fill="#0f172a"/>

      <rect x="145" y="20" width="45" height="45" fill="#0f172a"/>
      <rect x="153" y="28" width="29" height="29" fill="#ffffff"/>
      <rect x="159" y="34" width="17" height="17" fill="#0f172a"/>

      <rect x="20" y="145" width="45" height="45" fill="#0f172a"/>
      <rect x="28" y="153" width="29" height="29" fill="#ffffff"/>
      <rect x="34" y="159" width="17" height="17" fill="#0f172a"/>

      <!-- Matrix pixels -->
      <rect x="80" y="30" width="15" height="15" fill="#0f172a"/>
      <rect x="105" y="40" width="20" height="18" fill="#0f172a"/>
      <rect x="75" y="80" width="30" height="30" fill="#0f172a"/>
      <rect x="120" y="90" width="25" height="25" fill="#0f172a"/>
      <rect x="155" y="90" width="20" height="20" fill="#0f172a"/>
      <rect x="30" y="90" width="30" height="30" fill="#0f172a"/>
      <rect x="80" y="145" width="35" height="20" fill="#0f172a"/>
      <rect x="135" y="150" width="30" height="30" fill="#0f172a"/>

      <rect x="85" y="95" width="40" height="20" rx="4" fill="#38bdf8"/>
      <text x="105" y="109" fill="#0f172a" font-size="9" font-weight="900" text-anchor="middle">PASS</text>
    </g>

    <text x="167" y="435" fill="#cbd5e1" font-size="11" text-anchor="middle">Токен: HMAC-SHA256 • Валиден еще 42с</text>
    <text x="167" y="455" fill="#22c55e" font-size="11" font-weight="bold" text-anchor="middle">☼ Яркость дисплея выставлена на 100%</text>

    <!-- Apple Wallet button -->
    <g transform="translate(30, 475)">
      <rect width="275" height="42" rx="8" fill="#000000" stroke="#475569"/>
      <text x="137" y="26" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle"> Add to Apple Wallet</text>
    </g>
  </g>

  <!-- Bottom Navigation Bar -->
  <g transform="translate(0, 735)">
    <rect width="375" height="77" fill="#0f172acc" stroke="#334155" stroke-width="1"/>
    <text x="48" y="28" fill="#94a3b8" font-size="18" text-anchor="middle">📅</text>
    <text x="48" y="44" fill="#94a3b8" font-size="10" text-anchor="middle">Афиша</text>

    <text x="142" y="28" fill="#38bdf8" font-size="18" text-anchor="middle">🎟️</text>
    <text x="142" y="44" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Билеты</text>

    <text x="236" y="28" fill="#94a3b8" font-size="18" text-anchor="middle">👥</text>
    <text x="236" y="44" fill="#94a3b8" font-size="10" text-anchor="middle">Команды</text>

    <text x="328" y="28" fill="#94a3b8" font-size="18" text-anchor="middle">👤</text>
    <text x="328" y="44" fill="#94a3b8" font-size="10" text-anchor="middle">Профиль</text>
  </g>
</svg>'''
    with open("docs/assets/mockups/mockup_mobile_ticket.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_mockup_mobile_scanner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 375 812" width="375" height="812" font-family="'Inter', -apple-system, sans-serif">
  <!-- Phone Frame background -->
  <rect width="375" height="812" rx="42" fill="#0b1120" stroke="#334155" stroke-width="4"/>
  <rect x="125" y="12" width="125" height="28" rx="14" fill="#000000"/>

  <!-- Camera Viewfinder simulation (Darkened room behind) -->
  <rect x="8" y="48" width="359" height="716" rx="24" fill="#0f172a"/>

  <!-- Top Scanner Status Bar -->
  <g transform="translate(20, 65)">
    <rect width="335" height="52" rx="12" fill="#1e293bcc" stroke="#334155" stroke-width="1"/>
    <text x="18" y="24" fill="#ffffff" font-size="13" font-weight="700">Вход: Главный корпус БГУ</text>
    <text x="18" y="42" fill="#38bdf8" font-size="11">Волонтер: Даша М. • Режим: Offline</text>
    <text x="315" y="34" fill="#22c55e" font-size="16" font-weight="800" text-anchor="end">88/100</text>
  </g>

  <!-- Glowing Laser Viewfinder Reticle -->
  <g transform="translate(57, 180)">
    <rect width="260" height="260" rx="16" fill="none" stroke="#334155" stroke-width="2"/>
    
    <!-- Neon green brackets -->
    <path d="M 0 32 L 0 0 L 32 0" fill="none" stroke="#22c55e" stroke-width="6"/>
    <path d="M 228 0 L 260 0 L 260 32" fill="none" stroke="#22c55e" stroke-width="6"/>
    <path d="M 0 228 L 0 260 L 32 260" fill="none" stroke="#22c55e" stroke-width="6"/>
    <path d="M 228 260 L 260 260 L 260 228" fill="none" stroke="#22c55e" stroke-width="6"/>

    <!-- Animated Laser Line -->
    <line x1="8" y1="130" x2="252" y2="130" stroke="#22c55e" stroke-width="3"/>
    <rect x="40" y="118" width="180" height="24" rx="4" fill="#064e3b88"/>
    <text x="130" y="134" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">СКАНИРОВАНИЕ &lt; 500 МС</text>
  </g>

  <!-- Success Recognition Banner Overlay -->
  <g transform="translate(20, 480)">
    <rect width="335" height="135" rx="14" fill="#064e3b" stroke="#22c55e" stroke-width="2"/>
    
    <circle cx="45" cy="42" r="22" fill="#22c55e"/>
    <text x="45" y="50" fill="#0f172a" font-size="22" font-weight="900" text-anchor="middle">✓</text>

    <text x="82" y="34" fill="#a7f3d0" font-size="11" font-weight="800" letter-spacing="1">ВХОД РАЗРЕШЕН</text>
    <text x="82" y="58" fill="#ffffff" font-size="19" font-weight="800">Артём Ковалёв</text>
    <text x="82" y="78" fill="#cbd5e1" font-size="12">ФПМИ БГУ, 3 курс • Билет #8841-A</text>

    <rect x="18" y="96" width="299" height="26" rx="6" fill="#047857"/>
    <text x="167" y="113" fill="#ffffff" font-size="11" text-anchor="middle">Чекин: 16:48:12 • Тактильный отклик: OK</text>
  </g>

  <!-- Manual search by name -->
  <g transform="translate(20, 635)">
    <rect width="335" height="44" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="20" y="27" fill="#94a3b8" font-size="12">⌨ Ручной ввод ФИО при разбитом экране...</text>
  </g>

  <!-- Flashlight and Controls -->
  <g transform="translate(20, 695)">
    <rect x="0" y="0" width="160" height="38" rx="8" fill="#334155"/>
    <text x="80" y="24" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle">💡 Фонарик [ВКЛ]</text>

    <rect x="175" y="0" width="160" height="38" rx="8" fill="#334155"/>
    <text x="255" y="24" fill="#22c55e" font-size="12" font-weight="600" text-anchor="middle">🔔 Звук / Вибро [ВКЛ]</text>
  </g>
</svg>'''
    with open("docs/assets/mockups/mockup_mobile_scanner.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_wireframe_desktop_catalog()
    generate_wireframe_desktop_event_details()
    generate_wireframe_mobile_ticket()
    generate_wireframe_mobile_scanner()
    generate_wireframe_desktop_dashboard()
    generate_mockup_desktop_catalog()
    generate_mockup_desktop_event_details()
    generate_mockup_desktop_dashboard()
    generate_mockup_mobile_catalog()
    generate_mockup_mobile_ticket()
    generate_mockup_mobile_scanner()
    print("Successfully generated all 11 SVG wireframe and mockup assets!")
