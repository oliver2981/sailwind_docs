import {defineConfig} from 'rspress/config';
import path from 'node:path';


export default defineConfig({

    globalStyles: path.join(__dirname, 'theme/var.css'),
    multiVersion: {
        default: 'v4',
        versions: ['v3', 'v4'],
    },
    search: {
        versioned: true,
    },

    root: 'docs',
    base: '/sailwind_docs/',
    title: 'SailWind',
    description: 'SailWind',
    icon: '/favicon.ico',
    logoText: 'SailWind Docs',
    lang: 'zh',
    locales: [
        {
            lang: 'zh',
            label: '简体中文',
            title: 'SailWind',
            description: 'SailWind 文档',
        },
        {
            lang: 'pdf',
            label: 'English',
            title: 'SailWind',
            description: 'SailWind Docs',
        },

    ],
    themeConfig: {
        enableContentAnimation: true,
        enableAppearanceAnimation: true,
        enableScrollToTop: true,
        lastUpdated: true,
        locales: [
            {
                lang: 'zh',
                outlineTitle: '本页目录',
                prevPageText: '上一页',
                nextPageText: '下一页',
                lastUpdatedText: '最近更新时间',
                searchPlaceholderText: '搜索文档',
                overview: {
                    filterNameText: '快速查找',
                    filterPlaceholderText: '输入关键词',
                    filterNoResultText: '未查询到结果',
                },
                label: ''
            },
            {
                lang: 'pdf',
                outlineTitle: '本页目录',
                prevPageText: '上一页',
                nextPageText: '下一页',
                lastUpdatedText: '最近更新时间',
                searchPlaceholderText: '搜索文档',
                overview: {
                    filterNameText: '快速查找',
                    filterPlaceholderText: '输入关键词',
                    filterNoResultText: '未查询到结果',
                },
                label: ''
            },
        ],
        socialLinks: [
            {
                icon: 'github',
                mode: 'link',
                content: 'https://github.com/mikigo/sailwind_docs/',
            }
        ],

        footer: {
            message: `版权所有 © 2023-${new Date().getFullYear()} 派兹互连`,
        },
        hideNavbar: 'auto',
    },
});