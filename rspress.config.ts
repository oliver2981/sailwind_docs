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
    route: {
        cleanUrls: true,
    },

    root: 'docs',
    base: '/sailwind_docs/',
    title: 'SailWind',
    description: 'SailWind',
    icon: '/favicon.ico',
    logoText: 'SailWind Docs',
    themeConfig: {
        enableContentAnimation: true,
        enableAppearanceAnimation: true,
        enableScrollToTop: true,
        lastUpdated: true,
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