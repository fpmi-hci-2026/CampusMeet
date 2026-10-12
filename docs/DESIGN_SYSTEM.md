# Дизайн-система: Полная спецификация монохромного интерфейса

---

## 1. Философия и фундаментальные принципы

Данная дизайн-система базируется на концепции **«Интерфейса как чистого холста» (Subtractive Interface)**. В эпоху перенасыщенных веб-сервисов с кричащими градиентами, перегруженными анимациями и разноцветными акцентами, система придерживается эстетики строгого издательского дома и академической лаборатории:

1. **Субтрактивный дизайн (Minus-Front):** Любой визуальный элемент, который не несет смысловой нагрузки (декоративные подложки, цветные плашки, трехмерные тени), безжалостно удаляется. Дизайн определяется контентом и типографикой, а не рамками вокруг него.
2. **Абсолютная монохромность (Strict Monochromatic Palette):** Цветовая гамма ограничена чистым белым, абсолютным черным и калиброванной 10-ступенчатой шкалой нейтральных серых тонов. Цвет никогда не используется для украшения — только типографический вес, контраст и свободное пространство (Whitespace).
3. **Литературно-технологический симбиоз (Editorial + Tech):** Сочетание авторитетной современной антиквы (Serif) в заголовках и клинически нейтрального гротеска (Neo-Grotesk Sans) в интерфейсе создает ощущение солидности, научного авторитета и простоты.
4. **Волосковые направляющие (1px Hairlines):** Для зонирования вместо тяжелых теней и цветных заливок применяются субтильные однопиксельные линии с прозрачностью (от 8% до 15%), сохраняющие легкость страницы.
5. **Пространственный ритм (Spatial Precision):** Строгая 4px/8px модульная сетка, управляющая внутренними отступами компонентов и структурой блоков.

---

## 2. Цветовая палитра и дизайн-токены (Color System)

Цветовая модель построена на строгом дуализме (Light Mode / Dark Mode) с сохранением одинакового уровня семантической ясности.

### 2.1. Базовая шкала нейтралей (Neutral Greyscale Scale)

| Токен | HEX (Light) | HEX (Dark) | Назначение / Оптическая роль |
| :--- | :--- | :--- | :--- |
| `--gray-0` | `#ffffff` | `#000000` | Чистый базовый фон / Абсолютный контраст |
| `--gray-50` | `#f9f9f9` | `#0d0d0d` | Полотно страницы (Canvas) в темной теме / Сабтл-подложки |
| `--gray-100` | `#f4f4f4` | `#171717` | Вторичные поверхности (карточки, сайдбар) |
| `--gray-200` | `#ececec` | `#212121` | Приподнятые блоки (Elevated), поля ввода, hover-состояния |
| `--gray-300` | `#e3e3e3` | `#2f2f2f` | Разделители, границы по умолчанию (Hairline borders) |
| `--gray-400` | `#cdcdcd` | `#424242` | Активные границы, фокус-контуры, иконки в покое |
| `--gray-500` | `#9e9e9e` | `#666666` | Третичный текст, плейсхолдеры, отключенные элементы |
| `--gray-600` | `#737373` | `#8c8c8c` | Вспомогательный текст, метаданные, лейблы таблиц |
| `--gray-700` | `#404040` | `#b4b4b4` | Вторичный текст, подзаголовки, навигационные ссылки |
| `--gray-800` | `#262626` | `#e5e5e5` | Полужирный акцентный текст в Dark Mode |
| `--gray-900` | `#171717` | `#f4f4f4` | Основной чернильный текст (Light) / Первичный текст (Dark) |
| `--gray-950` | `#0d0d0d` | `#ffffff` | Глубокий черный уголь (Ink) / Чистый белый свет |

---

### 2.2. Семантические токены тем (Light vs. Dark Theme)

#### Light Theme (Светлая тема: Газетное полотно)
```css
:root {
  /* Поверхности (Surfaces) */
  --surface-canvas: #ffffff;
  --surface-primary: #ffffff;
  --surface-secondary: #f9f9f9;
  --surface-tertiary: #f4f4f4;
  --surface-hover: #ebebeb;
  --surface-active: #e1e1e1;
  --surface-translucent: rgba(255, 255, 255, 0.85);

  /* Границы (Borders) */
  --border-subtle: #e5e5e5;
  --border-default: #d4d4d4;
  --border-strong: #171717;
  --border-focus: #0d0d0d;

  /* Текст и чернила (Typography & Ink) */
  --text-primary: #0d0d0d;
  --text-secondary: #5d5d5d;
  --text-tertiary: #8c8c8c;
  --text-disabled: #b4b4b4;
  --text-inverse: #ffffff;

  /* Интерактивные монохромные действия (Interactive) */
  --action-primary-bg: #0d0d0d;
  --action-primary-text: #ffffff;
  --action-primary-hover: #262626;

  --action-secondary-bg: transparent;
  --action-secondary-border: #e5e5e5;
  --action-secondary-text: #0d0d0d;
  --action-secondary-hover: #f4f4f4;

  /* Скроллбар и оверлеи */
  --overlay-scrim: rgba(0, 0, 0, 0.45);
  --scrollbar-thumb: #d4d4d4;
  --scrollbar-thumb-hover: #a3a3a3;
}
```

#### Dark Theme (Темная тема: Угольная глубина)
```css
[data-theme="dark"], .dark {
  /* Поверхности (Surfaces) */
  --surface-canvas: #0d0d0d;
  --surface-primary: #171717;
  --surface-secondary: #212121;
  --surface-tertiary: #2a2a2a;
  --surface-hover: #333333;
  --surface-active: #3d3d3d;
  --surface-translucent: rgba(13, 13, 13, 0.85);

  /* Границы (Borders) */
  --border-subtle: #262626;
  --border-default: #383838;
  --border-strong: #ffffff;
  --border-focus: #ffffff;

  /* Текст и чернила (Typography & Ink) */
  --text-primary: #f4f4f4;
  --text-secondary: #a1a1aa;
  --text-tertiary: #71717a;
  --text-disabled: #52525b;
  --text-inverse: #0d0d0d;

  /* Интерактивные монохромные действия (Interactive) */
  --action-primary-bg: #ffffff;
  --action-primary-text: #0d0d0d;
  --action-primary-hover: #e5e5e5;

  --action-secondary-bg: transparent;
  --action-secondary-border: #2f2f2f;
  --action-secondary-text: #f4f4f4;
  --action-secondary-hover: #212121;

  /* Скроллбар и оверлеи */
  --overlay-scrim: rgba(0, 0, 0, 0.75);
  --scrollbar-thumb: #333333;
  --scrollbar-thumb-hover: #52525b;
}
```

---

### 2.3. Монохромные статусы без цветного шума (Zero-Color Semantics)

В классических UI принято красить ошибки в красный, а успехи в зеленый. В монохромной системе приоритет отдается **форме, иконке, типографике и штриховке**, исключая кричащие оттенки:

1. **Успех (Success):** 
   - Заливка: Тот же фоновый тон поверхности (`--surface-secondary`).
   - Бордюр: Однопиксельный нейтральный (`--border-default`).
   - Индикатор: Иконка галочки в окружности `✓` черного/белого цвета + четкий текстовый вердикт.
2. **Внимание / Замечание (Warning / Notice):**
   - Контурный прямоугольник с пунктирной или тонкой рамкой (`border: 1px dashed var(--border-default)`).
   - Префиксная иконка `⚠` или тег `[NOTE]`.
3. **Ошибка / Отказ (Error / Critical):**
   - Высококонтрастная монохромная инверсия (черная плашка с белым текстом в светлой теме) либо строгий полужирный контур (`border: 1.5px solid var(--text-primary)`).
   - Прямое текстовое сообщение с кодом ошибки без размытых цветных пятен.

---

## 3. Типографика (Typography System)

Типографика — главный структурообразующий элемент интерфейса. Здесь соблюдается строгое разделение между **публицистическими заголовками** и **интерфейсным гротеском**.

### 3.1. Шрифтовые гарнитуры (Font Stacks)

1. **Editorial Display (Заголовки и цитаты):**
   - Фирменный шрифт: `Signifier` (Klim Type Foundry).
   - Веб-стек / Fallback:
     ```css
     --font-serif: "Signifier", "Iowan Old Style", "Charter", "Georgia", "Times New Roman", serif;
     ```
   - Характер: Острые засечки, каллиграфическая дисциплина, книжный авторитет.
2. **UI & Body Copy (Основной интерфейс и текст):**
   - Фирменный шрифт: `Söhne` (Klim Type Foundry) / `Swiss Neo-Grotesk`.
   - Веб-стек / Fallback:
     ```css
     --font-sans: "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
     ```
   - Характер: Нео-гротеск швейцарской школы, закрытые апертуры, максимальная нейтральность.
3. **Code & Data (Код, формулы, числовые матрицы):**
   - Фирменный шрифт: `Söhne Mono` / `SF Mono` / `JetBrains Mono`.
   - Веб-стек / Fallback:
     ```css
     --font-mono: "Söhne Mono", "JetBrains Mono", Menlo, Monaco, Consolas, "Courier New", monospace;
     ```
   - Обязательное правило: `font-variant-numeric: tabular-nums;` для всех чисел, таймеров и счетчиков.

---

### 3.2. Матрица типографического масштаба

| Токен | Размер (px / rem) | Интерлиньяж (Line-Height) | Трекинг (Letter-Spacing) | Начертание (Weight) | Семья шрифта | Применение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `--type-display-xl` | `64px / 4.0rem` | `1.05` | `-0.035em` | `400 Regular` | Serif | Заглавные экраны, титульные манифесты |
| `--type-display-lg` | `48px / 3.0rem` | `1.10` | `-0.030em` | `400 Regular` | Serif | Заголовки страниц (H1) |
| `--type-title-xl` | `36px / 2.25rem` | `1.15` | `-0.025em` | `400 Regular` | Serif | Разделы исследований, главы (H2) |
| `--type-title-lg` | `28px / 1.75rem` | `1.20` | `-0.020em` | `500 Medium` | Sans | Подразделы верхнего уровня (H3) |
| `--type-title-md` | `22px / 1.375rem`| `1.25` | `-0.015em` | `500 Medium` | Sans | Заголовки карточек, модальных окон |
| `--type-title-sm` | `18px / 1.125rem`| `1.30` | `-0.010em` | `600 SemiBold`| Sans | Имена секций, заголовки списков |
| `--type-body-lg` | `18px / 1.125rem`| `1.60` | `-0.010em` | `400 Regular` | Sans / Serif| Лид-абзацы, вступительный текст |
| `--type-body-md` | `15px / 0.9375rem`| `1.55` | `-0.005em` | `400 Regular` | Sans | Основной текст интерфейса и чата |
| `--type-body-sm` | `13px / 0.8125rem`| `1.45` | `0.000em` | `400 Regular` | Sans | Второстепенные описания, метаданные |
| `--type-label-sm` | `12px / 0.75rem` | `1.35` | `+0.020em` | `500 Medium` | Sans | Метки полей ввода, бейджи, табы |
| `--type-micro` | `11px / 0.6875rem`| `1.30` | `+0.040em` | `600 SemiBold`| Sans | Верхний регистр (Caps), счетчики |
| `--type-code` | `13px / 0.8125rem`| `1.65` | `0.000em` | `400 Regular` | Mono | Блоки программного кода, выводы терминала |

---

### 3.3. Правила микротипографики

- **Ширина строки чтения:** Текстовые блоки жестко ограничиваются диапазоном `60–75 символов` (`max-width: 68ch;`). Запрещены растянутые на всю ширину монитора параграфы.
- **Оптический трекинг:** Чем крупнее кегль, тем плотнее расстояние между буквами (`-0.035em` на Display и `+0.02em` на микро-лейблах).
- **Символьная дисциплина:**
  - Длинное тире `—` с неразрывным пробелом слева.
  - Настоящие кавычки-лапки `« »` или `“ ”`, запрещены прямые машинные кавычки `""` в нарративном тексте.
  - Табличные цифры для предотвращения дрожания колонок: `font-feature-settings: "tnum" 1, "cv02" 1;`.

---

## 4. Сетка, модульные отступы и геометрия (Grid & Spacing)

### 4.1. Шкала отступов (4px / 8px Spatial Scale)

Каждый паддинг и марджин в интерфейсе кратен базовой единице 4px/8px:

```css
:root {
  --space-1: 4px;    /* 0.25rem — микроотступ между иконкой и текстом */
  --space-2: 8px;    /* 0.50rem — внутренний отступ тегов, компактных кнопок */
  --space-3: 12px;   /* 0.75rem — расстояние между связанными лейблами */
  --space-4: 16px;   /* 1.00rem — стандартный внутренний паддинг полей ввода */
  --space-5: 20px;   /* 1.25rem — модульный шаг карточек */
  --space-6: 24px;   /* 1.50rem — внутренний паддинг стандартных карточек */
  --space-8: 32px;   /* 2.00rem — расстояние между смысловыми блоками */
  --space-10: 40px;  /* 2.50rem — вертикальный отступ контентных разделов */
  --space-12: 48px;  /* 3.00rem — крупные модульные секции */
  --space-16: 64px;  /* 4.00rem — поля экрана на десктопе */
  --space-20: 80px;  /* 5.00rem — внешние отступы лендинга */
  --space-24: 96px;  /* 6.00rem — межсекционный простор */
  --space-32: 128px; /* 8.00rem — просторные паузы (Hero-блоки) */
}
```

---

### 4.2. Контейнеры и максимальные ширины

```css
:root {
  --container-reading: 720px;   /* Идеальная колонка для чтения статьи или ответа чата */
  --container-compact: 960px;   /* Формы настроек, консоль аккаунта */
  --container-base: 1140px;     /* Стандартная сетка документации */
  --container-wide: 1360px;     /* Широкий экран дашборда аналитики */
  --container-full: 1520px;     /* Максимальный охват на Ultra-Wide мониторах */
}
```

---

### 4.3. Система скругления углов (Border Radius)

Геометрия компонентов сдержанно смягчена, но избегает инфантильной округлости:

- `--radius-none: 0px` — Чистая бруталистская геометрия (таблицы данных, разделители во всю ширину).
- `--radius-xs: 4px` — Внутренние бейджики кода, микро-теги.
- `--radius-sm: 6px` — Контекстные меню, выпадающие дропдауны, тултипы.
- `--radius-md: 8px` — Поля ввода (`input`), кнопки по умолчанию, элементы списков.
- `--radius-lg: 12px` — Стандартные карточки контента, плавающие панели.
- `--radius-xl: 16px` — Модальные окна, центральное поле ввода сообщений и запросов (`prompt-box`).
- `--radius-full: 9999px` — Капсулы (Pill buttons), фильтры-чипсы, круглые кнопки-иконки.

---

### 4.4. Тени и глубина (Elevation & Hairlines)

Дизайн-система практически **отказывается от рассеянных темных теней**. Вместо них глубина передается контрастом светлых/темных поверхностей и сверхтонким контуром:

```css
:root {
  /* Уровень 0: Базовый плоский (Flat) */
  --shadow-none: none;

  /* Уровень 1: Карточка в покое / Hover-реакция */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);

  /* Уровень 2: Всплывающее меню / Dropdown */
  --shadow-md: 0 4px 12px -2px rgba(0, 0, 0, 0.08), 
               0 0 0 1px var(--border-subtle);

  /* Уровень 3: Модальный диалог / Centered Scrim Modal */
  --shadow-lg: 0 16px 36px -4px rgba(0, 0, 0, 0.16), 
               0 0 0 1px var(--border-subtle);
}
```

---

## 5. Компоненты интерфейса: Точные спецификации

### 5.1. Кнопки (Buttons)

Кнопки в монохромной системе предельно лаконичны. Никаких градиентных свечений — только монохромный контраст.

#### 1. Primary Action Button (Главное действие: Чернила)
- **Светлая тема:** Фон `#0d0d0d`, Текст `#ffffff`, Бордюр отсутствует.
- **Темная тема:** Фон `#ffffff`, Текст `#0d0d0d`, Бордюр отсутствует.
- **Hover:** Мягкое изменение яркости на 10% (`#262626` в светлой / `#e5e5e5` в темной).
- **Active:** Физическое микро-сжатие: `transform: scale(0.985);`.
- **CSS-код:**
```css
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: 40px;
  padding: 0 18px;
  background-color: var(--action-primary-bg);
  color: var(--action-primary-text);
  border: 1px solid transparent;
  border-radius: var(--radius-full); /* или var(--radius-md) для строгих форм */
  font-family: var(--font-sans);
  font-size: 14px;
  font-weight: 500;
  line-height: 1;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.1s ease;
  user-select: none;
}

.btn-primary:hover {
  background-color: var(--action-primary-hover);
}

.btn-primary:active {
  transform: scale(0.985);
}

.btn-primary:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--surface-canvas), 
              0 0 0 4px var(--border-focus);
}
```

#### 2. Secondary Outline Button (Второстепенное действие: Контур)
- **Фон:** `transparent`.
- **Бордюр:** `1px solid var(--border-default)`.
- **Текст:** `var(--text-primary)`.
- **Hover:** Фон меняется на `var(--surface-tertiary)`, бордюр на `var(--border-strong)`.

#### 3. Ghost Button (Минималистичная кнопка без рамки)
- **Фон:** `transparent`.
- **Бордюр:** `none`.
- **Текст:** `var(--text-secondary)`.
- **Hover:** Фон `var(--surface-hover)`, Текст `var(--text-primary)`.

---

### 5.2. Поля ввода и знаковое поле промпта (Input & Textarea)

Многострочное поле ввода запроса (Prompt Bar) является центральным артефактом интерфейса:

```css
.prompt-container {
  position: relative;
  width: 100%;
  max-width: var(--container-reading);
  margin: 0 auto;
  background-color: var(--surface-primary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-sm);
  padding: 12px 14px 10px 16px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.prompt-container:focus-within {
  border-color: var(--border-default);
  box-shadow: 0 0 0 1px var(--border-default);
}

.prompt-textarea {
  width: 100%;
  max-height: 200px;
  min-height: 24px;
  background: transparent;
  border: none;
  outline: none;
  resize: none;
  color: var(--text-primary);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.5;
}

.prompt-textarea::placeholder {
  color: var(--text-tertiary);
}

.prompt-action-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 10px;
}
```

---

### 5.3. Монохромные карточки контента (Editorial Cards)

Карточки не имеют тяжелых рамок или пестрых градиентов. Они представляют собой чистую поверхность с тончайшей окантовкой:

```css
.card {
  background-color: var(--surface-primary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  transition: border-color 0.2s ease, background-color 0.2s ease;
}

.card:hover {
  border-color: var(--border-default);
  background-color: var(--surface-secondary);
}

.card-kpi-value {
  font-family: var(--font-sans);
  font-size: 32px;
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  font-variant-numeric: tabular-nums;
  margin-bottom: 6px;
}

.card-kpi-label {
  font-size: 13px;
  font-weight: 400;
  color: var(--text-secondary);
  line-height: 1.4;
}
```

---

### 5.4. Таблицы данных (Monochrome Academic Tables)

Таблицы в стиле исследовательской академической документации оформляются строго по горизонталям без вертикальных разделителей:

```css
.table-monochrome {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: left;
}

.table-monochrome th {
  background-color: var(--surface-secondary);
  color: var(--text-secondary);
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 10px 16px;
  border-bottom: 1px solid var(--border-subtle);
}

.table-monochrome td {
  padding: 12px 16px;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-subtle);
  font-variant-numeric: tabular-nums;
}

.table-monochrome tr:last-child td {
  border-bottom: none;
}

.table-monochrome tr:hover td {
  background-color: var(--surface-secondary);
}
```

---

### 5.5. Блоки кода (Code Snippets & Terminal)

Блоки кода оформляются в темной или нейтральной гамме с кнопкой копирования в верхнем правом углу:

```css
.code-block {
  background-color: var(--surface-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  margin: var(--space-4) 0;
  overflow: hidden;
  font-family: var(--font-mono);
}

.code-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 14px;
  background-color: var(--surface-tertiary);
  border-bottom: 1px solid var(--border-subtle);
  font-size: 11px;
  color: var(--text-secondary);
  text-transform: lowercase;
}

.code-copy-btn {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  font-size: 11px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: color 0.15s ease;
}

.code-copy-btn:hover {
  color: var(--text-primary);
}

.code-content {
  padding: 16px;
  overflow-x: auto;
  font-size: 13px;
  line-height: 1.6;
  color: var(--text-primary);
  margin: 0;
}
```

---

### 5.6. Верхняя панель навигации (Sticky Blurred Topbar)

Навигация полупрозрачна и размывает фоновое содержимое при скролле:

```css
.topbar {
  position: sticky;
  top: 0;
  z-index: 100;
  width: 100%;
  height: 60px;
  background-color: var(--surface-translucent);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--space-6);
}

.topbar-brand {
  font-family: var(--font-sans);
  font-weight: 600;
  font-size: 16px;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  text-decoration: none;
}

.topbar-nav {
  display: flex;
  align-items: center;
  gap: var(--space-6);
}

.topbar-link {
  font-size: 14px;
  color: var(--text-secondary);
  text-decoration: none;
  transition: color 0.15s ease;
}

.topbar-link:hover,
.topbar-link.active {
  color: var(--text-primary);
}
```

---

## 6. Иконографика (Iconography System)

- **Стиль:** Строгий линейный контур (Outline), без скруглений или декоративных заливок.
- **Толщина штриха:** `1.5px` (консистентна по всей библиотеке).
- **Сетка и размер:** Стандартные боксы `16×16px`, `20×20px`, `24×24px`.
- **Цвет:** Всегда наследует текущий цвет текста через `stroke: currentColor; fill: none;`.
- **Приоритетный набор:** Набор иконок геометрического типа (Lucide / Feather / Radix Icons).

---

## 7. Анимации и микровзаимодействия (Motion Tokens)

Философия анимации интерфейса: **«Анимация не должна быть заметной; она должна ощущаться мгновенной и точной»**. Запрещены покачивания, пружинные отскоки (Spring Bounces) и медленные растворения.

```css
:root {
  /* Без задержек (Instant micro-interaction) */
  --duration-instant: 100ms;

  /* Быстрая реакция (Hover, Focus, Tooltip) */
  --duration-snappy: 150ms;

  /* Базовый интерфейсный переход (Dropdown, Accordion, Tab) */
  --duration-base: 200ms;

  /* Крупные переходы (Modal, Drawer, Page transition) */
  --duration-slow: 300ms;

  /* Кривые Безье */
  /* Фирменная резкая кривая затухания (Deceleration Curve) */
  --ease-out-cubic: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## 8. Чек-лист чистоты дизайна (Anti-Patterns / Что категорически запрещено)

1. ❌ **Никаких радужных градиентов:** Запрещены градиентные обводки, переливающийся текст и неоновые размытия (Glow-эффекты).
2. ❌ **Никаких тяжелых черных теней:** Тени не должны загрязнять макет. Объем создается разницей полутонов фона и 1px волосковыми линиями (`#e5e5e5` / `#262626`).
3. ❌ **Никакого низкоконтрастного серого текста:** Серый цвет второстепенного текста должен строго удовлетворять стандарту доступности WCAG AA (минимальный контраст 4.5:1 к фону).
4. ❌ **Никаких декоративных иллюстраций ради заполнения пустоты:** Пустое пространство (Whitespace) является самостоятельным архитектурным элементом, подчеркивающим значимость контента.
5. ❌ **Никаких пестрых статусов:** Ошибки, предупреждения и теги не должны выглядеть как разноцветные леденцы. Только структурные монохромные рамки и текстовые индикаторы.

---

## 9. Эталонный файл CSS-токенов (`tokens.css`)

Ниже приведен готовый модуль токенов для прямого подключения в любой веб-проект:

```css
/**
 * MONOCHROME MINIMALIST DESIGN SYSTEM TOKENS
 * License: MIT / Academic Research
 */

:root {
  /* --- TYPOGRAPHY STACKS --- */
  --font-sans: "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  --font-serif: "Signifier", "Charter", "Georgia", serif;
  --font-mono: "Söhne Mono", "JetBrains Mono", Menlo, Consolas, monospace;

  /* --- SPATIAL SCALE --- */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;

  /* --- GEOMETRY --- */
  --radius-xs: 4px;
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  /* --- MOTION --- */
  --ease-snappy: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-hover: 150ms;
  --duration-modal: 250ms;

  /* --- LIGHT THEME TOKENS --- */
  --bg-canvas: #ffffff;
  --bg-surface: #ffffff;
  --bg-subtle: #f9f9f9;
  --bg-muted: #f4f4f4;
  --bg-hover: #ebebeb;

  --border-subtle: #e5e5e5;
  --border-default: #d4d4d4;
  --border-strong: #171717;

  --text-primary: #0d0d0d;
  --text-secondary: #5d5d5d;
  --text-tertiary: #8c8c8c;
  --text-inverse: #ffffff;

  --action-bg: #0d0d0d;
  --action-text: #ffffff;
  --action-hover: #262626;

  --shadow-elevated: 0 4px 14px -2px rgba(0, 0, 0, 0.08), 0 0 0 1px #e5e5e5;
}

/* --- DARK THEME OVERRIDES --- */
[data-theme="dark"], body.dark {
  --bg-canvas: #0d0d0d;
  --bg-surface: #171717;
  --bg-subtle: #212121;
  --bg-muted: #2a2a2a;
  --bg-hover: #333333;

  --border-subtle: #262626;
  --border-default: #383838;
  --border-strong: #ffffff;

  --text-primary: #f4f4f4;
  --text-secondary: #a1a1aa;
  --text-tertiary: #71717a;
  --text-inverse: #0d0d0d;

  --action-bg: #ffffff;
  --action-text: #0d0d0d;
  --action-hover: #e5e5e5;

  --shadow-elevated: 0 4px 14px -2px rgba(0, 0, 0, 0.35), 0 0 0 1px #262626;
}

/* --- ACCESSIBILITY BASELINE --- */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
