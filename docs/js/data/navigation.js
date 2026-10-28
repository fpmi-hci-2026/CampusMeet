/**
 * CampusMeet / EventHub — Central Navigation & Course Registry
 * Single Source of Truth for all Portal Pages, Labs, Reports, and Repositories
 */

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.CampusMeetNavigation = factory();
    }
}(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    const NAV_DATA = {
        site: {
            title: 'CampusMeet Docs',
            subtitle: 'Проектирование человеко-машинных интерфейсов (ПЧМИ)',
            department: 'Белорусский государственный университет, ФПМИ',
            course: 'ПЧМИ • 2026–2027',
            version: 'v1.5.0',
            github: 'https://github.com/fpmi-hci-2026/CampusMeet',
            team: ['Минчук Станислав', 'Иванова Виктория', 'Шварцман Дидар']
        },

        portal: {
            id: 'portal',
            title: 'Главный портал',
            shortTitle: 'Главная',
            path: 'index.html',
            badge: 'Hub',
            icon: 'home'
        },

        labs: [
            {
                id: 'lab1',
                num: 1,
                title: 'Лабораторная работа №1',
                shortTitle: 'Лаб. №1',
                subtitle: 'Исследование пользователей и предметной области',
                path: 'pages/lab1.html',
                report: 'reports/Lab1_report.md',
                status: 'done',
                badge: 'L1',
                icon: 'users',
                desc: 'HCD, опрос студентов N=68, анализ Кано, 7 персон Купера, процессы As-Is'
            },
            {
                id: 'lab2',
                num: 2,
                title: 'Лабораторная работа №2',
                shortTitle: 'Лаб. №2',
                subtitle: 'Проектирование информационной архитектуры и взаимодействия',
                path: 'pages/lab2.html',
                report: 'reports/Lab2_report.md',
                status: 'done',
                badge: 'L2',
                icon: 'layout',
                desc: 'Sitemap (>3 уровней), карточная сортировка, CJM 7 персонажей, 7 раскадровок, 12 макетов'
            },
            {
                id: 'lab3',
                num: 3,
                title: 'Лабораторная работа №3',
                shortTitle: 'Лаб. №3',
                subtitle: 'Разработка требований к программной системе',
                path: 'pages/lab3.html',
                report: 'reports/Lab3_report.md',
                status: 'done',
                badge: 'L3',
                icon: 'file-text',
                desc: '12 User Stories (BDD/MoSCoW), 29 схем UML, EventStorming, C4 Model, ТЗ (SRS IEEE 830)'
            },
            {
                id: 'lab4',
                num: 4,
                title: 'Лабораторная работа №4',
                shortTitle: 'Лаб. №4',
                subtitle: 'Стили интеграции программных систем и проектирование API',
                path: 'pages/lab4.html',
                report: 'reports/Lab4_report.md',
                status: 'review',
                badge: 'L4',
                icon: 'code',
                desc: '33 операции OpenAPI, 17 таблиц, HTTP mock, MCP Tools / Resources / Prompts, Docker и CI'
            }
        ],

        wiki: {
            id: 'wiki',
            title: 'База знаний (Wiki)',
            shortTitle: 'Wiki',
            subtitle: 'Архитектурный паспорт, схема БД, REST API и токен HMAC',
            path: 'pages/wiki.html',
            badge: 'Docs',
            icon: 'book'
        },

        repos: [
            { id: 'repo-docs', name: 'CampusMeet', role: 'Портал и документация', url: 'https://github.com/fpmi-hci-2026/CampusMeet' },
            { id: 'repo-server', name: 'CampusMeet-Server', role: 'REST API & БД (10 таблиц)', url: 'https://github.com/fpmi-hci-2026/CampusMeet-Server' },
            { id: 'repo-web', name: 'CampusMeet-Web', role: 'Next.js кабинет организатора', url: 'https://github.com/fpmi-hci-2026/CampusMeet-Web' },
            { id: 'repo-mobile', name: 'CampusMeet-Mobile', role: 'React Native мобильный билет', url: 'https://github.com/fpmi-hci-2026/CampusMeet-Mobile' }
        ]
    };

    /**
     * Resolves path based on current document location
     */
    function isInPagesSubdir() {
        if (typeof window === 'undefined' || !window.location) return false;
        const p = window.location.pathname || '';
        return p.includes('/pages/') || (!p.endsWith('index.html') && p.includes('/pages'));
    }

    function resolvePath(targetRelPath) {
        if (!targetRelPath) return '';
        if (targetRelPath.startsWith('http://') || targetRelPath.startsWith('https://') || targetRelPath.startsWith('//') || targetRelPath.startsWith('#')) {
            return targetRelPath;
        }
        const inPages = isInPagesSubdir();
        if (inPages) {
            if (targetRelPath.startsWith('pages/')) {
                return targetRelPath.replace(/^pages\//, '');
            }
            if (!targetRelPath.startsWith('../')) {
                return '../' + targetRelPath;
            }
            return targetRelPath;
        } else {
            // Root index.html
            if (targetRelPath.startsWith('../')) {
                return targetRelPath.replace(/^\.\.\//, '');
            }
            return targetRelPath;
        }
    }

    function getCurrentPageId() {
        if (typeof document === 'undefined') return 'portal';
        if (document.body && document.body.dataset && document.body.dataset.page) {
            return document.body.dataset.page;
        }
        if (typeof window === 'undefined' || !window.location) return 'portal';
        const p = window.location.pathname || '';
        if (p.includes('lab1')) return 'lab1';
        if (p.includes('lab2')) return 'lab2';
        if (p.includes('lab3')) return 'lab3';
        if (p.includes('lab4')) return 'lab4';
        if (p.includes('lab5')) return 'lab5';
        if (p.includes('lab6')) return 'lab6';
        if (p.includes('lab7')) return 'lab7';
        if (p.includes('lab8')) return 'lab8';
        if (p.includes('wiki')) return 'wiki';
        return 'portal';
    }

    function getCurrentLab() {
        const id = getCurrentPageId();
        return NAV_DATA.labs.find(l => l.id === id) || null;
    }

    function getPrevNextLabs(currentId) {
        const id = currentId || getCurrentPageId();
        const index = NAV_DATA.labs.findIndex(l => l.id === id);
        if (index === -1) return { prev: null, next: null };
        return {
            prev: index > 0 ? NAV_DATA.labs[index - 1] : null,
            next: index < NAV_DATA.labs.length - 1 ? NAV_DATA.labs[index + 1] : null
        };
    }

    return {
        ...NAV_DATA,
        isInPagesSubdir,
        resolvePath,
        getCurrentPageId,
        getCurrentLab,
        getPrevNextLabs
    };
}));
