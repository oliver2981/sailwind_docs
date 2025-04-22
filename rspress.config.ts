import { defineConfig } from 'rspress/config';

export default defineConfig({
  root: 'docs',
  base: '/sailwind3.0_docs/',
  title: 'SailWind3.0',
  description: 'SailWind',
  icon: '/favicon.ico',
//   logo: '/logo.png',
  logoText: 'SailWind3.0',
  lang: 'en',
  locales: [
      {
      lang: 'zh',
      label: '简体中文',
      title: 'SailWind',
      description: 'SailWind3.0 文档',
    },
    {
      lang: 'en',
      label: 'English',
      title: 'SailWind',
      description: 'SailWind3.0 Docs',
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
      },
    ],

    footer: {
      message: `版权所有 © 2020-${new Date().getFullYear()} 派兹互连`,
    },
    hideNavbar: 'auto',

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
});