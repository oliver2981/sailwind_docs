import {defineConfig} from 'rspress/config';
import path from 'path';

export default defineConfig({

    globalStyles: path.join(__dirname, 'theme/var.css'),

    root: 'docs',
    base: '/sailwind_docs/',
    title: 'SailWind',
    description: 'SailWind',
    icon: '/favicon.ico',
//   logo: '/logo.png',
    logoText: 'SailWind Docs',
    lang: 'zh',
    locales: [
        {
            lang: 'zh',
            label: '简体中文',
            title: 'SailWind',
            description: 'SailWind 文档',
        },
        // {
        //     lang: 'en',
        //     label: 'English',
        //     title: 'SailWind',
        //     description: 'SailWind Docs',
        // },
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
                lang: 'en',
                outlineTitle: 'ON THIS PAGE',
            },
            {
                lang: 'zh',
                outlineTitle: '本页目录',
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
            },
            {
                lang: 'pdf',
                outlineTitle: '本页目录',
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
            },
        ],

        footer: {
            message: `版权所有 © 2020-${new Date().getFullYear()} 派兹互连`,
        },
        hideNavbar: 'auto',
    },
});