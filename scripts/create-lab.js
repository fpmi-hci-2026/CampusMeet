#!/usr/bin/env node

/**
 * CampusMeet / EventHub — Lab Page Scaffolding CLI
 * Usage:
 *   node scripts/create-lab.js <number> "<title>" "<subtitle>"
 * Example:
 *   node scripts/create-lab.js 4 "Стили интеграции программных систем и проектирование API" "OpenAPI, mock и MCP MVP"
 */

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 2) {
    console.log(`
Использование:
  node scripts/create-lab.js <номер> "<название>" ["<подзаголовок/описание>"]

Пример:
  node scripts/create-lab.js 4 "Стили интеграции программных систем и проектирование API" "OpenAPI, mock и MCP MVP"
`);
    process.exit(1);
}

const labNum = parseInt(args[0], 10);
if (isNaN(labNum) || labNum < 1 || labNum > 12) {
    console.error('Ошибка: Номер лабораторной работы должен быть числом от 1 до 12.');
    process.exit(1);
}

const title = args[1].trim();
const subtitle = (args[2] || 'Академические материалы и практические артефакты по дисциплине ПЧМИ').trim();

const targetFile = path.resolve(__dirname, '..', 'docs', 'pages', `lab${labNum}.html`);
if (fs.existsSync(targetFile)) {
    console.error(`Ошибка: Файл docs/pages/lab${labNum}.html уже существует!`);
    process.exit(1);
}

const template = `<!DOCTYPE html>
<html lang="ru" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Лаб. №${labNum}: ${title} — CampusMeet</title>
    <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
    <link rel="stylesheet" href="../css/style.css">
    <script src="../js/app-shell.js" defer></script>
</head>
<body data-page="lab${labNum}">
    <!-- Declarative Hero Header -->
    <lab-hero 
        lab="${labNum}" 
        title="Лабораторная работа №${labNum}: ${title}"
        subtitle="${subtitle}"
        status="planned"
        report="../reports/Lab${labNum}_report.md">
    </lab-hero>

    <!-- Declarative KPI Metrics Grid -->
    <stat-grid>
        <stat-card value="—" label="Показатель 1 (Запланировано)"></stat-card>
        <stat-card value="—" label="Показатель 2 (Запланировано)"></stat-card>
        <stat-card value="—" label="Показатель 3 (Запланировано)"></stat-card>
        <stat-card value="—" label="Показатель 4 (Запланировано)"></stat-card>
    </stat-grid>

    <!-- Declarative Document Sections (Auto-indexed into Right-Side TOC & Scrollspy) -->
    <doc-section id="lab${labNum}-overview" title="1. Цели и задачи исследования" badge="Обзор">
        <p>Описание целей и задач лабораторной работы №${labNum} по дисциплине ПЧМИ.</p>
        <callout-card type="info" title="Статус выполнения">
            Данный раздел подготовлен в рамках сквозного цикла проектирования CampusMeet.
        </callout-card>
    </doc-section>

    <doc-section id="lab${labNum}-methodology" title="2. Методология и стандарты" badge="Методика">
        <p>Описание используемой методологии, метрик и стандартов проектирования интерфейсов.</p>
    </doc-section>

    <doc-section id="lab${labNum}-artifacts" title="3. Артефакты и результаты" badge="Артефакты">
        <p>Итоговые аналитические таблицы, сводные протоколы и ссылки на материалы.</p>
    </doc-section>
</body>
</html>
`;

fs.writeFileSync(targetFile, template, 'utf8');
console.log(`✅ Успешно создана декларативная страница: docs/pages/lab${labNum}.html`);
console.log(`   Лаконичный шаблон содержит всего ${template.split('\n').length} строк!`);
console.log(`   Общий сайдбар, шапка, хлебные крошки, оглавление TOC со Scrollspy и пагинатор генерируются автоматически через app-shell.js.`);
